import re
mystr="""IN
Search






Avatar image
Home
Trending
Subscriptions
Library
History
Your videos
Watch later
Liked videos
Show more
SUBSCRIPTIONS

YT Battles

7mlc

Afrotechmods

Beast 文 Strike OP

Bhai Ki Padhai

Bilal Göregen

Billie Eilish
Show 45 more
AboutPressCopyrightContact usCreatorsAdvertiseDevelopers
TermsPrivacyPolicy & SafetyHow YouTube worksTest new features
© 2021 Google LLC



Python Exercise 11: Regex Email Extractor | Python Tutorials For Absolute Beginners In Hindi #96
CodeWithHarry
12K views
2 years ago


send this to your best friend with no context.
nadia
6.1M views
2 years ago


GTA V with Ultra Realistic Graphics Mod!
MrBeast Gaming
23M views
6 months ago


Billie Eilish - Ocean Eyes (Official Music Video)
Billie Eilish
338M views
4 years ago


AWESOME BOLLYWOOD MIMICRY (SHAH RUKH KHAN,HRITHIK ROSHAN AND MANY MORE)
Mithilesh Patankar
2.4M views
2 years ago


Robot Meets Self Driving Car - Sophia by Hanson & Jack by Audi
Mobilegeeks.de
9.7M views
4 years ago


The Lion King in 60 Seconds
Reedflower
2M views
3 weeks ago


Mission Prerna: प्रेरणा ज्ञानोत्सव एवं समृद्ध मॉड्यूल द्वारा उपचारात्मक शिक्षा हेतु प्रशिक्षण
Mission Prerna
Scheduled for 2/24/21, 11:00 AM
Latest YouTube posts

YT Battles
•
3 days ago
Thoughts on YouTube BANNING PewDiePie's "Coco" diss track?
5.5K votes

608


145


Fine Arts Guruji
•
23 hours ago
Final kro 😇
3K votes

315


20


TALENT TADKA
•
19 hours ago
Random Sawal😋
Ghar ke khaane ke alawa...Bahar ke Khaane me sabse zyaada kya pasand hai?
74K votes

4.7K


471


Zombie Experiment NYC
putzombiesback
58M views
8 years ago
Learning Path For Python Web Development | Python Tutorials For Absolute Beginners In Hindi #97
CodeWithHarry
39K views
2 years ago
Yashraj Mukhate Gets Creative With Rakhi's Dialogues | Bigg Boss S14 | बिग बॉस S14
Colors TV
27M views
1 month ago
Minecraft Speedrunner VS 4 Hunters GRAND FINALE
Dream
26M views
2 weeks ago
COVID-19 news

Coronavirus India Update: कोरोनावायरस के नए केस 10,584, Maharashtra Lockdown के आसार, CM Uddhav सख्त
Dainik Jagran - दैनिक जागरण
113K views
4 hours ago
Covid News: Coronavirus Cases Surging In India; 1st Phase Of Vaccination Underway | India Today
India Today
75K views
1 day ago
Coronavirus India Update: कोरोनावायरस मामलों में गिरावट दर्ज, ये आंकड़े देंगे राहत | COVID-19 India
Navbharat Times नवभारत टाइम्स
1.1K views
1 hour ago
Corona News Today : महाराष्ट्र में बेकाबू कोरोना !। CoronaVirus । Covid19 । Lock down Again। Corona
Zee Rajasthan
103K views
1 day ago
{"pulkit": "imperdiet.non.vestibulum@justoeu.co.uk",
 "gunjan": "consectetuer.adipiscing@metusurna.ca",
  "ayushi": "enim@vitaesodalesnisi.org",
"suman": "at.pretium.aliquet@nunc.co.uk"},
{"pulkit": "Praesent@cursuset.net", "
gunjan": "molestie.tortor.nibh@lectusantedictum.net",
"ayushi": "pretium.aliquet@pedeet.ca",
"suman": "In.at@vehiculaaliquetlibero.net"},
{"pulkit": "primis@Proin.edu",
"gunjan": "non.enim@eleifend.org",
"ayushi": "volutpat@libero.edu",
"suman": "vel@velvulputate.edu"},
{"pulkit": "rutrum@mauris.ca",
"gunjan": "at.velit.Cras@accumsanlaoreet.net",
"ayushi": "ipsum.dolor@sit.ca",
"suman": "Sed.dictum@ipsumnonarcu.edu"},
{"pulkit": "tincidunt.pede.ac@justoPraesent.com",
"gunjan": "ultrices@magnaseddui.ca",
"ayushi": "volutpat.Nulla@necmalesuada.org",
"suman": "mauris@porttitor.ca"},
{"pulkit": "velit@adipiscing.org",
"gunjan": "tempus@interdumenimnon.ca",
"ayushi": "Duis.elementum.dui@luctus.com",
"suman": "ante.ipsum.primis@quam.ca"},
{"pulkit": "amet@quamPellentesquehabitant.co.uk",
"gunjan": "erat@orciquislectus.co.uk",
"ayushi": "ornare.placerat@disparturientmontes.org",
"suman": "ad@volutpatNulla.edu"},
{"pulkit": "pede.Cras@amet.ca",
"gunjan": "Suspendisse@non.org",
"ayushi": "Proin@tincidunt.net",
"suman": "dolor.Donec@loremlorem.co.uk"},
{"pulkit": "ipsum.Curabitur.consequat@augueid.com",
"gunjan": "et@ametultriciessem.ca",
"ayushi": "quis.arcu@euultricessit.edu",
"suman": "Duis@Etiam.net"},
{"pulkit": "consequat.auctor@euismod.ca",
"gunjan": "auctor@quamCurabiturvel.edu",
"ayushi": "quis@tincidunt.org",
"suman": "at@nonummyac.net"},
{"pulkit": "cursus@ProinultricesDuis.net",
"gunjan": "eget.venenatis@arcueu.edu",
"ayushi": "Cras@Etiamlaoreet.ca",
"suman": "dignissim@antelectusconvallis.edu"},
{"pulkit": "nec@semperrutrumFusce.com",
"gunjan": "iaculis.quis.pede@iaculislacus.org",
"ayushi": "aliquet@facilisisSuspendissecommodo.net",
"suman": "orci.Donec@est.com"},
{"pulkit": "mattis.semper.dui@diam.org",
 "gunjan": "sed.dui@pharetrased.ca",
  "ayushi": "In@Curabitur.edu", "suman": "Etiam@Nunccommodoauctor.edu"}, {"pulkit": "ut@elitfermentum.co.uk", "gunjan": "diam.nunc.ullamcorper@auctorvelitAliquam.co.uk", "ayushi": "tempus.eu@inconsectetuer.com", "suman": "placerat.velit@vitae.com"}, {"pulkit": "lectus.ante.dictum@velitduisemper.org", "gunjan": "leo@dolortempus.org", "ayushi": "arcu@Proinultrices.ca", "suman": "arcu.imperdiet.ullamcorper@egestas.edu"}, {"pulkit": "feugiat.non@ante.com", "gunjan": "ac.metus.vitae@convallis.net", "ayushi": "nisi.sem.semper@arcu.co.uk", "suman": "sit@nonenim.net"}, {"pulkit": "rhoncus.Proin@nunc.edu", "gunjan": "dui@fringilla.ca", "ayushi": "viverra.Donec@mollisInteger.edu", "suman": "nec.urna@netus.net"}, {"pulkit": "fringilla.cursus.purus@porttitorvulputateposuere.ca", "gunjan": "eros.Nam.consequat@laoreet.ca", "ayushi": "lacinia.Sed@netus.com", "suman": "dolor.Nulla.semper@Cumsociis.org"}, {"pulkit": "nisl@gravidamauris.ca", "gunjan": "Cras.interdum.Nunc@Fuscemi.net", "ayushi": "Aliquam.rutrum@Nullamfeugiatplacerat.com", "suman": "a.feugiat@pellentesque.com"}, {"pulkit": "tempus@imperdietullamcorperDuis.net", "gunjan": "pede.Cum.sociis@Nulla.org", "ayushi": "Sed.eu.eros@enimgravidasit.net", "suman": "elit.Nulla@atvelit.com"}, {"pulkit": "mi.pede.nonummy@convalliserat.com", "gunjan": "dui@porttitor.org", "ayushi": "eget@orciadipiscing.org", "suman": "Duis.ac@ultriciesligulaNullam.org"}, {"pulkit": "lectus.Cum@Duisrisus.org", "gunjan": "enim.commodo@dolor.co.uk", "ayushi": "lacus.varius@bibendumsedest.com", "suman": "nunc.ac@tinciduntorci.ca"}, {"pulkit": "purus.mauris@nasceturridiculusmus.ca", "gunjan": "velit@ultriciesdignissim.ca", "ayushi": "vulputate.dui@nullamagnamalesuada.com", "suman": "tellus.Suspendisse.sed@MorbivehiculaPellentesque.com"}, {"pulkit": "Cras.convallis@metus.co.uk", "gunjan": "auctor@erosNam.org", "ayushi": "fames.ac.turpis@egetmetuseu.com", "suman": "massa.rutrum.magna@nislMaecenasmalesuada.co.uk"}, {"pulkit": "vel.nisl@dolor.co.uk", "gunjan": "Donec.est@posuere.ca", "ayushi": "est.mollis.non@auctor.co.uk", "suman": "fermentum.arcu.Vestibulum@Integervitae.org"}, {"pulkit": "lectus.pede.ultrices@vitaevelit.edu", "gunjan": "neque@neque.org", "ayushi": "vitae.erat.vel@mauris.com", "suman": "Integer@posuereat.edu"}, {"pulkit": "nibh@Curabitur.edu", "gunjan": "Suspendisse@purussapien.org", "ayushi": "eu.sem.Pellentesque@Infaucibus.ca", "suman": "sapien.molestie.orci@Sedeueros.org"}, {"pulkit": "volutpat.Nulla@Nullatemporaugue.co.uk", "gunjan": "Mauris.vel@Suspendisse.com", "ayushi": "nunc.sit@Sed.co.uk", "suman": "hymenaeos.Mauris.ut@ligulaAenean.net"}, {"pulkit": "convallis@nulla.ca", "gunjan": "nunc.est.mollis@urna.org", "ayushi": "gravida.Aliquam@semconsequat.co.uk", "suman": "nascetur@interdumfeugiat.co.uk"}, {"pulkit": "at@egestasDuis.edu", "gunjan": "nulla.Integer.vulputate@facilisis.com", "ayushi": "magna.malesuada@dui.co.uk", "suman": "ornare.lectus.ante@risus.net"}, {"pulkit": "eu.ligula.Aenean@erat.net", "gunjan": "sed@velit.co.uk", "ayushi": "eget.metus.eu@ultricesiaculis.org", "suman": "sociis.natoque@tempus.net"}, {"pulkit": "mauris@enim.ca", "gunjan": "Praesent@dapibus.ca", "ayushi": "est@vulputate.org", "suman": "hendrerit.neque@Vivamus.edu"}, {"pulkit": "ipsum@amet.com", "gunjan": "nec@Phasellus.ca", "ayushi": "Lorem.ipsum.dolor@Donecatarcu.org", "suman": "Nam.consequat@pretiumaliquet.edu"}, {"pulkit": "sem@sapienCras.org", "gunjan": "Nam@ipsumdolorsit.org", "ayushi": "faucibus.id@MorbivehiculaPellentesque.org", "suman": "hendrerit@metusAenean.edu"}, {"pulkit": "Sed@Donecnibhenim.co.uk", "gunjan": "faucibus.lectus@luctussitamet.net", "ayushi": "consectetuer@tellus.edu", "suman": "sed.est.Nunc@mauris.net"}, {"pulkit": "eu@vulputaterisusa.org", "gunjan": "amet.faucibus@enimcondimentumeget.com", "ayushi": "dictum@ligulaDonec.edu", "suman": "imperdiet.dictum.magna@etlibero.com"}, {"pulkit": "et.eros.Proin@necluctusfelis.co.uk", "gunjan": "id.nunc@Nullasemper.ca", "ayushi": "et.euismod@iaculisquispede.org", "suman": "malesuada.Integer@ipsumprimisin.ca"}, {"pulkit": "aliquam@nuncacmattis.org", "gunjan": "accumsan.laoreet.ipsum@scelerisquelorem.co.uk", "ayushi": "id.erat@enimSednulla.net", "suman": "sociis.natoque@vestibulumneque.co.uk"}, {"pulkit": "scelerisque.dui.Suspendisse@inceptos.com", "gunjan": "vitae.odio.sagittis@enimCurabitur.net", "ayushi": "mollis@atauctorullamcorper.com", "suman": "a@Duis.co.uk"}, {"pulkit": "Suspendisse.ac.metus@AliquamnislNulla.co.uk", "gunjan": "porttitor@lectusrutrum.net", "ayushi": "ultrices.Duis@magnaetipsum.org", "suman": "nunc.ac@Phasellusdolor.ca"}, {"pulkit": "fermentum@fringilla.edu", "gunjan": "ac.ipsum.Phasellus@nullaInteger.co.uk", "ayushi": "ornare@sapiengravidanon.net", "suman": "venenatis.vel.faucibus@et.com"}, {"pulkit": "venenatis.lacus.Etiam@faucibus.net", "gunjan": "Suspendisse.sagittis@placeratCras.org", "ayushi": "pellentesque@lobortisultrices.net", "suman": "egestas.Sed.pharetra@etpede.co.uk"}, {"pulkit": "mus@Quisquetinciduntpede.ca", "gunjan": "sodales.nisi.magna@eratvitaerisus.co.uk", "ayushi": "est@maurisid.co.uk", "suman": "sapien.imperdiet.ornare@mollisnon.net"}, {"pulkit": "magna.nec@nullaIntegervulputate.org", "gunjan": "sagittis.Nullam@ut.edu", "ayushi": "mauris@elitfermentumrisus.org", "suman": "Donec.dignissim.magna@habitantmorbi.edu"}, {"pulkit": "ornare.tortor@lacusEtiambibendum.ca", "gunjan": "blandit@aliquetmolestietellus.ca", "ayushi": "velit.Quisque@lectusNullamsuscipit.edu", "suman": "ipsum.Curabitur.consequat@morbitristique.co.uk"}, {"pulkit": "molestie@elitpellentesquea.org", "gunjan": "eu@Craseutellus.ca", "ayushi": "turpis.vitae@lacus.net", "suman": "a.facilisis.non@necleo.ca"}, {"pulkit": "dictum.mi@musProin.com", "gunjan": "non.luctus.sit@rutrumurna.org", "ayushi": "tempus.scelerisque.lorem@aliquetmetus.edu", "suman": "felis.adipiscing.fringilla@quamquisdiam.com"}, {"pulkit": "lacinia.orci.consectetuer@metus.com", "gunjan": "enim@fermentumvelmauris.com", "ayushi": "rutrum.Fusce@eliteratvitae.com", "suman": "Sed.molestie@eueuismod.org"}, {"pulkit": "risus@Fuscealiquet.net", "gunjan": "Curabitur@justo.co.uk", "ayushi": "egestas@parturientmontesnascetur.net", "suman": "ridiculus@acturpis.org"}, {"pulkit": "id@Phasellus.net", "gunjan": "ut.nulla.Cras@Aliquamauctor.com", "ayushi": "adipiscing.fringilla@nequeseddictum.edu", "suman": "Vivamus@magna.com"}, {"pulkit": "nunc.sed.pede@hendreritidante.edu", "gunjan": "Ut.tincidunt.vehicula@nonarcu.net", "ayushi": "pellentesque.Sed.dictum@tinciduntadipiscingMauris.com", "suman": "ac@Phasellus.com"}, {"pulkit": "eu.nibh.vulputate@ipsumac.org", "gunjan": "ut.sem@purusDuiselementum.net", "ayushi": "tincidunt.congue.turpis@ridiculus.com", "suman": "fermentum@montes.edu"}, {"pulkit": "orci@augueutlacus.com", "gunjan": "eget.varius@Donec.co.uk", "ayushi": "In@maurisid.com", "suman": "libero.at.auctor@posuerevulputatelacus.ca"}, {"pulkit": "elementum.sem.vitae@Integer.com", "gunjan": "sit.amet.ante@tempus.net", "ayushi": "vel.pede@dolordapibusgravida.co.uk", "suman": "Fusce.aliquam.enim@molestietortor.co.uk"}, {"pulkit": "sed@disparturientmontes.edu", "gunjan": "facilisis.non@eget.com", "ayushi": "ac@penatibusetmagnis.com", "suman": "leo.elementum.sem@nisiCum.net"}, {"pulkit": "congue@enim.org", "gunjan": "lorem@sed.com", "ayushi": "ut.pharetra@Vestibulumanteipsum.net", "suman": "ligula@purus.edu"}, {"pulkit": "dui.Fusce.diam@pedesagittisaugue.edu", "gunjan": "in.cursus@dignissimlacus.edu", "ayushi": "lectus@gravidaPraesent.net", "suman": "dapibus@consectetuercursuset.edu"}, {"pulkit": "mi@nonsapien.ca", "gunjan": "magna.nec.quam@eu.net", "ayushi": "orci.adipiscing.non@Cum.org", "suman": "facilisis.vitae.orci@magnaCras.edu"}, {"pulkit": "Sed.id@CraspellentesqueSed.com", "gunjan": "vulputate.lacus@vestibulum.co.uk", "ayushi": "varius@vel.org", "suman": "congue.In.scelerisque@turpis.edu"}, {"pulkit": "Ut.nec@urnaNuncquis.co.uk", "gunjan": "Quisque@Aeneangravidanunc.net", "ayushi": "magna.tellus.faucibus@necanteMaecenas.ca", "suman": "mi.Duis@Donectempus.net"}, {"pulkit": "mus@elit.edu", "gunjan": "mattis.velit.justo@utdolor.co.uk", "ayushi": "non.dapibus.rutrum@ultricies.com", "suman": "cursus.diam.at@imperdietnecleo.com"}, {"pulkit": "ut@a.co.uk", "gunjan": "nonummy.ut.molestie@Donec.org", "ayushi": "magna.Ut@estarcuac.ca", "suman": "sem.elit@non.co.uk"}, {"pulkit": "ante.dictum@atarcu.ca", "gunjan": "amet.consectetuer.adipiscing@magnaUttincidunt.ca", "ayushi": "venenatis@Crasconvallisconvallis.com", "suman": "egestas@vitaeerat.net"}, {"pulkit": "congue.a.aliquet@urnaUt.ca", "gunjan": "amet.ornare@etmagnis.com", "ayushi": "natoque@Craslorem.com", "suman": "est.Mauris@enim.net"}, {"pulkit": "nec.tellus.Nunc@Innec.com", "gunjan": "ut@Morbi.co.uk", "ayushi": "Quisque@adipiscing.org", "suman": "ac.facilisis@fames.co.uk"}, {"pulkit": "gravida.molestie.arcu@Donecfringilla.com", "gunjan": "Sed.eu@tincidunt.ca", "ayushi": "lacus@necorciDonec.com", "suman": "eros.turpis.non@idmollisnec.edu"}, {"pulkit": "amet@velitPellentesque.net", "gunjan": "in.lobortis.tellus@nibh.net", "ayushi": "Aliquam.ultrices.iaculis@tellus.org", "suman": "id@pede.edu"}, {"pulkit": "quis.tristique@afeugiattellus.net", "gunjan": "arcu.Vestibulum.ante@purussapien.net", "ayushi": "mus.Proin@ipsumprimis.edu", "suman": "faucibus.orci.luctus@ametultriciessem.net"}, {"pulkit": "ac.urna.Ut@non.ca", "gunjan": "magnis.dis.parturient@vestibulum.ca", "ayushi": "Maecenas.iaculis@imperdietdictum.co.uk", "suman": "est@egetmetus.org"}, {"pulkit": "nulla.magna@et.edu", "gunjan": "a@nibh.co.uk", "ayushi": "a.feugiat@magnaPraesent.edu", "suman": "mollis.non@augueSedmolestie.edu"}, {"pulkit": "vehicula.risus@Inornare.edu", "gunjan": "erat.volutpat@Fusce.net", "ayushi": "in.consectetuer.ipsum@placerateget.co.uk", "suman": "odio.a.purus@mienimcondimentum.co.uk"}, {"pulkit": "sit.amet.luctus@interdumlibero.net", "gunjan": "diam.Pellentesque.habitant@consectetueradipiscing.org", "ayushi": "magnis.dis@libero.com", "suman": "rutrum@Quisque.co.uk"}, {"pulkit": "et@Integersem.org", "gunjan": "blandit@Sedet.edu", "ayushi": "tempor.bibendum@Curabitursedtortor.org", "suman": "scelerisque.lorem.ipsum@sit.edu"}, {"pulkit": "magna.Lorem.ipsum@asollicitudin.org", "gunjan": "bibendum.sed@metusAliquam.org", "ayushi": "Phasellus.in.felis@diamvelarcu.ca", "suman": "iaculis@semmagnanec.edu"}, {"pulkit": "erat.eget.ipsum@risus.co.uk", "gunjan": "lacus.pede@congueaaliquet.co.uk", "ayushi": "felis.ullamcorper.viverra@tristiqueaceleifend.com", "suman": "pede@enimEtiam.ca"}, {"pulkit": "risus@convallis.co.uk", "gunjan": "sagittis@lacus.org", "ayushi": "egestas.a@Duis.org", "suman": "Mauris.vestibulum@nec.co.uk"}, {"pulkit": "Suspendisse.tristique@dolor.edu", "gunjan": "ac.turpis@commodoat.com", "ayushi": "mollis.Phasellus@mattisornarelectus.ca", "suman": "blandit.mattis@consectetuer.org"}, {"pulkit": "nec.cursus.a@semconsequatnec.org", "gunjan": "nunc@egetmollislectus.co.uk", "ayushi": "Donec.egestas@adipiscingelit.com", "suman": "aliquet@rhoncus.ca"}, {"pulkit": "sagittis@euplacerat.edu", "gunjan": "augue.Sed.molestie@dictumsapien.co.uk", "ayushi": "pretium.et@sitamet.org", "suman": "ipsum.Suspendisse.non@a.ca"}, {"pulkit": "Aenean@velarcu.net", "gunjan": "faucibus.Morbi.vehicula@enimmi.ca", "ayushi": "sociosqu.ad@venenatisa.ca", "suman": "auctor.non.feugiat@Duisrisusodio.edu"}, {"pulkit": "Sed.eget.lacus@fringillaornare.ca", "gunjan": "Mauris.ut@porta.edu", "ayushi": "non@Uttinciduntorci.com", "suman": "sed@magna.net"}, {"pulkit": "ullamcorper@Maurisvestibulumneque.edu", "gunjan": "a.dui.Cras@ornare.org", "ayushi": "arcu@acfermentum.com", "suman": "Aliquam.erat@nisinibh.ca"}, {"pulkit": "tellus.imperdiet.non@sit.net", "gunjan": "euismod.est.arcu@aliquam.co.uk", "ayushi": "dignissim.lacus@interdum.edu", "suman": "Etiam@nonloremvitae.com"}, {"pulkit": "pede@auctornonfeugiat.edu", "gunjan": "non@duiCraspellentesque.org", "ayushi": "dignissim@luctus.co.uk", "suman": "Quisque.varius.Nam@Donec.net"}, {"pulkit": "sollicitudin.a.malesuada@libero.co.uk", "gunjan": "mauris@Mauris.co.uk", "ayushi": "Nunc.quis.arcu@Nunc.net", "suman": "amet.metus@risus.ca"}, {"pulkit": "sagittis.lobortis@ligula.edu", "gunjan": "molestie@Sedcongue.co.uk", "ayushi": "accumsan@cursuspurusNullam.edu", "suman": "eu.tellus.Phasellus@augue.org"}, {"pulkit": "semper.auctor@commodohendreritDonec.com", "gunjan": "euismod@tempusscelerisquelorem.edu", "ayushi": "ante.Nunc.mauris@rutrumjustoPraesent.org", "suman": "eget.tincidunt.dui@Fuscedolorquam.co.uk"}, {"pulkit": "feugiat.non.lobortis@cubiliaCuraeDonec.org", "gunjan": "non.egestas.a@Namtempordiam.net", "ayushi": "faucibus@consequatenim.com", "suman": "pellentesque@In.co.uk"}, {"pulkit": "Suspendisse.ac@consequatdolor.com", "gunjan": "gravida.molestie.arcu@accumsaninterdum.co.uk", "ayushi": "pede.malesuada@eratneque.org", "suman": "risus.at.fringilla@montes.co.uk"}, {"pulkit": "consectetuer.euismod.est@magnamalesuadavel.org", "gunjan": "justo.faucibus.lectus@necluctusfelis.org", "ayushi": "Curae@egestas.ca", "suman": "cursus@sapienimperdietornare.org"}, {"pulkit": "nulla.ante.iaculis@lorem.net", "gunjan": "Integer.mollis.Integer@fermentumvel.org", "ayushi": "nulla.Donec.non@arcuSed.edu", "suman": "convallis.ante.lectus@elit.edu"}, {"pulkit": "cursus.in.hendrerit@tristique.edu", "gunjan": "dignissim@Nuncmauriselit.co.uk", "ayushi": "Duis@Nunclectus.edu", "suman": "Proin@estNunc.co.uk"}, {"pulkit": "lorem.Donec.elementum@nostraper.co.uk", "gunjan": "orci.Donec.nibh@idsapienCras.edu", "ayushi": "dolor.sit@pedePraesenteu.co.uk", "suman": "mauris.elit.dictum@maurisid.ca"}, {"pulkit": "imperdiet.ornare.In@orciPhasellus.net", "gunjan": "lobortis.quam@Integermollis.net", "ayushi": "quam.dignissim@euismodmauriseu.co.uk", "suman": "risus.at@eget.org"}, {"pulkit": "mattis.semper@sapienimperdiet.edu", "gunjan": "orci.in.consequat@tellusidnunc.ca", "ayushi": "ornare@Etiamligula.net", "suman": "eu@AeneanmassaInteger.edu"}, {"pulkit": "tempus.lorem@nonsapien.ca", "gunjan": "nostra.per@nuncrisus.org", "ayushi": "tempus.mauris@risus.co.uk", "suman": "dapibus@Maecenasmalesuadafringilla.com"}, {"pulkit": "sapien@famesac.com", "gunjan": "enim.gravida@dui.org", "ayushi": "nibh.dolor@quam.edu", "suman": "eu@utpellentesqueeget.net"}, {"pulkit": "dolor.sit@risus.co.uk", "gunjan": "est.mollis@Pellentesque.ca", "ayushi": "risus@auctorMauris.net", "suman": "placerat.velit.Quisque@porttitorscelerisque.net"}, {"pulkit": "ipsum.non@porttitoreros.com", "gunjan": "id.erat.Etiam@ipsumleo.co.uk", "ayushi": "tristique.senectus.et@eudolor.edu", "suman": "ornare@ut.ca"}, {"pulkit": "Quisque.porttitor@massanonante.net", "gunjan": "dapibus.ligula@placerataugueSed.org", "ayushi": "et.risus@nunc.co.uk", "suman": "mauris.elit@ProinvelitSed.edu"} ];
Daniel Radcliffe Raps Blackalicious' "Alphabet Aerobics"
The Tonight Show Starring Jimmy Fallon
110M views
6 years ago
American Tries Indian Food in New Delhi! (Thali + Nan)
Conner Sullivan
1.6M views
1 year ago
Class 12 Board - Small Motivational Clip
Apni Kaksha
767K views
2 months ago
Must Watch | Angrez Ne Kar DI Ulti | Foreigner Roasting Dhinchak Pooja
Wajahat Hasan
130K views
2 hours ago
A man falls into water in a canyon
RM Videos
4.5M views
3 years ago
How to control someone else's arm with your brain | Greg Gage
TED
9.4M views
5 years ago
All Enderman sounds in reversed!!! ( Secret language revealed?)
The Red Ash Asher88
2.8M views
2 years ago
Weirdest Moments in Sports
Spor Delisi HD
2.8M views
1 month ago

"""
compiled=re.compile(r'.@')
matches=compiled.finditer(mystr)
for items in matches:
  print(items)