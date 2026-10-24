"""Descarrega les fonts obertes de punts d'immersió i POIs a data/raw/pois/<font>/.

Només stdlib. Ús: python src/afons/sources/download_pois.py [font ...]
Sense arguments ho baixa tot; els fitxers que ja existeixen se salten.
Fonts i llicències: research_notes/Fonts obertes punts immersió/ i reports/.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parents[3] / "data" / "raw" / "pois"
UA = "afons/0.1 (projecte personal; QGIS/34000 compatible)"  # sig.gencat.cat rebutja UAs de curl/python
BBOX = (40.5, 0.15, 42.45, 3.35)  # S, W, N, E: costa catalana
# Polígon aproximat d'aigües costaneres (inclou una franja de terra)
GBIF_POLY = ("POLYGON((0.6 40.45,1.2 40.45,2.2 41.0,3.4 41.6,3.6 42.45,3.17 42.45,3.15 42.25,"
             "3.2 42.0,2.8 41.65,2.25 41.35,1.65 41.18,0.95 41.0,0.75 40.8,0.6 40.45))")


def get(url, data=None, tries=3):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, "Accept": "*/*"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read()
        except Exception as e:
            if i == tries - 1:
                raise
            print(f"   reintent ({e})")
            time.sleep(5 * (i + 1))


def save(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    print(f"   -> {path.relative_to(OUT)} ({len(content) / 1e6:.1f} MB)")


def wfs(base, typename, page=10000, sortby=None):
    """GetFeature paginat; retorna un FeatureCollection GeoJSON (CRS natiu)."""
    feats, start, crs = [], 0, None
    while True:
        q = {"SERVICE": "WFS", "VERSION": "2.0.0", "REQUEST": "GetFeature", "TYPENAMES": typename,
             "OUTPUTFORMAT": "application/json", "COUNT": page, "STARTINDEX": start}
        if sortby:
            q["SORTBY"] = sortby
        fc = json.loads(get(f"{base}?{urllib.parse.urlencode(q)}"))
        crs = crs or fc.get("crs")
        feats += fc["features"]
        if len(fc["features"]) < page:
            break
        start += page
    out = {"type": "FeatureCollection", "features": feats}
    if crs:
        out["crs"] = crs
    return out


def gencat_wfs(service, layers, sortby=None):
    base = f"https://sig.gencat.cat/ows/{service}/wfs"
    for layer in layers:
        path = OUT / "gencat" / service.lower() / f"{layer}.geojson"
        if path.exists():
            continue
        print(f"  {service}:{layer}")
        fc = wfs(base, f"{service}:{layer}", sortby=sortby)
        save(path, json.dumps(fc, ensure_ascii=False).encode())


def habitats():
    # Mapa dels hàbitats marins de Catalunya 2021-2024, CC0 1.0
    gencat_wfs("HABITATS", ["HABITATS_HABITATS_MARINS", "HABITATS_MARINS_COM", "HABITATS_TIPUS_FONS"], sortby="ID")


def espais():
    # Espais naturals protegits (PEIN/XN2000 CC BY 4.0)
    gencat_wfs("ESPAIS_NATURALS", ["ESPAISNATURALS_ENPE", "ESPAISNATURALS_PARCSNATURALS", "ESPAISNATURALS_PEIN",
                                   "ESPAISNATURALS_XARNAT_2000", "ESPAISNATURALS_ZEPA_LIC_MARI",
                                   "ESPAISNATURALS_ZEPIM", "ESPAISNATURALS_ESPAISINTGEOL"])


def oem():
    # Ordenació de l'espai marítim: esculls artificials, bionòmiques, zones prohibides (cartes IHM)
    gencat_wfs("ORDENACIO_ESPAI_MARITIM", ["OEM_ESCULLSARTIFICIALS", "OEM_CARTOBIONBADIAROSES",
                                           "OEM_CARTOBIONBAIXEMP", "OEM_LIMITSDIV_IHM_LIN",
                                           "OEM_LIMITSDIV_IHM_POL", "OEM_LIMITSDIV_IHM_PUNT"])
    # Descàrregues directes (SHP/GPKG): herbassars i mapa bionòmic de les Medes
    agri = "https://agricultura.gencat.cat/web/.content/12-serveis/bases-cartografiques/enllacos-documents/bases-cartografiques/fitxers-binaris/"
    for name, url in [("GestioHerbassars_gpkg.zip", "https://www.gencat.cat/agricultura/sig/bases/GestioHerbassars_gpkg.zip"),
                      ("mapa-bionomic-illes-medes.zip", agri + "mapa-bionomic-illes-medes.zip")]:
        path = OUT / "gencat" / "descarregues" / name
        if not path.exists():
            print(f"  {name}")
            save(path, get(url))


def centres():
    # Registre de centres d'immersió d'esbarjo (Llicència oberta d'ús d'informació - Catalunya)
    path = OUT / "gencat" / "centres_immersio_m5mm-yw6r.csv"
    if not path.exists():
        print("  centres d'immersió")
        save(path, get("https://analisi.transparenciacatalunya.cat/resource/m5mm-yw6r.csv?$limit=50000"))


def osm():
    # OSM/OpenSeaMap, ODbL
    path = OUT / "osm" / "overpass_pois.json"
    if path.exists():
        return
    b = ",".join(map(str, BBOX))
    query = f"""[out:json][timeout:180];
(
  nwr["scuba_diving:divespot"="yes"]({b});
  nwr["sport"="scuba_diving"]({b});
  nwr["amenity"="dive_centre"]({b});
  nwr["shop"="scuba_diving"]({b});
  nwr["seamark:type"="wreck"]({b});
  nwr["historic"="wreck"]({b});
  nwr["seamark:type"="mooring"]({b});
  nwr["man_made"="artificial_reef"]({b});
  nwr["natural"="cave_entrance"]["seamark:type"]({b});
);
out tags center;"""
    print("  overpass")
    for mirror in ["https://overpass-api.de/api/interpreter", "https://overpass.private.coffee/api/interpreter",
                   "https://overpass.kumi.systems/api/interpreter"]:
        try:
            save(path, get(mirror, urllib.parse.urlencode({"data": query}).encode(), tries=2))
            return
        except Exception as e:
            print(f"   {mirror} ha fallat: {e}")
    raise RuntimeError("Cap mirall Overpass ha respost")


def emodnet():
    # Derelictes mundials (UKHO via EMODnet Human Activities), CC BY 4.0
    path = OUT / "emodnet" / "wwshipwrecks.geojson"
    if not path.exists():
        print("  emodnet wwshipwrecks")
        s, w, n, e = BBOX
        save(path, get("https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature"
                       "&typeNames=emodnet:wwshipwrecks&outputFormat=application/json&srsName=EPSG:4326"
                       f"&bbox={s},{w},{n},{e},urn:ogc:def:crs:EPSG::4326"))


GBIF_DATASETS = {  # datasets de busseig amb llocs repetits / noms de punts
    "diveboard": "66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2",   # CC BY-NC 4.0: no redistribuir els registres
    "climatefish": "04036f89-d147-4e0c-adb1-93f9ba822257",  # CC BY 4.0 (T-MEDNet)
    "bioobs": "25e3e8f1-86ee-440c-adfc-8e63759a6505",       # CC BY 4.0 (FFESSM)
    "cromis": "8e9974a4-12e2-475f-9aec-5abdf24a1f50",       # CC BY 4.0 (FFESSM)
}


def gbif():
    for name, key in GBIF_DATASETS.items():
        path = OUT / "gbif" / f"{name}.json"
        if path.exists():
            continue
        print(f"  gbif {name}")
        meta = json.loads(get(f"https://api.gbif.org/v1/dataset/{key}"))
        recs, offset = [], 0
        # ponytail: l'API de cerca talla a offset 100k; per a més cal l'API de descàrrega (amb compte GBIF)
        while offset < 100000:
            q = urllib.parse.urlencode({"datasetKey": key, "geometry": GBIF_POLY, "limit": 300, "offset": offset})
            page = json.loads(get(f"https://api.gbif.org/v1/occurrence/search?{q}"))
            recs += page["results"]
            if page["endOfRecords"]:
                break
            offset += 300
        out = {"dataset": {k: meta.get(k) for k in ("key", "title", "license", "doi", "citation")}, "results": recs}
        save(path, json.dumps(out, ensure_ascii=False).encode())


SOURCES = {"osm": osm, "emodnet": emodnet, "centres": centres, "habitats": habitats,
           "espais": espais, "oem": oem, "gbif": gbif}

if __name__ == "__main__":
    failed = []
    for name in sys.argv[1:] or SOURCES:
        print(f"[{name}]")
        try:
            SOURCES[name]()
        except Exception as e:
            print(f"   ERROR {name}: {e}")
            failed.append(name)
    sys.exit(f"Han fallat: {', '.join(failed)}" if failed else 0)
