---
title: 2. Javascript functions
tags:
  - JS/functions
  - page
difficulty: 2
---

# 1. JavaScript functions
Functies in JavaScript zijn blokken code die kunnen worden hergebruikt. Ze nemen input (parameters), voeren bepaalde bewerkingen uit, en geven output (return waarde) terug. Er zijn verschillende manieren om functies te definiëren in JavaScript: functiedeclaraties en functie-expressies.

In JavaScript kennen we enkele verschillende typen functies. Dit zijn:
- Function declaration;
- Function expression;
- Arrow functions;
- Anonymous functions;
- Async functions;
- Generator functions;
- Constructor functions;
- Immediately Invoked Functions Expression (IIFE)

In deze deeltaak worden de functiedeclaraties (function declaration), functie-expressies (function expression), pijlfuncties (arrow functions) en anonieme functies (anonymous functions) behandeld.

## 1.1.1 JavaScript functions: `functiedeclaraties`
Een functiedeclaratie (function declaration) definieert een functie met het trefwoord `function`, gevolgd door de naam van de functie, de parameters tussen haakjes en de functionele code tussen accolades. Deze functies worden 'gehoist', wat betekent dat ze overal in hun scope beschikbaar zijn, zelfs voordat ze zijn gedeclareerd.

```javascript
function groet() {
  console.log("Hallo vanuit de 'groet' functie!")
}

groet()
```

## 1.1.2 JavaScript functions: `functie-expressies`
Een functie-expressie (function expression) definieert een functie als een deel van een expressie. Deze functies worden niet 'gehoist', wat betekent dat ze pas kunnen worden gebruikt nadat ze zijn gedefinieerd.

```javascript
const groet = function() {
  console.log("Hallo vanuit de 'groet' functie!")
}

groet()
```

## 1.1.3 JavaScript functions: `pijl -en anoniemene functies`
Een moderne manier om functies te definiëren is met pijlfuncties (arrow functions). Deze functies zijn altijd anoniem en hebben een kortere syntax. Zie in het voorbeeld hieronder dat er alleen gebruik word gemaakt van de ronde `()`-haakjes en daar een pijl naast staat. Vandaar de naam: anoniem -en pijlfuncties, omdat er geen naam is en een pijl.

```javascript
const groet = () => {
  console.log("Hallo vanuit de 'groet' functie!")
}

groet()
```

## 1.1.4 JavaScript functions: `parameters en return`
Parameters zijn variabelen die je aan een functie kunt doorgeven om de functie van input te voorzien. Je definieert ze tussen de haakjes in de functiedeclaratie of functie-expressie.

```javascript
function optellen(a, b) {
  return a + b;
}

console.log(optellen(2, 3));
```

In dit voorbeeld zijn `a` en `b` de parameters van de functie `optellen`. 

Een functie kan een waarde teruggeven met behulp van het return-trefwoord. Deze waarde kan worden opgeslagen in een variabele of direct worden gebruikt.

```javascript
function vermenigvuldig(a, b) {
  return a * b;
}

let resultaat = vermenigvuldig(4, 5);
console.log(resultaat);
```

In dit voorbeeld retourneert de functie `vermenigvuldig` het product van `a` en `b`, en deze waarde wordt opgeslagen in de variabele `resultaat`.


## 1.2 Oefeningen JavaScript functions
Hieronder enkele oefeningen betreffende JavaScript functions

## 1.2.1 Oefening JavaScript functions `functiedeclaratie`
Schrijf een functiedeclaratie `groet` die twee parameters inneemt: naam en leeftijd. Zorg dat deze functie een template literal returned waardoor de output "Ik ben **naam** en **leeftijd** jaar oud. Als je bent vergeten hoe dit moet, kijk dan ik basis/data-types onder het string data type.

```javascript runner
// Schrijf hier jouw functie

console.log(groet("Jouw naam", 20))
```

## 1.2.2 Oefening JavaScript functions `functie-expressie`
Schrijf een functie-expressie `deel` die twee getallen neemt en hun quotiënt teruggeeft. De output zou `4` moeten zijn.

```javascript runner
// Schrijf hier jouw functie

console.log(deel(20, 5))
```

## 1.2.3 Oefening JavaScript functions `anonieme -en pijlfuncties`
Schrijf een pijlfunctie `kwadraat` die een getal neemt en het kwadraat van dat getal teruggeeft. De output zou `25` moeten zijn.

```javascript runner
// Schrijf hier jouw functie

console.log(kwadraat(5)); // 25
```
