# Leerlijn content SE
Welkom bij de content voor leerlijnen van SE. 

## Branches
Op deze repository bestaan 4 vast branches, `main`, `staging`, `content` en `dev`. De dev branch is alleen nodig voor de mensen die werken aan de pipeline, scripts en dataset. De overige branches zijn contributie branches.

### Main
De main branch is een beschermde branch. Hierop kan niet gewerkt worden.\
In de main branch staat een `build` folder. Deze folder bevat de content die op de leerlijn wiki weergegeven zal worden.\
Verder staat in de main branch een `report.md`. Dit report bevat het overzicht over de inhoud van de leerlijn content (uit de `build` folder).
Verder is er nog een `.git` folder waarin de CODEOWNERS is opgenomen en een pull request template.

### Staging
De staging branch bevat de mappen `.github`, `build`, `content`, `test_cases`. Op deze branch kan niet gewerkt worden.
- `.github`:\
De `.github` folder bevat het script, de dataset en de pipeline files. **⚠️Deze bestanden moeten niet aangepast worden⚠️**
- `build`:\
De `build` folder bevat de content die overgezet moet worden naar de `main` branch.
- `content`:\
De `content` folder bevat dezelfde content die ook in de content branch staat (wat door pull requests wordt aangepast). Deze content wordt gebruikt om de `build` folder te vulllen met de aanpassingen door het script.
- `test_cases`:\
De `test_cases` folder bevat test files waarmee wordt gecheckt of het script de taxonomie codes juist kan uitlezen en omzetten.

### Content
In de content branch staat de map`content` en `test_cases`.
- `content`:\
De `content` folder bevat de content wat op de leerlijn wiki getoond wordt. Dit is de folder waarin de content aangepast moet worden.
- `test_cases`:\
De `test_cases` folder bevat de testen die in de staging branch worden gebruikt om het script mee te testen.

---

## Schrijven van content
Voor het schrijven van content worden freature branches gebruikt. Maak een nieuwe branch gebasseerd op `Content`. Zodra nieuwe content klaar is kan er een pull request worden aangemaakt van de feature branch naar de content branch.\
Content moet geschreven worden in `.md` files. Hierbij kunnen aan de hand van page properties kenmerken meegegeven worden aan een pagina.
- `title`:\
De title is de titel die wordt weergeven op de wiki.
- `tags`:\
Er kunnen tags toegevoegd worden aan een pagina om pagina's te kunnen categoriseren aan een onderwerp. 
- `taxonomie`:\
Taxonomie codes worden gebruikt om automatisch onderwerpen (als tags) toe te voegen aan een pagina.
- `difficulty`:\
Difficulty wordt aan de hand van sterren op de pagina weergegeven. Dit betreft de moeilijkheidsgraad van een file. De range voor deze difficulty is van 0 tot en met 5.

Een pull request (van feature naar content, van content naar staging en van staging naar main) heeft altijd de volgende eisen
- Er moet minimaal 1 approval zijn. Bij de pull request van content naar staging moeten dit er 2 zijn.
- Er moet een review zijn gegeven door een codeowner.
- Als er discussions/comments zijn toegevoegd, moeten deze eerst opgelost zijn.


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


### Pipelines
Zoals eerder uitgelegd zijn er 2 pipelines. Beide pipelines worden afgevuurd op de staging branch. 
- Test pipeline:\
De test pipeline checkt test bestanden als bestanden in  `test_cases` of `.github` folders worden aangepast.
- Rapport pipeline:\
De rapport pipeline zorgt ervoor dat `report.md` wordt gevuld met de juiste content op basis van taxonomie codes in de content.

### Dataset
In de staging branch in de map `.github` is een `dataset.xlsx` en een `dataset.csv` aanwezig. \
Als er nieuwe onderwerpen bij komen of een bestaand onderwerp wordt aangepast moet dit worden gedaan in `dataset.xlsx`. \
Vervolgens moet het Excel bestand worden geëxporteerd naar een csv met de naam `dataset.csv`.
- Het is **niet** nodig om elementen zoals tabelheaders te verwijderen
- Het Excel bestand en dus de CSV mogen ook geen lege regels hebben (`;;;;;;;;;;`)
