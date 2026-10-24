# Open sources for shipwrecks, underwater heritage and artificial reefs on the Catalan coast (state as of Oct 2026)

Method note: besides web research, live queries were run on 2026-10-24 against Overpass API, Wikidata SPARQL, EMODnet WFS and IHM WMS (bbox lat 40.5–42.45, lon 0.15–3.35). The counts below are from those runs.

## 1. CASC / Generalitat Patrimoni Cultural: underwater inventory, coordinates, WMS, legal limits

### Takeaway
Catalonia has about 876 registered underwater archaeological sites. No open, downloadable dataset of them with coordinates was found. The Generalitat inventory point layer (PATRIMONI_JAC_PUNT) has a WMS on an intranet host. Coordinates do get published in two places: Diputació de Barcelona municipal heritage cards (patrimonicultural.diba.cat), and BCIN declarations in the DOGC/BOE, which give exact UTM positions and polygons. Illes Formigues II (BCIN, July 2026) is the first underwater example. Under UNESCO 2001 Art. 19(3), location data shared between states is kept confidential while disclosure could endanger a site. Looting is on the rise. For both reasons, an open project should not republish archaeological site points beyond what officials have already published.

### Cited Findings
- 3Cat (published 3 Jun 2026, updated 22 Jun 2026) reports 876 registered underwater archaeological sites in Catalonia. The Mossos say looting has grown over the past two years, involving organised networks; this year 15 people were inspected, 6 investigated and 5 face proposed sanctions — [3Cat](https://www.3cat.cat/3catinfo/augmenta-lespoli-arqueologic-subaquatic-a-catalunya-amb-mes-de-800-jaciments/noticia/3412803/)
- The Generalitat SIG catalogue has a metadata record "Inventari del Patrimoni Arqueològic i Paleontològic de Catalunya (Punt)" (id PATRIMONI_JAC_PUNT_Metadata, Departament de Cultura, data date 2021-01-28). Per the search-result summary it lists the WMS at `http://sig.intranet.gencat.cat/ows/PATRIMONI_CULTURAL/wms`, which is an intranet host. I could not confirm external access: the PDF is compressed and my test requests to sig.gencat.cat/ows/... were rejected by a User-Agent filter or returned 404 — [sig.gencat.cat metadata PDF](https://sig.gencat.cat/geonetwork/srv/cat/pdf?id=2304); [record](https://sig.gencat.cat/geonetwork?uuid=PATRIMONI_JAC_PUNT_Metadata)
- The Diputació de Barcelona's municipal heritage cards include some coastal and underwater entries with lat/lon and UTM. Example: a Sitges card gives 41.2525, 1.8999 / UTM 407832, 4567374 and notes that CASC holds 17 records of finds there (Roman, medieval, contemporary) without a confirmed site — [patrimonicultural.diba.cat node 68565](https://patrimonicultural.diba.cat/print/pdf/node/68565)
- Cabrera de Mar cards say some sites are known through clandestine looting and describe locations as a "mooring area" with no precise position — [diba node 41887](https://patrimonicultural.diba.cat/print/pdf/node/41887); [diba node 41888](https://patrimonicultural.diba.cat/print/pdf/node/41888)
- **Illes Formigues II, the first underwater BCIN.** Acord GOV/211/2026 of 28 Jul 2026 (BOE-A-2026-18424, 1 Sep 2026; incoation Resolució CLT/809/2026, DOGC 9630, 23 Mar 2026). It is a Roman wreck at 46 m, 300 m from Foralló de Fora. Centre point ETRS89 UTM 31N X 515908, Y 4634119, and the annex 2 polygon vertices are published. Any research or geophysical survey there needs prior authorisation from Cultura — [BOE-A-2026-18424](https://www.boe.es/boe/dias/2026/09/01/pdfs/BOE-A-2026-18424.pdf)
- For Formigues II, the press reported a 92,000 m² protected perimeter where fishing is banned or restricted and buoys cannot be placed. The wreck is about 22 m long, 1st c. BC. CASC director Rut Geli says the BCIN helps against looting — [3Cat](https://www.3cat.cat/3catinfo/un-vaixell-roma-enfonsat-a-les-illes-formigues-primer-jaciment-subaquatic-protegit-de-catalunya/noticia/3405044/)
- Cala Cativa (Port de la Selva) was the first underwater archaeology intervention in Catalonia (1894): amphorae were recovered from a wreck at 33 m. No coordinates were found — [search summary of raco.cat / bibgirona sources](https://raco.cat/index.php/AnnalsEmpordanesos/article/download/93181/164876/164901)
- Legal frame: the archaeological inventory is created by Llei 9/1993 and developed mainly by Decret 78/2002 (Reglament de protecció del patrimoni arqueològic i paleontològic). The law defines citizens' access to inventory data, but I did not see the wording — [UB Biblio3W](https://www.ub.edu/geocrit/b3w-689.htm); [Llei 9/1993 consolidated text](https://participa.gencat.cat/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBbGlTIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--e53253c5fd8bd551c9bae867c923dd1126f29bc7/LPCC.pdf)
- UNESCO 2001 Convention Art. 19(3): information on the discovery or location of underwater cultural heritage that is shared between States Parties, or with UNESCO, is kept confidential and reserved to competent authorities, as far as national law allows, while disclosure might endanger the heritage. Spain is a State Party — [wetten.overheid.nl, English text, Art. 19](https://www.wetten-overheid.nl/wet/BWBV0006655/artikel/19)

### Inferences
- **Restricted for heritage protection (flag):** the CASC/Generalitat Carta Arqueològica Subaquàtica and the inventory points. No public download was found and the WMS is on an intranet host. Treat them as not redistributable.
- Positions published in the BOE/DOGC are official public acts. Spanish law (Ley 37/2007 on reuse of public sector information) generally allows reuse of official journal content. Even so, a polygon or point is safer than an "attraction" pin for protected sites, because diving operations inside need authorisation.
- Diba cards publish coordinates for some coastal and underwater entries, but those are mostly vague "find areas". I did not check the cards' licence.

### Gaps
- I did not see the exact wording of the Llei 9/1993 and Decret 78/2002 articles on access to or confidentiality of inventory data.
- I could not verify the public WMS/WFS URL or the licence of PATRIMONI_JAC_PUNT; the server blocked non-browser User-Agents.
- I found no evidence of whether the public Extranet/"Invarque" web viewer shows underwater sites or hides their coordinates.

## 2. Instituto Hidrográfico de la Marina (IHM): ENC wrecks/obstructions, WMS, licence

### Takeaway
IHM runs a public WMS of its ENC data. The `cartaENCp3` service includes a `WRECKS_P` layer, so wrecks can be viewed. The data is copyrighted and commercial reuse needs a contract. Raw S-57 ENCs are sold through official distributors and are not free; that part comes from background knowledge and I did not verify it. Do not use IHM-derived positions as an open source.

### Cited Findings
- I confirmed the WMS `https://ideihm.covam.es/wms/cartaENCp3?service=WMS&request=GetCapabilities` live on 2026-10-24. Its layers include ENC_ES3, BUAARE_P, **WRECKS_P**, LIGHTS and SOUNDG. AccessConstraints: "Los datos incluidos en este servicio están sometidos a copyright. La reutilización comercial … debe ser objeto de un contrato específico … «© Instituto Hidrográfico de la Marina». El uso … NO ES VÁLIDO … para la navegación." — [IHM WMS GetCapabilities](https://ideihm.covam.es/wms/cartaENCp3?service=WMS&request=GetCapabilities)
- The IHM geoportal licence says no commercial use of any information or service is authorised. It requires source citation and keeping update-date metadata, and forbids implying official endorsement — [ideihm.covam.es/licencias.html](http://ideihm.covam.es/licencias.html)
- The IHM's IHO national report lists nautical chart WMS services (cartaENCp2/p3/p4) mimicking S-52, plus a CSW — [IHO MSDIWG7 National Report Spain](https://docs.iho.int/mtg_docs/com_wg/MSDIWG/MSDIWG7/MSDIWG7-1.6C-National_Report-Spain.pdf)
- A separate IHM coastline WMS (INSPIRE Hydrography) is CC-BY 4.0. That licence covers the coastline only — [IDEE record](https://idee.es/csw-codsi-idee/srv/api/records/spaihmwms_hidrografia_costa)

### Inferences
- IHM WRECKS data is viewable but not reusable in a project that may be commercial. A non-commercial project could arguably overlay the WMS with attribution, but it cannot extract or redistribute the points.

### Gaps
- I did not verify ENC S-57 pricing or distributors for IHM (no results), whether WMS GetFeatureInfo works on WRECKS_P, or any Avisos a Navegantes open feed.
- I did not find a Spanish Ministerio de Cultura national underwater heritage inventory with open data.

## 3. EMODnet Human Activities: wreck layers

### Takeaway
`emodnet:wwshipwrecks` is the best open, redistributable wreck source for Catalonia. It is a UKHO-derived worldwide layer, licensed CC-BY 4.0 / OGL v3. The live WFS returned 69 wrecks in the Catalan bbox, 33 of them named, including Boreas, Reggio and Avvenire. `emodnet:heritageshipwrecks` has essentially no Catalan coverage.

### Cited Findings
- Worldwide wrecks (UKHO): more than 67,000 charted/uncharted, live/dead wrecks, provided by UKHO and compiled by AND-International. The record lists OGL v3 and CC-BY 4.0 with "no limitations on public access". It is updated quarterly; publication date 2024-12-28, metadata 2025-09-02. WFS: `https://ows.emodnet-humanactivities.eu/wfs`, layer `emodnet:wwshipwrecks` — [EMODnet catalogue](https://emodnet.ec.europa.eu/geonetwork/srv/api/records/108ef240-fa6e-4b83-8569-09b509e2959d)
- Live WFS query (2026-10-24, bbox above): **69 features**. By category: 35 dangerous wreck, 26 non-dangerous, 6 showing hull/superstructure, 1 mast, 1 distributed remains. Fields include position, depth, name, type, flag, date_sunk, cargo, circumstances, survey notes and last_amend — [WFS GetFeature](https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:wwshipwrecks&outputFormat=application/json&srsName=EPSG:4326&bbox=40.5,0.15,42.45,3.35,urn:ogc:def:crs:EPSG::4326)
- Named examples from that query:
  - BOREAS, depth 24, 41°50.067'N 3°07.367'E
  - REGGIO, 13.3 m, sunk 1991-12-12, 42°04.8'N 3°12.2'E
  - AVVENIRE, sunk 1971-05-17, 42°06.94'N 3°08.93'E
  - CIUDAD DE BARCELONA, 1937-05-30, 41°38.05'N 2°44.817'E
  - ALCIRA, 1938-02-04, 41°06.43'N 2°14.73'E
  - FERT, 1917-06-09, 40°38.333'N 0°53.5'E
  - SPERLONGA (tanker, 1970), AL HOCEIMA (1987), KYTHERA STAR (1987), BENSU (1979), ADONE (12.8 m), MALLORQUIN (12 m), CALA PINAR (1970), and several Tarragona fishing and motor vessels

  — [same WFS query](https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:wwshipwrecks&outputFormat=application/json&srsName=EPSG:4326&bbox=40.5,0.15,42.45,3.35,urn:ogc:def:crs:EPSG::4326)
- `emodnet:heritageshipwrecks` combines SHOM (FR), Ireland NMS, Historic England and the Oxford Roman Economy Project (OXREP) Mediterranean wrecks — [EMODnet catalogue](https://emodnet.ec.europa.eu/geonetwork/srv/api/records/877ebc1b-0a73-4a88-8a9f-dadf6b1bd728)
  - Live query: filtering country='Spain' returned only 2 records, both from OXREP, e.g. "Bera", 1st c. AD amphorae. That is effectively no Catalan coverage — [WFS](https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=1.1.0&request=GetFeature&typeName=emodnet:heritageshipwrecks&outputFormat=application/json&cql_filter=country=%27Spain%27)
- MACHU wrecks gives deliberately imprecise positions for protection, and covers BE, DE, NL, PL, PT, UK and SE only (not Spain) — [EMODnet catalogue](https://emodnet.ec.europa.eu/geonetwork/srv/api/records/706936f2-7ff2-4f7d-82be-bcae2234d01a)

### Inferences
- EMODnet/UKHO ultimately derives from national hydrographic charting (the record text cites "Cadiz NM", i.e. Spanish notices to mariners). It is still published openly under CC-BY by EMODnet, so attribution is required ("EMODnet Human Activities / UKHO").
- AVVENIRE at 42°06.9'N 3°08.9'E is probably the dive wreck known locally as "Avenir" (L'Escala/Montgó area). I have not verified this.
- Marmara, Montserrat/Medes, Deltebre and the Tossa wrecks did not appear by name in the EMODnet results. They may be among the 36 unnamed points.

### Gaps
- I did not check the precision of positions (many are given to 0.1') or whether the "dead" status flags removed wrecks.

## 4. OpenStreetMap / OpenSeaMap

### Takeaway
OSM coverage of wrecks in Catalonia is very thin: only 10 wreck-type objects in the bbox. Most are recent additions such as Boreas, Vapor del Miracle, La Dragonera, an Aiguablava archaeological wreck and El Marmoler. OSM does hold about 386 `seamark:type=mooring` objects, concentrated around Cap de Creus/Medes and Barcelona. Licence is ODbL 1.0, which allows redistribution with share-alike for derived databases.

### Cited Findings
- Overpass run 2026-10-24 (overpass-api.de; it needs a User-Agent and `Accept: application/json` header, otherwise HTTP 406). Results:
  - 3 objects with both historic=wreck and seamark:type=wreck
  - 6 with seamark:type=wreck only
  - 1 with historic=wreck only
  - 0 with man_made=artificial_reef
  - 0 with seamark:type=obstruction
  - 386 with seamark:type=mooring (335 pile, 9 buoy, 42 untagged category)

  — [Overpass API](https://overpass-api.de/api/interpreter)
- Wreck examples:
  - node 13099227819 "Boreas", 41.8479, 3.1392, depth 18–32, sunk 1989
  - node 11648728361 "Vapor del Miracle", 41.1093, 1.2673, 16 m, 1990 (Tarragona)
  - node 11646580121 "Pecio La Dragonera", 41.0888, 1.2297, 14–24 m, sunk 1994, plus 4 adjacent unnamed nodes (Cambrils/Salou area)
  - node 12132415101 "Aiguablava V i VII", 41.9349, 3.2166, 7 m, tagged historic=archaeological_site. This is an archaeological site published in OSM; flag it
  - node 14133079399 "El marmoler", 42.1031, 3.1918
  - node 14305791769 "Epave avion Douglac DC6", 42.445, 2.9148. This one is inland or at the border, not marine

  — [OSM node 13099227819](https://www.openstreetmap.org/node/13099227819); [OSM node 12132415101](https://www.openstreetmap.org/node/12132415101)
- Named mooring buoys in OSM include "Boia de l'Illa Negra", "Boia del Furió d'Aigua Xelida", "Boia dels Canons de Tamariu", "Punta des Plom (Buceig)", "Boia de l'Illa Fitor" and "Boia dels Ulls de Llop" (Begur/Palafrugell dive buoys). About 335 piles sit in the 42.2–42.3 latitude band (Cap de Creus/Cadaqués/Port de la Selva area) and 42 at lat ~41.4 (Barcelona) — [Overpass API](https://overpass-api.de/api/interpreter)
- Query used:
  ```
  [out:json][timeout:90];
  (nwr["historic"="wreck"](40.5,0.15,42.45,3.35);
   nwr["seamark:type"="wreck"](40.5,0.15,42.45,3.35);
   nwr["seamark:type"="obstruction"](40.5,0.15,42.45,3.35);
   nwr["man_made"="artificial_reef"](40.5,0.15,42.45,3.35);
   nwr["seamark:type"="mooring"](40.5,0.15,42.45,3.35););
  out center tags;
  ```

### Inferences
- OSM data is usable under ODbL with attribution and share-alike. The volume is too low to be a primary wreck source, but it is useful for curated dive wrecks and dive buoys.
- The "El marmoler" name suggests it is the Marmara wreck (Marmoler in Catalan), but I have not verified this.

### Gaps
- I did not check whether OSM mooring piles near Cap de Creus are dive buoys or harbour piles; many are probably port moorings.

## 5. Wrecksite.eu, Wikidata, Viquipèdia, global datasets

### Takeaway
Wikidata has only 1 georeferenced shipwreck in the Catalan bbox, so it is negligible. I could not retrieve wrecksite.eu's terms (the legal page errored). It is a proprietary, subscription database and should be assumed non-redistributable. I did not research global open wreck datasets (Kaggle/GitHub).

### Cited Findings
- Wikidata SPARQL run 2026-10-24 found **1 result**: Llanishen Point (Q1866834), 42.28421, 3.2992. Query: items `wdt:P31/wdt:P279* wd:Q852190` (shipwreck) with P625 inside the bbox filter — [Wikidata Query Service](https://query.wikidata.org/sparql)
- Wrecksite is a non-profit site, free to browse, with more data behind a subscription. In 2019 it held 187,030 wrecks and 164,050 positions, per a Wikipedia mirror (dated) — [Wikipedia mirror](https://bafybeiaysi4s6lnjev27ln5icwm6tueaw2vdykrtjkwiphwekaywqhcjze.ipfs.ipfs.hypha.coop/wiki/Wrecksite)
- wrecksite.eu/juridical.aspx returned an error page — [wrecksite.eu](https://www.wrecksite.eu/juridical.aspx)

### Inferences
- Without explicit permission, wrecksite positions should not be scraped or redistributed. Spain applies EU database sui generis rights.

### Gaps
- I did not obtain the wrecksite ToS text or API status.
- I did not review Viquipèdia "naufragis" lists, nor Kaggle/GitHub "global shipwrecks" datasets.

## 6. Artificial reefs (esculls artificials) and man-made underwater POIs

### Takeaway
Catalonia has 13 Generalitat reef areas (3,557 modules located in the 2022 monitoring), plus MAPA (state) reefs such as Tossa, Maresme III and Garraf-Penedès. MAPA publishes per-reef fact sheets without coordinates. I found no Catalan open GIS layer for reefs. Valencia does publish one on datos.gob.es, which can serve as a model. Nautical charts mark the reefs, but chart data falls under IHM copyright.

### Cited Findings
- Generalitat reef areas (13): Port de la Selva, l'Escala, l'Estartit, Pas del Congo (Blanes–Sant Feliu de Guíxols), el Masnou, Vilanova i la Geltrú, Calafell, Salou, golf de Sant Jordi Nord and Sud, l'Ampolla, l'Ametlla de Mar and Les Cases d'Alcanar. The 2022 monitoring located 3,557 modules (2,087 protection, 928 production, 542 mixed) — [Ebredigital](https://ebredigital.cat/?p=281993)
- Alcanar reef: installed 1998 on sand at 18 m, inspected in 2025 by the DG Política Marítima i Pesca Sostenible, still operational, marked on nautical charts — [Diari de Tarragona](https://www.diaridetarragona.com/ebre/219188/inspeccionen-l-escull-artificial-de-la-costa-d-alcanar-ia20318415.html)
- MAPA records 130 reef initiatives in Spain. The first were in Catalonia: Escorpora (1981) and Sa Riera–Begur (1982), followed by l'Ampolla, Salou and Medes in the 1980s. The page links a PDF and a map of reefs managed by the autonomous communities, with no GIS download — [MAPA arrecifes en España](https://www.mapa.gob.es/es/pesca/temas/proteccion-recursos-pesqueros/arrecifes-artificiales/arrecifes-artificiales-en-espana)
- MAPA Tossa del Mar reef: 2007, production type, 503 modules, 1,168.53 ha. No coordinates or depth on the page — [MAPA Tossa](https://www.mapa.gob.es/ca/pesca/temas/proteccion-recursos-pesqueros/arrecifes-artificiales/arrecifes-artificiales-instalados-por-la-sgp/tossa)
- MAPA also has sheets for Maresme III (1998, protection) and Garraf–Penedès (1999) — [MAPA Maresme](https://www.mapa.gob.es/ca/pesca/temas/proteccion-recursos-pesqueros/arrecifes-artificiales/arrecifes-artificiales-instalados-por-la-sgp/maresme); [MAPA Garraf](https://www.mapa.gob.es/en/pesca/temas/proteccion-recursos-pesqueros/arrecifes-artificiales/arrecifes-artificiales-instalados-por-la-sgp/garraf)
- The Valencian reef layer is on datos.gob.es (a model, not for Catalonia) — [datos.gob.es](https://datos.gob.es/catalogo/a10002983-pesca-arrecifes-artificiales-de-la-comunitat-valenciana)
- The Generalitat published *Els esculls artificials a Catalunya* (2001, Direcció General de Pesca); it is held by the Museu Marítim library — [MMB](https://biblioteca.mmb.cat/bib/661)
- Reef boundaries are often fixed in fishing regulations (BOE/DOGC orders). One example is the 1993 BOE order on an artificial reef zone — [BOE 1993](https://boe.es/boe/dias/1993/01/20/pdfs/A01429-01430.pdf) (I did not read it to confirm which reef it covers)
- Intentionally sunk dive wrecks seen in OSM: "Pecio La Dragonera" (1994) and "Vapor del Miracle" (1990) off Tarragona/Cambrils — [Overpass](https://overpass-api.de/api/interpreter)

### Inferences
- The best route to reef coordinates is probably the polygons in the DOGC/BOE orders that created each reef zone. Those are public official acts and generally reusable. Alternatively, request the data from DACC under transparency law.
- Artificial reefs are not heritage-restricted. Fishing restrictions apply, but there is no confidentiality.

### Gaps
- I found no Catalan Dades Obertes (analisi.transparenciacatalunya.cat) or IDEC reef layer; I did not search those portals exhaustively.
- I did not find coordinates for any Catalan reef.
- I did not research underwater museums or sculptures, or the itineraris submarins.

## 7. Mooring / ecological dive buoys

### Takeaway
I found no official open dataset of dive mooring buoys for Medes, Cap de Creus or other areas. The buoys are defined in park PRUG documents and permits. OSM has a partial community mapping of them (see section 4).

### Cited Findings
- The Medes PRUG and related allegations describe increasing buoys and dive zones, with carrying-capacity limits per zone as an adaptive model — [govern.cat doc 2018](https://govern.cat/govern/docs/2018/10/26/18/03/b3e8dc1c-47ae-4d42-a572-8d98df8f70fb.pdf); [govern.cat doc 2015](https://govern.cat/govern/docs/2015/04/28/18/32/e50ff3e4-b0ff-41ff-96f6-bad6a47d130b.pdf)
- A Diputació de Girona document notes the Cova de l'Infern buoy was moved to Sant Istiu (Meda Petita) for safety, and most Medellot dives were moved to two other buoys — [bibgirona](https://bibgirona.cat/assets/documents/000/198/819/article.pdf)
- Dive centre authorisations are issued by the Parc Natural del Montgrí, les Illes Medes i el Baix Ter through a biennial procedure, with applications in November — [search summary, govern.cat](https://govern.cat/govern/docs/2015/04/28/18/32/e50ff3e4-b0ff-41ff-96f6-bad6a47d130b.pdf)
- The BCIN rules for Illes Formigues II forbid placing buoys inside the polygon — [3Cat](https://www.3cat.cat/3catinfo/un-vaixell-roma-enfonsat-a-les-illes-formigues-primer-jaciment-subaquatic-protegit-de-catalunya/noticia/3405044/)

### Inferences
- PRUG annexes may contain buoy coordinates as official public documents; verify that before reusing them. OSM named buoys are ODbL.

### Gaps
- I did not check Ports de la Generalitat or MITECO "fondeos ecológicos" datasets (no results), or the Cap de Creus buoy inventory.
