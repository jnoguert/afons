# Marine habitats and protected areas: open sources for the Catalan coast (as of Oct 2026)

Method note: most endpoints below were checked live on 2026-10-24 (GetCapabilities, WFS GetFeature with COUNT/resultType=hits, JSON output, attribute sampling). Statements marked "live check" come from those requests. Statements without that mark come from the cited web pages.

**Access gotcha (live check):** `sig.gencat.cat/ows/*` (GeoServer) has a User-Agent filter. Requests sent with the default curl or `Python-urllib` UA get `ServiceException code="UserAgentFilterError"` ("Accés denegat. El User-Agent no és permès pel filtre de seguretat"). A browser UA or `User-Agent: QGIS/34000` works. Any ETL script must set a UA header.

---

## Q1. Generalitat de Catalunya: marine habitats, seagrass, coralligenous, protected areas, park zoning

### Takeaway
The canonical, highest-value source is the Generalitat's **Mapa dels hàbitats marins de Catalunya** (2021-2024 survey, 0-50 m, the whole coast from Portbou to les Cases d'Alcanar). It is served as **WMS and WFS at `https://sig.gencat.cat/ows/HABITATS/`**, with polygon layers `HABITATS_HABITATS_MARINS` (EUNIS/LPRE level 3-4, with HIC and depth attributes) and `HABITATS_TIPUS_FONS` (seabed type), plus the point layer `HABITATS_MARINS_COM` (EUNIS level 5, for example *Paramuricea clavata* coralligenous). The IDEC metadata gives the licence as **CC0 1.0**. The interactive MapLibre viewer named by the user is just a story map that draws these same WMS layers as raster tiles. It has no vector tiles, PMTiles or GeoJSON of its own. Seagrass ("herbassars"), legacy bionomic maps (Medes, Roses, Baix Empordà), artificial reefs and protected areas are all published as SHP/KMZ/GPKG downloads and through WMS/WFS on `sig.gencat.cat`.

### Cited Findings

**A. Mapa dels hàbitats marins de Catalunya (MHM): the priority source**
- Scope: the whole Catalan coast from Portbou to les Cases d'Alcanar, down to 50 m depth, 189,277 ha, surveyed and processed over 4 years (2021-2024). Products: marine habitats (EUNIS levels 3 and 4), complementary marine habitats (EUNIS level 5), seabed type, an elevation model of the littoral strip, and bathymetry — [mediambient.gencat.cat project page](https://mediambient.gencat.cat/ca/05_ambits_dactuacio/patrimoni_natural/sistemes_dinformacio/habitats/habitats-marins/projecte-mapa-dels-habitats-marins-de-catalunya/)
- Methods: airborne bathymetric LiDAR for the shallow part (to about 15 m); sub-bottom profiler, multibeam echosounder, side-scan sonar, grab samples, dives and ROV imagery for 10-50 m — [project page](https://mediambient.gencat.cat/ca/05_ambits_dactuacio/patrimoni_natural/sistemes_dinformacio/habitats/habitats-marins/projecte-mapa-dels-habitats-marins-de-catalunya/)
- It is part of the Pla Cartogràfic de Catalunya (official reference cartography). The project page lists "Suport a les activitats aquàtiques (submarinisme, navegació...)" as an intended use. Technical specifications were approved by the C4 on 15/07/2020: [habitats marins spec PDF](https://datacloud.ide.cat/especificacions/habitats-marins-v1r0-esp-01ca-20200715.pdf), [tipus de fons marí spec](https://datacloud.ide.cat/especificacions/tipus-fons-mari-v1r0-esp-01ca-20200715.pdf), [batimetria spec](https://datacloud.ide.cat/especificacions/batimetria-v1r0-esp-01ca-20200715.pdf), [elevacions franja litoral spec](https://datacloud.ide.cat/especificacions/elevacions-franja-litoral-v1r0-esp-01ca-20200715.pdf) — [project page](https://mediambient.gencat.cat/ca/05_ambits_dactuacio/patrimoni_natural/sistemes_dinformacio/habitats/habitats-marins/projecte-mapa-dels-habitats-marins-de-catalunya/)
- Viewers: [sig.gencat.cat/visors/habitats_marins.html](https://sig.gencat.cat/visors/habitats_marins.html) and the interactive story map [gencat.cat/mediamb/habitats/mapa-habitats-marins](https://www.gencat.cat/mediamb/habitats/mapa-habitats-marins/index.html)
- **Interactive viewer internals (live check):** the page loads MapLibre GL from unpkg, plus `dist/bundle.js`, `config.js` and `sources.js`. The basemap style is `https://geoserveis.icgc.cat/contextmaps/icgc_orto_estandard.json`. `sources.js` defines four **raster** sources, all built from WMS GetMap with `bbox={bbox-epsg-3857}` and 512 px tiles:
  - `https://sig.gencat.cat/ows/HABITATS/wms?...&layers=HABITATS_HABITATS_MARINS`
  - `https://sig.gencat.cat/ows/HABITATS/wms?...&layers=HABITATS_TIPUS_FONS`
  - `https://geoserveis.icgc.cat/servei/catalunya/batimetria/wms?...&layers=elevacions_franja_litoral`
  - `https://geoserveis.icgc.cat/servei/catalunya/batimetria/wms?...&layers=isobates_100000`
  
  The viewer has no vector tiles, PMTiles or GeoJSON. It is a scrollytelling page (ICGC template) — [sources.js](https://www.gencat.cat/mediamb/habitats/mapa-habitats-marins/sources.js), [config.js](https://www.gencat.cat/mediamb/habitats/mapa-habitats-marins/config.js)
- The viewer text says 26 ecosystems were identified, 4 of which are Habitats of Community Interest: *Posidonia oceanica* meadows, coralligenous, and tunnels and caves. Detritic bottoms dominate by area — [config.js](https://www.gencat.cat/mediamb/habitats/mapa-habitats-marins/config.js); also reported by [Fundació Alive](https://alivefund.org/mapa-dhabitats-marins/)
- **WMS (live check):** `https://sig.gencat.cat/ows/HABITATS/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities` (Fees/AccessConstraints: "none"). Marine layers: `HABITATS_HABITATS_MARINS`, `HABITATS_MARINS_COM`, `HABITATS_TIPUS_FONS`. The same service also holds the terrestrial/HIC layers `HABITATS_INTERES_COMUNITARI`, `HABITATS_TERRESTPOL`, and others — [GetCapabilities](https://sig.gencat.cat/ows/HABITATS/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities)
- **WFS (live check):** `https://sig.gencat.cat/ows/HABITATS/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities`. Feature types: `HABITATS:HABITATS_HABITATS_MARINS` (50,436 MultiPolygons), `HABITATS:HABITATS_MARINS_COM` (1,392 MultiPoints), `HABITATS:HABITATS_TIPUS_FONS` (49,142 MultiPolygons). Native CRS is EPSG:25831. The capabilities advertise only GML 3.2, but `OUTPUTFORMAT=application/json` works (GeoServer), and a full attribute-only download of the habitats layer is about 10.5 MB of JSON — [WFS GetCapabilities](https://sig.gencat.cat/ows/HABITATS/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities)
- **Attributes of `HABITATS_HABITATS_MARINS` (live check):** `NIV_EUNIS, CODI_LPRE3, NOM_LPRE3, CODI_LPRE4, NOM_LPRE4, COD_CORINE, CODI_HIC, CODI_FONS, AMENACA (threatened Y/N), FONDMIT/FONDMIN/FONDMAX (mean/min/max depth, m), CAT_LLEG (legend class), AREA_M2, ID`. Classification: **LPRE** (Lista Patrón de Referencia Estatal = the Spanish IEHM list, EUNIS-aligned codes), cross-walked to HIC (Habitats Directive Annex I) and CORINE. Sampled polygons are around 100 m² (fine-scale) — [WFS](https://sig.gencat.cat/ows/HABITATS/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=HABITATS:HABITATS_HABITATS_MARINS&COUNT=2&OUTPUTFORMAT=application/json)
- **Classes present in `HABITATS_HABITATS_MARINS` and their summed AREA_M2 (live check, my tally of all 50,436 features)** — [WFS](https://sig.gencat.cat/ows/HABITATS/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities):
  - 30102 Roca infralitoral superior moderadament exposada (HIC 1170): 1,627 polys, ~1,096 ha
  - 30103 Roca infralitoral superior protegida (1170): 710, ~371 ha
  - 30104 Roca infralitoral inferior (1170): 2,338, ~635 ha
  - 30201 Roca circalitoral dominada per algues (1170): 76, ~37 ha
  - 3020104 Coral·ligen amb dominància d'algues (1170): 144, ~41 ha
  - 30202 Roca circalitoral dominada per invertebrats (1170): 4,166, ~490 ha
  - 3020225 Coral·ligen amb dominància d'invertebrats (1170): 862, ~209 ha
  - **30302 Túnels i coves fosques (HIC 8330): only 1 polygon, ~0.5 ha**
  - 30401 Còdols i graves: 389, ~131 ha; 30402 Sorres: 9,782, ~52,123 ha; 30403 Fangs: 8,942, ~108,249 ha; 30405 Detrítics biògens: 482, ~16,725 ha; 3040506 Maërl (grapissar): 83, ~4,167 ha
  - 30509 Alguers de *Cymodocea nodosa*: 13,411, ~1,667 ha
  - **30512 Alguers de *Posidonia oceanica* (HIC 1120*): 5,630, ~4,498 ha**; 3051203 Mata morta de Posidonia: 242, ~84 ha
  - 30513 Alguers en badies i llacunes / Caulerpa (1130): 707, ~1,309 ha
  - 70102 Objectes antròpics: 92; 70108 Espigons / substrats durs de ports: 277; 70201/70202 port muds / beach nourishment sands
- **`HABITATS_MARINS_COM` (EUNIS level 5, points, live check):** 1,259 points "302022501 Coral·ligen amb *Paramuricea clavata*" (AMENACA = Si); 129 "Fons circalitorals rocosos ... amb *Leptogorgia sarmentosa*/*Eunicella verrucosa*"; 2 "*Eunicella singularis*"; 2 "Herbeis de *Caulerpa cylindracea*" (invasive). These are direct candidate points for gorgonian and coralligenous dive POIs — [WFS](https://sig.gencat.cat/ows/HABITATS/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=HABITATS:HABITATS_MARINS_COM&COUNT=2&OUTPUTFORMAT=application/json)
- **`HABITATS_TIPUS_FONS` attributes (live check):** `CODI_FONS, DES_FONS, GRUIX, RUGOSITAT, TEXTURA` (acoustic texture), `INT_RETROD` (backscatter intensity), `AREA_M2, ID` — [WFS](https://sig.gencat.cat/ows/HABITATS/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=HABITATS:HABITATS_TIPUS_FONS&COUNT=2&OUTPUTFORMAT=application/json)
- **IDEC metadata record** `mapa-habitats-marins`: formats CSV and SHP; access constraints "Sense limitacions"; licence **CC0 1.0 Universal** (`creativecommons.org/publicdomain/zero/1.0/`); responsible body: Departament de Territori, Habitatge i Transició Ecològica; record date 2025-11-14 — [IDEC record (XML)](https://catalegs.ide.cat/geonetwork/srv/api/records/mapa-habitats-marins/formatters/xml). The record's online resources point only to the viewer and the project page. It gives no direct ZIP link.
- **Bathymetry v2.1 (2021-2025)**, from the same programme. ICGC WMS: `https://geoserveis.icgc.cat/servei/catalunya/batimetria/wms` (layers used by the viewer: `elevacions_franja_litoral`, `isobates_100000`). Resolution values in the metadata: 1 m and 5 m. Licence **CC BY 4.0**. Metadata ZIP: `https://datacloud.ide.cat/metadades/batimetria-v2r1-metadades.zip`; spec: `https://datacloud.ide.cat/especificacions/batimetria-v2r1-20251124.pdf` — [IDEC record](https://catalegs.ide.cat/geonetwork/srv/api/records/batimetria-v2r1-2021-2025/formatters/xml), [ICGC Batimetria page](https://www.icgc.cat/ca/Geoinformacio-i-mapes/Dades-i-productes/Bessons-digitals-Elevacions/Batimetria)

**B. Seagrass meadows: "Herbassars o praderies de fanerògames marines" (DACC / DG Política Marítima i Pesca Sostenible)**
- Content: polygons of the known seagrass meadows (*Posidonia oceanica*, *Cymodocea nodosa*, *Zostera noltei*, *Zostera marina*) along the Catalan coast, plus 5 m and 20 m influence buffers. The cartography is "indicative" and informative. Last update **16.10.2026**. It integrates the Mapa dels Hàbitats Marins with earlier specific studies (the DGPMPS's Cartografia d'Herbassars Marins), harmonised and expert-reviewed. CRS UTM 31N ETRS89 — [agricultura.gencat.cat herbassars page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/herbassars-praderies-fanerogames-marines/)
- Attributes: `OBJECT_ID, COMUNITAT` (Posidonia / Cymodocea / mata morta / altres), `CODI_LPRE3/NOM_LPRE3, CODI_LPRE4/NOM_LPRE4, CODI_HIC, CODI_CORINE, AMENAÇA, AREA_M2, PROMOTOR, FONT_DADES, DATA_DADES` — [same page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/herbassars-praderies-fanerogames-marines/)
- Direct downloads: `https://www.gencat.cat/agricultura/sig/bases/GestioHerbassars.zip` (SHP), `.../GestioHerbassars_gpkg.zip` (GPKG), `.../GestioHerbassars.kmz`; buffers `.../AI5Herbassars.zip|.kmz`, `.../AI20Herbassars.zip|.kmz`. Tech spec PDF: `/web/.content/12-serveis/bases-cartografiques/enllacos-documents/generics/fitxers-binaris/gestio-herbassars.pdf` — [same page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/herbassars-praderies-fanerogames-marines/)
- WMS/WFS (live check): `https://sig.gencat.cat/ows/ORDENACIO_ESPAI_MARITIM/wms|wfs`, layers `VEGETACIO_GESTIOHERBASSARS`, `VEGETACIO_AI5HERBASSARS`, `VEGETACIO_AI20HERBASSARS` — [WMS GetCapabilities](https://sig.gencat.cat/ows/ORDENACIO_ESPAI_MARITIM/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities)
- The IDEC record `herbassars` lists SHP/MMZX/KMZ and a scale denominator of 1,000. Related IDEC records exist for "Grau de fiabilitat dels herbassars" and "Herbassars. Zones d'envolvents" — [IDEC CSW search](https://catalegs.ide.cat/geonetwork/srv/cat/csw?service=CSW&version=2.0.2&request=GetRecords&typeNames=csw:Record&resultType=results&elementSetName=full&constraintLanguage=CQL_TEXT&constraint=AnyText%20like%20'%25herbassars%25')
- The data serves the FANCAT "fondeig respectuós" (respectful anchoring) programme — [herbassars page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/herbassars-praderies-fanerogames-marines/)

**C. Other DACC marine bases (agricultura.gencat.cat "Pesca marítima i protecció del litoral")** — index: [pesca-maritima-proteccio-litoral](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/)
- **Mapa bionòmic de les Illes Medes:** marine and terrestrial communities, bathymetry, toponymy and marine geological features. Digitised (Dec 1999) from paper maps at about 1:5,000, based on Ros, Olivella & Gili 1984 (IEC). Classes include coralligenous, precoralligenous, "Fàcies de *Paramuricea*", Posidonia, and coralligenous platform. SHP: `/web/.content/12-serveis/bases-cartografiques/enllacos-documents/bases-cartografiques/fitxers-binaris/mapa-bionomic-illes-medes.zip` (+ .kmz) — [page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/mapa-bionomic-illes-medes/)
- **Cartografia bionòmica Badia de Roses:** infralittoral communities from side-scan sonar, coast to about -25 m, 3,350 ha (Castelló d'Empúries, L'Escala, Roses, Sant Pere Pescador), Aug 2018. SHP `.../cartografia-bionomica-badia-roses.zip`. WMS/WFS layer `OEM_CARTOBIONBADIAROSES` — [page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/cartografia-bionomica-badia-roses/)
- **Cartografia bionòmica Baix Empordà** (Natura 2000 area, Begur-Palafrugell-Mont-ras-Palamós): side-scan sonar, 0 to -35 m, 1,181 ha, Dec 2019. SHP `.../cartografia-bionomica-baix-emporda.zip`. WMS/WFS layer `OEM_CARTOBIONBAIXEMP`. IDEC record `oem-cartobionbaixemp` at scale 1:5,000 — [page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/cartografia-bionomica-baix-emporda/)
- **Esculls artificials** (artificial reefs; possible dive POIs): polygons with name, promoter, status, year, area. Feb 2001, from IHM charts at about 1:50,000. SHP `.../esculls-artificials.zip`. Layer `OEM_ESCULLSARTIFICIALS` — [page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/esculls-artificials/)
- **Elements i zones prohibides a la navegació** (anchoring prohibited, restricted zones, submarine cables/pipelines, "zona de prohibició d'ancoratge i pesca"), digitised from IHM nautical charts, Feb 2001. SHP `.../elements-zones-prohibides-navegacio.zip`. Layers `OEM_LIMITSDIV_IHM_LIN|POL|PUNT` — [page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/elements-zones-prohibides-navegacio/)
- **Cartografia d'hàbitats marins EUNIS 2019 (litoral):** despite the name, it covers only the **supralittoral to about -1 m** strip (coastline segments of at least 10 m, mapped at 1:1,500 from a 2010-2011 boat survey; CEAB-CSIC + ICGC; update 2016). It includes 143 rocky-shore transects and 47 beach characterisations. KMZ `/web/.content/12-serveis/bases-cartografiques/enllacos-documents/bases-cartografiques/fitxers-binaris/habitats-litorals.kmz`; MiraMon base; ICES metadata link. WMS/WFS layer `OEM_EUNIS_2019` — [page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/habits-marins/)
- **Full ORDENACIO_ESPAI_MARITIM service (live check):** WMS and WFS at `https://sig.gencat.cat/ows/ORDENACIO_ESPAI_MARITIM/wms|wfs`. Layers include `OEM_CARTOBIONBADIAROSES, OEM_CARTOBIONBAIXEMP, OEM_ESCULLSARTIFICIALS, OEM_EUNIS_2019, OEM_LIMITSDIV_IHM_*, OEM_PESCARECREATIVA, OEM_PESCAMARINARECREATIVA, OEM_BATIMETRIA_IHM, OEM_BATIMETRIAGEBCO, OEM_LINIACOSTA_LMUNIC, OEM_ZON_BIO, OEM_CIN_BIO, OEM_CT_BIO, VEGETACIO_*HERBASSARS` — [WFS GetCapabilities](https://sig.gencat.cat/ows/ORDENACIO_ESPAI_MARITIM/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities)

**D. Protected areas from the Generalitat (beyond DIBA)**
- The DACC "Espais naturals" page links, for PEIN, Xarxa Natura 2000, ENPE, ZEPIM, RAMSAR and others, to "Consulta i descàrrega des de l'Hipermapa" (for example `https://sig.gencat.cat/visors/hipermapa.html#...&layers=ESPAISNATURALS_PEIN`) and to sig.gencat.cat metadata (PEIN uuid `TMP0000A_80766`, XN2000 `TMP0000A_28468`, ENPE `TMP0000A_82047`, ZEPIM `f8ed0943-..._ZEPIM_Catalunya`). It also has a section "Espais Natura 2000 d'àmbit marí a Catalunya competència de l'AGE" — [agricultura.gencat.cat espais naturals](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/espais-naturals/)
- **WMS/WFS (live check):** `https://sig.gencat.cat/ows/ESPAIS_NATURALS/wms|wfs`. Relevant layers: `ESPAISNATURALS_PEIN, ESPAISNATURALS_XARNAT_2000, ESPAISNATURALS_ENPE, ESPAISNATURALS_PARCSNATURALS, ESPAISNATURALS_ZEPA_LIC_MARI, ESPAISNATURALS_ZEPIM, ESPAISNATURALS_NAT2000_AMP` (N2000 enlargements), `ESPAISNATURALS_RES_BIOSFERA, ESPAISNATURALS_ESPAISINTGEOL` (geological interest sites) — [WMS GetCapabilities](https://sig.gencat.cat/ows/ESPAIS_NATURALS/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities)
- `ESPAISNATURALS_ENPE` / `PARCSNATURALS` attributes (live check): `CODI_ESPAI` (pnat, rni, rnp...), `NOM_ESPAI, ESCALA_DEL` (delineation scale), `NOM_PNAT/NOM_PNIN/NOM_RNI/NOM_RNP...`, `ANY_APROV, NORMATIVA, LINK_NORM` (DOGC PDF), `AMBIT` (Terrestre/Marí), `CODI_CDDA, AREA_HA`. **Features with AMBIT = Marí:** Parc Natural de Cap de Creus (1:5,000), Reserva Natural Integral del Cap de Creus (1:5,000), RNP Cap Gros-Cap de Creus (1:5,000), RNP Cap de Norfeu (1:5,000), Parc Natural del Montgrí, les Illes Medes i el Baix Ter (1:50,000), **Reserva Natural Parcial marina de les Medes (1:50,000)**, **Zona perifèrica de protecció de la RNP marina de les Medes (1:50,000)**, Parc Natural del Delta de l'Ebre (1:50,000) — [WFS](https://sig.gencat.cat/ows/ESPAIS_NATURALS/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities)
- `ESPAISNATURALS_ZEPA_LIC_MARI` (7 features, live check): state-competence marine N2000. LIC ESZZ16001 "Sistema de canons submarins occidentals del golf de Lleó"; ZEPA ES0000514 "Espai marí de l'Empordà"; ZEPA ES0000512 "Espai marí del Delta de l'Ebre - Illes Columbretes"; ZEPA ES0000513 "Espai marí del Baix Llobregat - Garraf"; LIC/ZEPA ESZZ16016 "Espai Marí de la Costa Central Catalana" — [WFS](https://sig.gencat.cat/ows/ESPAIS_NATURALS/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities)
- **INSPIRE PEIN service (ICGC/IDEC):** WMS `https://geoserveis.ide.cat/servei/catalunya/inspire-pla-espais-interes-natural/wms`, ATOM `https://geoserveis.ide.cat/servei/catalunya/inspire-pla-espais-interes-natural/atom/inspire-pla-espais-interes-natural.atom.xml`, OGC API Features `https://geoserveis.ide.cat/servei/catalunya/inspire/ogc/features` — [IDEC CSW search](https://catalegs.ide.cat/geonetwork/srv/cat/csw?service=CSW&version=2.0.2&request=GetRecords&typeNames=csw:Record&resultType=results&elementSetName=full&constraintLanguage=CQL_TEXT&constraint=AnyText%20like%20'%25marins%25')
- **PEIN v1.0 (May 2026)**: IDEC record `espais-interes-natural-v1r0-202605`, scales 1:5,000 and 1:50,000, licence **CC BY 4.0** — [IDEC record](https://catalegs.ide.cat/geonetwork/srv/api/records/espais-interes-natural-v1r0-202605/formatters/xml)
- Natura 2000 v1.1 (Oct 2019) IDEC record: formats MMZX, SHP, GML, CSV, KML; licence CC BY 4.0, "noLimitations" — [IDEC record](https://catalegs.ide.cat/geonetwork/sidl/api/records/natura-2000-v1r1-201910)
- General Generalitat open-data licence page (I did not open it to check its exact terms): [administraciodigital.gencat.cat llicències](https://administraciodigital.gencat.cat/ca/dades/dades-obertes/informacio-practica/llicencies/)

**E. Park zoning and diving regulation (Medes, Cap de Creus)**
- Medes: use is governed by the Pla rector d'ús i gestió (Decret 222/2008). Ordre AAM/112/2015 amended annexes 1 and 6 and set annual dive caps per buoy/zone, moving to adaptive management with annual and simultaneous maximums per dive zone — [Govern 2016 note PDF](https://govern.cat/govern/docs/2016/10/17/11/35/6603537a-491e-42e1-87bd-8d7f2453e341.pdf), [vlex Ordre AAM/112/2015](https://vlex.es/vid/ordre-aam-112-2015-568788818), [UB diagnosis of diving effects](https://diposit.ub.edu/items/1e9e5758-7dd3-4810-9d07-4cecc840bfdd/full)
- Cap de Creus marine area: about 3,056 ha in three protection levels: park zone about 2,237 ha, two partial reserves (Cap Gros-Cap de Creus, Cap de Norfeu, about 800 ha) and the integral reserve s'Encalladora (about 20.6 ha). The draft PRUG (2022 consultation) has a diving annex with no fixed caps ("adaptive planning") and about 268 ha of "zones de dinàmica natural" (no-take) — [participa.gencat.cat PRUG memòria](https://participa.gencat.cat/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBc1VOIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--e548f4234f8f89e65bb30376a98dd4799f6c534f/memoria-general.pdf), [comments (Garrabou 2022)](https://participa.gencat.cat/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdXMwIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--1b4001b8ac512d43733c6dadb1b68d3cd3529c9d/Comentaris%20PRUG%20Garrabou%202022.pdf)
- The reserve polygons (RNI Cap de Creus, RNP Cap Gros-Cap de Creus, RNP Cap de Norfeu, RNP marina de les Medes plus its peripheral zone) **are** available as GIS in `ESPAISNATURALS_ENPE` (see D above).

### Inferences
- For a dive-POI app, the MHM WFS (`HABITATS_HABITATS_MARINS` filtered to CODI_HIC 1170/1120*/8330 and the coralligenous classes, plus `HABITATS_MARINS_COM` points) is the best single source. It has depth attributes (FONDMIN/FONDMAX), so polygons can be filtered to recreational depth, and the CC0 licence allows redistribution without conditions. Citing the Generalitat is still good practice.
- The interactive viewer adds no data of its own beyond WMS. Bulk vector access means using WFS paging (`COUNT`/`STARTINDEX`, about 50k features) or asking DTHTE for the SHP/CSV listed in the IDEC metadata.
- The Medes marine reserve boundary in ENPE is delineated at 1:50,000. That is too coarse for exact in-water boundary checks, so it should be shown only as indicative.
- The herbassars layer (updated 16.10.2026) is more recent and more consolidated for seagrass than the MHM habitat polygons. Use it as the primary seagrass layer (for anchoring-sensitive zones) and use MHM for rocky/coralligenous bottoms.

### Gaps
- No official GIS was found for the Medes **dive buoys / dive zones** (the per-zone caps in Ordre AAM/112/2015) or for Cap de Creus diving zones. These seem to exist only as annex maps in DOGC/PRUG PDFs. Ses Negres (Begur) and Masia Blanca (El Vendrell) marine reserves were not verified as separate layers. They are probably inside PEIN/XN2000 polygons, or are fishing-regulation reserves under DACC, but this was not confirmed.
- I found no direct ZIP download URL for the MHM. The IDEC record lists CSV/SHP but links only to viewers. Hipermapa download for the `HABITATS_*` layers was not tested.
- The CC0 licence comes from the IDEC record for MHM. The herbassars and bionomic pages state no explicit licence (their IDEC records just say "otherRestrictions").

---

## Q2. IDEC / ICGC geoservices: catalogue, coastal/seabed geology, caves

### Takeaway
The IDEC catalogue (GeoNetwork CSW at `catalegs.ide.cat/geonetwork/srv/cat/csw`) indexes all of the above. The ICGC contributes the bathymetry/topobathymetric services (CC BY 4.0). No submarine-cave layer was found in IDEC/ICGC. The only cave-like class in official cartography is a single "Túnels i coves fosques" polygon in the MHM.

### Cited Findings
- The IDEC CSW works anonymously with CQL `AnyText like '%...%'`. The GeoNetwork JSON search API (`/srv/api/search/records/_search`) returned HTTP 403 without a session (live check) — [CSW example](https://catalegs.ide.cat/geonetwork/srv/cat/csw?service=CSW&version=2.0.2&request=GetRecords&typeNames=csw:Record&resultType=results&elementSetName=full&constraintLanguage=CQL_TEXT&constraint=AnyText%20like%20'%25marins%25')
- Records found for "fons marí": AMB "Batimetria multifeix metropolitana", "Model d'elevacions topobatimètric metropolità" and "Cartografia topobatimètrica metropolitana" (AMB Geoportal), and an ICGC sediment-cover protocol for the Catalan littoral (`https://datacloud.icgc.cat/datacloud/descarregues-web/bd/litoral/documentacio/icgc_CG_0001_25.pdf`) — [CSW search](https://catalegs.ide.cat/geonetwork/srv/cat/csw?service=CSW&version=2.0.2&request=GetRecords&typeNames=csw:Record&resultType=results&elementSetName=full&constraintLanguage=CQL_TEXT&constraint=AnyText%20like%20'%25fons%20mar%C3%AD%25')
- A municipal "Hàbitats de Castelló d'Empúries" geoportal is also indexed: `https://www.castello.cat/geoportal/habitats.html` — [CSW search](https://catalegs.ide.cat/geonetwork/srv/cat/csw?service=CSW&version=2.0.2&request=GetRecords&typeNames=csw:Record&resultType=results&elementSetName=full&constraintLanguage=CQL_TEXT&constraint=AnyText%20like%20'%25herbassars%25')
- `ESPAISNATURALS_ESPAISINTGEOL` (Inventari d'espais d'interès geològic) is on the ESPAIS_NATURALS WMS/WFS (metadata uuid `TMP0000A_08901`) and could contain coastal/karst sites. It was not checked for submarine caves — [agricultura.gencat.cat espais naturals](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/espais-naturals/)

### Inferences
- "Geologia del fons marí" as such does not appear as a separate ICGC product. The MHM "tipus de fons" layer (with backscatter, rugosity and texture) is effectively the modern seabed-substrate map.

### Gaps
- No IDEC record for submarine caves was found. I did not query the ICGC geological WMS (`icgc_mg50m` is referenced in viewer comments) for coastal geology.

---

## Q3. MITECO (Spanish state)

### Takeaway
MITECO provides authoritative downloads for the **Red de Áreas Marinas Protegidas (RAMPE 2025: SHP/KMZ/GeoJSON)** and **Red Natura 2000 (GML 2025)**. Its re-use terms are "free re-use citing the source" (Ley 37/2007). **There are no MITECO Ecocartografías for Catalonia** (the list covers only Valencia/Murcia/Andalucía/Baleares/Canarias provinces). The IEHM is a classification list with habitat factsheets (PDF), not a map. The IEPNB GeoServer (WMS) was down when I checked.

### Cited Findings
- Ecocartografías index lists Alicante, Almería, Baleares, Castellón, Cádiz, Granada, Las Palmas, Murcia, Málaga, Santa Cruz de Tenerife and Valencia. **It has no Girona, Barcelona or Tarragona entry** (live check) — [MITECO ecocartografías](https://www.miteco.gob.es/es/costas/temas/proteccion-costa/ecocartografias.html)
- RAMPE downloads: `/content/dam/miteco/es/biodiversidad/temas/biodiversidad-marina/rampe/Rampe_2025_shape.zip`, `Rampe_2025.kmz`, `Rampe2025_geojson.zip`, data dictionary `rampe2025_dd.xlsx` (prefix `https://www.miteco.gob.es`) — [RAMPE page](https://www.miteco.gob.es/es/biodiversidad/temas/biodiversidad-marina/espacios-marinos-protegidos/red-areas-marinas-protegidas-espana/bm_emprot_rampe_espacios.html)
- Red Natura 2000: `/content/dam/miteco/es/biodiversidad/servicios/banco-datos-naturaleza/3-rn2000/PS.Natura2000_2025_gml.zip` (INSPIRE PS GML), data dictionary `rn2000-dd.xlsx`, metadata at `mapama.gob.es/ide/metadatos ... 0d427e21-be52-4723-b78e-8b00a43319cb` — [RN2000 descargas](https://www.miteco.gob.es/es/biodiversidad/servicios/banco-datos-naturaleza/informacion-disponible/rednatura2000_descargas.html)
- The BDN quick-access table also links ENP (`ENP_Descargas.html`), ZEPIM (`zepim_descargas.html`), "Mallas marinas", and IEHM/IEEM lists — [Acceso rápido a los datos](https://www.miteco.gob.es/es/biodiversidad/servicios/banco-datos-naturaleza/acceso-rapido-datos.html)
- The IEHM "download" page holds the LPRE list and per-habitat factsheet PDFs (for example "Praderas de *Posidonia oceanica*", "Roca circalitoral dominada por invertebrados", "Túneles y cuevas semioscuras infralitorales y circalitorales"). I saw no spatial layer — [IEHM list page](https://www.miteco.gob.es/es/biodiversidad/temas/biodiversidad-marina/habitats-especies-marinos/inventario-espanol-habitats-especies-marinos/list-inventario-habitats-marinas.html). The LPRE was adopted by Resolución of 22 March 2013 — [IEHEM page](https://www.miteco.gob.es/es/biodiversidad/temas/biodiversidad-marina/habitats-especies-marinos/inventario-espanol-habitats-especies-marinos/inventario-habitats-especies.html)
- WMS catalogue (BDN): `https://geoserver.iepnb.es/geoserver/areas_marinas_protegidas/rampe/wms`, `.../RN2000/rn2000/wms`, `.../ENP/enp/wms`, `.../convenio_internacional/ZEPIM/wms`, `.../ecosistemas/habitats_art17_2013_2018/wms` — [Servidor cartográfico WMS](https://www.miteco.gob.es/es/biodiversidad/servicios/banco-datos-naturaleza/servidor-cartografico-wms-.html). Live check on 2026-10-24: every one returned "no healthy upstream" (a temporary outage, or the service has moved).
- Re-use terms: MITECO web content "puede ser utilizada en parte o en su integridad, sin necesidad de autorización expresa, siempre que se cite la fuente", under Ley 37/2007 / RD 1495/2011. Conditions: do not alter the data's meaning, do not imply endorsement, and keep update metadata — [MITECO aviso legal](https://www.miteco.gob.es/es/atencion-al-ciudadano/aviso-legal.html)

### Inferences
- The MHM already uses LPRE codes, so it is directly interoperable with the IEHM classification.
- For marine N2000 in Catalan waters, the Generalitat WFS layer `ESPAISNATURALS_ZEPA_LIC_MARI` mirrors the state sites. For legal accuracy, use the MITECO GML 2025 as the canonical source.

### Gaps
- No INDEMARES cartography specific to Catalonia (Cap de Creus canyon) was found as a download in this pass.
- The MITECO datasets' licence is "re-use with attribution" under the legal notice. I found no explicit CC BY 4.0 tag on the RAMPE/RN2000 pages.

---

## Q4. EU and international sources

### Takeaway
EMODnet Seabed Habitats is CC BY 4.0 and gives Mediterranean-wide layers. In Catalan waters, though, its seagrass polygons come from an old IFREMER/EUSeaMap compilation and its coralligenous coverage is almost empty, so the Generalitat MHM is far better locally. **WDPA (Protected Planet) prohibits redistribution and commercial use. MAPAMED is CC BY-NC-SA 4.0.** Avoid both as redistributable app data.

### Cited Findings
- EMODnet SBH WMS endpoints: `https://ows.emodnet-seabedhabitats.eu/geoserver/emodnet_view/wms` and `.../emodnet_view_maplibrary/wms` — [EMODnet SBH guidance (GitHub)](https://github.com/emodnetseabedhabitats/EMODnetSBH-Guidance)
- `emodnet_view` layer names (live check): `seagrass_eov_poly_2025`, `seagrass_eov_points_2025`, `coralligenous_platforms_poly_2025`, `coralligenous_platforms_points_2023`, `eusm2025_eunis2019_full` (and the `_200/_400/_800` simplifications), `eusm2025_msfd_full`, `eusm2025_subs_full`, Article 17 grids `a17_1120`, `a17_1170`, `art17_hab_1120`, `art17_hab_1170` — [emodnet_view GetCapabilities](https://ows.emodnet-seabedhabitats.eu/geoserver/emodnet_view/ows?SERVICE=WMS&REQUEST=GetCapabilities&VERSION=1.3.0)
- `emodnet_view_maplibrary` layer names (live check): `mediseh_posidonia` (modelled occurrence probability of *P. oceanica*, MEDISEH), `mediseh_cora` (coralligenous), `mediseh_maerl` — [maplibrary GetCapabilities](https://ows.emodnet-seabedhabitats.eu/geoserver/emodnet_view_maplibrary/ows?SERVICE=WMS&REQUEST=GetCapabilities&VERSION=1.3.0)
- Metadata (ICES GeoNetwork): coralligenous 2025 `c94bdb30-4a72-4cf2-a990-fb5778104ce7`, seagrass EOV 2025 `39746d9c-4220-425c-bc26-7cb3056c36a5`, EUSeaMap 2025 `cec07b5e-3a9c-4492-b115-126a17c08697` — [emodnet_view GetCapabilities](https://ows.emodnet-seabedhabitats.eu/geoserver/emodnet_view/ows?SERVICE=WMS&REQUEST=GetCapabilities&VERSION=1.3.0)
- WFS on `emodnet_view` supports JSON (live check). In a Catalonia bbox (40.5-42.42 N, 0.5-3.35 E): `seagrass_eov_poly_2025` has **94 polygons, all from map_id "EUSM16me", determiner "MV, IFREMER", 2016-09-20**; `coralligenous_platforms_poly_2025` has **1 polygon** — [WFS endpoint](https://ows.emodnet-seabedhabitats.eu/geoserver/emodnet_view/wfs?service=WFS&version=2.0.0&request=GetCapabilities)
- Licence: EMODnet Seabed Habitats products are credited "Licensed under CC-BY 4.0 from the European Marine Observation and Data Network (EMODnet) Seabed Habitats initiative" — [marine.gov.scot EMODnet SBH copyright](https://marine.gov.scot/copyright/emodnet-seabed-habitats-consortium)
- MEDISEH source layers on D4Science need a login — [D4Science CKAN](https://ckan-d4s1.d4science.org/dataset/posidonia-oceanica-meadows-distribution-historical-distribution-polygons1)
- WDPA: commercial use (broadly defined, including revenue-generating non-profits) needs prior written permission from UNEP-WCMC. **Redistribution in whole or in part through web downloads, web services or interactive maps offering download is prohibited** without permission — [Protected Planet terms](https://protectedplanet.net/c/terms-and-conditions)
- MAPAMED: licence **CC BY-NC-SA 4.0**. Commercial use needs written permission from SPA/RAC and MedPAN. The 2021 edition covers 1,320 sites (1,126 MPAs) — [mapamed.org](https://mapamed.org/), [MAPAMED user manual](https://www.mapamed.org/data/2021-04_MAPAMED_user_manual_ENG.pdf)

### Inferences
- EMODnet is useful only as an offshore fallback (EUSeaMap substrate/biozone beyond 50 m) or for cross-border continuity. Inside 50 m in Catalonia, the MHM outperforms it.
- For protected areas, use Generalitat ENPE/PEIN/XN2000 (CC BY 4.0) and MITECO RN2000/RAMPE rather than WDPA or MAPAMED, both of which come with redistribution restrictions.

### Gaps
- EEA Natura 2000 / CDDA download licence was not checked in this pass. EEA data is generally CC BY 4.0, but this is unverified here.

---

## Q5. Underwater caves (coves submarines)

### Takeaway
There is no open GIS inventory of Catalan submarine caves. The official MHM has a single "Túnels i coves fosques" (HIC 8330) polygon. Literature exists for the Medes caves (IEC, UB), but none of it is a dataset with coordinates.

### Cited Findings
- MHM class 30302 "Túnels i coves fosques" (HIC 8330): 1 polygon, about 0.5 ha (live check) — [HABITATS WFS](https://sig.gencat.cat/ows/HABITATS/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities)
- Bibiloni, Gili & Ros (IEC) proposed a classification of submarine cavities and studied the Medes cave system in detail (a closed cave and a large tunnel) — [IEC publication PDF](https://publicacions.iec.cat/repository/pdf/00000353\00000012.pdf)
- UB monitoring of bryozoans, red gorgonian and caves in the Medes reserve (2015 report) — [UB dipòsit](https://diposit.ub.edu/dspace/bitstream/2445/120282/1/Briozous%202015.pdf)
- The 1999 Medes bionomic map includes "altres accidents geològics marins", which could include caves (not verified) — [Mapa bionòmic Medes page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/mapa-bionomic-illes-medes/)

### Inferences
- Cave POIs will have to come from diving-centre/crowd sources or be digitised from literature, then checked against the MHM rocky-substrate polygons.

### Gaps
- No speleology federation (FCE) or CSIC submarine cave inventory was found. Named caves (Cova de la Reina, Cova del Bisbe) were not located in any dataset.

---

## Q6. Open scientific datasets (Posidonia / coralligenous)

### Takeaway
I found no Catalonia-specific open Posidonia/coralligenous dataset on Zenodo/PANGAEA/Digital.CSIC in this pass. The Generalitat herbassars layer already integrates research-centre cartographies (its `PROMOTOR`/`FONT_DADES` fields keep the provenance).

### Cited Findings
- The herbassars layer harmonises the MHM with cartographies from research centres and public institutions, with per-polygon source and date fields — [herbassars page](https://agricultura.gencat.cat/ca/serveis/cartografia-sig/bases-cartografiques/pesca-maritima-proteccio-litoral/herbassars-praderies-fanerogames-marines/)
- Mediterranean-wide MEDISEH compilation: known current Posidonia area 1,224,707 ha and about 34% regression over 50 years (Telesca et al. 2015) — [Sci Rep / PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4516961/)

### Inferences
- Querying `FONT_DADES` in GestioHerbassars would show which CEAB/UB/ICM studies were folded in, which avoids hunting for the papers separately.

### Gaps
- Zenodo, PANGAEA, Digital.CSIC, Seagrass-Watch and the Xarxa de Vigilància de Praderies de Posidònia were not searched individually because of the tool budget. This needs a follow-up if monitoring-station points are wanted.
