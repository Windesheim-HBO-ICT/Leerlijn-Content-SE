# Leerlijn content SE
Welkom bij de content voor leerlijnen van SE. 

## Branches
Op deze repository bestaan drie vast branches, `main`, `staging` en `content`.

### Main
De main branch is een beschermde branch. Hierop kan niet gewerkt worden.\
In de main branch staat een `build` folder. Deze folder bevat de content die op de leerlijn wiki weergegeven zal worden.\
Verder staat in de main branch een `taxco_report.md` en `content_report.md`. Deze reports bevatten het overzicht over de inhoud van de leerlijn content (uit de `build` folder).
Verder is er nog een `.git` folder waarin de een pull request template.

### Staging
De staging branch bevat de mappen `.github` en `build`. Op deze branch kan niet gewerkt worden.
- `build`:\
De `build` folder bevat de content die overgezet moet worden naar de `main` branch.

PR's mergen naar deze branch

### Content
In de content branch staat de map`content`.
- `content`:\
De `content` folder bevat de content wat op de leerlijn wiki getoond wordt. Dit is de folder waarin de content aangepast moet worden.

Vanaf deze branch worden feature branches gemaakt.

---

## Schrijven van content
Voor het schrijven van content worden freature branches gebruikt. Maak een nieuwe branch gebasseerd op `content`. Zodra nieuwe content klaar is kan er een pull request worden aangemaakt van de **feature** branch naar de **content** branch.\
Content moet geschreven worden in `.md` files. Zie de schrijfwijze in de branch `content` en dan in de map `content/schrijfwijze/`

Een pull request (van feature naar content, van content naar staging en van staging naar main) heeft altijd de volgende eisen
- [ ] Content voldoet aan gestelde eisen uit `Kwaliteitseisen Onderwijs Aanbod.docx`
- [ ] Spellingscheck gedaan
- [ ] Content geschreven volgens de gekoppelde 4C/ID componenten templates
- [ ] De naam van het onderwerp in de tekst is bold
- [ ] MD koppen hebben geen bold teksten
- [ ] Juiste format voor image/figuur naamgevingen
- [ ] Figuur onderschriften toegevoegd waar nodig
- [ ] Taxonomie codes toegevoegd
- [ ] Witregels gecheckt
- [ ] Bronnenlijst toegevoegd (indien nodig)
- [ ] Content-branch gepulled in de feature branch
- [ ] Benodigde verwijzingen toegevoegd


*Extra zaken met betrekking tot taxonomie codes:*
- Uit een taxonomie code worden het onderwerp (tc-3) en het niveau (tc-2) weergegeven als tags op een pagina.
- Er kunnen meerdere taxonomie codes toegevoegd worden aan een pagina.
- Taxonomie codes moeten als een lijst worden toegevoegd, anders pakt het script de code niet. In het voorbeeld hieronder zijn twee taxonomie codes toegevoegd van hetzelfde onderwerp maar op 2 verschillende niveaus.
  ```
  ---
  title: 
  Tags: None
  difficulty: 2
  taxonomie:
    - ib-19.2.Controlestructuur-Beslissingen-If-Else.OI
    - ib-19.3.Controlestructuur-Beslissingen-If-Else.OI
  ---
  ```
- Als een taxonomie code ongeldig is, zal de pagina in het report komen te staan onder de tabel van de `niet-geslaagde bestanden`. Er zullen dan ook geen tags toegevoegd worden van die taxonomie code.
- In Obsidian (een markdown editor) kan een tag niet een `.` bevatten. Taxonomie codes worden automatisch als een tag toegevoegd aan een pagina. Haal deze niet weg ondanks dat het als een fout eruit kan zien.
