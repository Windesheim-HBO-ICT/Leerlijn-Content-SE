---
title: JavaScript Debugging
tags:
  - JS/debugging
  - page
difficulty: 2
---

# 1. JavaScript Debugging
In deze deeltaak wordt JavaScript debugging behandeld. Specifiek console methodes, debug statements en de devtools.

## 1.1 Debugging: console methods
De **console methods** zijn hulpmiddelen die je kunt gebruiken om informatie in de console van de browser weer te geven. Dit is handig voor debugging en het bijhouden van de staat van je applicatie tijdens de ontwikkeling.

### Console: log
`console.log()` is de meest gebruikte methode om informatie naar de console te sturen. Hiermee kun je de waarde van variabelen en de uitvoer van functies weergeven.

```javascript
const naam = "Alice";
console.log("Hallo", naam);
```

### Console: warn
`console.warn()` toont een waarschuwing in de console. Dit kan nuttig zijn om aandacht te vestigen op potentieel problematische code zonder dat het een fout is.

```javascript
console.warn("Dit is een waarschuwing!");
```

### Console: error
`console.error()` wordt gebruikt om foutmeldingen weer te geven in de console. Dit is nuttig voor het weergeven van ernstige fouten in je applicatie.

```javascript
console.error("Er is een fout opgetreden!");
```

### Console: info
`console.info()` toont informatieve berichten in de console. Het wordt vaak gebruikt om algemene informatie weer te geven die nuttig kan zijn voor debugging.

```javascript
console.info("Dit is een informatief bericht.");
```

### Console: debug
`console.debug()` is vergelijkbaar met `console.log()`, maar kan worden gefilterd door de console-instellingen van de browser. Dit kan handig zijn om specifieke debug-informatie weer te geven.

```javascript
console.debug("Debug-informatie: x =", 42); // Output: Debug-informatie: x = 42
```

### Console: table
`console.table()` toont gegevens in een tabelvorm in de console. Dit is vooral handig voor het weergeven van arrays of objecten.

```javascript
const mensen = [
  { naam: "Alice", leeftijd: 25 },
  { naam: "Bob", leeftijd: 30 }
];
console.table(mensen);
```

### Console: group / groupEnd
`console.group()` en `console.groupEnd()` worden gebruikt om berichten in groepen te organiseren, wat de leesbaarheid kan verbeteren wanneer je meerdere gerelateerde berichten hebt.

```javascript
console.group("Groep 1");
console.log("Bericht in groep 1");
console.log("Bericht in groep 1");
console.groupEnd();
```

## 1.2 Debuggging: debugger statement
De `debugger` statement pauzeert de uitvoering van JavaScript en opent de debugger in de ontwikkelaarstools van de browser, indien deze is ingeschakeld. Dit is handig om de staat van je code op specifieke punten te inspecteren.

```javascript
function berekenSom(a, b) {
  debugger; // Code pauzeert hier wanneer de debugger is geopend
  return a + b;
}

const resultaat = berekenSom(5, 10);
console.log(resultaat);
```

Wanneer de `debugger` statement wordt bereikt, opent de browser zijn ingebouwde debugger, waardoor je de waarde van variabelen en de uitvoering van de code kunt inspecteren.


## 1.3 Debugging: Developer Tools
**Browser Developer Tools** bieden een reeks krachtige hulpmiddelen voor het debuggen, testen, en optimaliseren van webapplicaties. Deze tools zijn beschikbaar in moderne browsers zoals Google Chrome, Firefox, Safari, en Edge. Hieronder een lijst met de hoofdcomponenten van Deveveloper Tools.

### Elementen (Elements)
Hier kun je de DOM van de pagina inspecteren en manipuleren. Je kunt elementen selecteren, wijzigen en de toegepaste CSS-stijlen bekijken en aanpassen.

### Console
Dit is waar de uitvoer van `console.log()`, `console.error()`, etc. verschijnt. Je kunt hier ook JavaScript uitvoeren in de context van de huidige pagina.

### Netwerk (Network)
Deze tab toont netwerkverkeer, zoals aanvragen voor bestanden en API-verzoeken, inclusief hun status, timing, en headers.

### Sources
Hier kun je de JavaScript-bestanden en andere bronnen van de pagina bekijken, pauzeren, en de code debuggen met behulp van breakpoints.

### Applicatie (Application)
De Application tab geeft toegang tot gegevensopslag zoals cookies, LocalStorage, sessionStorage, en IndexedDB. Het biedt ook toegang tot Service Workers en PWA-functies.

### Prestaties (Performance)
Hier kun je de prestaties van je webpagina analyseren door een opname van de activiteit te maken en te bekijken hoe verschillende processen bijdragen aan laadtijd en interactie.

### Geheugen (Memory)
Gebruik deze tab om geheugengebruik te monitoren en te analyseren. Dit is handig voor het opsporen van geheugenlekken.

### Netwerkcondities (Network Conditions)
Simuleer verschillende netwerkcondities zoals langzame netwerken om te zien hoe je applicatie presteert onder verschillende omstandigheden.

### Lighthouse
Gebruik Lighthouse om de prestaties, toegankelijkheid, best practices en SEO van je webpagina te analyseren. Het genereert een gedetailleerd rapport met aanbevelingen.

### Developer tools openen
* **Chrome**: `Ctrl+Shift+I` of `Cmd+Opt+I` (Mac). 
* **Firefox**: `Ctrl+Shift+I` of `Cmd+Opt+I` (Mac). 
* **Safari**: `Cmd+Opt+I`. 
* **Edge**: `F12`.

### Developer tools extra
Rechtsboven in het Developer tools scherm staan 3 puntjes. Klik hier op `more tools`. Hier staat een lijst met extra opties zoals animaties, lagen of recording.

> Om snel resultaat te zien van bijvoorbeeld een CSS media feature gebruik dan de `rendering` optie. Hier staan verschillende opties op die CSS features te testen. Ook staat hier bijvoorbeeld opties om jouw pagina te bekijken met gezichtsvermogen tekorten. Ook is het rendering tabje handig om content layout shift(CLS) problemen op te sporen.