[![Check api directory](https://github.com/freifunk/directory.api.freifunk.net/actions/workflows/check_directory.yml/badge.svg)](https://github.com/freifunk/directory.api.freifunk.net/actions/workflows/check_directory.yml)

Freifunk Community Directory
==========

Dieses Github Repository enthält das [Community Directory](https://freifunk.net/blog/2013/12/die-freifunk-api/) der [Freifunk Initiative](https://freifunk.net/).
Das Community Directory wird von zahlreichen Anwendungen / Apps verwendet, z.B. von der [Freifunk Karte](https://www.freifunk-karte.de/), der [Community Website](http://community.freifunk.net) oder der [App Freifunk](https://apps.apple.com/de/app/freifunk/id687078875)) für das iPhone oder das iPad.

Dein Source Code Beitrag
==========

Erstelle einfach einen Pull Request, wenn Du Deine Community hier eintragen oder einen bestehenden Eintrag ändern bzw. löschen willst.

Voraussetzungen:
----------------
1. Wir können nur Einträge annehmen, bei denen sichergestellt ist, dass diese langfristig gepflegt werden. Deine Community hat mindestens. 2-3 aktive Personen die diesen Ort betreuen (sie müssen keine Anwohner dieses Ortes sein).
2. Deine Community hat mehrere Router in diesem Ort online.
3. Dein Eintrag im Community Directory entspricht den [Qualitätskriterien](QUALITY.md)
4. Deine Community API Datei entspricht den [Qualitätskriterien](QUALITY.md)
5. Organisatorisch stellt Deine Community sicher, dass die Ansprechpartner (Team) binnen 7 Tagen auf Anfragen antworten und binnen 28 Tagen Probleme beheben können. 

Zu Punkt 5 empfehlen wir:
- E-Mail-Verteiler statt persönliche E-Mail-Adressen in der Community API Datei hinterlegen
- Mehrere Kontakt-Kanäle in der Community API Datei hinterlegen, um nicht von einem Kanal abhängig zu sein (Mailserver down, Postfach voll)
- Wissen und Zugriffsrechte im Team entsprechend verteilen
- Urlaubsvertretung und Zuständigkeiten klar absprechen 
- Regelmäßig das Freifunk Forum besuchen, oder sicherstellen das Euch einen Eintrag bzgl. Community API Datei weiterleiten wird

Mit Deinem Pull Request bestätigst Du, dass Du oben genannte Voraussetzungen aktuell und in Zukunft erfüllst / gewährleisten kannst.

Hilfe
==========

Zur Erstellung des Pull Requests oder der Community API Datei kannst Du im Freifunk Forum Hilfe finden.

Entstehung
==========

Zum Wireless Community Weekend 2013 in Berlin fand ein ersten Treffen
zum Relaunch unserer Website freifunk.net statt. Dabei kam auch die
Frage auf, wie man die einzelnen Freifunkcommunities am besten
präsentieren kann, ohne alle Daten zentral zu erfassen und zudem den
Communities eine einfache Möglichkeit zu bieten, eigene Daten selbst
aktuell zu halten.

In Anlehnung an die Hackerspaces API (https://hackerspaces.nl/spaceapi/)
wurde die Idee einer Freifunk API geboren: Jede Community stellt ihre
Daten in einem definierten Format an einer ihr zugänglichen Stelle
(Webspace, Wiki, Webserver) bereit und trägt sich in das Verzeichnis
ein. Das Verzeichnis besteht lediglich aus einer Zuordnung von
Communitynamen und URL zu den den bereitgestellten Daten. Die erste
Anwendung soll eine Karte mit darin angezeigten Freifunkcommunities
sein, um Besuchern und Interessierten einen Überblick zu geben und
lokale Ansprechpartner zu vermitteln.

Die Freifunk API soll die Metadaten der Communities dezentral sammeln und anderen Nutzern zur Verfügung stellen. Die API ist nicht zu verwechseln mit einer Datenbank für Freifunkknoten oder als Verzeichnis von Firmwareeinstellungen einzelner Communities.

Weitere Informationen zur API sind in einem Blogartikel unter https://blog.freifunk.net/2013/die-neue-freifunk-api-aufruf-zum-mitmachen zusammengefasst.

History
=======

At the Wireless Community Weekend 2013 in Berlin there was a first meeting to relaunch freifunk.net. To represent local communities without collecting and storing data centrally, a way had to be found. Another requirement was to enable local communities to keep their data up to date easily.

Based on the Hackerspaces API (https://hackerspaces.nl/spaceapi/) the idea of the freifunk API was born: Each community provides its data in a well defined format, hosted on their places (web space, wiki, web servers) and contributes a link to the directory. This directory only consists of the name and an url per community. First services supported by our freifunk API are the global community map and a community feed aggregator.

The freifunk API is designed to collect metadata of communities in a decentral way and make it available to other users. It's not designated to be a freifunk node database or a directory of individual community firmware settings.

Licence
=======

Please feel free to use this data in any (usefull) way you want.
All code and content in this git repository is provided under [Creative Commons Zero 1.0 Universal](LICENSE) license to you.

Contribution
=======
Feel free to contribute to this project by creating a pull request. 
Please sign-off your git commits before pushing it to your repository.

You confirm that you are allowed to contribute all code and content of your commit to this repository by simply adding 
a sign-off to your commit message. 

Please ensure that the sign-off is done with the same e-mail address as your committer e-mail address.

Easyest way to do this is to use the git sign-off feature:

**Sign-off your commit (directly)**

```git commit --signoff -m "Commit message here"```

**Sign-off your last commit (if you forgot to sign-off)**

```git commit --amend --no-edit --signoff ```

**Force pushing last commit (if already pushed before sign-off)**

```git push --force-with-lease origin your-branch-name-here ```

