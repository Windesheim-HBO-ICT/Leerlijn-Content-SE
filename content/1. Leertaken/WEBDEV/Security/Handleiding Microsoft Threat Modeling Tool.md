---
title: Handleiding Microsoft Threat Modeling Tool
---
## Stap 1. Downloaden
---
Om toegang te krijgen tot de Microsoft Threat Modeling Tool, kun je de onderstaande link openen. Scroll vervolgens helemaal naar beneden op de pagina en onder het kopje "Next Steps" vind je de downloadlink voor de tool. Klik erop om de tool te downloaden.

[Microsoft Threat Modeling Tool downloaden](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool)
## Stap 2. Nieuwe model aanmaken
---
Voordat je een [threat model](2.%20Wat%20is%20een%20Threat%20Model.md) kan maken moet er eerst een nieuw project worden opgestart.
![[stap2.png]]

## Stap 3. Ontwerp een threat model
---
Aan de rechterzijde van het scherm bevinden zich de beschikbare componenten waarmee het threat model kan worden opgebouwd. In de onderstaande afbeelding zijn de volgende componenten gebruikt: 
- Generic Data Flow (verzoek en respons) om de stroom van verzoeken te illustreren. 
- Generic TrustLine Boundary om de locaties van de niet-vertrouwde grenzen aan te geven. 
- Browser 
- Webapplicatie 
- Web-API 
- Database 

**Een handige tip**: door op een component te klikken, kunt u aan de rechterzijde van het scherm, onder het gedeelte van het component, de naam wijzigen.
![[stap3.png]]
## Stap 4. Rapport generen
---
Om een volledig rapport te genereren, klik je bovenaan op "Rapports". Selecteer vervolgens de optie "Generate full rapport". Zodra je een naam hebt ingevoerd, wordt het rapport automatisch gegenereerd. In dit rapport worden alle mogelijke kwetsbaarheden op basis van het **STRIDE-model** beschreven, samen met mogelijke maatregelen om ze te verminderen.

![[stap4.png]]

## Stap 5. Threat List genereren
---
### Stap 5.1. Analysis View
Om de Threat List te genereren die je kunt exporteren naar csv klik je bovenaan op Analysis View.

![[stap6_1.png]]

### Stap 5.2 Exporteren
Klik vervolgens op ‘Export to csv’.

![[stap6_2.png]]

### Stap 5.3 Opslaan
Sla het project op in de map van het vak security of bij je showcase bestanden. Op deze manier kan je gaandeweg de realisatie van het project de threat model eenvoudig aanpassen als dit nodig is.

Om het project op te slaan klik je links boven op `File`, `Save As` en geef een logische locatie en bestandsnaam op. Klik vervolgens op `Opslaan` om het bestand op te slaan.

![[stap5.3 opslaan.png]]
### Stap 5.4 Openen in Excel
Importeer het `.csv` bestand in Excel en zet het om naar een tabel. Door de threat list te exporteren naar een `xls` of vergelijkbaar bestandstype kan je erg eenvoudig de lijst langslopen en passende mitigaties uitwerken. 
#### Stap 5.4.1. Tekst naar kolommen / Text to Columns
Om dit te doen selecteer eerst de eerste kolom. Ga vervolgens in het lint naar het tabblad `Gegevens / Data` en klik op `Tekst naar kolommen / Text to Columns`.
#### Stap 5.4.2 Scheidingsteken
In de `Wizard Tekst naar kolommen / Convert Text to Columns Wizard` selecteer de optie `Gescheiden / Delimited` en klik op `Volgende / Next`. 
#### Stap 5.4.3 Opties
Zorg ervoor dat alleen de optie `Komma / Comma` en `Dubbele scheidingsteken als één beschouwen / Treat consecutive delimiters as one` zijn geselecteerd en klik op `Volgende / Next`. 
#### Stap 5.4.4 Voltooien
Laat de instellingen staan zoals ze standaard staan en klik op `Voltooien / Finish`.

![[stap6_3.png]]
#### Stap 5.4.5 Opslaan
Om het bestand later te kunnen gebruiken zorg ervoor dat je het opslaan als een `.xls` of vergelijkbaar bestandstype en niet als `.csv`. `.csv` ondersteund geen tabellen.