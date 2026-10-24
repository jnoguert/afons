"""Retalla la batimetria ICGC i l'ortofoto al voltant de cada punt del catàleg (web/sites/index.js).

Ús: python src/afons/bathy/clip_site.py            # genera els punts que encara no tenen site.js
    python src/afons/bathy/clip_site.py boreas     # (re)genera aquests punts
Sortida: web/sites/<slug>/site.js, que es versiona i es publica a GitHub Pages.
Requereix numpy i tifffile (els porta Anaconda). Coordenades en ETRS89 / UTM 31N (EPSG:25831).
"""
import base64
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
import tifffile
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[3]
TIF = ROOT / "data/raw/Batimetria-ICGC-v2r1-2021-2025/batimetria-v2r1-elevacions-2021-2025.tif"
NODATA = -9999
ORTO_WMS = "https://geoserveis.icgc.cat/servei/catalunya/orto-territorial/wms"
HAB_WFS = "https://sig.gencat.cat/ows/HABITATS/wfs"  # Mapa dels hàbitats marins de Catalunya, CC0
# categoria simplificada per paraula clau del nom LPRE (l'ordre importa: el primer que coincideix)
CATS = [("mata morta", "Mata morta de posidònia"), ("posidonia", "Posidònia"), ("cymodocea", "Altres fanerògames"),
        ("zostera", "Altres fanerògames"), ("coral", "Coral·ligen"), ("portu", "Antròpic"), ("espigon", "Antròpic"),
        ("antròp", "Antròpic"), ("roca", "Roca"), ("còdol", "Còdols i graves"), ("maërl", "Detrític"),
        ("detrític", "Detrític"), ("fangs i fangs", "Fang"), ("sorr", "Sorra"), ("fang", "Fang")]


def categoria(nom):
    n = nom.lower()
    return next((c for k, c in CATS if k in n), "Altres")


assert categoria("30403 - Fangs i fangs sorrencs infralitorals i circalitorals") == "Fang"
assert categoria("30402 - Sorres i sorres fangoses infralitorals i circalitorals") == "Sorra"
assert categoria("70201 - Fangs i sorres fangoses portuàries") == "Antròpic"
assert categoria("3051203 - Alguers de mata morta de Posidonia oceanica") == "Mata morta de posidònia"


def wfs(layer, xmin, ymin, xmax, ymax):
    q = {"SERVICE": "WFS", "VERSION": "2.0.0", "REQUEST": "GetFeature", "TYPENAMES": f"HABITATS:{layer}",
         "OUTPUTFORMAT": "application/json", "COUNT": 20000,
         "BBOX": f"{xmin},{ymin},{xmax},{ymax},urn:ogc:def:crs:EPSG::25831"}
    req = urllib.request.Request(f"{HAB_WFS}?{urllib.parse.urlencode(q)}", headers={"User-Agent": "QGIS/34000 (afons)"})
    with urllib.request.urlopen(req, timeout=180) as r:  # sig.gencat.cat rebutja UAs de curl/python
        return json.load(r)["features"]


def habitats(xmin, ymax, size, res, w, h):
    """Rasteritza els polígons d'hàbitat a la graella del retall: (índexs Uint8, classes)."""
    grid, names = Image.new("L", (w, h), 0), []
    for f in wfs("HABITATS_HABITATS_MARINS", xmin, ymax - size, xmin + size, ymax):
        nom = f["properties"].get("CAT_LLEG") or "?"
        if nom not in names:
            names.append(nom)
        g = f["geometry"]
        for poly in g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]:
            mask = Image.new("1", (w, h), 0)
            draw = ImageDraw.Draw(mask)
            for k, ring in enumerate(poly):  # anell exterior 1, forats 0
                draw.polygon([((x - xmin) / res, (ymax - y) / res) for x, y, *_ in ring], fill=0 if k else 1)
            grid.paste(names.index(nom) + 1, mask=mask)
    assert len(names) < 255
    return grid.tobytes(), [{"nom": n, "cat": categoria(n)} for n in names]


def read_window(path, col0, row0, w, h):
    """Llegeix una finestra d'un GeoTIFF tessel·lat sense carregar-lo sencer."""
    with tifffile.TiffFile(path) as tif:
        page = tif.pages[0]
        tw, th = page.tilewidth, page.tilelength
        tiles_x = -(-page.imagewidth // tw)
        out = np.full((h, w), np.nan, np.float32)
        fh = tif.filehandle
        for ty in range(row0 // th, (row0 + h - 1) // th + 1):
            for tx in range(col0 // tw, (col0 + w - 1) // tw + 1):
                i = ty * tiles_x + tx
                fh.seek(page.dataoffsets[i])
                tile = page.decode(fh.read(page.databytecounts[i]), i)[0].reshape(th, tw)
                # retall de la intersecció tessel·la ∩ finestra
                r0, c0 = max(row0, ty * th), max(col0, tx * tw)
                r1, c1 = min(row0 + h, (ty + 1) * th), min(col0 + w, (tx + 1) * tw)
                out[r0 - row0:r1 - row0, c0 - col0:c1 - col0] = tile[r0 - ty * th:r1 - ty * th, c0 - tx * tw:c1 - tx * tw]
    out[out <= NODATA + 1] = np.nan
    return out


def geo(path):
    """Origen (vora superior esquerra) i mida de píxel des dels tags GeoTIFF."""
    with tifffile.TiffFile(path) as tif:
        tags = tif.pages[0].tags
        _, _, _, x0, y0, _ = tags["ModelTiepointTag"].value
        res = tags["ModelPixelScaleTag"].value[0]
    return x0, y0, res


def main(slug, name, x, y, half=500, step=2):
    x, y, half, step = float(x), float(y), int(half), int(step)
    gx0, gy0, res = geo(TIF)
    col0, row0 = int((x - half - gx0) / res), int((gy0 - (y + half)) / res)
    n = int(2 * half / res)
    elev = read_window(TIF, col0, row0, n, n)
    k = int(step / res)  # remostreig per blocs (mitjana ignorant NaN)
    elev = np.nanmean(elev[: n // k * k, : n // k * k].reshape(n // k, k, n // k, k), axis=(1, 3)).astype(np.float32)
    xmin, ymax = gx0 + col0 * res, gy0 - row0 * res  # vora superior esquerra del retall
    size = n * res
    valid = np.isfinite(elev)
    print(f"{name}: {elev.shape[1]}x{elev.shape[0]} a {step} m, {valid.mean():.0%} amb dades, "
          f"cota {np.nanmin(elev):.1f}..{np.nanmax(elev):.1f} m")

    q = {"SERVICE": "WMS", "VERSION": "1.3.0", "REQUEST": "GetMap", "LAYERS": "ortofoto_color_vigent",
         "STYLES": "", "CRS": "EPSG:25831", "BBOX": f"{xmin},{ymax - size},{xmin + size},{ymax}",
         "WIDTH": 2048, "HEIGHT": 2048, "FORMAT": "image/jpeg"}
    req = urllib.request.Request(f"{ORTO_WMS}?{urllib.parse.urlencode(q)}", headers={"User-Agent": "afons/0.1"})
    with urllib.request.urlopen(req, timeout=120) as r:
        if not r.headers.get("Content-Type", "").startswith("image/"):
            raise RuntimeError(f"WMS no ha retornat imatge: {r.read(300)!r}")
        ortho = r.read()

    hab, classes = habitats(xmin, ymax, size, step, elev.shape[1], elev.shape[0])
    print(f"   hàbitats: {', '.join(sorted({c['cat'] for c in classes}))}")

    # NaN (terra fora de la franja) -> null via NaN en Float32; el visor ho tracta com a terra
    site = {"slug": slug, "name": name, "center": [x, y], "xmin": xmin, "ymax": ymax, "res": step,
            "w": elev.shape[1], "h": elev.shape[0],
            "elev": base64.b64encode(elev.tobytes()).decode(),  # Float32 little-endian, files de nord a sud
            "ortho": "data:image/jpeg;base64," + base64.b64encode(ortho).decode(),
            "hab": base64.b64encode(hab).decode(), "habClasses": classes,  # Uint8: 0 = sense dades, i = habClasses[i-1]
            "attribution": "Batimetria i ortofoto © ICGC, CC BY 4.0 · Hàbitats marins © Generalitat de Catalunya, CC0"}
    out = SITES / slug / "site.js"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("window.AFONS_SITE = " + json.dumps(site, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"-> {out.relative_to(ROOT)} ({out.stat().st_size / 1e6:.1f} MB)")


SITES = ROOT / "web/sites"


def catalog():
    src = (SITES / "index.js").read_text(encoding="utf-8")
    return json.loads(src[src.index("["):src.index("];") + 1])  # AFONS_SITES és JSON estricte


if __name__ == "__main__":
    wanted = sys.argv[1:]
    for s in catalog():
        if (s["slug"] in wanted) or (not wanted and not (SITES / s["slug"] / "site.js").exists()):
            main(s["slug"], f'{s["name"]} ({s["zone"]})', s["x"], s["y"])
