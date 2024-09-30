---
title: Basis JavaScript syntax
tags:
  - JS/Destructuring
  - page
difficulty: 2
---

# 1. JavaScript Destructuring
**Destructuring assignments** in JavaScript laten je toe om elementen uit arrays of eigenschappen uit objecten eenvoudig toe te wijzen aan variabelen. De **rest** en **spread** operators zijn aanvullingen hierop die werken met de rest van de elementen of eigenschappen.

## 1.1 JavaScript Destructuring `arrays`
Dit hoofdstuk gaat specifiek over het destructuren van `arrays`. Hier worden voorbeelden gegeven.

### Voorbeeld: Basis Array Destructuring
```javascript
const cijfers = [10, 20, 30];

const [eerste, tweede, derde] = cijfers;

console.log(eerste); // 10
console.log(tweede); // 20
console.log(derde);  // 30

```

### Overslaan van Elementen
```javascript
const cijfers = [10, 20, 30];

const [eerste, , derde] = cijfers;

console.log(eerste); // 10
console.log(derde);  // 30

```

### Default Waarden
```javascript
const cijfers = [10];

const [eerste, tweede = 50] = cijfers;

console.log(eerste); // 10
console.log(tweede); // 50

```

### Rest Syntax
```javascript
const cijfers = [10, 20, 30, 40, 50];

const [eerste, ...rest] = cijfers;

console.log(eerste); // 10
console.log(rest);   // [20, 30, 40, 50]
```

### Spread Operator
De **spread** operator `...` kan worden gebruikt om elementen uit een array te verspreiden in een nieuwe array of als argumenten in een functie.

```javascript
const cijfers1 = [1, 2, 3];
const cijfers2 = [4, 5, 6];

const gecombineerd = [...cijfers1, ...cijfers2];

console.log(combineerd); // [1, 2, 3, 4, 5, 6]
```

### Functie Argumenten met Spread
```javascript
function som(a, b, c) {
  return a + b + c;
}

const cijfers = [10, 20, 30];

console.log(som(...cijfers)); // 60
```

## 1.2 JavaScript Destructuring `objects`
Dit hoofdstuk gaat specifiek over het destructuren van `objects`. Hier worden voorbeelden gegeven.

### Basis Object Destructuring
```javascript
const persoon = {
  naam: "Alice",
  leeftijd: 30,
  stad: "Amsterdam"
};

const { naam, leeftijd, stad } = persoon;

console.log(naam);     // "Alice"
console.log(leeftijd); // 30
console.log(stad);     // "Amsterdam"
```

### Destructuring met Aliassen
```javascript
const persoon = {
  naam: "Alice",
  leeftijd: 30,
  stad: "Amsterdam"
};

const { naam: voornaam, leeftijd: jaren, stad: woonplaats } = persoon;

console.log(voornaam);  // "Alice"
console.log(jaren);     // 30
console.log(woonplaats);// "Amsterdam"
```

### Default Waarden
```javascript
const persoon = {
  naam: "Alice"
};

const { naam, leeftijd = 25 } = persoon;

console.log(naam);     // "Alice"
console.log(leeftijd); // 25
```

### Rest Syntax
```javascript
const persoon = {
  naam: "Alice",
  leeftijd: 30,
  stad: "Amsterdam"
};

const { naam, ...rest } = persoon;

console.log(naam); // "Alice"
console.log(rest); // { leeftijd: 30, stad: "Amsterdam" }

```

### Spread Operator
De **spread** operator kan worden gebruikt om de eigenschappen van een object te verspreiden in een nieuw object.

```javascript
const adres = {
  stad: "Amsterdam",
  postcode: "1011 AB"
};

const persoon = {
  naam: "Alice",
  ...adres
};

console.log(persoon); // { naam: "Alice", stad: "Amsterdam", postcode: "1011 AB" }
```





## 1.3 JavaScript Nested Destructuring

### Nested Array Destructuring
```javascript
const cijfers = [10, [20, 30], 40];

const [eerste, [tweede, derde]] = cijfers;

console.log(eerste); // 10
console.log(tweede); // 20
console.log(derde);  // 30
```

### Nested Object Destructuring
```javascript
const persoon = {
  naam: "Alice",
  adres: {
    stad: "Amsterdam",
    postcode: "1011 AB"
  }
};

const { naam, adres: { stad, postcode } } = persoon;

console.log(naam);     // "Alice"
console.log(stad);     // "Amsterdam"
console.log(postcode); // "1011 AB"
```

## 1.4 JavaScript Parameters Destructuring

### Array Parameters
```javascript
function toonEersteTwee([eerste, tweede]) {
  console.log(eerste);
  console.log(tweede);
}

toonEersteTwee([10, 20, 30]); // 10, 20
```

### Object Parameters
```javascript
function toonPersoon({ naam, leeftijd }) {
  console.log(`Naam: ${naam}`);
  console.log(`Leeftijd: ${leeftijd}`);
}

const persoon = {
  naam: "Alice",
  leeftijd: 30
}

toonPersoon(persoon); // "Naam: Alice", "Leeftijd: 30"
```

## 2 Oefeningen
Hieronder enkele oefeningen betreffende destructuring.

### Oefening 1: Basis Array Destructuring
Destructureer de eerste twee elementen van de array `cijfers` in de variabelen `eerste` en `tweede`.

```javascript runner
let cijfers = [5, 10, 15, 20, 25];

// Destructureer hier

console.log(eerste); // Verwacht: 5
console.log(tweede); // Verwacht: 10
```

### Oefening 2: Default Waarden bij Objecten
Destructureer de eigenschappen `naam` en `leeftijd` van het object `persoon`, waarbij `leeftijd` een standaardwaarde van 18 krijgt als deze niet aanwezig is.

```javascript runner
let persoon = {
  naam: "Bob"
};

// Destructureer hier

console.log(naam);     // Verwacht: "Bob"
console.log(leeftijd); // Verwacht: 18
```

### Oefening 3: Rest Syntax bij Objecten
Destructureer de eigenschap `naam` en plaats de overige eigenschappen in een variabele `rest`.

```javascript runner
let persoon = {
  naam: "Charlie",
  leeftijd: 40,
  stad: "Rotterdam"
};

// Destructureer hier

console.log(naam); // Verwacht: "Charlie"
console.log(rest); // Verwacht: { leeftijd: 40, stad: "Rotterdam" }

```

### Oefening 4: Nested Object Destructuring
Destructureer de eigenschappen `stad` en `postcode` uit het geneste object `adres` van het object `persoon`. javascript

```javascript runner
let persoon = {
  naam: "David",
  adres: {
    stad: "Utrecht",
    postcode: "3521 BC"
  }
};

// Destructureer hier

console.log(stad);     // Verwacht: "Utrecht"
console.log(postcode); // Verwacht: "3521 BC"
```

### Oefening 5: Functie Parameters Destructuring
Schrijf een functie `toonAdres` die een object met de naam `adres` met de eigenschappen `straat` en `nummer` accepteert, en deze waarden logt. Gebruik destructuring in de functie parameter.

```javascript runner
function toonAdres({ straat, nummer }) {
  console.log(`Straat: ${straat}`);
  console.log(`Nummer: ${nummer}`);
}

// Test de functie
toonAdres(adres);
// Verwacht: "Straat: Hoofdstraat", "Nummer: 123"

```

### Oefening 6: Spread Operator met Arrays
Maak een nieuwe array `cijfersCombineerd` door `cijfers1` en `cijfers2` samen te voegen met de spread operator.

```javascript runner
let cijfers1 = [1, 2, 3];
let cijfers2 = [4, 5, 6];

// Voeg samen hier

console.log(cijfersCombineerd); // Verwacht: [1, 2, 3, 4, 5, 6]
```

### Oefening 7: Spread Operator met Objecten
Maak een nieuw object `persoonVolledig` door `persoon` en `adres` samen te voegen met de spread operator.

```javascript runner
let persoon = {
  naam: "Emma",
  leeftijd: 22
};

let adres = {
  stad: "Den Haag",
  postcode: "2511 AA"
};

// Voeg samen hier

console.log(persoonVolledig); // Verwacht: { naam: "Emma", leeftijd: 22, stad: "Den Haag", postcode: "2511 AA" }
```