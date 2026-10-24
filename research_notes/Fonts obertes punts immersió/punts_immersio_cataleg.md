# Fonts obertes/reutilitzables de punts d'immersió a la costa catalana (estat a 2026-10)

## OpenStreetMap / OpenSeaMap: quins tags s'usen a Catalunya, recomptes reals i consulta Overpass

### Takeaway
OSM (ODbL) és l'única font oberta real amb coordenades de punts d'immersió a Catalunya, però és escassa. Un Overpass real (2026-10-24) sobre el bbox 40.5,0.15,42.45,3.35 retorna uns 47 elements que són punts d'immersió o derelictes, concentrats a les Medes/l'Estartit (~18) i Begur-Tamariu-Aiguablava (~22). Pràcticament no hi ha res a Tossa, Palamós (tret del Boreas), l'Escala, Llançà, Maresme, Garraf ni l'Ebre. El tag de facto és `sport=scuba_diving` + `scuba_diving:divespot=yes` (+ `scuba_diving:maxdepth`). `leisure=dive_site` no s'usa.

### Cited Findings
- Esquema recomanat a la wiki d'OSM: es marca l'element físic (natural=reef, historic=wreck…) amb `sport=scuba_diving` + `scuba_diving:divespot=yes`, i s'hi afegeixen `name`, `scuba_diving:depth`, `scuba_diving:maxdepth`, `scuba_diving:entry=boat|shore|pier|ladder`, `scuba_diving:drift=yes` i `scuba_diving:hazard=*`. `scuba_diving:difficulty` i `scuba_diving:type:*` surten al preset JOSM però queden fora de l'esquema actual. Els centres de busseig es marquen `amenity=dive_centre` + `sport=scuba_diving`, i les botigues d'equip `shop=scuba_diving` — [OSM Wiki Tag:sport=scuba_diving](https://wiki.openstreetmap.org/wiki/Tag:sport=scuba_diving)
- **Consulta Overpass real** (executada el 2026-10-24 a https://overpass.private.coffee/api/interpreter, perquè overpass-api.de va respondre primer "406" sense User-Agent i després "502 at capacity"): 106 elements en total. Recompte per tag, amb solapaments:
  - `sport=scuba_diving`: 53
  - `scuba_diving:divespot=yes`: 34
  - `amenity=dive_centre`: 34
  - `shop=scuba_diving`: 19
  - `seamark:type=wreck`: 8
  - `historic=wreck`: 2
  - `leisure=dive_site`: 0
  - claus `diving*`: 0

  Font: [Overpass API](https://overpass-api.de/api/interpreter)
- Claus d'atributs presents al resultat: `scuba_diving:entry` (32), `scuba_diving:maxdepth` (21), `scuba_diving:difficulty` (21), `scuba_diving:rental` (10), `scuba_diving:courses` (9), `seamark:wreck:category` (8), `depth` (4), `wreck:date_sunk` (3) — [Overpass API](https://overpass-api.de/api/interpreter)
- Distribució geogràfica dels punts, de la mateixa consulta:
  - **Illes Medes / l'Estartit (~18 nodes):** la Pedrosa, les Salines, Tasco Gros, Tasco Petit, Dolfi Nord, Dolfi Sud, la Vaca, el Medallot, el Salpatxot, la Pota del Llop, la Pedra de Déu, les Ferranelles, Carall Bernat, Cova de la Reina, el Reggio, el Rossinyol, la Ferriola, Negre del Falaguer. Cap no té `maxdepth`.
  - **Begur / Tamariu / Aiguablava / Sa Riera (~22 punts):** Badia de Tamariu (18 m), Aigua Xelida (25), Furió d'Aigua Xelida (38), Canons de Tamariu (40), Roca Montiell (25), Illa de Sa Gavina (28), Aiguablava (16), Illa Negra (25), Barda de l'Illa Negra (31), Barda de Pere el Flaquer (44), Cap de Begur (38), Barda de Fitor (54), S'Encalladora (29), Punta des Plom (40), Les Alzines (45), Cala de Cap sa Sal (31), sa Tuna (25), Cala d'Aiguafreda (24), Cala de sa Riera (12), Boia dels Ulls de Llop (20), Cala des Tramadiu (18), més el derelicte arqueològic Aiguablava V i VII (7 m). Gairebé tots porten `scuba_diving:maxdepth`.
  - **Cap de Creus:** només Massa d'Or (la Rata).
  - **Roses:** "L embarrancat".
  - **Palamós:** derelicte Boreas (`depth=18-32`, enfonsat el 1989).
  - **Tarragona/Salou:** derelicte Dragonera (14-24 m, 1994) amb 4 nodes `seamark:type=wreck` sense nom al voltant, Vapor del Miracle (16 m, 1990) i "mARdEhIELO".
  - **Barcelona:** dos elements són clubs o centres, no punts.

  Font: [Overpass API](https://overpass-api.de/api/interpreter)
- Llicència OSM: ODbL 1.0. Obliga a atribuir "© OpenStreetMap contributors" i aplica share-alike a les bases de dades derivades. Encaixa amb un projecte de dades ODbL; no es pot rellicenciar com a CC BY — [OSM Copyright](https://www.openstreetmap.org/copyright)

**Consulta Overpass a punt per usar:**
```
[out:json][timeout:120];
(
  nwr["scuba_diving:divespot"="yes"](40.5,0.15,42.45,3.35);
  nwr["sport"="scuba_diving"][!"amenity"][!"shop"](40.5,0.15,42.45,3.35);
  nwr["seamark:type"="wreck"](40.5,0.15,42.45,3.35);
  nwr["historic"="wreck"](40.5,0.15,42.45,3.35);
);
out tags center;
// centres: nwr["amenity"="dive_centre"](40.5,0.15,42.45,3.35); nwr["shop"="scuba_diving"](...);
```
Cal enviar un User-Agent. Si overpass-api.de està saturat, es pot fer servir un mirall (overpass.private.coffee, overpass.kumi.systems).

### Inferences
- OSM pot servir de llavor del dataset (uns 45 punts útils), però s'haurà de completar mapejant directament a OSM. Les fonts tancades (vegeu la secció de plataformes) només poden servir de referència manual, i els noms i posicions s'han de verificar sobre el terreny o amb fonts obertes.
- El `sport=scuba_diving` sense `divespot` inclou clubs i centres mal etiquetats. Cal filtrar per `amenity`/`shop`/`leisure=sports_centre`.
- Els seamarks d'OpenSeaMap són tags OSM normals (`seamark:*`) i ja entren a la mateixa consulta. No hi ha cap font OpenSeaMap separada.

### Gaps
- No s'ha consultat taginfo per obtenir recomptes globals. No s'ha mirat l'historial d'edicions per saber qui va mapejar Begur (el 2024, per l'ID del node), ni la seva font: convé verificar que no es va copiar d'una font tancada.

## Wikidata i Viquipèdia

### Takeaway
Wikidata no serveix: Q1145276 NO és "dive site" (és "fictional country"). Les classes correctes són **Q2141554** ("recreational dive site", 345 ítems al món) i **Q26205080** ("underwater diving site", 723 ítems al món). Dins del bbox català només hi ha **1 ítem**, el Pont del Petroli (Badalona).

### Cited Findings
- SPARQL executat a query.wikidata.org el 2026-10-24:
  - Q1145276 té l'etiqueta "fictional country".
  - La cerca d'entitats "dive site" retorna Q2141554 i Q26205080.
  - Recompte mundial de `P31/P279*`: 345 ítems per a Q2141554 i 723 per a Q26205080.
  - Filtrant per P17=Espanya, Q2141554 dona 0 ítems i Q26205080 només en dona un, el Q11942340 "Pont del Petroli" (Point 2.24739 41.4409, Badalona).
  - Una consulta `wikibase:box` sobre el bbox català, amb P31 directe, retorna 0 resultats.

  Font: [Wikidata Query Service](https://query.wikidata.org/)
- Les dades de Wikidata són CC0, però per a aquest projecte no aporten gairebé res — [Wikidata Query Service](https://query.wikidata.org/)

### Inferences
- Wikidata pot servir com a enllaç (`wikidata=*` a OSM) per a llocs famosos com les Medes o el Cap de Creus, no com a font de punts.

### Gaps
- No s'han revisat les llistes de la Viquipèdia (per exemple, l'article "Illes Medes"). Qualsevol llista que hi hagi seria CC BY-SA, que és incompatible amb ODbL per a una importació directa, i normalment no té coordenades.

## Plataformes col·laboratives (Divessi, Diveboard, Zentacle, Wannadive, divesites.com, ScubaEarth, Subsurface…)

### Takeaway
No s'ha trobat cap plataforma de punts d'immersió amb un bolcat obert o una llicència permissiva per als *punts*. L'única dada oberta és el dataset d'**observacions d'espècies** de Diveboard (CC0, a GBIF/OBIS), que no és un catàleg de punts. Totes les altres s'han de tractar com a **NO obertes: només referència manual, sense scraping ni redistribució**.

### Cited Findings
- **Wannadive.net:** el peu de pàgina diu "© Wannasurf.com ltd - All right reserved". Els continguts són "copyright of Wannadive.net and its licensors". No hi ha cap API, cap llicència CC ni cap exportació documentada. La pàgina mostra "11473 GPS waypoints" a escala mundial — [Wannadive](https://www.wannadive.net/); [Wannadive Copyright](https://www.wannadive.net/help/index.html?wdaction=lib.WDPageHelp.copyright). → NO obert.
- **Diveboard:** el dataset "Diveboard – Scuba diving citizen science observations" és CC0 a GBIF, EurOBIS i OBIS-SEAMAP. Són observacions d'espècies registrades per bussejadors, prop del 80 % peixos, no un catàleg de punts. ARDC hi mostra una etiqueta CC BY-NC contradictòria — [GBIF](https://gbif.org/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2); [EurOBIS ERDDAP](https://erddap.eurobis.org/erddap/info/diveboard/index.html); [ARDC](https://researchdata.edu.au/diveboard-scuba-diving-science-observations/3546014). Podria contenir coordenades d'immersions a Catalunya; no s'ha verificat.
- **Divessi (SSI):** té una base de dades de punts dins el MySSI app/web ("This data is provided from the logbook information in the MySSI app"), però no s'ha trobat cap API ni llicència oberta — [Divessi dive site](https://www.divessi.com/en/mydiveguide/divesite/96173). → NO obert.
- **Zentacle:** és una app de dive log i punts amb reviews. No s'ha trobat cap API pública ni cap llicència oberta — [Hive Index](https://thehiveindex.com/communities/zentacle/). → NO obert (no verificat).
- **divesites.com "Dive Sites API":** `http://api.divesites.com/` no ha respost (curl ha retornat el codi 000) el 2026-10-24. Sembla inactiva, i no s'ha trobat documentació de llicència — prova directa amb curl.
- **PADI ScubaEarth:** la pàgina de copyright de PADI limita els materials a ús personal no comercial. No s'han trobat els ToS concrets de ScubaEarth — [PADI copyright](https://www.padi.com/ja/copyright). → NO obert.
- **Subsurface:** el programari és lliure (GPLv2 segons LWN el 2012). Gestiona punts amb GPS dins el log de cada usuari, però no publica cap base de dades de punts — [Subsurface](https://subsurface-divelog.org/); [LWN](https://lwn.net/Articles/521092/). Submersion (GPL-3.0) exporta el log en UDDF o CSV, però només les dades de l'usuari — [ecosyste.ms](https://awesome.ecosyste.ms/projects/github.com%2Fsubmersion-app%2Fsubmersion).
- **API comercial:** Zylalabs ven una "World Scuba Diving Sites API" de pagament, sense llicència oberta — [Zylalabs](https://zylalabs.com/api-marketplace/top-search/diving).

### Inferences
- Per a un projecte MIT + ODbL, l'única via neta és OSM més dades públiques amb llicència compatible. Les plataformes només serveixen per contrastar manualment noms i profunditats, no per copiar coordenades.

### Gaps
- No s'han pogut llegir els ToS de Divessi, Zentacle, DiveAdvisor, Deeperblue, MacDive, Divelogs.de, Garmin/Diviac ni Shearwater Cloud. Tampoc s'ha comprovat dive-site.org. Cap no consta com a obert, però no s'ha confirmat per a cadascuna una clàusula explícita contra el scraping. Fins que no es verifiqui, cal considerar-les totes tancades.
- No s'ha comptat quants punts catalans té cada plataforma.

## Fonts oficials: parcs naturals, Generalitat dades obertes, turisme, municipis, FECDAS

### Takeaway
La Generalitat publica a Socrata el **Registre de centres d'immersió d'esbarjo de Catalunya** (151 centres, sense coordenades), sota la Llicència oberta d'ús d'informació – Catalunya, però no publica cap dataset obert de punts d'immersió. Les Medes es regulen per zones i boies amb quotes anuals, i el Cap de Creus pel PRUG. Tot està en PDF o normativa, sense GIS obert localitzat.

### Cited Findings
- Cerca al catàleg Socrata (api.eu.socrata.com, domini analisi.transparenciacatalunya.cat) de "busseig", "immersio", "buceo" i "submarinisme". Només surten tres datasets rellevants: `m5mm-yw6r` "Registre de centres d'immersió d'esbarjo de Catalunya", `9qmy-ujbd` "Centres nàutics" i `9fry-i62f` "Notícies sobre nàutica i busseig" — [m5mm-yw6r](https://analisi.transparenciacatalunya.cat/d/m5mm-yw6r); [9qmy-ujbd](https://analisi.transparenciacatalunya.cat/d/9qmy-ujbd)
- `m5mm-yw6r`:
  - Té 151 files i els camps `nom, adre_a, cp, municipi, comarca, prov_ncia, sortides, ensenyament, cif_nif`, sense lat/lon.
  - La llicència de les metadades és "See Terms of Use".
  - API: `https://analisi.transparenciacatalunya.cat/resource/m5mm-yw6r.json`, també en CSV.

  Font: [API views m5mm-yw6r](https://analisi.transparenciacatalunya.cat/api/views/m5mm-yw6r.json)
- **Llicència oberta d'ús d'informació – Catalunya:**
  - Permet reutilitzar, distribuir i fer obres derivades.
  - Obliga a no alterar el contingut, a citar la font (Generalitat i departament) i la data d'actualització.
  - No autoritza el subllicenciament ni permet imposar altres restriccions.
  - No es poden usar logos de la Generalitat.

  Font: [web.gencat.cat llicències](https://web.gencat.cat/ca/generalitat/dades-indicadors/dades-obertes/llicencies). La compatibilitat amb ODbL o CC BY no és explícita; vegeu les Inferences.
- **Medes:**
  - El PRUG (Decret 222/2008) es va modificar amb l'Ordre AAM/112/2015, que fixa un límit anual per boia.
  - La quota diària de 400 immersions es va substituir per una quota anual per zona: 77.012 a la proposta i 76.151 a l'aprovació. N'hi ha 15 zones de busseig.
  - El Medellot va quedar tancat com a zona de referència, i la Pedra de Déu té una quota de 5.687 immersions l'any.

  Fonts: [bibgirona 197037](https://bibgirona.cat/assets/documents/000/197/037/article.pdf); [bibgirona 196980](https://bibgirona.cat/assets/documents/000/196/980/article.pdf). Són notícies de premsa sense data clara, i cal verificar-les al DOGC. Les autoritzacions de centres se sol·liciten cada dos anys, de l'1 al 30 de novembre — [govern.cat 2018](https://govern.cat/govern/docs/2018/10/26/18/03/b3e8dc1c-47ae-4d42-a572-8d98df8f70fb.pdf)
- **Cap de Creus:** el PRUG regula la immersió i fixa màxims d'embarcacions, escafandristes i immersions a les reserves naturals parcials (Cap Gros–Cap de Creus i Cap Norfeu) i a la reserva integral (Encalladora). També limita el nombre d'empreses de busseig — [Document de bases PRUG](https://participa.gencat.cat/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdXdJIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--d63aec487f68914cac49924d8e3495654ae3da71/Document_de_bases_PRUG_Cap_de_Creus_20201223_def.pdf); [NacióDigital](https://naciodigital.cat/impacte/terra/installen-cameres-amb-ia-al-cap-de-creus-per-vigilar-que-no-es-facin-festes-en-vaixells.html)
- Un estudi RAC/SPA sobre l'ús del fons per part dels bussejadors a les Medes cita 450 bussejadors al dia i immersions des de 10 punts, i diu que es van georeferenciar elements del paisatge. Les dades no són publicades — [RAC/SPA](https://rac-spa.org/node/424)

### Inferences
- Les dades de la Generalitat es poden incloure en un projecte derivat amb l'atribució exigida. Com que la llicència prohibeix el subllicenciament, val més distribuir-les com a capa separada amb la seva llicència original que fusionar-les dins la base ODbL.
- La base legal de les Medes (zones i boies amb nom, les dels annexos del PRUG) és normativa pública. Els noms de zona es poden usar com a referència, i les coordenades s'han de mapejar a OSM.

### Gaps
- La pàgina de busseig de parcsnaturals.gencat.cat (URL provada) dona 404. No s'han trobat capes GIS de boies o zones de busseig de les Medes ni del Cap de Creus a l'IDEC/ICGC; cal buscar-les al geoportal de l'ICGC i als annexos del PRUG publicats al DOGC.
- No s'han trobat mapes oberts de punts del Patronat de Turisme Costa Brava Girona, de l'ACT, de la Diputació, dels municipis (Tossa, l'Escala, Palamós, Begur, Llançà) ni de la FECDAS. Probablement són PDF amb copyright: només per a referència manual.

## Dades acadèmiques i d'ONG (Zenodo, PANGAEA, CSIC Digital)

### Takeaway
No s'ha trobat cap dataset obert amb coordenades de punts d'immersió de les Medes o del Cap de Creus. Hi ha estudis sobre la freqüentació dels bussejadors, però sense dades publicades.

### Cited Findings
- L'API de Zenodo, consultada amb "Cap de Creus diving", "Medes divers" i "Medes buceo", no retorna cap registre rellevant. N'apareix un de densitats d'eriçons i biomassa de peixos al voltant d'una AMP (zenodo 22829909), que no s'ha verificat si és de les Medes ni si inclou punts — [Zenodo records API](https://zenodo.org/api/records?q=Medes%20divers); [Zenodo 22829909](https://zenodo.org/records/22829909)
- Sala, Garrabou i Zabala (1996, Marine Biology) estudien els briozous a llocs freqüentats i no freqüentats pels bussejadors a les Medes. És un article, no un dataset obert — [marineinfo](https://marineinfo.org/id/publication/240533)
- DiverReef (Zenodo) és un dataset global de 176 punts, però no inclou la Mediterrània catalana — [Bangor](https://research.bangor.ac.uk/cy/publications/diverreef-a-global-database-of-the-behavior-of-recreational-diver/)
- Seguiment de les Medes 2008 (UB) i cartografia bionòmica del Montgrí: són PDF de l'UB, que poden contenir mapes de zones, amb llicència no verificada — [diposit.ub.edu Seguiment Medes 2008](https://diposit.ub.edu/dspace/bitstream/2445/23686/1/Seguiment%20Medes%202008.pdf); [Cartografia bionòmica Montgrí](https://diposit.ub.edu/dspace/bitstream/2445/22563/1/Cartografia%20bionomica%20del%20litoral%20submergit%20de%20la%20costa%20del%20Montgr%c3%ad.pdf)

### Inferences
- Les dades acadèmiques serveixen de context, no de catàleg de punts. Es podrien demanar als autors, per exemple a l'equip ICM-CSIC de Garrabou.

### Gaps
- No s'han cercat PANGAEA ni Digital.CSIC directament. Tampoc s'ha revisat GBIF/OBIS per extreure les coordenades de les observacions de Diveboard a Catalunya, que podrien aproximar punts reals amb llicència CC0.
