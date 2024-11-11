---
draft: true
---
# Algemeen
De template bestanden hebben een page property draft true. Let erop dat je geschreven content geen draft true heeft.

## Checklist content
- [ ] Content voldoet aan gestelde eisen uit `Kwaliteitseisen Onderwijs Aanbod.docx`
- [ ] Spellingscheck gedaan
- [ ] Zinnen niet te lang
- [ ] Figuur onderschrift
- [ ] Casussen toegevoegd
- [ ] Verwijzingen gemaakt of een post in Discord `#verwijzingen` gezet
- [ ] Pull request gemaakt

## Page properties
Aan het begin van een pagina moeten page properties toegevoegd worden.
```
---
title: Titel
tags: None
difficulty: 2
taxonomie:
  - ib-19.2.Controlestructuur-Beslissingen-If-Else.OI
  - ib-19.3.Controlestructuur-Beslissingen-If-Else.OI
---
```
- **title:** Dit is de titel die op de webpagina weergeven zal worden. 
- **tags:** Tags kunnen handmatig worden toegevoegd. Tags kunnen verschillende pagina's verbinden door het onderwerp van de tag.
- **difficulty:** Dit is optioneel. Dit kan gebruikt worden om de moeilijkheid van een deeltaak/leertaak aan te duiden.
- **taxonomie:** Dit zijn de taxonomie codes die gebruikt worden om automatische tags te genereren op de webpagina.

## Taxonomie
* Binnen Obsidian kan je door aan het begin gelijk `---` te typen page properties opgeven.
* De taxco's moeten als volgt worden geformuleerd: TC1.TC2.TC3.Type
* Alles moet worden geschreven voor niveau twee en drie. Voeg dus ook twee taxco's toe. (In Obsidian moet je de page property dan een list maken, of je opent het MD in iets als Vscode om dat te doen)
Voorbeeld: 
```
ib-19.2.Controlestructuur-Beslissingen-If-Else.OI, 
ib-19.2.Controlestructuur-Beslissingen-If-Else.PI, 
ib-19.3.Controlestructuur-Beslissingen-If-Else.OI, 
ib-19.3.Controlestructuur-Beslissingen-If-Else.PI, 
ib-19.2.Controlestructuur-Beslissingen-If-Else.DT, 
ib-19.2.Controlestructuur-Beslissingen-If-Else.DT
```
* Let op hoofdletters, de pipeline is nu (nog) hoofdletter gevoelig

## Headings
- De grootste heading die gebruikt moet worden is `##`.
- Elke subheading moet worden verkleind met een extra #, dus bijv. `###`.

## Witregels
- Tussen de page properties en het begin van de tekst moet een witregel worden geplaatst.
- Tussen een einde van een alinea en een nieuwe heading moet één witregel worden gebruikt. 

## Afbeeldingen
Als je een afbeeldingen toevoegt maak dan een mapje `src` aan in dezelfde map als de `md` bestanden
Voeg figuur onderschrift toe door onder de afbeelding / diagram *italic* toelichting te geven.
Format: `Figuur [nummer]: [toelichting]`

## Diagrammen
Als je een diagram toevoegen doe dit dan via mermaid.
Bij diagrammen kan je denken aan sequentie, flowchart, class.

## Blokken
In veel pagina's worden gekleurde blokken gebruikt om bijvoorbeeld een waarschuwing te geven of bronnen te vermelden. Het standaard format om een blok aan te maken is als volgt:
```
> [!Keywoord] Titel
> Tekst in het blok
```

Dit ziet er dan als volgt uit:
> [!Keyword] Titel 
> Tekst in het blok

Om een inklapbare melding te gebruiken moet er een `-` worden toegevoegd:
```
> [!Keywoord]- Titel
> Tekst in het blok
```

Dit ziet er als volgt uit:
> [!info;slk]- Titel
> Tekst in het blok

Bij het gebruik van blokken zijn er een aantal standaard veelgebruikte keywoorden:
- **Info:**
	- Wordt gebruikt om korte belangrijke informatie te highlighten en bronnenlijst weer te geven.
- **Succes:**
	- Aan het eind van opdrachten (Deeltaken en Leertaken) kan een succes blok gebruikt worden wanneer de opdracht geslaagd is.
- **Warning:**
	- Aanduiden waar mogelijke gevaren zitten.

### Bronnen
In het geval dat er bronnen gebruikt zijn om informatie/opdrachten te schrijven voor een pagina, moet er onderaan de pagina een bronnenlijst opgenomen worden. Als er meerdere bronnen zijn, dan moet elke bronlink afgesloten worden met een `\`.
> [!info] Bronnen
> Bron: https://bron.bron \
> Bron2: https://bron.bron

```
> [!info] Bronnen
> Bron: https://bron.bron \
> Bron2: https://bron.bron
```

## Pagina afsluiting
Het format om een pagina af te sluiten is als volgt:
```
> [!info] Bronnen
> Bron: https://bron.bron 

---

> Volgende stap: [[bestandsnaam]]
```
- Onderaan wordt de bronnenlijst opgenomen.
- Dan wordt een scheidingslijn gebruikt met boven en onder een witregel.
- Als laatste wordt een verwijzing gemaakt naar het volgende document (indien van toepassing).

Dit zou er als volgt uit zien:
> [!info] Bronnen
> Bron: https://bron.bron 

---

> Volgende stap: [[bestandsnaam]]

# Ondersteunende informatie
Gebruik dezelfde structuur als `if-else`
Controleer of je content voldoet aan de eisen uit het Word bestand: `Kwaliteitseisen Onderwijs Aanbod.docx`

# Procedurele informatie
Gebruik dezelfde structuur als `if-else`
Controleer of je content voldoet aan de eisen uit het Word bestand: `Kwaliteitseisen Onderwijs Aanbod.docx`

# Deeltaken
* Structuur gelijk aan die van If-else
* 4 opdrachten voor eenvoudige onderwerpen zoals primitieve datatypes
* 10 opdrachten voor complexere onderwerpen met klein beetje oplopende complexiteit
* Mogelijke uitwerking aanwezig
* Gebruik de taal C#
* Vergeet niet dingen als `using System;`

## Codeblock / Coderunner
Er zijn drie verschillende soorten codeblocks: read only, runnable en sandbox. Om de codeblock werkt te hebben binnen de editor Obsidian, moet een community plugin worden geïnstalleerd.

1. Ga naar de instellingen > Community plugins
	1. Als deze nog niet zijn aangezet, zet deze aan
2. Klik op browse en zoek naar `interactive-code-blocks`. 
3. Installeer deze.

Daarnaast moet de coderunner nog worden aangezet. Dat kan met het volgende commando:
```
docker run -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 --rm -d ghcr.io/windesheim-hbo-ict/coderunner
```
### Read only
```javascript
const list = [1, 2, 3, 4];

list.forEach(e => console.log(e))

list.map(e => 'Element: ' + e).forEach(e => console.log(e))
```
### Runnable
```javascript runner
const list = [1, 2, 3, 4];

list.forEach(e => console.log(e))

list.map(e => 'Element: ' + e).forEach(e => console.log(e))
```
### Sandbox
```javascript sandbox
const list = [1, 2, 3, 4];

list.forEach(e => console.log(e))

list.map(e => 'Element: ' + e).forEach(e => console.log(e))
```

Coderunner mag **alleen** worden gebruikt bij de deeltaken, in de overige pagina's enkel met code blokken werken
