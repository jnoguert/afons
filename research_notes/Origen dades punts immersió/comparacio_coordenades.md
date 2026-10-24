# Forensic comparison of Catalan dive-site databases (coordinates, names, depths, texts), as of 2026-10-24

Method: about 15 Costa Brava sites were compared across OSM (local Overpass file plus the node and changeset history API), Diveboard via GBIF (local file), Wannadive, Zentacle, Meteoconsult, DiveBuddy, the UKHO wrecks layer via EMODnet (local file), dive-centre pages (gidive) and other aggregators (duikersgids, diveplannerpro). Wannadive stores positions as degrees plus decimal minutes (3 decimals). Those were converted to decimal degrees (`deg + min/60`), and haversine distances were computed against the Wannadive point ("Δ WD") or the UKHO point ("Δ UKHO"). Only the ~35 individual pages needed were fetched; no site was bulk-scraped.

Source codes used in the tables:
- **WD** = Wannadive.net spot pages (URL given per row).
- **DB** = Diveboard via GBIF, dataset `66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2` ([GBIF dataset](https://www.gbif.org/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2); local file `C:\Codi\afons\data\raw\pois\gbif\diveboard.json`). Coordinates are rounded to 4 decimals of latitude and ≤5 of longitude, with `coordinateUncertaintyInMeters = 100`. The `depth` field is the depth of each logged dive, not a property of the site.
- **ZT** = Zentacle (`/Beach/<id>/…` pages; coordinates read from the map-link parameters).
- **OSM** = OpenStreetMap node or way, with history read from `https://api.openstreetmap.org/api/0.6/node/<id>/history`.
- **UKHO** = UKHO world wrecks layer from EMODnet (local file `C:\Codi\afons\data\raw\pois\emodnet\wwshipwrecks.geojson`).
- **MC** = Meteoconsult marine "spots de plongée".
- **DBY** = DiveBuddy.

## 1. Comparison table: site × source → name spelling, lat, lon, depth

### Takeaway
For every Medes site tested, plus Boreas, Formigues, Ullastre I/II, Mar Menuda, Illa de Tossa, Reggio and Negre de Falaguer, Wannadive, Diveboard, Zentacle and (for Boreas) Meteoconsult give the same point to within 0–5.6 m. That 5.6 m is exactly Diveboard's 4-decimal rounding grid. OSM, UKHO and DiveBuddy are 20 m to 2.5 km away from that cluster, so their positions were placed independently.

### Cited Findings

**Medes Islands (L'Estartit)**

| Site | Source | Name spelling (+ aliases) | Lat | Lon | Depth | Δ WD | Notes |
|---|---|---|---|---|---|---|---|
| Carall Bernat | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Carall_Bernat/) | Carall Bernat (alt "Islote Mogote Bernat, Cavall Bernat") | 42°2.484'N = 42.0414 | 3°13.699'E = 3.2283167 | avg 25 m / max 45 m | – | Precision "Exact", author "Chris" |
| Carall Bernat | [ZT](https://www.zentacle.com/Beach/1773/carall-bernat) | Carall Bernat (alt "Islote Mogote Bernat, Cavall Bernat") | 42.0414 | 3.2283166666666667 | "max 82 ft" (= 25 m, WD's *average*) | 0.0 m | |
| Carall Bernat | [DB](https://www.gbif.org/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2) | "Carall Bernat" (2014 logs); "Cavall Bernat" (2003–2013 logs) | 42.0414 | 3.22832 | dive depths 9–15.5 m | 0.3 m | verbatimLocality "…, Estartit & Medes Islands" |
| Carall Bernat | [OSM n791018619](https://www.openstreetmap.org/node/791018619/history) | Carall Bernat | v1 (2010): 42.0412627; v4 (2012 to now): 42.0414835 | v1: 3.2274772; v4: 3.2286086 | none | v1 71.0 m; now 25.8 m | ZMWandelaar |
| Carall Bernat | [diveplannerpro](https://diveplannerpro.com/spots/es/costa-brava/es-medes-carall-bernat) | Carall Bernat | – | – | 5–45 m | – | no coordinates on page |
| Carall Bernat | [duikersgids](https://www.duikersgids.nl/en/dive-spots/carall-bernat) | CARALL BERNAT | – | – | 6–50 m | – | region given wrongly as "Spanje, Cantabria" |
| La Vaca | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/La_Vaca/) | La Vaca (alt "Cova de la Vaca, Punta de la Galera, Punta de la Guilla") | 42°2.852'N = 42.0475333 | 3°13.554'E = 3.2259 | avg 22 / max 45 | – | Exact, Chris |
| La Vaca | [ZT](https://www.zentacle.com/Beach/1765/la-vaca) | La Vaca (same three aliases) | 42.047533333333334 | 3.2259 | "72.2 ft" (= 22 m, WD avg) | 0.0 m | |
| La Vaca | DB | La Vaca | 42.0475 (2012–15 logs); 42.0474 (2017–18); 42.0474 (2019) | 3.2259; 3.22574; 3.22617 | dive depths 9–17 m | 3.7 m (main variant) | |
| La Vaca | [OSM n791018574](https://www.openstreetmap.org/node/791018574/history) | la Vaca | v1: 42.0474975; now: 42.0473849 | 3.2256198 | none | 23.5 / 28.4 m | |
| Dofí | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Dolphin_s_cave/) | Dolphin's cave (alt "El Dofí, Tunels del Dofi") | 42°2.637'N = 42.04395 | 3°13.592'E = 3.2265333 | avg 20 / max 28 | – | Exact, Chris |
| Dofí | [ZT](https://www.zentacle.com/Beach/1764/dolphins-cave) | Dolphin's cave (alt El Dofí, Tunels del Dofi) | 42.04395 | 3.2265333333333333 | "65.6 ft" (= 20 m, WD avg) | 0.0 m | |
| Dofí | DB | "Dolphin's Cave"; "Le Dofi" | 42.0439; 42.0439 | 3.22653; 3.22646 | ~10 m | 5.6 m | |
| Dofí | [OSM n791018624](https://www.openstreetmap.org/node/791018624/history) / [n791018571](https://www.openstreetmap.org/node/791018571/history) | "Dolfi Nord" / "Dolfi Sud" | N v1: 42.0441649, now 42.0442477; S: 42.0437364 | N v1: 3.2259576, now 3.2258048; S: 3.2264109 | none | N 53–69 m; S 25.8 m | spelling "Dolfi" is found only in OSM |
| Pota del Llop | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Pota_del_Llop/) | Pota del Llop (alt "Punta del Llop, Punta de la Pota del Llop") | 42°2.961'N = 42.04935 | 3°13.55'E = 3.2258333 | avg 21 / max 50 | – | Exact, Chris |
| Pota del Llop | [ZT](https://www.zentacle.com/Beach/1770/pota-del-llop) | Pota del Llop (same aliases) | 42.04935 | 3.2258333333333336 | "68.9 ft" (= 21 m, WD avg) | 0.0 m | |
| Pota del Llop | DB | "Pota Del Llop" | 42.0494 (2018); 42.0495 (2014) | 3.22583; 3.22341 | 12–14 m | 5.6 m; 200.8 m | |
| Pota del Llop | [OSM n791018588](https://www.openstreetmap.org/node/791018588/history) | la Pota del Llop | v1 (2010): 42.0493549; v2 (2012): 42.0493917 | v1: 3.2258531; v2: 3.2262165 | none | v1 **1.7 m**; now 32 m | |
| Tascó Gros | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Tasco_Gros/) | Tasco Gros | 42°2.532'N = 42.0422 | 3°13.615'E = 3.2269167 | avg 18 / max 30 | – | "Approximate", author "fritz" |
| Tascó Gros | [ZT](https://www.zentacle.com/Beach/7184/tasco-gros) | Tasco Gros | 42.0422 | 3.226916666666667 | "59.1 ft" (= 18 m, WD avg) | 0.0 m | |
| Tascó Gros | DB | (no Tasco Gros locality; only "Tasco Petit") | – | – | – | – | |
| Tascó Gros | [OSM n791018569](https://www.openstreetmap.org/node/791018569/history) | Tasco Gros | v1: 42.0421149; v4 (2012): 42.0420658 | v1: 3.2267037; v4: 3.2279425 | none | 20.0 / 86.0 m | |

**Other Costa Brava sites**

| Site | Source | Name spelling | Lat | Lon | Depth | Δ | Notes |
|---|---|---|---|---|---|---|---|
| Boreas (Palamós) | UKHO wreck_id 35618 (local file) | BOREAS | 41°50.067'N = 41.834444 | 3°7.367'E = 3.122778 | least depth 24 m; water depth 26 m | – | 1989 entry "sunk … by bearing and distance (CADIZ NM 489/89)"; amended to "dead" in 2000 ("not shown on Spanish 492") |
| Boreas | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/El_Boreas_wreck/) | "El Boreas wreck" (alt "Boreas") | 41°49.626'N = 41.8271 | 3°7.701'E = 3.12835 | avg 25 / max 32; "Wreck starts at 18 m depth. bottom is 32 m." | Δ UKHO 938 m | Precision "Approximate", author "Albert" |
| Boreas | MC spot 5434 ([page](https://marine.meteoconsult.fr/meteo-marine/bulletin-detaille/spot-de-plongee-5434/previsions-meteo-el-boreas-wreck-aujourdhui), from search snippet) | "El Boreas wreck" | 41°49',626 N | 3°7',701 E | – | Δ WD 0.0 m | the identical DDM string |
| Boreas | DB | "El Boreas Wreck" (verbatimLocality "El Boreas Wreck, Palamos Town To Cap De Begur") | 41.8271 | 3.12836 | dive depths 13.4–15.3 m | Δ WD 0.8 m | |
| Boreas | [OSM n13099227819](https://www.openstreetmap.org/node/13099227819/history) | Boreas | 41.8479002 | 3.1391767 | depth=18-32 | Δ WD 2,481 m; Δ UKHO 2,021 m | elmagosamu 2025-08-26; image hotlinked from gidive.com |
| Boreas | [gidive](https://www.gidive.com/es/Boreas) | Boreas | – | – | bow rope ~22 m, propeller 32 m; 40 m long; sunk 1989 | – | dive centre; no coordinates |
| Boreas | [duikersgids](https://www.duikersgids.nl/en/boreas-wreck) | BOREAS WRECK ("The Pellworm") | – | – | 35 m; 15–32.5 m; length 30 m; sunk 23 Jan 1989 | – | "Spanje, Cantabria" again |
| Formigues | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/Islas_Formigas/) | "Islas Formigas" (alt "Formigas isles") | 41°51.704'N = 41.8617333 | 3°11.268'E = 3.1878 | avg 15 / max 25 | – | Approximate, "overwings" |
| Formigues | DB | "Islas Formigas" (2011, 2015); "Illes Formigues" (2014) | 41.8617 | 3.18779 | 8.5–15 m | 3.8 m | |
| Formigues | [OSM n14071084203](https://www.openstreetmap.org/node/14071084203/history) | Illes Formigues | 41.8625334 | 3.1865238 | maxdepth 20 | 138 m | Chompas 2026-08-03 |
| Ullastre I | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/Ullastre_I/) | Ullastre I | 41°52.772'N = 41.8795333 | 3°11.873'E = 3.1978833 | avg 15 / max 30 | – | Albert |
| Ullastre I | DB | "Ullastre I" (also "Ullastre 1" at 41.8886, 3.19924) | 41.8795 | 3.19788 | 10–14.6 m | 3.7 m ("Ullastre 1": 1,014 m) | |
| Ullastre II | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/Ullastre_II/) | Ullastre II (alt "Ullastre 2") | 41°52.687'N = 41.8781167 | 3°11.996'E = 3.1999333 | avg 25 / max 53 | – | "Athe" |
| Ullastre II | DB | "Ullastre Ii" | 41.8781 | 3.19994 | 10.7–14.6 m | 1.9 m | |
| Ullastre III | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/Ullastre_III/) | Ullastre III | 41°52.602'N = 41.8767 | 3°12.122'E = 3.2020333 | avg 15 / max 54 | – | Albert |
| Ullastre III | DB | "Ullastre Iii" at 5 different positions (e.g. 41.88/3.19716; 41.8909/3.20708) | – | – | – | 545 m and more | no match |
| Furió Fitó | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/Furio_de_Fito/) | "Furio de Fito" | 41°58.691'N = 41.9781833 | 3°13.644'E = 3.2274 | avg 20 / max 54; "underwater rock starts at 16 m and bottom is at 54 m" | – | Approximate, Albert |
| Furió Fitó | [OSM n12132826563](https://www.openstreetmap.org/node/12132826563/history) | "Barda de Fitor" (alt "Furió Fitor") | 41.9575979 | 3.2369798 | maxdepth **54** | 2,422 m | mauriciabad 2024 |
| Furió Fitó | [OSM way356731947](https://www.openstreetmap.org/way/356731947/history) | "S'Encalladora" (alt "Furió Fitor;Illa Fitor") | 41.9577 | 3.2347 | maxdepth 29 | 2,355 m | |
| Massa d'Or (Cap de Creus) | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Cadaques/Massa_d_ors/) | "Massa d ors" (alt "Cadaques") | 42°19.179'N = 42.31965 | 3°19.932'E = 3.3322 | avg 20 / max 40 | – | Approximate, "Juanola" |
| Massa d'Or | [OSM n663869684](https://www.openstreetmap.org/node/663869684/history) | "Massa d'Or (la Rata)" (earlier "Massa d\`Or (La Rata)") | v1 (2010): 42.3199540; v5 (2026): 42.3199775 | v1: 3.3314833; v5: 3.3315002 | none | 67.9 m | `source=www.dive-links.com` |
| Massa d'Or | [DBY 3213 (Wayback 2015)](https://web.archive.org/web/20150330103459/http://divebuddy.com/divesite/3213/illa-de-massa-dor-aka-la-rata-spain/) | "Illa de Massa d'Or aka La Rata" | 42.319208740798730 | 3.332033157348633 | max 28–30 m | 51.0 m | text credited "From; montjoi.com/en/diving-roses/points-immersion" |
| Tossa: Mar Menuda | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Tossa_de_Mar/Mar_Menuda/) | Mar Menuda (alt "Tossa de mar") | 41°43.301'N = 41.7216833 | 2°56.378'E = 2.9396333 | avg 16 / max 20 | – | "Brunola" |
| Tossa: Mar Menuda | DB | Mar Menuda | 41.7217 | 2.93964 | 4–14.6 m | 1.9 m | |
| Tossa: Illa | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Tossa_de_Mar/Ile_de_Tosca/) | **"Ile de Tosca"** | 41°43.197'N = 41.71995 | 2°56.423'E = 2.9403833 | avg 10 / max 30 | – | "whu" |
| Tossa: Illa | DB | **"Ile De Tosca"** | 41.72 | 2.94039 | 10.2 m | 5.6 m | |
| L'Escala: Ferriola | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/L_Escala/Ferriola/) | Ferriola (alt "Ferriola, Illa Ferriol") | 42°5.078'N = 42.0846333 | 3°11.832'E = 3.1972 | avg 20 / max 33 | – | "tauchertom" |
| L'Escala: Ferriola | [OSM n1788581871](https://www.openstreetmap.org/node/1788581871/history) | la Ferriola | 42.0844478 | 3.1971438 | none | 21.1 m | ZMWandelaar 2012 |
| L'Escala: Marmoler | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/L_Escala/Marmoler/) | Marmoler (alt **"Avverine"**) | 42°6.482'N = 42.1080333 | 3°11.363'E = 3.1893833 | avg 38 / max 42 | – | tauchertom |
| L'Escala: Marmoler | [OSM n14133079399](https://www.openstreetmap.org/node/14133079399/history) | El marmoler (historic=wreck) | 42.1031431 | 3.1918318 | none | 580 m | KaiserDr 2026-08-29 |
| L'Escala: Marmoler | UKHO wreck_id 35612 (local file) | AVVENIRE ("struck rocks at Punta Grossa in front of La Escala", 1971) | 42.115667 | 3.148833 | – | ~3.5 km | "POSN 420700N, 030900E FOR FILING ONLY" |
| Reggio (Estartit) | UKHO 35642 (local file) | REGGIO | 42°4.8'N = 42.08 | 3°12.2'E = 3.203333 | 13.3 m least depth | Δ WD 64.6 m | "reported sunk as part of wreck and diving resort" (1993) |
| Reggio | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Reggio_Messina_Wreck/) | Reggio Messina Wreck | 42°4.8'N = 42.08 | 3°12.153'E = 3.20255 | avg 28 / max 35 | – | "Dariusz" |
| Reggio | DB / [ZT](https://www.zentacle.com/loc/es/ct/gi/lestartit) | "Reggio Messina Wreck" (both) | DB 42.08 | DB 3.20256 | – | 0.8 m | |
| Reggio | [OSM n1788581869](https://www.openstreetmap.org/node/1788581869/history) | el Reggio | 42.0810324 | 3.2018565 | – | 128 m | ZMWandelaar 2012 |
| Negre del Falaguer | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Negre_de_Falaguer/) | "Negre de Falaguer" | 42°4.006'N = 42.0667667 | 3°12.695'E = 3.2115833 | avg 15 / max 20 | – | "Anonymous" |
| Negre del Falaguer | DB | "El Negre De Fallaguer" (and "Negre Del Falaguer" at 42.067/3.21033) | 42.0668 | 3.21158 | – | 3.7 m (other: 107 m) | |
| Negre del Falaguer | [OSM n1788581872](https://www.openstreetmap.org/node/1788581872/history) | Negre del Falaguer | 42.0660198 | 3.2106594 | – | 113 m | ZMWandelaar 2012 |
| La Pedrosa (Estartit) | [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/La_pedrosa/) | "La pedrosa" | 42°4.431'N = 42.07385 | 3°12.299'E = 3.2049833 | avg 18 / max 40 | – | "grenouille64" |
| La Pedrosa | [OSM n663869682](https://www.openstreetmap.org/node/663869682/history) | "la Pedrosa" (formerly "Isla Pedrosa (Höhle)") | v1 (2010): 42.0736000 | v1: 3.2050667 | – | 28.6 m | `source=www.dive-links.com` |
| La Pedrosa | [ZT](https://www.zentacle.com/loc/es/ct/gi/lestartit) | "La pedrosa" (lower-case p, as in WD) | – | – | – | – | |

- Diveboard also has several localities in Cap de Creus ("Cala Figuera", "Ralé D'en Sanes", "Cova Del Pelegrí", "Ses Ielles", "Es Carals", "Es Cucurucua") that all share **one** coordinate, 42.289, 3.27839, so user-created spots there received a default point (local file `diveboard.json`).

### Inferences
- The Wannadive, Diveboard, Zentacle and Meteoconsult cluster is a single dataset: Diveboard's 0.3–5.6 m offsets are fully explained by its 4-decimal latitude rounding (0.0001° ≈ 11 m), and Zentacle reproduces WD to the last digit.
- OSM's Medes nodes (ZMWandelaar, 2010/2012), the dive-links-derived OSM nodes, DiveBuddy and UKHO are each 20 m to 2.5 km from WD, which is typical of independent placement.
- The OSM v1 Pota del Llop node (2010) lies 1.7 m from WD. It has 7 decimals, not WD's 1/60 pattern, and the other ZMWandelaar v1 nodes are 20–71 m off, so this is most likely coincidence. Treat it as inconclusive.
- No source agrees with UKHO for Boreas. UKHO itself is a 1989 "bearing and distance" report later marked dead, so the true wreck position remains unverified.
- WD's "Furio de Fito" sits about 2.4 km north of the Fitor shoal mapped in OSM, apparently a misplaced "Approximate" entry. Diveboard has no record there, so the error has not propagated in the GBIF data.

### Gaps
- No official ground truth was found: the Medes park buoy and dive-zone coordinates (PRUG / Ordre AAM/112/2015) were not located online.
- "Rascassa" (L'Escala) and "Ses Illetes / Punta de la Bauma" (Tossa) were not found in any source searched. Ferriola/Marmoler and Mar Menuda/Illa de Tossa were used as substitutes.
- Zentacle was checked only for the Medes and Estartit sites; its entries for Boreas, Formigues and Massa d'Or were not found.
- Meteoconsult returned HTTP 403 to direct fetches. Only the Boreas coordinates came via a search snippet; spot 5394 "Carall Bernat" exists ([MC 5394](https://marine.meteoconsult.fr/meteo-marine/bulletin-detaille/spot-de-plongee-5394/previsions-meteo-carall-bernat-aujourdhui)), but its coordinates were not read.

## 2. Identical coordinates and identical rounding

### Takeaway
Zentacle coordinates are WD's decimal-minute values converted with no rounding, which produces repeating sixtieths (…3333, …16667) that betray the conversion. Diveboard has the same values rounded to 4–5 decimals. Meteoconsult shows the identical decimal-minute string.

### Cited Findings
- Each Zentacle longitude ends in a 1/60 fraction: Carall Bernat 3.2283166666666667 ([ZT](https://www.zentacle.com/Beach/1773/carall-bernat)), Pota del Llop 3.2258333333333336 ([ZT](https://www.zentacle.com/Beach/1770/pota-del-llop)), Dolphin's cave 3.2265333333333333 ([ZT](https://www.zentacle.com/Beach/1764/dolphins-cave)), La Vaca 42.047533333333334 ([ZT](https://www.zentacle.com/Beach/1765/la-vaca)), Tasco Gros 3.226916666666667 ([ZT](https://www.zentacle.com/Beach/7184/tasco-gros)). These are exactly 13.699′, 13.550′, 13.592′, 2.852′ and 13.615′ divided by 60, the WD values ([WD Carall Bernat](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Carall_Bernat/), [WD Pota del Llop](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Pota_del_Llop/), [WD Dolphin's cave](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Dolphin_s_cave/), [WD La Vaca](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/La_Vaca/), [WD Tasco Gros](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Tasco_Gros/)).
- Diveboard's GBIF coordinates match WD after rounding at 13 sites: Carall Bernat, La Vaca, Dolphin's Cave, Pota del Llop, Pedra de Deu (WD 42.0502333/3.2249167 ↔ DB 42.0502/3.22492; [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Pedra_de_Deu/)), El Boreas wreck, Islas Formigas, Ullastre I, Ullastre II, Mar Menuda, Ile de Tosca, Reggio Messina Wreck and Negre de Falaguer. All offsets are ≤5.6 m (local file `diveboard.json`; WD pages cited in section 1).
- The Meteoconsult "El Boreas wreck" position, "Lat: 41°49',626 N, Lon: 3°7',701 E" (as shown in the search-result snippet for [MC spot 5434](https://marine.meteoconsult.fr/meteo-marine/bulletin-detaille/spot-de-plongee-5434/previsions-meteo-el-boreas-wreck-aujourdhui)), is identical digit for digit to WD's "41° 49.626' N / 3° 7.701' E" ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/El_Boreas_wreck/)).
- WD flags the Boreas position as "Precision: Approximate", yet three downstream sources reproduce it as is ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/El_Boreas_wreck/)).
- UKHO Boreas sits at 41.834444, 3.122778, 938 m from the WD/DB/MC point. The OSM Boreas node is 2.0 km from UKHO and 2.5 km from WD (local file `wwshipwrecks.geojson`; [OSM n13099227819](https://www.openstreetmap.org/node/13099227819/history)).
- DiveBuddy's Massa d'Or coordinates (42.319208740798730, 3.332033157348633) have 15 significant digits, the signature of a web-map click. They are 51 m from WD and about 70 m from the OSM/dive-links point ([DBY Wayback](https://web.archive.org/web/20150330103459/http://divebuddy.com/divesite/3213/illa-de-massa-dor-aka-la-rata-spain/)).

### Inferences
- A repeating-sixtieth decimal is a reliable fingerprint for "converted from Wannadive DDM". It can be used to classify any further dataset (for example, Meteoconsult's other spots, or the afons pipeline's own inputs).
- In GBIF, the rounding happened at Diveboard's export (or IPT), not at the source. Zentacle's full-precision values therefore cannot have come from the GBIF export. They came either from WD directly or from Diveboard's internal spot table.

### Gaps
- Diveboard's internal (unrounded) spot coordinates could not be checked. The Diveboard spot pages were not retrieved, and the Wayback CDX API was intermittently "Temporarily Offline" during the session.

## 3. Identical typos and name spellings

### Takeaway
Distinctive non-standard names coined on Wannadive ("Ile de Tosca", "Islas Formigas", "Dolphin's cave", "Reggio Messina Wreck", "Canyones de Fallaguer", "La pedrosa", "Puig de la sardina") reappear in Diveboard and/or Zentacle at the same coordinates. OSM uses its own Catalan forms ("Dolfi Nord", "Illes Formigues", "el Reggio").

### Cited Findings
- WD names the Illa de Tossa site **"Ile de Tosca"**, a French form with "Tosca" for Tossa ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Tossa_de_Mar/Ile_de_Tosca/)). Diveboard has the locality "Ile De Tosca" at the matching coordinates (local file `diveboard.json`).
- WD uses **"Islas Formigas"**, a Spanish/Catalan hybrid; Catalan is "Formigues" and Spanish "Hormigas" ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/Islas_Formigas/)). Diveboard has "Islas Formigas" at the same point; OSM has "Illes Formigues" ([OSM](https://www.openstreetmap.org/node/14071084203/history)).
- The alias string "Islote Mogote Bernat, Cavall Bernat" is identical in WD and Zentacle ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Carall_Bernat/); [ZT](https://www.zentacle.com/Beach/1773/carall-bernat)). Diveboard logs use both "Cavall Bernat" and "Carall Bernat" for one coordinate.
- The alias strings for La Vaca ("Cova de la Vaca, Punta de la Galera, Punta de la Guilla") and Pota del Llop ("Punta del Llop, Punta de la Pota del Llop") are identical in WD and ZT ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/La_Vaca/); [ZT](https://www.zentacle.com/Beach/1765/la-vaca); [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Pota_del_Llop/); [ZT](https://www.zentacle.com/Beach/1770/pota-del-llop)).
- Zentacle's 21 L'Estartit sites ([ZT list](https://www.zentacle.com/loc/es/ct/gi/lestartit)) correspond one for one to WD's 21 Estartit spot pages (set taken from the links in the WD pages, e.g. [WD Carall Bernat](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Carall_Bernat/)). The match includes WD-specific forms such as "Puig de la sardina" (lower-case s), "La pedrosa" (lower-case p), "La Llossa Revesa", "Els Arquets" and "Reggio Messina Wreck".
- Diveboard and Zentacle share "Escrivana", "El Negre de Fallaguer" and "Canyones de Fallaguer" (double l). WD's current slugs are "Estribania" and "Negre_de_Falaguer", with the title "Negre de Falaguer", but WD's other slug is "Canyones_de_Fallaguer" ([ZT list](https://www.zentacle.com/loc/es/ct/gi/lestartit); `diveboard.json`; [WD Negre](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Negre_de_Falaguer/)).
- Meteoconsult writes "El Boreas wreck" with a lower-case "w", exactly as WD; Diveboard title-cases it to "El Boreas Wreck" ([MC](https://marine.meteoconsult.fr/meteo-marine/bulletin-detaille/spot-de-plongee-5434/previsions-meteo-el-boreas-wreck-aujourdhui); [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/El_Boreas_wreck/)).
- Diveboard's verbatimLocality suffix "Palamos Town To Cap De Begur" is WD's region name "Palamos town to Cap de Begur" title-cased. The title-casing also produces "Ullastre Ii" and "Ullastre Iii" ([WD region](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/index.html); `diveboard.json`).
- WD gives the Marmoler an alias, "Avverine", a misspelling of the wreck AVVENIRE (UKHO wreck 35612, which struck rocks at Punta Grossa, L'Escala, in 1971) ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/L_Escala/Marmoler/); `wwshipwrecks.geojson`).
- OSM spells the Dofí caves "Dolfi Nord" / "Dolfi Sud", a misspelling of Catalan "Dofí" not found in any other source ([OSM](https://www.openstreetmap.org/node/791018624/history)).
- The alias "La Rata" for Massa d'Or appears in the 2010 OSM import from dive-links.com ("Massa d\`Or (La Rata)") ([OSM](https://www.openstreetmap.org/node/663869684/history)). It also appears in DiveBuddy, whose URL changed from "illa-de-massa-dor-spain" (2013 capture) to "illa-de-massa-dor-aka-la-rata-spain" (2015 capture) ([Wayback 2013](https://web.archive.org/web/20131108194137/http://www.divebuddy.com/divesite/3213/illa-de-massa-dor-spain/); [Wayback 2015](https://web.archive.org/web/20150330103459/http://divebuddy.com/divesite/3213/illa-de-massa-dor-aka-la-rata-spain/)).
- Duikersgids labels both Carall Bernat and Boreas "Spanje, Cantabria" ([duikersgids Carall](https://www.duikersgids.nl/en/dive-spots/carall-bernat); [duikersgids Boreas](https://www.duikersgids.nl/en/boreas-wreck)).

### Inferences
- "Ile de Tosca" + identical coordinates is the strongest single proof that Diveboard took WD records; independent creation of that typo is implausible.
- Diveboard and Zentacle share spellings ("Escrivana", "El Negre de Fallaguer") that differ from WD's current titles. Either both copied WD at a time when its titles were different (WD names are editable, slugs are not), or Zentacle copied Diveboard's spot table, which was itself seeded from WD. Both readings put WD at the root.
- "La Rata" alone is weak evidence that DiveBuddy reused the OSM/dive-links name, since it may simply be local usage. The coordinates differ (≈70 m), so the position is not copied.
- The duikersgids "Cantabria" error is an internal template or geocoding bug, not evidence of copying between databases.

### Gaps
- WD's title and edit history ("GPS History", contributors) requires login, so it could not be checked whether "Estribania" or "Negre de Falaguer" were renamed.

## 4. Identical depth values

### Takeaway
The clearest depth fingerprint is Zentacle: in 5 of 5 Medes sites its "max depth" equals WD's *average* depth (a field-mapping error). OSM's Boreas "18-32" matches only WD. Site depths cannot be compared with Diveboard, because its depths are per-dive.

### Cited Findings
- Zentacle's max depth and WD's average depth agree at every Medes site checked: Carall Bernat 82 ft ↔ WD avg 25.0 m/82 ft (max 45 m); La Vaca 72.2 ft ↔ 22.0 m/72.2 ft (max 45 m); Dolphin's cave 65.6 ft ↔ 20.0 m/65.6 ft (max 28 m); Pota del Llop 68.9 ft ↔ 21.0 m/68.9 ft (max 50 m); Tasco Gros 59.1 ft ↔ 18 m/59.1 ft (max 30 m) ([ZT](https://www.zentacle.com/Beach/1773/carall-bernat), [ZT](https://www.zentacle.com/Beach/1765/la-vaca), [ZT](https://www.zentacle.com/Beach/1764/dolphins-cave), [ZT](https://www.zentacle.com/Beach/1770/pota-del-llop), [ZT](https://www.zentacle.com/Beach/7184/tasco-gros); WD pages in section 1).
- The Boreas depth range "18-32" appears in OSM (depth=18-32) and in WD ("Wreck starts at 18 m depth. bottom is 32 m."). The other depths are different: gidive gives a ~22 m bow rope and 32 m propeller, duikersgids 15–32.5 m and 35 m, and UKHO 24 m least depth / 26 m water depth ([OSM](https://www.openstreetmap.org/node/13099227819/history); [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/El_Boreas_wreck/); [gidive](https://www.gidive.com/es/Boreas); [duikersgids](https://www.duikersgids.nl/en/boreas-wreck); `wwshipwrecks.geojson`).
- Fitor's max depth is 54 m both in OSM "Barda de Fitor" (mauriciabad, who cites the Llamas book) and in WD "Furio de Fito" ("bottom is at 54 m"). WD's Ullastre III also has a 54 m max ([OSM](https://www.openstreetmap.org/node/12132826563/history); [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/Furio_de_Fito/)).
- Formigues: OSM maxdepth 20 vs WD max 25. Massa d'Or: DiveBuddy max 28–30 m vs WD max 40 m. No match ([OSM](https://www.openstreetmap.org/node/14071084203/history); [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/Islas_Formigas/); [DBY](https://web.archive.org/web/20150330103459/http://divebuddy.com/divesite/3213/illa-de-massa-dor-aka-la-rata-spain/)).
- Diveboard/GBIF `depth` values (e.g. Boreas 13.41–15.325 m) are per-dive logged depths, many with dive-computer precision (e.g. 14.52) (local file `diveboard.json`; [GBIF dataset description](https://www.gbif.org/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2)).

### Inferences
- The avg→max depth confusion proves that Zentacle ingested WD's structured fields (average and max depth) programmatically and mis-mapped them. A human retyping the data would not produce this.
- OSM Boreas has mixed provenance: its image and narrative come from gidive (paraphrased), its depth matches WD, and its position matches no other source.
- The shared 54 m at Fitor is a round, physically determined value (the base of the shoal) and could come from local knowledge or the book. It is weak evidence.

### Gaps
- The Andreu Llamas book could not be consulted to check whether OSM's Begur maxdepth values were transcribed from it.

## 5. Identical description text (copy-paste)

### Takeaway
Zentacle reproduces WD's English descriptions verbatim, including the original non-native typos. DiveBuddy openly copies a dive centre's text. The OSM Boreas text is a paraphrase of gidive.

### Cited Findings
- Carall Bernat. WD: "One of the best dive, cos of the huge groupers that live here. If you don't breath too much, you can try to turn around the Carall Bernat rock, and go to 35-40m…", with access text "SE of Meda Petita, after Tascons rocks." Zentacle has the same text, typos included ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Carall_Bernat/); [ZT](https://www.zentacle.com/Beach/1773/carall-bernat)).
- Dolphin's cave: "A the southern entry of the cavern, there is a small, bronze statue of a dolphin… There is another on on the E side (deeper and darker)…" appears in both WD and ZT ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Dolphin_s_cave/); [ZT](https://www.zentacle.com/Beach/1764/dolphins-cave)).
- Pota del Llop: "This is one of the most beautifull wall of Medes Islands. Just a the begining of the dive…" appears in both WD and ZT ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Pota_del_Llop/); [ZT](https://www.zentacle.com/Beach/1770/pota-del-llop)).
- Tasco Gros: "Large groupers, groakes, breams, etc, all quite big since the Médes Islands are a wildlife reserve and fishing ist forbidden." appears in both WD and ZT ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Tasco_Gros/); [ZT](https://www.zentacle.com/Beach/7184/tasco-gros)).
- La Vaca: "Don't dive directly under the boat buoy, but swim at 3m deep to the cave." and "This cave is across Punta de la Galeta, E part of Meda Gran." appear in both WD and ZT ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/La_Vaca/); [ZT](https://www.zentacle.com/Beach/1765/la-vaca)).
- WD's Carall Bernat text was already online in the 2008-10-07 Wayback capture, together with a dive log by "chris" dated 2008-06-27 ([Wayback 2008](https://web.archive.org/web/20081007113510/http://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Carall_Bernat)).
- DiveBuddy's Massa d'Or text carries an explicit credit: "From; montjoi.com/en/diving-roses/points-immersion | A legendary dive of the Cap de Creus." (entry dated 9/27/2010) ([DBY Wayback](https://web.archive.org/web/20150330103459/http://divebuddy.com/divesite/3213/illa-de-massa-dor-aka-la-rata-spain/)). The Montjoi page now returns 404, and no Wayback copy could be retrieved.
- The OSM Boreas description ("El Boreas fue originalmente un remolcador alemán construido en los años 30… adquirido por contrabandistas, y finalmente confisc", cut at OSM's 255-character limit) is not verbatim gidive. Gidive's text reads "…40 metros de eslora, que fue hundido en 1989… Su nombre original era Pellworm… remolcador de altura de la marina alemana…", and the OSM `image` tag hotlinks `gidive.com/archivos/imagenes/boreas-03203923.jpg` ([OSM](https://www.openstreetmap.org/node/13099227819/history); [gidive](https://www.gidive.com/es/Boreas)).
- The modern diveplannerpro text ("Carall Bernat is the iconic pinnacle of the Illes Medes — a tower of rock that breaks the surface…") and the duikersgids Dutch text do not reuse WD wording ([diveplannerpro](https://diveplannerpro.com/spots/es/costa-brava/es-medes-carall-bernat); [duikersgids](https://www.duikersgids.nl/en/dive-spots/carall-bernat)).

### Inferences
- Verbatim reproduction of idiosyncratic typos ("cos of", "breath", "A the", "on on", "beautifull", "begining", "groakes", "ist") across five pages makes Zentacle ← Wannadive conclusive, at least for the text fields.
- The same OSM user, elmagosamu, created the mARdEhIELO club node and edited the Dragonera wreck node that day (2025-08-26) ([OSM n13098914339](https://api.openstreetmap.org/api/0.6/node/13098914339/history); [OSM n11646580121](https://www.openstreetmap.org/node/11646580121/history)). That makes it likely the OSM wreck texts were written or paraphrased by a club member from dive-centre material, not copied from an aggregator.

### Gaps
- It was not checked whether Diveboard spot pages carried the WD description text (pages not retrieved).
- Montjoi's original text (2010) could not be retrieved, so its wording cannot be compared.

## 6. Which source appears oldest (Wayback and edit dates)

### Takeaway
Wannadive is the oldest dated source for the Medes records (≤ June 2008). dive-links.com predates March 2010 but is now dead. The other members of the Wannadive cluster are all dated later: Diveboard's GBIF dataset dates from 2013, Meteoconsult was captured by 2019 and Zentacle by 2023.

### Cited Findings
- **Wannadive Carall Bernat**: first Wayback capture 2008-10-07, with a dive log dated 2008-06-27 on the page ([Wayback](https://web.archive.org/web/20081007113510/http://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Carall_Bernat)). **WD El Boreas wreck**: first capture 2012-07-01 ([Wayback](https://web.archive.org/web/20120701204635/http://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/El_Boreas_wreck/)).
- **dive-links.com**: imported into OSM on 2010-03-10 (changeset 4094075, see section 7). The source pages `tauchplatz.php?id=1834/1835` appear in Wayback only as 404 captures (2021-05-06, 2024-01-17) ([Wayback 404](https://web.archive.org/web/20210506183657/http://www.dive-links.com/tauchplatz.php?id=1834)). A live fetch failed (connection reset).
- **OSM Medes nodes**: created 2010-06-26 by ZMWandelaar; most were repositioned on 2012-06-15 ([OSM n791018619](https://www.openstreetmap.org/node/791018619/history)).
- **DiveBuddy Massa d'Or**: entry text dated 2010-09-27; first capture 2013-11-08 ([Wayback 2013](https://web.archive.org/web/20131108194137/http://www.divebuddy.com/divesite/3213/illa-de-massa-dor-spain/)).
- **Diveboard**: the GBIF dataset was created 2013-10-01 ([GBIF API](https://api.gbif.org/v1/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2)). Diveboard logs contain retro-logged dives back to 2000/2003 (e.g. "Cavall Bernat" 2003-05-17), so event dates do not date the spot records (local file `diveboard.json`).
- **Meteoconsult "El Boreas wreck"**: first capture 2019-12-08 ([Wayback](https://web.archive.org/web/20191208212859/https://marine.meteoconsult.fr/meteo-marine/meteo-spots-de-plongee/bassin-par-defaut/previsions-meteo-el-boreas-wreck-5434-0.php)).
- **Zentacle**: first captures of /Beach/1764 and /Beach/1773 are 2023-08-31 ([Wayback](https://web.archive.org/web/20230831135221/https://www.zentacle.com/Beach/1773/carall-bernat)). The Medes IDs 1764–1773 are consecutive, which suggests a batch insert ([ZT list](https://www.zentacle.com/loc/es/ct/gi/lestartit)).
- **UKHO Boreas**: record originates in 1989 (Cadiz NM 489/89), last amended 2000-07-03. UKHO Reggio: 1992, amended 2019 (local file `wwshipwrecks.geojson`).

### Inferences
- Chronology (WD 2008 → Diveboard by about 2013 → Meteoconsult by 2019 → Zentacle by 2023) is consistent with WD as the root and the others as copies. No data runs the other way: WD cannot have copied Diveboard or Zentacle.

### Gaps
- Diveboard spot-page Wayback dates were not obtained (the CDX API was intermittently offline).
- WD's own spot-creation timestamps are not shown to anonymous users.

## 7. OSM provenance of the Begur and Medes dive spots (node history, changesets, `source=`)

### Takeaway
OSM has three unrelated provenance streams. (a) A 2010 bulk import from dive-links.com, still tagged unverified. (b) Medes spots hand-mapped by a Dutch mapper in 2010–2012, with no source declared. (c) Begur spots added in 2024 citing local knowledge plus a printed guidebook. No OSM edit cites Wannadive, Diveboard or Zentacle.

### Cited Findings
- **Changeset 4094075** (Tric, 2010-03-10, JOSM, 1,651 changes) has the comment **"Data import divespots from dive-links.com"**. Its nodes keep `source=www.dive-links.com`, `website=http://www.dive-links.com/tauchplatz.php?id=…` and `verified="no, please check and del this tag"` in 2026: Massa d'Or n663869684 and La Pedrosa n663869682 ([changeset](https://www.openstreetmap.org/changeset/4094075); [OSM n663869684](https://www.openstreetmap.org/node/663869684/history); [OSM n663869682](https://www.openstreetmap.org/node/663869682/history)). Tric's follow-up changeset 7339249 (2011-02-20) is "changing wrong link" ([changeset](https://www.openstreetmap.org/changeset/7339249)).
- The dive-links coordinates carry the same 1/60 artefact (e.g. 3.2050667 = 3°12.304′; 3.3314833 = 3°19.889′), so dive-links also stored decimal minutes. They differ from WD by 29–68 m ([OSM n663869682](https://www.openstreetmap.org/node/663869682/history); [WD La pedrosa](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/La_pedrosa/)).
- **Medes**: the node histories checked (791018569 Tasco Gros, 791018574 la Vaca, 791018578 el Medallot, 791018588 Pota del Llop, 791018619 Carall Bernat, 791018624 Dolfi Nord) were all created by ZMWandelaar on 2010-06-26 (changeset 5080187, "Changes Achterberg", JOSM nl) and adjusted on 2010-07-31 (5364350, "Changes Diving"). Most were repositioned on 2012-06-15 (11905429, "Changes Estartit", 1,039 changes), which also created El Reggio, la Ferriola and Negre del Falaguer. None of these changesets has a `source` tag ([changeset 5080187](https://www.openstreetmap.org/changeset/5080187); [changeset 5364350](https://www.openstreetmap.org/changeset/5364350); [changeset 11905429](https://www.openstreetmap.org/changeset/11905429)). In the same 2012 changeset, ZMWandelaar also moved the dive-links "la Pedrosa" node from 42.0736000/3.2050667 to 42.0734310/3.2048378 ([OSM n663869682](https://www.openstreetmap.org/node/663869682/history)).
- Later Medes edits only changed tags: thetornado76 2015-12-09 "correct same scuba tags" ([changeset 35841584](https://www.openstreetmap.org/changeset/35841584)), and LifeEncrypter 2025-06-18 "Added scuba diving related tags to sites in the estartit area", `source=survey;aerial imagery` ([changeset 167799743](https://www.openstreetmap.org/changeset/167799743)).
- **Begur**: mauriciabad, changeset 155672598 (2024-08-23, iD, 67 changes), "Dive sites in Begur", `source=local knowledge;Book: Guia Submarina de la Costa Brava de Sant Feliu de Guíxols a Begur by Andreu Llamas`, imagery ICGC/PNOA, review_requested=yes ([changeset](https://www.openstreetmap.org/changeset/155672598)). Follow-ups: 185118771 (2026-07-05, "Add sport:scuba_diving…", source local knowledge) ([changeset](https://www.openstreetmap.org/changeset/185118771)), and 2026-09 position tweaks to Canons de Tamariu and Barda de Fitor ([OSM n12132826555](https://www.openstreetmap.org/node/12132826555/history); [OSM n12132826563](https://www.openstreetmap.org/node/12132826563/history)).
- **Boreas**: elmagosamu, changeset 171054076 (2025-08-26, comment "Boreas", iD, the user's 6th changeset, iD walkthrough started), followed by 171087663 "Correccion". Neither has a source tag ([changeset](https://www.openstreetmap.org/changeset/171054076); [changeset](https://www.openstreetmap.org/changeset/171087663)).
- **Formigues**: Chompas, changeset 186884685 (2026-08-03, "Add dive spot"), no source tag ([changeset](https://www.openstreetmap.org/changeset/186884685)).

### Inferences
- OSM is not a downstream copy of the Wannadive cluster for any site examined. Its only documented external source is dive-links.com, a German site from before 2010 that is now dead and independent of WD (positions differ by 30–70 m).
- The dive-links nodes have been flagged "please check" for 16 years. For the afons project they should be treated as unverified third-party data, and their licence status (a 2010 import, pre-ODbL) is questionable.
- The Begur set is the best-documented OSM provenance (declared book plus local knowledge). Its coordinates are hand-placed against ICGC orthophotos.

### Gaps
- No contact with or statement from ZMWandelaar on how the Medes points were obtained (GPS survey or estimate). The changeset comments are non-informative.

## 8. Inferred copying and derivation graph

### Takeaway
The databases form one large copy cluster rooted in Wannadive (Diveboard, Zentacle, Meteoconsult), plus several independent lineages (OSM-ZMWandelaar, OSM via dive-links, OSM-Begur via the Llamas book, DiveBuddy via Montjoi, UKHO). Corroborating a position by counting matching websites is invalid inside the cluster.

### Cited Findings
- WD to Diveboard: identical coordinates after rounding at 13 sites, the WD region hierarchy in verbatimLocality, and WD-specific names ("Ile de Tosca", "Islas Formigas", "Dolphin's Cave", "Reggio Messina Wreck") (sections 2–3; `diveboard.json`; WD pages).
- WD to Zentacle: exact coordinates with 1/60 artefacts, verbatim descriptions and aliases with typos, WD average depth mapped to max depth (5/5), and the same 21-site L'Estartit set (sections 2–5; [ZT list](https://www.zentacle.com/loc/es/ct/gi/lestartit)).
- WD to Meteoconsult: an identical DDM string and lower-case "El Boreas wreck" ([MC](https://marine.meteoconsult.fr/meteo-marine/bulletin-detaille/spot-de-plongee-5434/previsions-meteo-el-boreas-wreck-aujourdhui); [WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Palamos_town_to_Cap_de_Begur/El_Boreas_wreck/)).
- dive-links.com to OSM: declared import in changeset 4094075 ([changeset](https://www.openstreetmap.org/changeset/4094075)).
- Llamas book plus local knowledge to OSM Begur: declared in changeset 155672598 ([changeset](https://www.openstreetmap.org/changeset/155672598)).
- montjoi.com text to DiveBuddy: declared "From; montjoi.com…" ([DBY](https://web.archive.org/web/20150330103459/http://divebuddy.com/divesite/3213/illa-de-massa-dor-aka-la-rata-spain/)).
- gidive to OSM Boreas: hotlinked image and paraphrased narrative. The depth of 18–32 m matches WD ([OSM](https://www.openstreetmap.org/node/13099227819/history); [gidive](https://www.gidive.com/es/Boreas)).
- Wannadive's terms on each spot page: "You are free to use Wannadive.net KML/GPS data files ONLY for your personal use" ([WD](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/Carall_Bernat/)).
- GBIF lists the Diveboard dataset licence as CC BY-NC 4.0, while its description text says Diveboarders dedicated the data "to the public domain under a Creative Commons Zero waiver" ([GBIF](https://www.gbif.org/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2); [GBIF API](https://api.gbif.org/v1/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2)).

```
                       Wannadive.net (user wiki, ≤2008; DDM 3-dec)
                      /            |               \
     (rounded; region names;   (DDM string;      (exact DDM→dec, texts+typos,
      "Ile de Tosca")           "El Boreas wreck") avg→max depth, same 21 sites)
            v                      v                      v
   Diveboard spot DB  - - ?- - -> Zentacle (≤2023)    Meteoconsult (≤2019)
            |   ("Escrivana", "El Negre de Fallaguer" shared by DB & ZT)
            v
   GBIF Diveboard export (4-5 dec, ±100 m)

 Independent lineages (no coordinate match with the cluster):
   dive-links.com (≤2010, dead) ──import 2010──> OSM Massa d'Or, La Pedrosa (unverified)
   ZMWandelaar (2010/2012, no source) ─────────> OSM Medes, Reggio, Ferriola, Negre
   Llamas guidebook + local knowledge (2024) ──> OSM Begur (Fitor, Canons, Aigua Xelida…)
   gidive (image/text) + WD-like depth ────────> OSM Boreas (2025, position ~2 km off)
   montjoi.com (text) + map click ─────────────> DiveBuddy Massa d'Or (2010)
   UKHO / Spanish NM 1989 (bearing & distance) ─> EMODnet wrecks (Boreas 938 m from WD)
   duikersgids, diveplannerpro, dive.site ──────> own texts; no coordinates exposed
```

### Inferences
- For afons deduplication, treat WD, DB, ZT and MC as **one** source ("Wannadive lineage"). Agreement among them is not independent confirmation, and WD's "Approximate" flags (Boreas, Tasco Gros, Formigues, Ullastre, Furió, Massa d'Or) apply to all of them.
- The only genuinely independent cross-checks available are OSM (with its three sub-lineages), UKHO (for wrecks) and DiveBuddy. Where these disagree with the cluster by 20–140 m (Medes, Formigues), the truth is unknown without an official or survey source. For Boreas (≥0.9 km between every source pair) and Furió Fitó (WD ~2.4 km off), at least one lineage is clearly wrong.
- Licensing risk: WD restricts GPS data to personal use, and the GBIF licence for Diveboard is NC (conflicting with the CC0 text). Data in the WD lineage is therefore questionable for redistribution, whatever the channel it arrives through. OSM-Begur (ODbL, declared sources) and UKHO/EMODnet are cleaner.

### Gaps
- **PADI (travel.padi.com)** was skipped. Its robots.txt has `User-agent: *` followed by `Disallow: /dive-site/`, `/site-plongee/` and `/dive-sites/` (lines ~129–148 at fetch time) ([robots.txt](https://travel.padi.com/robots.txt)).
- **Scubago / divessi**: divessi site URLs 301-redirect to a generic Scubago "forward-mdg" page, and Scubago site pages render client-side, so no coordinates were obtained. SSI labels its data "provided from the logbook information in the MySSI app" ([divessi](https://www.divessi.com/en/mydiveguide/divesite/tasco-petit-spain-89309); [scubago](https://www.scubago.com/en/explore/divesite/carall-bernat-73474)).
- **dive.site** serves a Cloudflare JS challenge, so it was not fetched ([dive.site](https://dive.site/explore/site/carall-bernat-j8Lv)).
- **divezone, DeeperBlue, DiveAdvisor**: no Catalan dive-site pages with coordinates were found. DiveAdvisor search hits were dive-shop listings ([DiveAdvisor](https://diveadvisor.com/medaqua)), and DeeperBlue had only a general article ([DeeperBlue](https://www.deeperblue.com/scuba-diving-spain/)).
- **Wikiloc** and **tourism pages** (Estartit, Costa Brava): searches returned no dive-site pages with coordinates.
- No public statement from Diveboard or Zentacle about importing Wannadive was found. The derivation rests on the forensic evidence above.
