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

ROOT = Path(__file__).resolve().parents[3]
TIF = ROOT / "data/raw/Batimetria-ICGC-v2r1-2021-2025/batimetria-v2r1-elevacions-2021-2025.tif"
NODATA = -9999
ORTO_WMS = "https://geoserveis.icgc.cat/servei/catalunya/orto-territorial/wms"


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

    # NaN (terra fora de la franja) -> null via NaN en Float32; el visor ho tracta com a terra
    site = {"slug": slug, "name": name, "center": [x, y], "xmin": xmin, "ymax": ymax, "res": step,
            "w": elev.shape[1], "h": elev.shape[0],
            "elev": base64.b64encode(elev.tobytes()).decode(),  # Float32 little-endian, files de nord a sud
            "ortho": "data:image/jpeg;base64," + base64.b64encode(ortho).decode(),
            "attribution": "Batimetria i ortofoto © Institut Cartogràfic i Geològic de Catalunya (ICGC), CC BY 4.0"}
    out = SITES / slug / "site.js"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("window.AFONS_SITE = " + json.dumps(site, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"-> {out.relative_to(ROOT)} ({out.stat().st_size / 1e6:.1f} MB)")


SITES = ROOT / "web/sites"


def catalog():
    src = (SITES / "index.js").read_text(encoding="utf-8")
    return json.loads(src[src.index("["):src.rindex("]") + 1])  # el catàleg és JSON estricte


if __name__ == "__main__":
    wanted = sys.argv[1:]
    for s in catalog():
        if (s["slug"] in wanted) or (not wanted and not (SITES / s["slug"] / "site.js").exists()):
            main(s["slug"], f'{s["name"]} ({s["zone"]})', s["x"], s["y"])
