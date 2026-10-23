# 🤿 Afons

**Atles batimètric de punts d'immersió de la costa catalana.**

![Estat](https://img.shields.io/badge/estat-exploraci%C3%B3-orange) ![Llicència](https://img.shields.io/badge/llic%C3%A8ncia-MIT-blue)

Afons creua la ubicació dels punts d'immersió de la Costa Brava (i la resta de la costa catalana) amb dades obertes de batimetria i cartografia per generar, per a cada immersió, un mapa del fons: isòbates, perfil de profunditat, relleu 3D i punts d'interès (derelictes, coves, agulles, praderies...). L'objectiu és tenir una eina per **planificar immersions** i **documentar-les** marcant el que hi ha sota l'aigua.

> ⚠️ Projecte personal i experimental. Les dades batimètriques poden tenir errors, buits o resolució insuficient. **No substitueix les cartes nàutiques oficials, el briefing del centre d'immersió ni el sentit comú.**

---

## Índex

- [Objectius](#objectius)
- [Fonts de dades](#fonts-de-dades)
- [Stack](#stack)
- [Estructura prevista](#estructura-prevista)
- [Full de ruta](#full-de-ruta)
- [Llicències i atribució](#llicències-i-atribució)

## Estat actual

Fase 0: definició del projecte. Encara no hi ha codi; el primer pas és el notebook d'exploració de fonts sobre les illes Medes (vegeu el [full de ruta](#full-de-ruta)).

## Objectius

- [ ] Recopilar un catàleg obert de punts d'immersió de la costa catalana (coordenades, profunditat màxima, tipus, nivell recomanat).
- [ ] Descarregar i normalitzar la batimetria disponible (alta resolució a prop de costa, regional més enllà).
- [ ] Per a cada punt: retallar la batimetria en un radi configurable i generar isòbates, mapa ombrejat, perfil i vista 3D.
- [ ] Afegir punts d'interès: derelictes, coves, esculls artificials, boies d'amarratge, zones protegides.
- [ ] Permetre afegir POIs propis i traces d'immersió (logs de l'ordinador de busseig).
- [ ] Visor web senzill per consultar-ho tot des del mòbil abans de tirar-se a l'aigua.

## Fonts de dades

| Font | Què aporta | Format / accés | Llicència | Estat |
|---|---|---|---|---|
| **[ICGC – Batimetria v2r1 2021-2025](https://www.icgc.cat/en/Geoinformation-and-Maps/Data-and-products/Elevations/Bathymetry)** | Model topobatimètric de la franja litoral (malla 1 m, de ~50 m terra endins fins a −50 m), isòbates cada 1 m, línia de costa | COG GeoTIFF (2,8 GB zip), GeoPackage, SHP a [`datacloud.icgc.cat/datacloud/batimetria/`](https://datacloud.icgc.cat/datacloud/batimetria/). [Metadades](https://catalegs.ide.cat/geonetwork/srv/cat/catalog.search#/metadata/batimetria-v2r1-2021-2025) · [Especificacions](https://datacloud.ide.cat/especificacions/batimetria-v2r1-20251124.pdf) | CC BY 4.0 | ✅ Descarregat a `data/raw/` (ràster + isòbates 2021-2025, línia de costa 2021-2024) |
| **ICGC – Ortofoto batimètrica** | Ortofoto de costa a 5 cm (Delta de l'Ebre–el Vendrell i Llavaneres–Cap de Creus) | ECW (25 GB), GeoPackage (48 GB), [WMS](https://www.icgc.cat/en/Geoinformation-and-Maps/Online-services-Geoservices/WMS-Bathymetry) `geoserveis.icgc.cat/servei/catalunya/batimetria/wms` | CC BY 4.0 | Consultar pel WMS; no descarregar sencera |
| **ICGC – Models d'elevacions de costa** | MDT/MDS LiDAR de la franja costanera (50 cm) | GeoTIFF | CC BY 4.0 | Pendent. Útil per a la part emergida: entrades des de costa, penya-segats |
| **[EMODnet Bathymetry (DTM 2024)](https://emodnet.ec.europa.eu/en/bathymetry)** | Batimetria regional de tota la Mediterrània (~115 m, referida a LAT) | 59 tessel·les en GeoTIFF, NetCDF, XYZ des del [visor](https://emodnet.ec.europa.eu/geoviewer/); ERDDAP; WMS/WCS | Gratuïta amb atribució (llicència exacta per verificar) | Pendent. Només per al context més enllà de −50 m |
| **[OpenStreetMap](https://www.openstreetmap.org) / [OpenSeaMap](https://map.openseamap.org)** | Punts d'immersió, derelictes, centres de busseig, balisament | Overpass API. Tags: `sport=scuba_diving`, `scuba_diving:divespot=yes`, `scuba_diving:maxdepth`, `historic=wreck`, `seamark:type=wreck`, `amenity=dive_centre` | ODbL (atribució + compartir igual les bases derivades) | Pendent |
| **Espais protegits (Medes, Cap de Creus...)** | Límits d'ENPE, PEIN i Xarxa Natura 2000 | ArcGIS REST de la Diputació de Barcelona ([ENPE](https://gissrv.diba.cat/arcgis/rest/services/SITXELL/ENPE/MapServer), [PEIN/XN2000/ENPE](https://gissrv.diba.cat/arcgis/rest/services/SITXELL/PEIN_XN2000_ENPE/MapServer)), exportable a GeoJSON | © Generalitat de Catalunya | Pendent. Els límits legals són els dels decrets |
| **Catàlegs de PADI / SSI / altres** | Punts d'immersió amb descripcions | Web | Contingut de tercers, sense llicència oberta | Només com a referència per contrastar a mà. No fer scraping ni redistribuir |
| **Dades pròpies** | POIs i logs d'immersió | CSV / UDDF / FIT, exportats de l'ordinador de busseig | Pròpia | Pendent |

## Stack

- **Python + Jupyter** per a exploració i processament
  - `geopandas`, `shapely`, `pyproj` – vectors i projeccions (ETRS89 / UTM 31N, EPSG:25831)
  - `rasterio`, `rioxarray`, `xarray` – rasters batimètrics, retalls, remostreig
  - `overpy` / `osmnx` – consultes a OSM
  - `matplotlib`, `contourpy` – isòbates i perfils
  - `folium` / `leafmap`, `plotly` / `pydeck` – mapes interactius i 3D
- **MySQL 8** (tipus espacials) – catàleg de punts d'immersió i POIs
- **MongoDB** – fitxes d'immersió i metadades poc estructurades (opcional)
- **InfluxDB** – sèries temporals dels logs d'immersió (profunditat, temperatura vs temps) (opcional)
- **Node.js** – petit visor web amb Leaflet o MapLibre GL
- **Entorn**: WSL + VS Code + GitHub (Actions per a tests i, més endavant, regeneració de mapes)

## Estructura prevista

```
afons/
├── data/
│   ├── raw/            # descàrregues originals (no versionades, a .gitignore)
│   ├── interim/        # dades netejades / reprojectades
│   └── processed/      # productes per immersió
├── notebooks/          # exploració (01_fonts, 02_batimetria, 03_punts...)
├── src/afons/
│   ├── sources/        # connectors: icgc, emodnet, osm...
│   ├── bathy/          # retall, isòbates, perfils, 3D
│   ├── sites/          # model de dades de punts i POIs
│   └── db/             # MySQL / Mongo / Influx
├── web/                # visor Node + Leaflet/MapLibre
├── sql/                # esquema MySQL
├── docker-compose.yml  # MySQL, Mongo, Influx en local
└── README.md
```

## Full de ruta

1. **Exploració de fonts** – notebooks per descarregar una zona de prova (p. ex. illes Medes) des de l'ICGC, EMODnet i OSM, i comparar cobertura i resolució.
2. **Catàleg de punts** – extreure punts d'OSM, revisar-los a mà i desar-los a MySQL.
3. **Producte per immersió** – donat un punt i un radi: mapa d'isòbates, ombrejat, perfil entrada→punt més profund i vista 3D.
4. **POIs** – importar derelictes d'OSM/OpenSeaMap i permetre afegir-ne de propis.
5. **Logs** – importar immersions (UDDF/CSV) a InfluxDB i superposar la traça al mapa.
6. **Visor web** – mapa amb punts clicables que obren la fitxa i el mapa batimètric.

## Llicències i atribució

- Codi: [MIT](LICENSE).
- Dades: cada font manté la seva llicència (ICGC CC BY 4.0, OSM ODbL, EMODnet amb atribució). Les dades derivades s'han de distribuir respectant-les i citant la font:
  - *© Institut Cartogràfic i Geològic de Catalunya (ICGC), CC BY 4.0*
  - *© Col·laboradors d'OpenStreetMap, ODbL*
  - *EMODnet Bathymetry Consortium, EMODnet Digital Bathymetry (DTM)*

---

*Fet a la Costa Brava, amb ganes de veure què hi ha a −30 m abans de baixar-hi.*
