---
title: 1. Basis JavaScript syntax
tags:
  - JS/Variablen
  - page
difficulty: 2
---

# 1. JavaScript variablen
In JavaScript worden de keywords `var`, `let`, of `const` gebruikt om variabelen te declareren. Een variabele is iets wat een waarde kan opslaan, zoals een **number**, een **string**, etc.

# Javascript variabelen met `var`

```javascript
var naam = "John Doe";
var leeftijd = 25;
var isStudent = true;
```

## Kenmerken
1. **Functie scoped** Een variabele gedeclareerd met var is function-scoped. Dit betekent dat als een variabele binnen een functie wordt gedeclareerd, deze alleen binnen die functie beschikbaar is.

```javascript
function functieNaam() {
  var lokaal = "T5.32";
  console.log(lokaal); // Dit werkt
}
console.log(lokaal); // Dit geeft een foutmelding
```

2. **Hoisting** Variabelen gedeclareerd met var worden 'gehoist', wat betekent dat de declaratie naar de top van hun scope wordt verplaatst, maar niet de toewijzing.

```javascript
console.log(naam); // undefined
var naam = "Ernst";
console.log(naam); // "Ernst"
```

In dit voorbeeld wordt de declaratie var naam; naar boven verplaatst (gehoist), maar de waarde wordt pas toegewezen wanneer de toewijzing `naam = "Ernst` wordt uitgevoerd. Wat er eigenlijk staat:

```javascript
var naam;
console.log(naam); // undefined
var naam = "John Doe";
console.log(naam); // "Ernst"
```

3. **Globale scope**
Als var buiten een functie wordt gedeclareerd, is het een globale variabele en dus beschikbaar in het hele script.
```javascript
var globaal = "Ik ben een globale variable";

function functieNaam() {
  console.log(globaal); // "Ik ben een globale variable"
}

functieNaam();
console.log(globaal); // "Ik ben een globale variable"
```

## Beperkingen
Hoewel var lang de standaard was voor het declareren van variabelen, heeft het enkele beperkingen die het gebruik van `let` en `const` hebben gestimuleerd:
- Scoping problemen: Omdat `var` function-scoped is en niet block-scoped (zoals binnen een if-statement of for-loop), kan dit leiden tot onvoorziene fouten en moeilijkheden bij het debuggen. Voorbeeld:

```javascript
if (true) {
  var blockScoped = "Hey! Ik ben hierbuiten ook beschikbaar";
}
console.log(blockScoped); 
```
- Hoisting verwarring: Hoisting kan soms leiden tot verwarring en bugs, omdat variabelen beschikbaar zijn voordat ze gedeclareerd lijken te zijn.


# Javascript variabelen met `let`

```javascript
let naam = "John Doe";
let leeftijd = 25;
let isStudent = true;
```

## Kenmerken
1. **Block Scope** Een van de belangrijkste voordelen van `let` is dat het block-scoped is. Dit betekent dat een variabele gedeclareerd met `let` alleen toegankelijk is binnen het blok waarin het is gedeclareerd.

```javascript
if (true) {
  let locatie = "Brug T5";
  console.log(locatie); // Dit werkt
}
console.log(locatie); // Dit geeft een foutmelding
```

2. **Geen Hoisting zoals bij `var`** Hoewel let ook gehoist wordt, is het niet op dezelfde manier als var. Variabelen gedeclareerd met let zijn niet toegankelijk voordat de declaratie wordt uitgevoerd, wat leidt tot een ReferenceError als je probeert om de variabele te gebruiken voordat deze gedeclareerd is.

```javascript
console.log(naam); // Uncaught ReferenceError: naam is not defined
let naam = "John Doe";
console.log(naam);
```

3. **Geen herhaalde declaratie binnen dezelfde scope** Met `let` kun je een variabele niet meer dan eens binnen dezelfde scope declareren, wat helpt om fouten te vermijden.

```javascript
let leeftijd = 25;
let leeftijd = 30; // SyntaxError: Identifier 'leeftijd' has already been declared
```

# Javascript variabelen met `const`

```javascript
const naam = "John Doe";
const leeftijd = 25;
const isStudent = true;
```

## Kenmerken
1. **Block Scope**: Net als `let` is een variabele gedeclareerd met `const` block-scoped. Dit betekent dat de variabele alleen toegankelijk is binnen het blok waarin het is gedeclareerd.

```javascript
if (true) {
  const locatie = "Brug T5";
  console.log(locatie); // Dit werkt
}
console.log(locatie); // Dit geeft een foutmelding
```

2. **Constante Binding**: De waarde van een `const` variabele kan niet opnieuw worden toegewezen. Dit betekent dat zodra je een waarde aan een `const` hebt toegewezen, je deze niet meer kunt veranderen.

```javascript
const leeftijd = 25;
leeftijd = 30; // TypeError: Assignment to constant variable.
```

3. **Initieel Verplicht**: Je moet een `const` variabele gelijk een waarde geven op het moment dat je deze declareert. Het achterwege laten van een initiële waarde leidt tot een fout.

```javascript
const naam; // SyntaxError: Missing initializer in const declaration
```


# 1.1 Oefening JavaScript variablen - var
Maak in de codeblock hieronder 2 variabelen met `var`: naam en leeftijd. Zorg ervoor dat de jouw naam en leeftijd geeft.

```javascript runner

console.log(`Ik ben ${naam} en ben ${leeftijd} jaar oud.`)
```

# 1.2 Oefening JavaScript variablen - let
Maak in het codeblock hieronder 1 variabele met `let`. Bij de initialisatie van de variabele moet dit jouw naam worden. Wijs vervolgens jouw leeftijd toe aan dezelfde variabele. De output zou beiden jouw naam en leeftijd moeten geven met het gebruik van 1 variabele.

```javascript runner
// Maak de variabele hier aan
console.log(`Ik ben ${dynamischeVariable}`)
// Geef hier de variabele een andere value.
console.log(`Ik ben ${dynamischeVariable} jaar oud`)
```

# 1.3 Oefening JavaScript variablen - const
Maak in het codeblock hieronder 2 variabelen. Beiden met de naam `naam`. Zorg ervoor dat de output twee keer jouw naam geeft.

```javascript runner

function zegMijnNaam(){

  console.log(`Mijn naam is ${naam}`)
}

zegMijnNaam()

console.log(`Mijn naam is ${naam}`)
```