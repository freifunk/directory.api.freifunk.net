Qualitätssicherung
==================

Bei jedem Pull Request prüfen wir jeden neuen und veränderten Eintrag in das Freifunk Community Directory gründlich, d.h. sowohl die Qualität des Eintrages selbst als auch die Qualität der Community API Datei.
Diese Prüfungen werden teils automatisiert (Travis CI) und teils manuell durchgeführt. 
Ein Pull Request wird nur akzeptiert und mit dem Master Branch zusammengeführt, wenn dieser den Qualitätskriterien entspricht.

Zusätzlich prüfen wir in regelmäßigen Abständen und bei Bedarf alle Einträge des Freifunk Community Directory bzgl. der Qualität. 

Qualität des Eintrages / Basis-Anforderung an die Community API Datei
--------------

* eine Freifunk Community muss immer ortsbezogen sein. Ist eine Freifunk Community überregional oder in mehreren Orten aktiv müssen für die verschiedenen Städte und Ortschaften mehrere Einträge erstellt werden. Um deutlich zu machen, das diese Ortsgruppen zusammen gehören sollte im Feld `metacommunity` ein gemeinsamer Namen eingetragen werden. 
* je Community API Datei ist eine Zeile in [`directory.json`](directory.json) hinzuzufügen / zu pflegen
* die betreffende Zeile (key/value) enthält eine Freifunk Community Identity (ID) (key) und einen URL (value)
* die Freifunk Community Identity (ID) muss eindeutig sein, keine andere Freifunk Community Identity (ID) darf genauso heißen
* die Freifunk Community Identity (ID) muss komplett in Kleinschreibung geschreiben sein und darf nur die Zeichen a bis z bzw. A bis Z sowie den Unterstrich (_) enthalten, Ä,Ö,Ü etc. sind nicht erlaubt.
* die Freifunk Community Identity (ID) soll folgender Namenskonvention entsprechen: Stadtname + "_" + Bezeichnung. Diese Konvention ist Pflicht, wenn in diesem Ort bereits eine andere Community aktiv ist, ein Zusammenschluss aber nicht geplant ist. Beispiel: "duesseldorf_ffdue" (Wir empfehlen die Kräfte in einer einzigen Community zu vereinen.) Die Bezeichnung darf auch nummerisch oder alphanumerisch sein. Beispiel "duesseldorf_2"
* die Freifunk Community Identity (ID) darf der vereinfachten Namenskonvention entsprechen, falls für diese Stadt noch keine andere Freifunk Community eingetragen ist. Konvention: Stadtname. Beispiel: "duesseldorf"
* die Freifunk Community Identity (ID) soll alphabetisch-korrekt einsortiert werden
* der URL soll ein öffentlich abrufbarer API-Endpunkt sein
* der URL muss per HTTP oder HTTPS erreichbar sein. HTTPS wird empfohlen. 
* die Domain muss per DNS auf eine öffentliche IP auflösen
* der HTTPS-URL muss ein gültiges SSL / TLS Zertifikat ausliefern, welches durch ein allseits bekannte Zertifizierungsstelle ausgestellt wurde. Einfach mit einem aktuellen Browser testen. Details findest Du bei [Mozilla](https://wiki.mozilla.org/CA/Included_Certificates) dem Hersteller des [Browsers Firefox](https://www.mozilla.org/de/firefox/new/)
* der Webserver muss die Freifunk Community API Datei mit dem HTTP Code 200 (also keine Fehlerseite, etc.) oder 307 (Temporary Redirect) ausliefern
* der Webserver darf insbesondere keine anderen Weiterleitungen durchführen (Moved Permanently 301, Found 302, See Other 303, Permanent Redirect 308), stattdessen bitte den direkten Ziel-URL eintragen 
* die Freifunk API Datei muss im JSON Format sein
* die JSON Datei muss auf oberster Ebene das Feld "api" gesetzt haben und dieses muss der aktuellen Versionsnummer des [Freifunk JSON Schemas](https://github.com/freifunk/api.freifunk.net/tree/master/specs) entsprechen
* die Datei muss gegen das aktuelle [Freifunk JSON Schema](https://github.com/freifunk/api.freifunk.net/tree/master/specs) valide sein. Das kann z.B. mit dem [API-Generator](https://freifunk.net/api-generator/) geprüft werden.

Qualität der Community API Datei (erweitert)
--------------
* jede Community muss mindestens eine Möglichkeit zur Kontaktaufnahme bereitstellen. Je mehr Kontaktdaten desto besser.
* eine Freifunk-Community besteht aus einer Gruppe von min. 2-3 Personen, die auch bereits einige Freifunk-Knoten vor Ort betreiben.
* die Gruppe muss organisatorisch sicherstellen, dass Kontaktanfragen an die genannten Kontaktdaten binnen 7 Tagen beantwortet werden. Z.B. E-Mail-Verteiler statt persönliche E-Mail-Adressen. Urlaubsvertretung. Gemeinsamer Zugriff auf die Datei.
* in der Datei genannte URL (z.B. Website-, Map-, NodeList-, Firmware-URL) müssen einen HTTP Code 200 liefern und die Response (Payload) muss augenscheinlich dem jeweiligen Format entsprechen (keine Detailprüfung)
* Die Dateien müssen UTF-8 kodiert sein und ein korrekter Charset HTTP-Header vom [Webserver ausgeliefert](https://serverfault.com/questions/581760/how-do-i-set-proper-headers-for-json-in-apache) werden. Github-URLs sind von dieser Regel ausgenommen.
* Das Feld 'state.lastchange' muss einen Zeitstempel vom Tag der Erstellung des Pull Requests haben (bei Folge-Commits: Tag des Commits/Push), das automatisiere setzen dieses Feldes (z.B. täglich) ist nur erlaubt, wenn tatsächlich am restlichen Inhalt eine Änderung vorgenommen wurde.

Regelmäßige Prüfung / Löschen von Einträgen
--------------
Mindestens einmal im Jahr prüfen wir alle Einträge bzgl. Qualität des Eintrages. Zudem prüfen wir anlassbezogen, z.B. auf Grund eines Issues in Github.

Wenn wir Qualitätsprobleme feststellen, gehen wir wie folgt vor:
1. wir erstellen für jede betroffene Freifunk Community ein Github Issue. 
2. zusätzlich kontaktieren wir die betreffende Freifunk Community gemäß der [letzten verfügbaren Version der Community API Datei](https://api.freifunk.net/data/ffSummarizedDir.json).
3. wir warten auf eine Rückmeldung (siehe Wartefrist)
4. erfolgt keine Rückmeldung, werden wir im Freifunk Forum einen Beitrag verfassen und um Mithilfe bitten, um geeignte Ansprechpartner zu finden und auf das Problem aufmerksam zu machen. Um Weiterleitung des Forum-Eintrages wird gebeten. Zusätzlich versuchen wir (mit überschaubarem Aufwand) Ansprechpartner / weitere Kontaktmöglichkeiten zu finden (z.B. per Website)
5. erfolgt eine Meldung, dass das Problem behoben ist, wird nachgeprüft und bei erfolgreicher Bestätigung das Issue geschlossen. 
6. erfolgt eine Meldung, dass das Problem behoben ist, wird nachgeprüft und bei nicht erfolgreicher Bestätigung das Issue entsprechend kommentiert und auf Rückmeldung gewartet (siehe Wartefrist)
7. erfolgt eine Meldung, das an dem Problem gearbeitet wird oder die Info weitergeleitet wurde, wird das Issue entsprechend kommentiert und auf Rückmeldung gewartet (siehe Wartefrist)
8. verstreicht die Wartefrist ohne Rückmeldung wird der Eintrag gelöscht und das Issue geschlossen
9. erfolgt eine Rückmeldung, dann wird wie in Punkt 4-8 verfahren. Ist die maximale Wartezeit überschritten, gibt es keine neue Wartefrist: der Eintrag wird gelöscht und das Issue geschlossen.

Wartefrist für Rückmeldungen
-------------
Wir warten mindestens 7 Tage auf eine Rückmeldung.

Maximale Bearbeitungszeit des Gesamtprozesses
-------------
Ohne Mitwirkung der Ansprechpartner der betroffnen Community endet o.g. Prozess bereits nach 2 Wartefristen, also nach 14 Tagen. 
Wenn es binnen der Wartefrist (7 Tage) eine Rückmeldung gibt, kann es jeweils eine zusätzliche Wartezeit von 7 Tagen geben. 
Sollte es in der Community zu Verzögerungen in der Bearbeitung kommen, dann müssen die Ansprechpartner der Community selbständig neue Rückmeldungen geben, damit der Prozess weiterläuft. 

Sollte die Issue-Bearbeitung von Seiten des Freifunk Community Directory Teams ins Stocken geraten, dann werden neue Wartefristen ggf. 
erst mit einigen Tagen Verspätung bekannt gegeben. Diese Verzögerung sind "geschenkte Tage", die zu der Regel Wartezeit hinzugezählt werden (z.B. dann 33 Tage). 
Der Prozess endet also nicht mit 28 Tagen, nur weil das Community Directory Team zu langsam war. 

Gelöschte Einträge / erneut eintragen
-------------
Es gibt viele Gründe warum ein Eintrag gelöscht wurde (siehe oben).
Ein gelöschter Eintrag darf jederzeit erneut per Pull Request eingereicht werden - z.B. wenn das Problem beseitigt wurde. 

Einträge die auf Grund eines Beschlusses des Freifunk Community Directory Council gelöscht wurden, können nur durch einen neuen Beschluss des Freifunk  Community Directory Council wieder aufgenommen werden.

Was nicht geprüft wird
-------------
Wir prüfen nur o.g. Minimalanforderungen an die Freifunk Community API Datei und den Eintrag. Eine weitergehende semantische Prüfung von z.B. Eurer Adresse, Geo Daten, Website, Social Media, etc. erfolgt im Rahmen der Pull Request Prüfung nicht.

Optional geben wir Tips, die über o.g. Qualitätskriterien hinausgehen, aber keine Einfluss auf den Prozess haben.

Das Freifunk Community Direcory Team ist sich dessen bewusst, dass das Freifunk Community Directory ein zentraler Dienst ist und das zur Freifunk-Philosophie gehört, dass wir bestrebt sind Dienste dezentral zu gestalten. Aus diesem Grund möchten wir das Freifunk Community Directory ausschließlich als technischen Dienst umsetzen und bewerten daher keine nicht-technische Kriterien - wie z.B. ob die Community eine "echte" Freifunk Community ist.

Wir gehen initial davon aus, dass Ihr sowohl die [Freifunk Vision](https://freifunk.net/worum-geht-es/vision/)  als auch das [Freifunk Memorandum of Understanding](https://blog.freifunk.net/2015/05/15/memorandum-understanding/) unterstützt und bitten den PR-Ersteller dieses im Pull Request zu bestätigen. Diese Selbsterklärung wird - ähnlich wie eine CE-Konformitätserklärung von Hardware-Herstellern - ohne Prüfung akzeptiert.

DRAFT: Nachprüfung / Anlassbezogene Prüfung / Löschen von Einträgen
-------------
Die Gemeinschaft aller Freifunk Communities kann über ein Github Issue klären lassen, ob eine Community der Freifunk Vision und dem Freifunk Memorandum of Understanding folgt oder zu unrecht eingetragen wurde.
Die Entscheidung, ob ein Eintrage gelöscht wird trift jedoch nicht das Community Directory Team. Das Community Directory Team ist nur dafür zuständig die Entscheidung umzusetzen und das Ticket zu schließen.

Jede bereits eingetragene Freifunk Community ist berechtigt ein solches Github Issue zu erstellen. Bitte ein Github Issue Titel nach folgendem Muster erstellen: 

"API: Löschung der Community FREIFUNK COMMUNITY ID HERE" 

Im Text muss beschrieben werden, warum man glaubt, dass es sich nicht um eine Freifunk Community im Sinne der Vision und des Memorandum of Understanding handelt.
Die betreffende Community muss am selben Tag, auf mindestens einer in der API Datei angegebenen Kontaktmöglichkeit, auf dieses Github Issue aufmerksam gemacht werden.
Die betroffene Freifunk Community kann selbstverständlich auch Stellung nehmen. Mit der Issue Erstellung beginnt die Abstimmung. Im Laufe der Diskussion darf das eigene Stimme geändert werden (die letzte Stimme der jeweiligen Person zählt).

Nach 30 Tagen ist die Abstimmung beendet, egal, wie viele Stimmen abgegeben wurden. Wenn in einfacher Mehrheit der Abstimmungsteilnehmer eine Löschung beschlossen wurde. Bei Unentschieden oder 0 Stimmen wird der Eintrag nicht gelöscht. 
Stimmberechtigt ist jede Freifunk Community (jeder Freifunk Community Director Eintrag), jeweils mit je einer Stimme, egal wie viele Freifunker in dieser Community organisiert sind. Meta Communities haben keine Stimme, den sie sind über die Einträge der API-Dateien entsprechend oft vertreten. 

Lösch-Beschlüsse vom Freifunk Community Directory Council werden vom Freifunk Community Directory Team zeitnah umgesetzt. 

**Hinweis:**
Oben genannter Prozess ist noch im Entwurfsmodus. 
Einige Details sind noch zu klären, daher ist die First bis auf weiteres ausgesetzt. 
Auf Grund der Fristaussetzung kann es keine Beschlüsse geben. 
Das Community Directory Team setzt daher keine Beschlüsse um und schließt solche Github Isses derzeit nicht.
Details zu Freifunk Community Directory Council findest Du hier: https://github.com/freifunk/directory.api.freifunk.net/issues/606
