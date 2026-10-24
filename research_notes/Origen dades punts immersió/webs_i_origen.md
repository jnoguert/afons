# Webs i apps que publiquen punts d'immersió de la costa catalana, i d'on diuen que treuen les dades (estat a 2026-10-24)

Abast: només la costa catalana. Cada lloc s'ha consultat a mà, amb poques pàgines per lloc. Les úniques consultes per API han estat petites i filtrades (OpenDiveMap amb `country=ES`, un Overpass sobre la bbox catalana i unes 30 lectures de changesets a l'API d'OSM). No s'ha fet cap scraping massiu. La Wayback Machine (web.archive.org) està bloquejada per a l'eina de fetch, de manera que no s'ha pogut reconstruir l'historial de llançament de cap web (vegeu els Gaps).

## 1. Plataformes internacionals: quants punts catalans tenen, quins camps publiquen, d'on diuen que surten les dades, llicència i API

### Takeaway
Totes les plataformes grans es basen en l'aportació d'usuaris: bussejadors (Wannadive, Deepblu, Zentacle, Diveboard, divebuddy), el logbook dels usuaris de l'app (SSI/Scubago, i la base que comparteix Mares) o els centres membres (PADI). Cap no publica els punts sota llicència oberta ni amb API pública. L'excepció és un grup de bases "obertes" noves (2025-2026). Algunes d'aquestes **copien dades d'altres**: OpenDiveMap porta les fitxes d'SSI amb `source: ssi`, i OpenWaterAtlas i dive-vibe-community parteixen d'OSM.

### Cited Findings

**Wannadive.net (Wannasurf.com ltd)**
- Té **97 punts a "Catalonia" repartits en 16 subzones**. L'enllaç de Catalunya és `/spot/Europe/Spain/Costa_Brava/`. La suma de les subzones dona 94: Estartit & Medes 21, Palamós–Cap de Begur 18, Roses 9, Cadaqués 8, l'Escala 8, Port de la Selva 6, Tarragona 5, l'Ametlla de Mar 4, Lloret 3, Vilanova & Sitges 3, Mataró 2, Tossa 2, Sant Feliu 2, Barcelona 1, Colera 1 i Malgrat 1 — [Wannadive Spain](https://www.wannadive.net/spot/Europe/Spain/index.html); [Wannadive Catalonia](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/index.html)
- Camps d'una fitxa (La Vaca, l'Estartit): coordenades "42° 2.852' N; 3° 13.554' E", datum "WGS84", precisió "Exact", noms alternatius, profunditat mitjana de 22 m i màxima de 45 m, corrent, visibilitat, nivell "CMAS ** / AOW", tipus, perills, accés i text lliure. La fitxa porta "Author: Chris" i "Contributors (1)", sense data de creació — [Wannadive La Vaca](https://www.wannadive.net/spot/Europe/Spain/Costa_Brava/Estartit/La_Vaca/index.html)
- Origen declarat: "A dive site atlas made by divers for divers", "Enjoy and contribute!", "New dive sites are being continuously added as they are submitted from divers around the world" i "we will bring areas on-line as data are submitted by divers". Hi ha rols d'"atlas editor, a translator or a forum moderator". No es descriu cap procés de validació. Total mundial: 11.675 punts i 18.569 membres — [Wannadive Help](https://www.wannadive.net/help/)
- Copyright: "copyright of Wannadive.net and its licensors". El lloc "posts data submitted by users, sometimes anonymously" i diu que "we do and will remove any postings which can be proven to have been posted without permission". No hi ha cap llicència oberta — [Wannadive Copyright](https://www.wannadive.net/help/index.html?wdaction=lib.WDPageHelp.copyright)
- Exportació: "You are free to use Wannadive.net KML/GPS data files ONLY for your personal use". No hi ha API. Peu de pàgina: "© Wannasurf.com ltd - All right reserved" — [Wannadive Spain](https://www.wannadive.net/spot/Europe/Spain/index.html)

**SSI: divessi.com / MyDiveGuide / Scubago (i l'app de Mares)**
- `divessi.com/mydiveguide/...` redirigeix (301) a `scubago.com/en/explore/...`. La pàgina de destinació Catalunya (`catalonia-9751398`) conté **239 enllaços únics a fitxes de punt**. Hi ha un bloc de "Trending Dive Sites" global (Koh Tao, etc.), així que el nombre de punts catalans és una mica inferior. És un recompte d'enllaços d'una sola pàgina, no una xifra publicada — [Scubago Catalonia](https://www.scubago.com/en/explore/destination/catalonia-9751398)
- Camps d'una fitxa (Tascó Petit): `GeoCoordinates` 42.0411, 3.2267 (schema.org), descripció, "Max Depth", "Visibility", "Average Dive Time", "Logged Dives", valoració i centres SSI — [Scubago Tascó Petit](https://www.scubago.com/en/explore/divesite/tasc-petit-89309)
- Origen declarat: "This data is provided from the logbook information in the MySSI app" (és el títol de la fitxa a divessi.com) — [divessi Tascó Petit](https://www.divessi.com/en/mydiveguide/divesite/tasco-petit-spain-89309). Els busseigs registrats i verificats "contribute to populating SSI's dive site data in Scubago". L'app parla de "thousands of verified dive sites" — [SSI blog: updated MySSI app](https://www.divessi.com/en/blog/updated-myssi-app-8863.html)
- Edició per l'usuari: "The user can then enter a new dive site description or modify the existing one". Les imatges es pugen "with assignment of all image rights" i "the rights to SSI must be assigned" — [SSI blog: Wildlife Logbook](https://www.divessi.com/en/blog/wildlife-logbook-1020)
- Mares comparteix la base d'SSI. L'app de Mares (2022) diu: "We collaborated with our sister company SSI and our global customer base", "creating the largest dive-site database in the world" — [Divenewswire, 21-08-2022](https://www.divenewswire.com/?p=29718)
- No hi ha cap llicència oberta ni API pública. Els termes d'SSI/PADI s'analitzen a `Fonts obertes punts immersió/padi_ssi_termes_legals.md`.

**PADI (padi.com/dive-sites, travel.padi.com)**
- Espanya: "506 dive sites" (238 wall, 182 reef, 76 cave). No hi ha cap pàgina regional de Catalunya: les URL `/catalonia/`, `/costa-brava/` i `/girona/` donen 404 — [PADI dive sites Spain](https://www.padi.com/dive-sites/spain/). La pàgina d'Estartit i les Medes llista 16 punts (11 de paret, 3 d'escull i 2 de cova) — [PADI IT Estartit e isole Medes](https://www.padi.com/it/dive-sites/spagna/estartit-e-isole-medes/) (xifra del fragment de cerca)
- Origen declarat: "Dive Guides content at the destination and dive-site level is provided by PADI Members" mitjançant "an easy and intuitive online portal". El personal de PADI escriu les visions generals per continent, país i regió. "PADI Members who create and edit destination guides and dive sites are listed as contributors on these pages" — [PADI Pros blog, 13-01-2021](https://pros-blog.padi.com/padi-dive-guides-inform-inspire-acquire/). Els membres hi accedeixen des de "PADI Dive Guide & Dive Site Editor". No es descriu cap revisió per part de PADI — [PADI Pros blog, 07-07-2021](https://pros-blog.padi.com/2021/07/07/dive-guides-make-your-dive-destination-the-real-mvp/)
- La pàgina de l'Estartit diu "This page wouldn't be possible without contributions from the following PADI members:" i cita Costa Brava Divers i Unisub Estartit. Avís legal: "the information displayed has been provided by one or multiple third parties" — [PADI Travel L'Estartit](https://travel.padi.com/diving-in/spain/l-estartit/). Els usuaris poden "cast your vote if you know the site" — [PADI dive sites Spain](https://www.padi.com/dive-sites/spain/)

**Zentacle**
- "Full dive log with 15k+ locations, reviews, and photos". El peu enllaça "Add a new location", "Suggest an edit" i ShoreDiving.com. No hi ha cap pàgina de termes ni d'API visible — [Zentacle](https://www.zentacle.com/)
- El formulari d'alta comença amb "Search on Google Maps", i si no troba res, "Nothing found! Please enter the rest of the info below". Camps: nom, ciutat, dificultat, "Max Depth" i descripció ("Any extra info/links you're aware of about the dive site"). Moderació: "New dive spots you add will credit you as the discoverer once approved" — [Zentacle add spot](https://www.zentacle.com/add/spot)

**Deepblu**
- "If your dive spot does not exist on our Dive Site Map, you can add it to our database" — [Deepblu FAQ](https://support.deepblu.com/if-my-dive-spot-isnt-there-how-do-i-add-it/). Una pàgina d'ajuda parla de "over 20,000 dive spots", i el 2017 Planet Deepblu hi va posar "virtually all popular global dive locations" — [Deepblu Academy](https://academy.deepblu.com/adding-dive-spots-on-web-lets-break-it-down-real-easy/); [DivePhotoGuide](https://www.divephotoguide.com/underwater-photography-scuba-ocean-news/planet-deepblu-dive-trip-planning-tool-launched/)

**Diveboard (no ha tancat)**
- Els punts els creen els usuaris quan registren una immersió: poden "create a new 'locality or dive site', by naming it and placing a pin on the map". El paper de dades parla de "2500 different localities in 106 different countries" i diu que les dades són "dedicated to the public domain under a Creative Commons Zero waiver" — [Datafable paper.md](https://github.com/Datafable/diveboard-data-publication/blob/master/paper.md). GBIF mostra en canvi CC BY-NC 4.0, una contradicció — [GBIF dataset](https://www.gbif.org/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2)
- El servei continua: "the company turned into a non-profit with a focus on citizen-science" (2021). Hi ha una "full rewrite" i una plataforma de prova des de l'abril del 2023. Cap avís de tancament — [Diveboard community](https://www.diveboard.com/community)

**divesites.com i la "Divesites API"**
- El 2026-10-24 `https://www.divesites.com/` dona "ECONNREFUSED" i `api.divesites.com` no respon. Sembla inactiva — prova directa amb WebFetch i curl.
- Descripció d'agregador: "Returns database information for scuba divers including location, weather" (latitud i longitud, mapa, estacions de marea). Calia una API key, i no hi ha cap llicència indicada — [PublicAPIs](https://publicapis.io/divesites-sports-api). La fitxa de ProgrammableWeb ja no és accessible (ECONNRESET) — [ProgrammableWeb](https://www.programmableweb.com/api/divesites-rest-api)
- Qualitat (2012): de divesites.com un usuari diu que la majoria de punts tenien "the coordinates for the nearest city on the island" — [ScubaBoard "Source for dive site coordinates?"](https://scubaboard.com/community/goto/post?id=6407065)

**divezone.net, Deeperblue, divebuddy, DiveAdvisor, divelogs.de**
- divezone.net té articles editorials per país. El d'Espanya és del 2018-09-01 i diu "Listing a few great dive sites would not do justice…". Mostra "No dive sites reviews found". No té una base de punts catalans — [divezone Spain](http://divezone.net/diving/spain)
- A Deeperblue no s'ha trobat cap directori de punts; només hi ha fils de fòrum — [Deeperblue forum](https://forums.deeperblue.com/threads/dive-spots-or-courses-in-spain.52187/latest)
- divebuddy.com: punts "community-maintained", "© 2026 Dive Buddy LLC. All rights reserved" — [divebuddy Spain](https://www.divebuddy.com/divesites/Spain/)
- DiveAdvisor: el 2026-10-24 l'arrel retorna 404 i té un certificat TLS incomplet. Es fa servir com a font de validació a dive-vibe (vegeu més avall) — prova directa amb curl.
- divelogs.de oferia el 2014 un fitxer KML amb "over 4K sites" (25 MB) — [ScubaBoard KMZ thread](https://scubaboard.com/community/threads/free-dive-sites-kmz-files-for-google-earth.443522/)

**Programari de log i fabricants**
- Subsurface: no té cap catàleg compartit. Un catàleg compartit "have also been discussed previously" — [Subsurface Google Group](https://groups.google.com/g/subsurface-divelog/c/6ODmKXoAa9w). Scuba-sites.com (2020) accepta la importació dels punts exportats des de Subsurface: "you can export all dive sites and then import them into this website" — [ScubaBoard](https://scubaboard.com/community/threads/dive-site-listing-for-subsurface.601683/)
- MacDive: no té cap base central. Es comparteixen "Critters and Dive Sites with any buddies… within local WiFi or Bluetooth range", i hi ha una petició oberta de base compartida — [MacDive iOS](https://mac-dive.com/ios.php); [MacDive forum RFF](https://mac-dive.com/forum/viewtopic.php?p=13644)
- Garmin: l'app Garmin Dive permet "view the location details and photos shared by other users" — [Garmin manual](https://www8.garmin.com/manuals/webhelp/GUID-2A58ED2A-14A3-4161-ADB5-259E1781AF1B/EN-US/GUID-317F0E90-9031-46E3-83B6-2658B3AE3DA9.html). Un usuari diu "There's no way to add dive sites in the app" i un altre que "The location of some dive sites at the map are not accurate" — [Garmin forum](https://forums.garmin.com/apps-software/mobile-apps-web/f/garmin-dive-android/425907/dive-sites). Els mapes DiveView inclouen "more than 4,000 dive sites" i "DiveView covers the United States, Europe, and northern Africa", sense proveïdor indicat — [ScubaBoard Mk3i maps](https://scubaboard.com/community/threads/garmin-mk3i-maps.641545/)
- Suunto: no s'ha trobat cap base de punts. Un usuari escriu el nom a mà al mapa ("i only add the dive site name in the map, click on the pencil and add name") i un altre demana "pull dive sites from PADI, SSI, or DAN" — [Suunto forum](https://forum.suunto.com/topic/15070/dive-spots). Els mapes offline "are compiled using the community generated ©OpenStreetMap (OSM) database" — [Suunto offline maps](https://www.suunto.com/Support/disclaimers/offline-maps/). Una ressenya esmenta una "dive site database" per a la reproducció 3D de la Nautic, sense dir-ne la font — [DIVEIN](https://www.divein.com/review/suunto-nautic/)
- Shearwater: no s'ha trobat cap base de punts a Shearwater Cloud. L'app "Dive Shearwater" fa mapes personals ("build your own personal guide") — [App Store Dive Shearwater](https://apps.apple.com/us/app/dive-shearwater/id6751863035)

**Wikiloc**
- L'activitat "Submarinisme" té "9.790 rutes" al món. Les catalanes que surten a la portada són sobretot d'esnòrquel des de costa: l'Ametlla de Mar, Cadaqués (Perefet), Tossa (Cala Futadera) — [Wikiloc rutes submarinisme](https://ca.wikiloc.com/rutes/submarinisme)
- Llicència: contingut "Proprietary" — [Wikipedia Wikiloc](https://en.wikipedia.org/wiki/Wikiloc). Una font secundària cita l'ús "personal and non-commercial" (ToS §1.6). La pàgina de termes oficial ha donat 403 — [Wikiloc terms](https://www.wikiloc.com/wikiloc/terms_en.html)

**Bases "obertes" noves (2025-2026) i agregadors menors**
- **OpenDiveMap**: "3,123" punts, ODbL, "community-driven". API a `https://api.opendivemap.com/v1/sites` (GeoJSON) — [OpenDiveMap](https://opendivemap.com/); [Docs](https://opendivemap.com/docs). La consulta real (2026-10-24) mostra que 499 de 500 registres porten `tags.source = "ssi"`, `ssi_id`, `ssi_url` (divessi.com), la descripció i els camps `logged_dives`, `average_rating` i `average_vis_m` d'SSI. Amb `country=ES` hi ha 6 punts, tots de Canàries més un "test", i **0 punts catalans** — [API OpenDiveMap](https://api.opendivemap.com/v1/sites?country=ES&limit=500)
- **dive-vibe-community / DiveVibe.io** (2026-03): "2,800+ dive sites", ODbL, "vibe coded". Dos scrapers d'Overpass sobre OSM. Després, agents d'IA validen cada punt contra "ScubaBoard threads, dive operator descriptions, wreck databases, and the DiveAdvisor and Wannadive databases". Un usuari l'acusa d'haver "mangled / scraped / stolen from DiverNet" a Scapa Flow — [ScubaBoard](https://scubaboard.com/community/threads/i-open-sourced-a-database-of-2-800-dive-sites-across-122-destinations-free-for-everyone.667171/); [GitHub](https://github.com/jbunderwater/dive-vibe-community). El `destinations.json` no conté Espanya.
- **OpenWaterAtlas**: "2,928 dive, kite, surf and freedive spots", **CC-BY 4.0**, amb "spot locations imported from OSM · ODbL 1.0" — [OpenWaterAtlas datasets](https://openwateratlas.com/en/datasets/)
- **divelog-sites** (Bakhuis): ODbL / CC BY-SA. "Initial content was imported from the maintainer's personal log" — [GitHub](https://github.com/dennisbakhuis/divelog-sites)
- **Divers Atlas** (ONG): segons el perfil de la ONG, 6.316 punts — [GuideStar](https://www.guidestar.org/Profile/33-2061219). **OpenDiveSites.org** cobreix només Califòrnia i Zelanda, CC BY-NC-SA — [OpenDiveSites](https://opendivesites.org/)
- **DivePlanner Pro** (Carbon Intelligence SASU, París): "23 sitios de buceo" a la Costa Brava, amb profunditat, nivell i espècies. No diu d'on surten les dades. Usa noms com "Negre del Falaguer", "Arcs del Duï" i "Illes Medes - El Dolç" — [DivePlanner Pro Costa Brava](https://diveplannerpro.com/es/spots/es/costa-brava); [About](https://diveplannerpro.com/es/about)
- **duikersgids.nl** (neerlandès): fitxa de Carall Bernat amb profunditat de 6–50 m i sense coordenades. Està mal classificada com "Spanje, Cantabria". Per reutilitzar fitxes cal demanar una "key" — [Duikersgids Carall Bernat](https://www.duikersgids.nl/en/dive-spots/carall-bernat)
- **Meteo Consult Marine** té pàgines meteo per punt d'immersió amb coordenades, per exemple el Boreas a "Lon : 3°7',701 E Lat : 41°49',626 N" (dada del fragment de cerca; la pàgina va donar 403) — [Meteo Consult Boreas](https://marine.meteoconsult.fr/meteo-marine/meteo-spots-de-plongee/bassin-par-defaut/previsions-meteo-el-boreas-wreck-5434-6.php)

### Inferences
- Els "grans" (SSI/Mares, PADI, Wannadive) **no van importar cap base massiva coneguda**, si més no cap que declarin. SSI s'alimenta dels logs i dels centres, PADI dels centres membres i Wannadive dels usuaris. Les descripcions de PADI i SSI per a Catalunya són molt probablement obra dels centres locals: la pàgina de PADI de l'Estartit ho diu explícitament, i a SSI les fitxes de Mataró parlen de l'"Special Protected Area of Mataró" amb to de centre local.
- OpenDiveMap és, de fet, **un bolcat de MyDiveGuide/SSI rellicenciat com a ODbL**. Ho mostren els camps `source: ssi` i `ssi_url` i el text copiat. Els termes d'SSI no ho permeten (vegeu la nota legal germana), de manera que no es pot considerar una font oberta neta.
- OpenWaterAtlas publica com a CC BY 4.0 punts importats d'OSM (ODbL). Si la base derivada és substancial, això és incompatible amb el share-alike de l'ODbL.
- Zentacle comença cada alta amb una cerca a Google Maps. Per tant, les ubicacions de Zentacle poden derivar de llocs de Google, amb les restriccions dels termes de Google.

### Gaps
- No s'han pogut fer recomptes catalans per a Zentacle, divebuddy, Deepblu, Garmin Dive ni Divers Atlas sense navegar massivament.
- Història de divesites.com: no s'ha trobat qui la gestionava, des de quan ni quines apps usaven l'API. ProgrammableWeb i la Wayback Machine no han estat accessibles.
- No s'ha trobat qui subministra els "4,000 dive sites" de Garmin DiveView.
- Scubapro (LogTRAK) i divelogs.de: no hi ha documentació de primera mà sobre l'origen dels punts.
- Els termes de Google Maps Platform (clàusula "No Scraping") no s'han pogut citar textualment perquè la pàgina va sortir truncada.
- Els termes de Wikiloc han donat 403. Només es disposa d'una cita secundària.

## 2. Webs espanyoles i catalanes (portals, turisme, associacions, ajuntaments, FECDAS): qui va escriure les llistes

### Takeaway
Les llistes catalanes en castellà o català són de centres d'immersió, de la seva associació o de particulars. Cap no publica coordenades ni diu de quina font surt la llista. Els organismes públics (Patronat de Turisme Costa Brava, ajuntaments, FECDAS) no publiquen cap catàleg de punts que s'hagi pogut trobar.

### Cited Findings
- **Associació de centres d'immersió de la Costa Brava** (submarinismocostabrava.com / subcostabrava.com, Vall-llobrega). Peu: "© 2026 Asociación de centros de inmersión de la costa brava". Classifica per tipus (principiant, avançat, pecio…) i cita el Marmoler, el Boreas, el Reggio Messina, el Tregastel, el Furió Fitó, les Formigues i els Ullastres, sense coordenades ni profunditats per punt. Hi surten els logos de la Generalitat, la Diputació de Girona i Costa Brava Pirineus, però no se'ls atribueixen les dades — [Submarinismo Costa Brava](https://www.submarinismocostabrava.com/en/recommended-dives). Té pàgines per zona (Llançà, Cap de Creus…) — [Diving Llançà](https://www.submarinismocostabrava.com/en/scuba-diving-costa-brava/diving-llanca/). El seu president és Genís Dalmau — [Bibgirona](https://bibgirona.cat/assets/documents/000/197/037/article.pdf)
- **sóc Balena** (busseig.abellot.net, que ara és web-busseig.pages.dev): 109 entrades (108 noms únics) de Blanes a Portbou. Blanes 13, Lloret 12, Tossa 10, l'Estartit 22 (6 a la Meda Gran i 16 a la Meda Petita), Cadaqués–Port Lligat 11, l'Escala 9, Roses 8, Begur 7… Només dona nom i dificultat (asteriscs), sense coordenades. Es defineix com un "arxiu recopilatori" i no en cita cap font. "© 2026 sóc Balena · Powered by Hugo & PaperMod" — [sóc Balena](https://web-busseig.pages.dev/page/puntsimmersio/)
- **Patronat de Turisme Costa Brava Girona**: no llista punts. Diu "35 diving centres based along the coast from Blanes to Portbou" i "© 2026 Patronat de Turisme Costa Brava Girona" — [costabrava.org scuba diving](https://costabrava.org/en/what-to-do/active-tourism/scuba-diving/)
- **Premsa local**: el blog "L'Empordà sota l'aigua" de Surtdecasa el signa Bernadette Grassi, instructora des del 1998 i titular del centre Grassi-sub de l'Escala. Per exemple, "Ruta submarina La Xinxa" dona profunditats ("uns 8-9 m", "uns 20 m") sense coordenades. El mitjà avisa que "no es fa responsable de la redacció i contingut d'aquest post" — [Surtdecasa La Xinxa](https://surtdecasa.cat/emporda/blogs/l-emporda-sota-l-aigua/ruta-submarina-la-xinxa)
- **disfrutadelbuceo** (Google Sites, "Mapa inmersiones – Costa Brava", per zones: Tossa, Calella, Medes, Montgrí): redirigeix al login de Google i no s'ha pogut llegir — [disfrutadelbuceo](https://sites.google.com/site/disfrutadelbuceo/inmersiones)
- **Generalitat (Cap de Creus)**: hi ha un PDF "Itineraris d'immersió lleugera PN de Cap de Creus" (2023), d'itineraris d'immersió lleugera o esnòrquel. Ha donat 403 i se'n coneix només el fragment de cerca — [govern.cat PDF](https://govern.cat/govern/docs/2023/06/19/13/31/7fa90412-a0ac-46fa-b572-15c3cd8bcde9.PDF)
- **Medes**: la regulació per boies amb nom es troba a la normativa. Per exemple, "Es canvia la ubicació de la boia I6 (cova de l'infern)…" — [govern.cat 2015](https://govern.cat/govern/docs/2015/04/28/18/32/e50ff3e4-b0ff-41ff-96f6-bad6a47d130b.pdf). La normativa de boies es tracta a la nota germana `punts_immersio_cataleg.md`.

### Inferences
- Els textos descriptius de la Costa Brava que circulen per la xarxa els escriuen sobretot professionals locals: centres, l'associació, instructors que escriuen a la premsa local. Aquests són els autors originals probables de moltes descripcions que després apareixen a PADI i SSI.

### Gaps
- No s'han trobat pàgines de "buceoenlacostabrava", "ojo submarino", buceo.com, submarinismo.com ni "visitestartit" amb llistes de punts. O no existeixen amb aquests noms o el cercador no les indexa.
- No s'ha trobat cap mapa municipal de punts d'immersió (l'Escala, Begur, Tossa, Palamós, Llançà) ni cap publicació de la FECDAS amb punts.
- No s'ha pogut obrir l'avís legal ni els termes de submarinismocostabrava.com.

## 3. Centres d'immersió: publiquen mapes de punts amb coordenades?

### Takeaway
Els centres consultats publiquen nom, descripció i a vegades profunditat, però **no coordenades**. Les guarden com a coneixement operatiu. L'única web d'entitat local consultada que dona coordenades és el club SASBA de Badalona.

### Cited Findings
- **Gidive Center Palamós**: 17 punts (els Ullastres, el Boreas, les Formigues, la Llosa de Palamós, Gorgònies, Tabal, Canons de Tamariu, Furió Fitó…). Té descripció curta i imatge, però ni coordenades ni mapa. "©2026 Gidive Center Palamós" — [Gidive Punts de busseig](https://www.gidive.com/ca/Punts-de-busseig)
- **Blanes-Sub** classifica els punts per profunditat i per accés (barca o platja): els Bolets, la Seca, els 3 Arcs (fragment de cerca) — [Blanes-Sub](https://blanessub.com/)
- **Marina Diving (l'Ametlla de Mar)**: "disposem de 3 punts d'immersio amb blocs formigo dels Biotops a 25 metres", sense coordenades (fragment de cerca) — [Marina Diving](https://marinadiving.cat/immersio-biotopos)
- **SASBA Badalona** ("Club de busseig SASBA Badalona des de 1973"): mapa de "607" punts arreu del món. Per exemple, Illa Sa Palma (Tossa) és a 41.7196902, 2.9397064, amb 30 m, nivell, mapa 3D i espècies. No hi ha cap llicència. "© 2026 Copyright: SASBA Badalona" — [SASBA Illa Sa Palma](https://www.sasbabadalona.com/ca/diving_spot/illa-sa-palma)
- **Begur Dive** anuncia "un total de 16 immersions" (via Femturisme) — [Femturisme Begur Dive](https://femturisme.cat/establiments/begur-dive)
- A les Medes, un centre diu tenir "alrededor de 20 puntos de inmersión diferentes, algunos no visitados por el resto de centros" (fragment de cerca) — [PADI IT Estartit](https://www.padi.com/it/dive-sites/spagna/estartit-e-isole-medes/)

### Inferences
- Les coordenades públiques de punts catalans surten sobretot de Wannadive (posades per usuaris), de Scubago/SSI (logs), d'OSM i de clubs com SASBA. Els centres, que són els que millor coneixen el terreny, no les publiquen.

### Gaps
- No s'han revisat un per un els webs dels centres de l'Estartit, Tossa, Begur, Roses i Cadaqués, perquè el pressupost era de poques pàgines per lloc. Pot ser que algun publiqui KML o coordenades.

## 4. Guies impreses: fonts upstream probables

### Takeaway
La font impresa de referència per a la costa catalana és la sèrie d'**Andreu Llamas** (biòleg), amb **Pepi Cáceres** com a coautora i il·lustradora. La van publicar Planeta i després l'editorial pròpia Anthias, entre el 1997 i el 2010, amb mapes i rutes dibuixats a mà. Cap web consultada no la cita, però **sí que la cita un changeset d'OSM** com a font dels punts de Begur. No s'ha trobat cap "Guia de busseig de la Costa Brava" ni cap "Immersions a la Costa Brava" de Josep Maria Dacosta.

### Cited Findings
- **"Guía submarina de la Costa Brava"**, Andreu Llamas. Editorial Planeta, 1997, tapa dura, ISBN 9788408020615. La fitxa cita Caroline Phipps i els il·lustradors Lluís Rizo Rey i Pepi Cáceres Hernández — [IberLibro](https://www.iberlibro.com/9788408020615/Guia-submarina-costa-brava-Llaunas-8408020617/plp); [AbeBooks 1997](https://www.abebooks.com/Gu%C3%ADa-Submarina-Costa-Brava-Andreu-Llamas/32218230569/bd)
- Edició posterior: "Guía submarina de la Costa Brava. Las 200 mejores inmersiones, a fondo", ISBN 978-84-08-03887-0, 288 p., 2001 — [Agapea](https://www.agapea.com/libros/GUIA-SUBMARINA-DE-LA-COSTA-BRAVA-9788408038870-i.htm); [Librería Iguazu](https://www.libreriaiguazu.com/libro/guia-submarina-de-la-costa-brava_4964)
- **"Guías submarinas: Barcelona y Tarragona: las mejores inmersiones"**, Andreu Llamas, amb Pepi Cáceres Hernández i Lluís Rizo Rey. Anthias, Barcelona, 2003, 191 p., ISBN 84-933167-0-9 — [Biblioteca Museu Marítim](https://biblioteca.mmb.cat/bib/3483). NacióDigital la data el 2000, en contradicció amb el catàleg — [NacióDigital 2010](https://naciodigital.cat/girona/societat-girona/neix-una-guia-per-a-submarinistes-que-treu-a-la-llum-amb-fotografies-inedites-el-fons-mari-de-les-illes-medes.html)
- **"Guia Submarina de les Illes Medes i la Costa del Montgrí"**, Andreu Llamas i Pepi Cáceres. Editorial Anthias, 2010, 27 €, venuda primer "als centres d'immersió". El mètode és "molt artesanal": totes les fotos són seves i els mapes els dissenyen ells, amb "fotografies preses al fons del mar i dibuixos cartogràfics" recollits des del 2004. Hi havia en preparació les guies de Begur–Sant Feliu i de la Selva (Blanes, Lloret, Tossa), i se'n preveia una del Cap de Creus — [NacióDigital 2010](https://naciodigital.cat/girona/societat-girona/neix-una-guia-per-a-submarinistes-que-treu-a-la-llum-amb-fotografies-inedites-el-fons-mari-de-les-illes-medes.html); [Catalan News](https://www.catalannews.com/life-style/item/new-guidebook-maps-out-the-bottom-of-the-illes-medes-seafloor)
- **"Guía submarina Costa Brava: De Sant Feliu de Guíxols a Begur"**, Andreu Llamas, 210 p., cartoné, codi 9788493316785, 29 €. Inclou "precisas ilustraciones tridimensionales de las rutas submarinas" i una "descripción detallada de cada punto de inmersión" — [Librería Náutica](https://www.librerianautica.com/producto/guia-submarina-costa-brava/)
- La "Guía submarina de las Islas Baleares" (Planeta, col·lecció geoPlaneta) recull "300 inmersiones en 282 itinerarios", com a referència del mètode de la sèrie — [Periódico de Ibiza 2000](https://www.periodicodeibiza.es/noticias/cultura/2000/08/12/898351/los-fascinantes-paisajes-submarinos-de-balears-reunidos-en-un-solo-volumen.html)
- **Kirschner & Bergbauer**, "Guía del submarinista: España, Baleares y costa mediterránea", Omega, 2008, ISBN 9788428215152, 222 p. Inclou Cap de Creus, Calella de Palafrugell i Tamariu — [Google Books](https://books.google.com/books/about/Gu%C3%ADa_del_submarinista.html?id=7O4ISQAACAAJ). L'original alemany és "Tauchreiseführer Spanien: Balearen und Mittelmeerküste", ISBN 978-3-440-11482-7 — [Alibris](https://origin-www.alibris.com/Tauchreisef%C3%A3-Hrer-Spanien-Balearen-Und-Mittelmeerk%C3%A3-Ste-Paperback/book/-344011482)
- **J. Ma. Dacosta**: l'únic llibre trobat és "Balenes i dofins a la Costa Brava" (amb Pere Pagès), El Brau, Figueres, 1993, ISBN 8488589042. No és una guia de busseig — [Biblioteca MMB](https://biblioteca.mmb.cat/bib/23508)
- **Una web que cita la guia**: el changeset d'OSM 155672598 (2024-08-23, usuari mauriciabad, "Dive sites in Begur") té `source = "local knowledge;Book: Guia Submarina de la Costa Brava de Sant Feliu de Guíxols a Begur by Andreu Llamas"` — [OSM changeset 155672598](https://www.openstreetmap.org/changeset/155672598)

### Inferences
- El codi 978-84-933167-8-5 comparteix el prefix editorial 84-933167 amb el llibre de Barcelona i Tarragona (84-933167-0-9, Anthias). Per tant, la guia de Sant Feliu a Begur és gairebé segur d'Anthias, i per tant les guies anunciades el 2010 almenys en part es van publicar.
- Moltes toponímies submarines que es repeteixen a les webs (Barda de Pere el Flaquer, Furió d'Aigua Xelida, Canons de Tamariu, Negre del Falaguer…) poden venir d'aquestes guies o de l'ús dels centres. Sense comparar textos no es pot dir quina font és la primera.

### Gaps
- No s'han pogut consultar el CCUC, la BNE ni la Biblioteca de Catalunya per confirmar editorial i any de la guia de Sant Feliu a Begur, ni per saber si van sortir la de la Selva i la del Cap de Creus.
- No s'han trobat guies franceses impreses de la Costa Brava.
- No s'ha trobat cap web (Wannadive, PADI, SSI, sóc Balena…) que citi la sèrie Llamas ni Kirschner & Bergbauer.

## 5. Cadenes de còpia i agregació: d'on vénen, al capdavall, els punts?

### Takeaway
Hi ha quatre fonts primàries reals:
1. el coneixement dels centres i guies locals;
2. les guies impreses de Llamas i Cáceres;
3. els GPS i logs de bussejadors particulars, que arriben a Wannadive, als logbooks de SSI i a OSM;
4. importacions antigues fetes amb permís, com dive-links.com a OSM el 2010.

Sobre aquestes fonts hi ha cadenes de còpia documentades:
- SSI → Mares, i SSI → OpenDiveMap;
- OSM → OpenWaterAtlas, dive-vibe i DivePlanner(?);
- guia Llamas → OSM;
- dive-links → OSM.

### Cited Findings
- **dive-links.com → OSM (2010)**: el changeset 4094075 de l'usuari "Tric" (2010-03-10, 1.651 canvis) porta el comentari "Data import divespots from dive-links.com" — [OSM changeset 4094075](https://www.openstreetmap.org/changeset/4094075). El permís de dive-links.com, del 18-12-2009, diu: "Mit Quellenhinweis darfst Du die Daten gerne verwenden" — [OSM talk-de, 9-03-2010](https://lists.openstreetmap.org/pipermail/talk-de/2010-March/064416.html). A les Medes encara hi ha nodes amb `source=www.dive-links.com`. La v1 del node 663869682 era "Isla Pedrosa (Höhle)" amb "verified: no, please check and del this tag", i hi ha també Massa d'Or (la Rata) — [OSM node 663869682](https://www.openstreetmap.org/node/663869682/history). El 2017 la comunitat alemanya va criticar aquest "weltweiten Massenimport" — [OSM Community 2017](https://community.openstreetmap.org/t/massenimport-von-sport-scuba-diving/81600)
- **Altres nodes d'OSM a les Medes**: Tasco Gros i La Vaca els va crear ZMWandelaar el 2010-06-26 (changeset 5080187, "Changes Achterberg"). El Reggio i Negre del Falaguer, el mateix usuari el 2012-06-15 (changeset 11905429, "Changes Estartit"), sense font declarada — [OSM changeset 11905429](https://www.openstreetmap.org/changeset/11905429). El 2025-06-18 LifeEncrypter els va retocar ("Added scuba diving related tags to sites in the estartit area", source "survey;aerial imagery") — [OSM changeset 167799743](https://www.openstreetmap.org/changeset/167799743)
- **Guia Llamas → OSM (Begur, 2024)**: el changeset 155672598 cita el llibre com a font (vegeu la secció 4). El 2026 el mateix usuari hi va afegir `scuba_diving:divespot=yes` (changeset 185118771, source "local knowledge") i va desplaçar boies i punts (changesets 188986620 i 188986670, "local knowledge;aerial imagery") — [OSM changeset 185118771](https://www.openstreetmap.org/changeset/185118771). De 60 elements de busseig d'OSM dins la bbox catalana, 51 no tenen `source` i 2 tenen `www.dive-links.com` — consulta [Overpass API](https://overpass-api.de/api/interpreter) del 2026-10-24.
- **OSM → tercers**: OpenWaterAtlas ("spot locations imported from OSM", publicat CC-BY 4.0) — [OpenWaterAtlas](https://openwateratlas.com/en/datasets/). dive-vibe-community (scrapers d'Overpass + IA que "validates" contra Wannadive i DiveAdvisor) — [ScubaBoard](https://scubaboard.com/community/threads/i-open-sourced-a-database-of-2-800-dive-sites-across-122-destinations-free-for-everyone.667171/). Els mapes base offline de Suunto — [Suunto](https://www.suunto.com/Support/disclaimers/offline-maps/)
- **SSI → Mares → OpenDiveMap**: Mares va construir la seva base "with our sister company SSI" — [Divenewswire](https://www.divenewswire.com/?p=29718). OpenDiveMap porta `source: ssi`, `ssi_id` i `ssi_url` als registres — [API OpenDiveMap](https://api.opendivemap.com/v1/sites?country=ES&limit=500)
- **Centres → PADI**: les fitxes les creen i editen els membres PADI i els acrediten com a "contributors" — [PADI Pros blog](https://pros-blog.padi.com/padi-dive-guides-inform-inspire-acquire/); [PADI Travel L'Estartit](https://travel.padi.com/diving-in/spain/l-estartit/)
- **Opinió de la comunitat sobre l'origen**: "Most of these sites just take what their members give them" (Rich Keller, ScubaBoard, 2012) — [ScubaBoard](https://scubaboard.com/community/goto/post?id=6407065). Un KMZ popular es va compilar "from all over the internet" (2013), sense llicència — [ScubaBoard KMZ](https://scubaboard.com/community/threads/free-dive-sites-kmz-files-for-google-earth.443522/). Sobre la qualitat: "the names are variable and the locations are flaky", segons si la coordenada és la boia, l'entrada o la sortida (tursiops, 2022) — [ScubaBoard Dive Sites Catalogue](https://scubaboard.com/community/threads/dive-sites-catalogue.620620/)

### Inferences
- La sospita de l'usuari ("tots ho han tret d'algun lloc") es confirma en part:
  - Els agregadors nous (2025-2026) **copien de manera demostrable**: OpenDiveMap copia SSI, i OpenWaterAtlas i dive-vibe parteixen d'OSM, amb IA que contrasta amb Wannadive i DiveAdvisor.
  - Els grans (PADI, SSI, Wannadive) són sobretot **recol·lectors d'aportacions** de centres i bussejadors. Aquests bussejadors al seu torn fan servir el coneixement oral dels centres i, molt probablement, les guies de Llamas.
- Per a Afons, **una part de l'OSM català no és "neta"**:
  - Els punts de Begur declaren com a font un llibre amb copyright. Una base ODbL no hauria d'incorporar dades copiades d'una obra protegida sense permís. Caldria contactar l'editor per comentar-ho, o no reutilitzar aquests punts.
  - Els de dive-links.com van entrar amb un permís informal condicionat a citar la font.
- Els noms compartits entre fonts (per exemple, "Negre del Falaguer" a OSM des del 2012 i a DivePlanner Pro) no proven còpia: també poden ser toponímia local comuna.

### Gaps
- No s'han pogut consultar les instantànies de la Wayback Machine per veure com eren al llançament Wannadive, divesites.com, Diveboard, Zentacle o Scubago, ni si van començar amb una importació massiva.
- No s'ha comparat el text de les descripcions de SSI, PADI, Wannadive, DivePlanner i la guia Llamas per detectar còpies literals. Seria la prova directa de les cadenes, i caldria fer-la a mà amb poques fitxes.
- No se sap d'on va treure ZMWandelaar els punts de les Medes del 2010-2012, perquè els changesets no declaren cap font.
