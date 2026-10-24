# Open biodiversity observation and citizen-science datasets for underwater POIs on the Catalan coast (as of 2026-10)

Method note: live API calls were made on 2026-10-24 against api.gbif.org, api.obis.org, api.inaturalist.org and api.minka-sdg.org. The GBIF and OBIS calls used this rough WKT polygon for Catalan coastal waters, from Cerbère to the Ebro delta:
`POLYGON((0.6 40.45,1.2 40.45,2.2 41.0,3.4 41.6,3.6 42.45,3.17 42.45,3.15 42.25,3.2 42.0,2.8 41.65,2.25 41.35,1.65 41.18,0.95 41.0,0.75 40.8,0.6 40.45))`
The polygon is approximate and also takes in a strip of coastal land, so the raw totals include terrestrial records such as birds. Counts filtered by taxon or dataset are the reliable ones. Read every count as "about, on that date".

## 1. GBIF: coverage, filters, licenses, and can locality strings be clustered into dive sites?

### Takeaway
GBIF holds about 5.2M occurrences in the polygon, but most are plankton or survey data. The datasets that matter for dive sites are smaller and have clean site names. Three stand out:
- **Diveboard**: 923 records, 86 named dive sites, every record has depth, CC BY-NC.
- **ClimateFish (T-MEDNet)**: 3,030 records with named sites such as Punta Salines, El Gat and Cap Gros. CC BY.
- **BioObs and CROMIS (FFESSM)**: 26.7k and 8.1k records, mostly Cap de Creus and Medes. CC BY, but no locality strings, only coordinates that repeat at the same sites.

GBIF iNaturalist records carry no `locality` field. Records of sensitive taxa such as Pinna come through obscured, with about 27.7 km uncertainty.

### Cited Findings
- **API endpoint**: `https://api.gbif.org/v1/occurrence/search` accepts `geometry` (WKT), `depth=min,max`, `basisOfRecord`, `license`, `taxonKey`, `datasetKey`, and `facet=datasetKey|license|year|basisOfRecord`. All were tested live — [GBIF API](https://api.gbif.org/v1/occurrence/search)
- **Live counts in the polygon** (2026-10-24) — [GBIF API](https://api.gbif.org/v1/occurrence/search):
  - All records: 5,194,465
  - `basisOfRecord=HUMAN_OBSERVATION`: 1,564,005 (includes coastal land records)
  - `depth=0,100`: 3,455,163
  - `depth=0,100` together with HUMAN_OBSERVATION: only 1,716. Citizen observations rarely fill the depth field.
- **Licenses for depth=0,100 records**: CC BY-NC 4.0 3,438,565; CC BY 4.0 16,504; CC0 94. The NC total is dominated by one dataset (next item) — [GBIF API](https://api.gbif.org/v1/occurrence/search?license=CC_BY_NC_4_0)
- **Licenses for HUMAN_OBSERVATION records**: CC BY 919,260; CC BY-NC 488,736; CC0 156,009 — [GBIF API facet=license](https://api.gbif.org/v1/occurrence/search?basisOfRecord=HUMAN_OBSERVATION&facet=license)
- **Largest datasets with depth in the polygon**:
  - Ebro delta phytoplankton: 3,431,219 records, CC BY-NC — [dataset cd359f61](https://api.gbif.org/v1/dataset/cd359f61-5eea-4e9c-ad45-284e7594b6de)
  - ICATMAR bottom trawl: 8,895 records, CC BY — [fafbf6ab](https://api.gbif.org/v1/dataset/fafbf6ab-a219-464d-8783-940528298b66)
  - ClimateFish: 3,030 records, CC BY — [04036f89](https://api.gbif.org/v1/dataset/04036f89-d147-4e0c-adb1-93f9ba822257)
  - ARMS metabarcoding: 2,570 records — [17930d18](https://api.gbif.org/v1/dataset/17930d18-ba23-4954-95b0-c919b743086d)
  - ICM-CSIC CBMR collections: 1,311 records, CC BY-NC — [1d743188](https://api.gbif.org/v1/dataset/1d743188-1e65-4d99-a814-fa3fd51f1490)
  - Diveboard: 923 records, CC BY-NC — [66f6192f](https://api.gbif.org/v1/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2)
  - Seawatchers: 736 records with depth, 1,234 in total, CC BY-NC — [aa0eee05](https://api.gbif.org/v1/dataset/aa0eee05-8fb0-4dcb-8f20-41b7e4e7fca5)
- **Target-taxon counts in the polygon** — [GBIF API](https://api.gbif.org/v1/occurrence/search?taxonKey=4374731):

  | Taxon | taxonKey | Records |
  |---|---|---|
  | Pinna nobilis | 4374731 | 212 |
  | Epinephelus marginatus | 2388507 | 1,397 |
  | Hippocampus | 8156547 | 192 |
  | Corallium rubrum | 5185014 | 1,099 |
  | Paramuricea clavata | 2261251 | 905 |
  | Posidonia oceanica | 5328663 | 856 |
  | Nudibranchia | 980 | 4,376 |

- **Where the Pinna nobilis records come from**:
  - Datasets: BioObs 76, iNaturalist 50, Seawatchers 47, CROMIS 15, Observation.org 5, MCNB-Malac 4, MINKA BioPlatgestMet 2, Generalitat "Citacions biodiversitat ENPE" 1
  - Licenses: CC BY-NC 114, CC BY 97, CC0 1
  - Basis of record: HUMAN_OBSERVATION 159, MACHINE_OBSERVATION 47, preserved specimen 6
  - Locality is null in 193 of 212. Coordinate uncertainty is about 27,661–27,785 m on about 49 records, which is iNaturalist obscuring.

  Source: [GBIF API facets](https://api.gbif.org/v1/occurrence/search?taxonKey=4374731&facet=datasetKey)
- **Epinephelus marginatus**: the first 300 records were all from "iNaturalist research-grade observations", and all had `locality = null` — [GBIF API](https://api.gbif.org/v1/occurrence/search?taxonKey=2388507)
- **iNaturalist research-grade dataset on GBIF** (50c9509d): 80,497 records in the polygon — [GBIF API](https://api.gbif.org/v1/occurrence/search?datasetKey=50c9509d-22c7-4a22-a47d-8c48425ef4a7)
- **Diveboard** ("Scuba diving citizen science observations", DOI 10.15468/tnjrgy, CC BY-NC 4.0) — [GBIF dataset](https://api.gbif.org/v1/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2):
  - 923 records in the polygon, 86 distinct `locality` values, every record has `depth` (example: La Vaca, depth 11.9 m, coordinateUncertaintyInMeters 100), years 1987–2019.
  - Locality values are real dive-site names with consistent coordinates, for example: Ullastre I/II/III (41.89, 3.20), Mar Menuda and L'Illa in Tossa (41.72, 2.94), Port Salvi (41.771, 3.03), El Pinell, La Caleta, La Vaca, Boreas wreck (41.827, 3.128), Furió d'Aigua Xelida, Canons de Tamariu, La Llosa de Palamós, Ferranelles, Carall Bernat, Tascó Petit, Pota del Llop, Cala Viuda, Lanishen wreck (42.285, 3.297) and Illes Formigues.
  - Some strings have mojibake ("Ruta Cl�sica").
- **ClimateFish (T-MEDNet)**, DOI 10.15468/wphfqt, CC BY 4.0 — [GBIF dataset](https://api.gbif.org/v1/dataset/04036f89-d147-4e0c-adb1-93f9ba822257):
  - 3,030 records. Localities are site names such as Punta_Salines, Punta_del Falco, Punta_Forallons, El_Gat, Cap_Gros, Encalladora, Sarnella, Illa_Grossa, Punta_Cala Culip and Punta_Tres Frares.
  - Depth is given (for example 2 m). Years 2009–2020, with 1,290 records in 2020.
- **BioObs** (FFESSM "observations naturalistes en milieux aquatiques"), CC BY 4.0 — [GBIF dataset 25e3e8f1](https://api.gbif.org/v1/dataset/25e3e8f1-86ee-440c-adfc-8e63759a6505):
  - 26,736 records in the polygon. Depth and locality are empty in the sample.
  - Coordinates repeat at the same points, for example 42.433/3.175 (Cerbère–Banyuls border) 135 times and 42.06/3.213 (Medes).
- **CROMIS** ("carnet de plongée en ligne de la FFESSM", an online dive logbook), CC BY 4.0 — [GBIF dataset 8e9974a4](https://api.gbif.org/v1/dataset/8e9974a4-12e2-475f-9aec-5abdf24a1f50):
  - 8,078 records in the polygon, no depth or locality in the sample.
  - Repeated coordinates at Medes (42.047/3.225, 42.042/3.226) and Cap de Creus (42.238/3.265).
- **Seawatchers / Observadores del Mar on GBIF** ("Global Marine biodiversity data from Seawatchers Marine Citizen Science Platform", CC BY-NC 4.0) — [GBIF dataset aa0eee05](https://api.gbif.org/v1/dataset/aa0eee05-8fb0-4dcb-8f20-41b7e4e7fca5):
  - 1,234 records in the polygon, `locality` null in the sample, coordinateUncertainty null.
  - A separate dataset, "Observadores del Mar – Crustáceos Decápodos" (ba5f097c, CC BY-NC), has 197 records in the polygon, also without locality — [GBIF](https://api.gbif.org/v1/dataset/ba5f097c-54d3-48ac-a57f-6d93cdbc85c8)
- **Reef Life Survey** datasets on GBIF return 0 records in the Catalan polygon. This covers the Global reef fish dataset 38f06820 (CC BY), Cryptic Fish f8f683a8, e2b51a4e and e8443518 — [GBIF dataset search](https://api.gbif.org/v1/dataset/search?q=Reef%20Life%20Survey)
- **Generalitat "Citacions biodiversitat Espais Naturals Protecció Especial"** (792ec010, CC BY-NC) — [GBIF dataset](https://api.gbif.org/v1/dataset/792ec010-bfd7-4cae-b05e-8ad1553bac9e):
  - 5,414 records in the polygon.
  - Localities are mostly coastal or terrestrial ENPE places ("Bassa de Cap Gros", "Punta de Cap de Creus, Cadaqués", "Roses [518/680]").
- **Bulk download**: GBIF downloads need a free account and give a citable DOI (`POST https://api.gbif.org/v1/occurrence/download/request`) — [GBIF API docs](https://techdocs.gbif.org/en/openapi/v1/occurrence)

### Inferences
- **Clustering**: yes, for the dive-focused datasets. Group Diveboard by `locality` plus rounded lat/lon to get a ready list of about 80+ named Costa Brava sites. ClimateFish gives T-MEDNet-style named monitoring sites. For BioObs and CROMIS, cluster on repeated exact coordinates (DBSCAN about 100–200 m) to get unnamed hotspot points. iNaturalist-in-GBIF is the least useful for site names because it has no locality and its sensitive taxa are obscured.
- **License filtering**: filtering to `license=CC_BY_4_0` and `CC0_1_0` gives redistributable records (BioObs, CROMIS, ClimateFish, ICATMAR). CC BY-NC (Diveboard, Seawatchers, iNaturalist, MINKA) can only go into an open project that is itself non-commercial. Otherwise use it only to derive facts (a site name plus approximate position), without republishing the records. The legal reading that a derived site list is not covered by NC terms is an inference, not legal advice.
- **Depth filter**: `depth` together with HUMAN_OBSERVATION is too restrictive (1,716 records). Filter by taxon or dataset instead.

### Gaps
- GBIF occurrence search has no `locality` facet, so the distinct-locality counts above come from paging through records; the full counts for the larger datasets were not computed.
- No precise land/sea mask was used, so the raw polygon totals overstate marine records.

## 2. OBIS (api.obis.org)

### Takeaway
OBIS has about 5.0M records and 107 datasets in the polygon. Most of the volume is OBSEA seabed observatory video data off Vilanova i la Geltrú (CC BY). OBIS also carries the iNaturalist marine subset (36k records, CC BY-NC). It adds little in the way of dive-site names, and has only 93 Pinna nobilis records.

### Cited Findings
- **Polygon totals**: `GET https://api.obis.org/v3/statistics?geometry=<WKT>` returned 5,008,765 records, 2,131 species, 107 datasets, years 1893–2026 — [OBIS API](https://api.obis.org/v3/statistics)
- **Top datasets** from `GET /v3/dataset?geometry=<WKT>` — [OBIS API](https://api.obis.org/v3/dataset):
  - Biodiversity at OBSEA seabed observatory: 2024 2,668,752; 2025 1,422,068; 2023 529,631; 2026 145,353. All CC BY 4.0.
  - Ebro delta phytoplankton: 126,876, CC BY-NC
  - iNaturalist Research-grade Observations Marine Subset: 36,100, CC BY-NC 4.0
  - HMAP Dataset 10, Catalonian Coast (historical fisheries): 17,077, CC BY
  - MEDITS trawl: 13,264, CC BY
- **Pinna nobilis**: `GET /v3/occurrence?scientificname=Pinna nobilis&geometry=<WKT>` returned 93 records — [OBIS API](https://api.obis.org/v3/occurrence?scientificname=Pinna%20nobilis)

### Inferences
- OBIS records include `minimumDepthInMeters`/`maximumDepthInMeters` and quality flags, which makes OBIS a useful marine-only filter. For POIs, though, GBIF's Diveboard, ClimateFish, BioObs and CROMIS datasets are more direct. OBSEA is a single fixed point (an observatory), not a dive site.

### Gaps
- No per-dataset check of whether OBIS includes Diveboard, BioObs or CROMIS in this area. They did not appear in the top 12.

## 3. iNaturalist and MINKA

### Takeaway
iNaturalist has thousands of marine observations in Catalonia (place_id 61614), mostly CC BY-NC. Every Pinna nobilis, Corallium rubrum and Epinephelus marginatus record there is obscured, and nearly all Hippocampus records are.

MINKA (ICM-CSIC, iNaturalist-software fork) has far more Catalan marine data: the "Biodiversitat Marina a Catalunya" umbrella project holds 540k observations. Its `place_guess` field often holds real dive-site names (Carall Bernat, Massa d'Or, Llosa de Garbí, Sot d'en Boada). Groupers were not obscured in the sample, but Pinna nobilis is.

### Cited Findings
- **iNaturalist Catalunya place**: id 61614 — [iNat API places](https://api.inaturalist.org/v1/places/autocomplete?q=Catalunya)
- **iNaturalist counts in place 61614** (`/v1/observations?place_id=61614&taxon_id=..&per_page=0`, plus `taxon_geoprivacy=obscured` and `license=` filters) — [iNat API](https://api.inaturalist.org/v1/observations?place_id=61614&taxon_id=118945):

  | Taxon | Total | Obscured | CC BY-NC | CC BY | CC0 |
  |---|---|---|---|---|---|
  | Pinna nobilis | 35 | 35 | 29 | 1 | 0 |
  | Epinephelus marginatus | 207 | 207 | 176 | 6 | 0 |
  | Hippocampus | 224 | 210 | 147 | 6 | 1 |
  | Corallium rubrum | 37 | 37 | 32 | 0 | 0 |
  | Nudibranchia | 5,316 | 0 | 4,585 | 14 | 15 |

  The remaining records are under other licenses or none.
- **Project search**: iNaturalist project autocomplete returned no hits for "marina catalunya", "observadores del mar" or "costa brava marine". The well-known Catalan marine projects live on MINKA — [iNat API projects](https://api.inaturalist.org/v1/projects/autocomplete?q=marina%20catalunya)
- **How obscuring works**: the public location becomes a random point within a 0.2 x 0.2 degree cell, and positional accuracy is set to that cell's diagonal. Locality text is coarsened too. True coordinates stay private, though country, state and county searches use them — [iNaturalist Help](https://help.inaturalist.org/en/support/solutions/articles/151000169938-what-is-geoprivacy-what-does-it-mean-for-an-observation-to-be-obscured-). This matches the 27.7 km uncertainty on GBIF iNat records — [GBIF API](https://api.gbif.org/v1/occurrence/search?taxonKey=4374731)
- **MINKA API**: iNaturalist-compatible, `https://api.minka-sdg.org/v1/observations?project_id=..` (tested live). The Python client `mecoda-minka` notes an API cap of 20,000 observations per query — [PyPI mecoda-minka](https://pypi.org/project/mecoda-minka)
- **MINKA governance and GBIF sharing**: run by ICM-CSIC; research-grade data is shared with GBIF — [GBIF.es](https://gbif.es/en/coleccion/icm-csic-minka-observatorio-de-ciencia-ciudadana/); [MINKA about](https://minka-sdg.org/pages/about_us). Citation guidelines exist (Zenodo, CC BY for the guidelines document itself) but do not state a license for observations — [Zenodo](https://zenodo.org/records/14647613)
- **MINKA projects and live counts** — [MINKA API](https://api.minka-sdg.org/v1/projects/autocomplete?q=marina):

  | id | Project | Total | CC BY-NC | CC BY | CC0 | CC BY-SA |
  |---|---|---|---|---|---|---|
  | 175 | biodiversitat-marina-a-catalunya | 540,522 | 384,283 | 113,381 | 453 | 59 |
  | 74 | BMMATARÓ | 36,665 | 20,829 | 3,312 | – | – |
  | 146 | ANERIS UNISUB l'Estartit | 34,904 | 23,161 | 5,532 | – | – |
  | 174 | Biodiversitat Marina al PNMMBT (Montgrí–Medes–Baix Ter) | 41,134 | 28,211 | 6,543 | – | – |
  | 263 | Biodiversitat Marina al PNCC (Cap de Creus) | 30,741 | 16,634 | 8,325 | – | – |
  | 576 | BioMARató 2026 (Catalunya) | 96,429 | 49,422 | 41,395 | 106 | – |
  | 417 | BioMARató 2025 (Catalunya) | 95,410 | 65,711 | 22,781 | 116 | 46 |

  Other projects: ANERIS Port de Tarragona (160), L'Ametlla de Mar (290), Banys del Fòrum DIVA (25), VIMAR (179), Platges de Barcelona (3), and BioMARató editions 2022–2026 with Girona and Tarragona splits (20, 124, 280, 281, 283, 418, 577, 578).
- **MINKA place_guess, Epinephelus marginatus** in project 175 (3,910 observations; sample of 200, all `obscured: false`). Top values: "Massa d'Or" 44, "el Portitxol, Torroella de Montgrí" 28, "Carall Bernat" 16+6, "Illes Medes", "Masia Blanca (Reserva Marina)", "Punta dels Forallons", "Sot d'en Boada (Tossa de Mar)", "LLOSA DE GARBI", "morro de vedell" — [MINKA API](https://api.minka-sdg.org/v1/observations?project_id=175&taxon_name=Epinephelus%20marginatus)
- **MINKA place_guess, Nudibranchia**: "Embarcador del Francès, Illes Medes", "Dic de Llevant, Parc Subaquàtic, Tarragona", "Pota del Llop", "Tascó Petit", "Zona de Banys Fòrum" — [MINKA API](https://api.minka-sdg.org/v1/observations?project_id=175&taxon_name=Nudibranchia)
- **MINKA Pinna nobilis** (project 175): 168 observations. The sample is `obscured: true`, `taxon_geoprivacy: obscured`, place_guess "Spain", cc-by-nc — [MINKA API](https://api.minka-sdg.org/v1/observations?project_id=175&taxon_name=Pinna%20nobilis)
- **MINKA datasets on GBIF are CC BY-NC**: MINKA_BioPlatgestMet (9a51436f), MINKA_Medusa_a_la_vista (247fd45a, jellyfish sightings) — [GBIF dataset search](https://api.gbif.org/v1/dataset/search?q=MINKA)

### Inferences
- MINKA project 175 with `license=cc-by` (113k observations) is the largest redistributable citizen-science pool for the Catalan sea. Its free-text place_guess plus coordinates can be clustered to name sites. Normalize strings first: mixed Catalan/Spanish reverse-geocoded addresses, case and encoding.
- Hotspots of protected species (Pinna, red coral) cannot be located precisely from iNaturalist or MINKA. That is a deliberate conservation choice, and an open POI project should respect it.

### Gaps
- No MINKA terms-of-use page was found stating default observation and photo licenses. Licenses are per record (`license_code`).
- No full-population check was made of how often MINKA records are obscured for Epinephelus. The sample of 200 showed none.

## 4. Observadores del Mar / Seawatchers, Reef Check, jellyfish, Pinna projects, BDBC, Biodiversidad Virtual

### Takeaway
Observadores del Mar (ICM-CSIC) reaches GBIF as "Seawatchers" (CC BY-NC, 1,234 records in the polygon, no locality). Its own site is online, but no documented API or bulk-download terms were found. BDBC (biodiver.bio.ub.es) did not respond, and its GBIF datasets such as MolusCat are CC BY-NC with 0 marine records in the polygon. Reef Check Med, Biodiversidad Virtual, "Projecte Pinna" and "Tropical Signals" were not verified in this session.

### Cited Findings
- **Observadores del Mar**: launched 2012, about 5,500 scientist-validated observations, published as "Global Marine biodiversity data from Seawatchers Marine Citizen Science Platform 1980-2020" — [data.biodiversity.be](https://data.biodiversity.be/ja/dataset/aa0eee05-8fb0-4dcb-8f20-41b7e4e7fca5); license CC BY-NC per [GBIF](https://api.gbif.org/v1/dataset/aa0eee05-8fb0-4dcb-8f20-41b7e4e7fca5). It was used to collect diver reports on Pinna nobilis mortality — [Noudiari](https://www.noudiari.es/noticias-ibiza-formentera-sidebar/jornada-informativa-la-extincion-del-molusco-gigante-pinna-nobilis/)
- **observadoresdelmar.es** returned HTTP 200 on 2026-10-24 — [observadoresdelmar.es](https://www.observadoresdelmar.es/)
- **BDBC GBIF datasets**: "Banc de dades de biodiversitat de Catalunya-MolusCat" (85864fc6) and ArtroCat are CC BY-NC. MolusCat has 0 records in the marine polygon — [GBIF](https://api.gbif.org/v1/dataset/search?q=Biodiversitat%20Catalunya)
- **Jellyfish data**: MINKA "Medusa a la vista" on GBIF, CC BY-NC — [GBIF](https://api.gbif.org/v1/dataset/247fd45a-0dd7-415d-9f47-699090f39cf5)

### Gaps
- No verified data access or license details for Reef Check Mediterranean, Biodiversidad Virtual (underwater photo galleries), "Projecte Pinna", "Tropical Signals" or the "Alerta Meduses" app.
- biodiver.bio.ub.es/biocat did not connect (HTTP 000), so the BDBC marine coverage is unknown.

## 5. Dive-oriented monitoring: RLS, T-MEDNet, ClimateFish, CEAB/Medes, MedPAN

### Takeaway
T-MEDNet is the best structured source for named monitoring sites: temperature sites (Spanish Catalan coast region), mortality data and ClimateFish. The site states "T-MEDNet data is open access", with registration required for downloads. ClimateFish is on GBIF as CC BY with site names. Reef Life Survey has no records in Catalan waters on GBIF.

### Cited Findings
- **What T-MEDNet offers**: in situ temperature, Monitoring Mortality, Mass Mortality Events, Climate Fish and marine heatwaves, with a focus on MPAs — [T-MEDNet](https://t-mednet.org/)
- **T-MEDNet access** — [T-MEDNet request data](https://t-mednet.org/request-data):
  - "T-MEDNet data is open access."
  - Temperature data is requested per site.
  - Mortality and ClimateFish downloads come from the Explore pages after registering.
  - Sites are grouped by region, including "Spanish Catalan and Balearic coasts".
  - No explicit license is stated on the page.
- **ClimateFish on GBIF**: CC BY 4.0, 3,030 Catalan records with site names and depth — [GBIF](https://api.gbif.org/v1/dataset/04036f89-d147-4e0c-adb1-93f9ba822257)
- **Reef Life Survey on GBIF**: 0 records in the Catalan polygon — [GBIF](https://api.gbif.org/v1/occurrence/search?datasetKey=38f06820-08c5-42b2-94f6-47cc3e83a54a)
- **Generalitat monitoring contract**: a contract with the Universitat de Barcelona extends marine community monitoring to all PEIN and Natura 2000 marine areas, beyond the marine parks — [govern.cat 2021](https://govern.cat/govern/docs/2021/07/22/13/23/5fc191df-d00c-426c-b034-02df39d9507d.pdf)
- **FECDAS / CEM participatory Posidonia monitoring in Garraf**: 2025 report — [FECDAS](https://fecdas.cat/wp-content/uploads/INFORME_Posidonia_Garraf_2025.pdf)

### Gaps
- The T-MEDNet temperature site-list page with coordinates could not be fetched (a guessed URL returned 404), so the Catalan site names and coordinates are unverified. The Terms of Use were not read.
- CEAB Medes long-term monitoring and MedPAN datasets were not located as open downloads.

## 6. Generalitat open data (Dades Obertes)

### Takeaway
The Socrata catalog of analisi.transparenciacatalunya.cat has no marine-species occurrence datasets. Searches for "biodiversitat marina" and "posidonia" returned 0 results; "litoral" found only context layers. Generalitat species citations appear on GBIF instead, as "Citacions biodiversitat ENPE" (CC BY-NC).

### Cited Findings
- **Socrata catalog API** (`https://api.eu.socrata.com/api/catalog/v1?domains=analisi.transparenciacatalunya.cat&q=...`) — [Socrata catalog](https://api.eu.socrata.com/api/catalog/v1?domains=analisi.transparenciacatalunya.cat&q=litoral):
  - "litoral" returned: Lidar litoral de Catalunya (g97a-sa72), Batimetria de Catalunya (xc5v-h37b), Platges de Catalunya (83qv-sib8), Ortofoto de costa (7i72-2qm9), Risc per Contaminació Marina (ht7z-bwsq).
  - "biodiversitat marina" and "posidonia" returned 0 results.
- **Generalitat species citations on GBIF**: "Citacions biodiversitat Espais Naturals Protecció Especial" (792ec010), CC BY-NC, 5,414 records in the polygon — [GBIF](https://api.gbif.org/v1/dataset/792ec010-bfd7-4cae-b05e-8ad1553bac9e)
- **Marine habitat mapping of the Catalan coast** (2022 presentation) — [participa.gencat.cat](https://participa.gencat.cat:443/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdnMwIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--cac3d46a6e7b7dfe0509f77a99deecba18a1b9d/2022_Mapa_Habitats_Marins_Sessio_Transferencia.pdf)

### Inferences
- Bathymetry (xc5v-h37b) and the beaches list (83qv-sib8) are useful for context and for checking POIs, but they are not observation data.

### Gaps
- The Generalitat habitat map (Cartografia d'hàbitats marins) and its download or license were not confirmed in the catalog.
