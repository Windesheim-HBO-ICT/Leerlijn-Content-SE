# Leerlijn content SE
Welkom bij de content voor leerlijnen van SE. 

## Branches
Er bestaan drie branches op deze repository. Hieronder wordt verder uitgelegd wat in elke branch staat. \
De veranderingen moeten gemaakt worden op de `content` branch. Dit moet met een handmatige pull requests door worden gevoerd naar `staging`. Deze pull request moet door minimaal twee personen worden gecontroleerd.\
Zodra de pull request is doorgevoerd naar `staging` wordt de pipeline geactiveerd, waarna een automatisch pull request naar `main` wordt aangemaakt. Deze pull request moet door minimaal één persoon worden gecontroleerd.\

### Main
De main branch is een beschermde branch. Hierop kan niet gewerkt worden.\
In de main branch staat een `build` folder. Deze folder bevat de content die op de leerlijn wiki weergegeven zal worden.\
Verder staat in de main branch een `report.md`. Dit report bevat het overzicht over de inhoud van de leerlijn content (uit de `build` folder).

### Staging
De staging branch bevat de mappen `.github`, `build`, `content`, `test_cases`. Op deze branch kan niet gewerkt worden.
- `.github`:\
De `.github` folder bevat het script, de dataset en de pipeline files. **⚠️Deze scripts moeten niet aangepast worden⚠️**\
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

### Schrijven van content
Content moet geschreven worden in `.md` files. Hierbij kunnen aan de hand van page properties kenmerken meegegeven worden aan een pagina.

- `title`:\
De title is de titel die wordt weergeven op de wiki.
- `tags`:\
Er kunnen tags toegevoegd worden aan een pagina om pagina's te kunnen categoriseren aan een onderwerp. 
- `taxonomie`:\
Taxonomie codes worden gebruikt om automatisch onderwerpen (als tags) toe te voegen aan een pagina.
- `difficulty`:\
Difficulty wordt aan de hand van sterren op de pagina weergegeven. Dit betreft de moeilijkheidsgraad van een file. De range voor deze difficulty is van 0 tot en met 5.


*Extra zaken met betrekking tot taxonomie codes:*
- Uit een taxonomie code worden het onderwerp (tc-3) en het niveau (tc-2) weergegeven als tags op een pagina.
- De taxonomie code moet geschreven worden met kleine letters
- Er kunnen meerdere taxonomie codes toegevoegd worden aan een pagina.
- Taxonomie codes moeten als een lijst worden toegevoegd, anders pakt het script de code niet \
  <img width="915" alt="Screenshot 2024-09-17 at 12 02 11" src="https://github.com/user-attachments/assets/51b8125f-84c7-440e-81de-b3533f87e440"> [Page properties in obsidian](https://help.obsidian.md/Editing+and+formatting/Properties)

  Ook kan het in markdown zelf toegevoegd worden op de volgende manier\
  <img width="356" alt="Screenshot 2024-09-17 at 12 11 59" src="https://github.com/user-attachments/assets/0a7183d1-9ac5-4604-a51b-4dfa78c605d4">
- Als een taxonomie code ongeldig is, zal de pagina in het report komen te staan onder de tabel van de `niet-geslaagde bestanden`. Er zullen dan ook geen tags toegevoegd worden van die taxonomie code
- In Obsidian kan een tag niet een `.` bevatten. Taxonomie codes worden automatisch als een tag toegevoegd aan een pagina. Haal deze niet weg ondanks dat het als een fout eruit kan zien.


### Pipelines
Zoals eerder uitgelegd zijn er 2 pipelines. Beide pipelines worden afgevuurd op de staging branch. 
- Test pipeline:\
De test pipeline checkt test bestanden als bestanden in  `test_cases` of `.github` folders worden aangepast.
- Rapport pipeline:\
De rapport pipeline zorgt ervoor dat `report.md` wordt gevuld met de juiste content op basis van taxonomie codes in de content.

### Dataset
In de staging branch in de map `.github` is een `dataset.xls` en een `dataset.csv` aanwezig. \
Als er nieuwe onderwerpen bij komen of een bestaand onderwerp wordt aangepast moet dit worden gedaan in `dataset.xls`. \
Vervolgens moet het Excel bestand worden geëxporteerd naar een csv met de naam `dataset.csv`.
- Het is **niet** nodig om elementen zoals tabelheaders te verwijderen
- Het Excel bestand en dus de CSV mogen ook geen lege regels hebben (`;;;;;;;;;;`)
