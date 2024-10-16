---
title: 2. JavaScript data types
tags:
  - JS/Data-types
  - page
difficulty: 2
---

# 2 JavaScript Data Types
JavaScript heeft verschillende data types die gebruikt kunnen worden om verschillende soorten waarden op te slaan. In JavaScript kennen we 7 `primitive` data types. Dit zijn: 
- number; 
- string;
- boolean; 
- null;
- undefined;
- object;
- symbol;

## 2.1.1 Data type: `number`
Een number is een numerieke waarde, zowel gehele getallen als decimale getallen.
```javascript
let geheelGetal = 42
let decimaalGetal = 3.14
```

## 2.1.2 Data type: `string`
Een string is een reeks van karakters, zoals tekst. In JavaScript zijn er enkele manieren om een string te definiëren. Dit kan met enkele quotes `''`, dubbele quotes `""` of backquotes ` `` `.

```javascript
let enkeleQuotes = 'Hallo Wereld';
let dubbeleQuotes = "Hallo Wereld";
let templateLiterals = `Hallo Wereld`;
```

De backquotes hebben nog een speciale functie. Deze kunnen gebruikt worden voor `template literals`. Gebruik `${variabele}` om een variable in een tekst te zetten.

```javascript
let naam = 'Elsje';
let groet = `Hoi ${naam}! Hoe gaat het?`;
```

## 2.1.3 Data type: `Boolean`
Een boolean is een logische waarde die `true` of `false` kan zijn.
```javascript
let isWaar = true;
let isNietWaar = false;
```

## 2.1.4 Data type: `null`
`null` is een speciale waarde die aangeeft dat een variabele bewust leeg of niet toegewezen is.
```javascript
let legeWaarde = null;
console.log(legeWaarde); // null
```

> Let op!
- **Definitie**: `null` is een expliciete waarde die aangeeft dat een variabele leeg of niet toegewezen is
- **Handmatige toewijzing**: Je moet `null` handmatig aan een variabele toewijzen om aan te geven dat deze variabele geen waarde heeft
- **Gebruik**: `null` wordt vaak gebruikt om aan te geven dat een object of waarde later zal worden toegewezen of dat iets opzettelijk is geleegd

## 2.1.5 Data type: `undefined`
`undefined` betekent dat een variabele is gedeclareerd, maar nog geen waarde heeft gekregen.
```javascript
let ongedefinieerdeWaarde;
console.log(ongedefinieerdeWaarde); // undefined
```

> Let op! 
- **Definitie**: `undefined` betekent dat een variabele is gedeclareerd maar nog geen waarde heeft gekregen
- **Automatische toewijzing**: Wanneer je een variabele declareert zonder een waarde toe te wijzen, krijgt deze automatisch de waarde `undefined`
- **Eigenschappen van objecten**: Als je probeert een eigenschap van een object op te vragen die niet bestaat, krijg je `undefined`
- **Functies zonder return**: Een functie zonder expliciete return-waarde geeft `undefined` terug.

## 2.1.6 Data type: `Object`
Een object is een complexe data type die meerdere waarden kan bevatten in de vorm van key-value pairs.

```javascript
let persoon = {
    naam: "John Doe",
    leeftijd: 25,
    isStudent: true
};
```

## 2.1.7 Data type: `Symbol`
Een symbol is een uniek en onveranderlijk primitief waarde, vaak gebruikt als unieke object keys.
```javascript
let symbool = Symbol('beschrijving');
```
## Oefeningen JavaScript data types
Hieronder staan enkele oefeningen betreft de bovenstaande data types.

### 2.2 Oefening data types `number` en `string`
Maak in het codeblock hieronder een variabele `a` die jouw leeftijd opslaat als een number en een variabele `b` die jouw naam opslaat als een string. Log beide variabelen naar de console.

```javascript runner
// Maak de variabelen hier aan

console.log(`Mijn naam is ${b} en ik ben ${a} jaar oud.`);
```

### 2.3 Oefening data types `boolean`
Maak een variabele `isStudent` die aangeeft of je een student bent (true/false). Log de variabele naar de console.

```javascript runner
// Maak de variabele hier aan

console.log(`Ben ik een student? ${isStudent}`);
```

### 2.4 Oefening data types `null` en `undefined`
Maak een variabele `onbekend` die gelijk is aan null. Maak een andere variabele `nietGedefinieerd` zonder deze een waarde te geven. Log beide variabelen naar de console.

```javascript runner
// Maak de variabelen hier aan

console.log(onbekend); // null
console.log(nietGedefinieerd); // undefined
```

### 2.5 Oefening data types `object`
Maak een object `auto` met de properties `merk`, `model`, en `jaar`. Log het object naar de console.

```javascript runner
// Maak het object hier aan

console.log(auto);
```

### 2.6 Oefening data types `symbol`
Maak een symbol `sym` met een beschrijving 'uniekSymbool'. Log het symbool naar de console.

```javascript runner
// Maak het symbool hier aan

console.log(sym);
```
