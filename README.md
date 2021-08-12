[![Build Status](https://travis-ci.com/freifunk/directory.api.freifunk.net.svg?branch=master)](https://travis-ci.com/freifunk/directory.api.freifunk.net)

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

Qualitätssicherung
==================

* Die API-Datei sollten mit dem [API-Generator](https://freifunk.net/api-generator/) erstellt bzw. validiert worden sein.
* Eine Community muss immer ortsbezogen sein. Ist eine Community überregional oder in mehreren Orten aktiv müssen für die verschiedenen Städte und Ortschaften mehrere Einträge erstellt werden. Um deutlich zu machen, das diese Ortgruppen zusammen gehören sollte im Feld `metacommunity` ein gemeinsamer Namen eingetragen werden. Alternativ kann der Communityname auch in allen Orten identisch sein.
* Jede Community muss mindestens Kontaktdaten und eine Möglichkeit zur Teilnahme bereitstellen. Je mehr Daten desto besser.
* Eine Freifunk-Community besteht aus einer Gruppe von min. 2-3 Personen, die auch bereits einige Freifunk-Knoten vor Ort betreibten.
* Die Dateien müssen UTF8 codiert sein und so auch vom [Webserver ausgeliefert](https://serverfault.com/questions/581760/how-do-i-set-proper-headers-for-json-in-apache) werden.
* Die API-Datei sollte möglichst aktuell gehalten werden. Stark veraltete oder ungültige Dateien werden nach Rückfrage wieder entfernt. 
* Damit die API-Dateien verarbeitet werden können müssen diese in der [`directory.json`](directory.json) eingetragen werden.

History
=======

At the Wireless Community Weekend 2013 in Berlin there was a first meeting to relaunch freifunk.net. To represent local communities without collecting and storing data centrally, a way had to be found. Another requirement was to enable local communities to keep their data up to date easily.

Based on the Hackerspaces API (https://hackerspaces.nl/spaceapi/) the idea of the freifunk API was born: Each community provides its data in a well defined format, hosted on their places (web space, wiki, web servers) and contributes a link to the directory. This directory only consists of the name and an url per community. First services supported by our freifunk API are the global community map and a community feed aggregator.

The freifunk API is designed to collect metadata of communities in a decentral way and make it available to other users. It's not designated to be a freifunk node database or a directory of individual community firmware settings.

Licence
=======

Please feel free to use this data in any (usefull) way you want.
All code and content in this git repository is proviced unter [Creative Commons Zero 1.0 Universal](LICENSE) license to you.

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

```git commit --amend --signoff ```

**Force pushing last commit (if already pushed before sign-off)**

```git push --force-with-lease origin your-branch-name-here ```

