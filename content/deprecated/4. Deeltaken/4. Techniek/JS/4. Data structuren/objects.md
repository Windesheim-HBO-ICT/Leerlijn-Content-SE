---
title: JavaScript objecten
tags:
  - JS/objecten
  - page
difficulty: 2
---

# 1 JavaScript objecten
In JavaScript is een object een complexe datatype waarmee je gegevens in de vorm van key-value paren kunt opslaan. Een object kan verschillende soorten waarden bevatten, zoals strings, getallen, functies, arrays, en zelfs andere objecten.

## 1.1 JavaScript Objects `basis`
Objecten worden gedefinieerd met accolades `{}` en bevatten een set key-value paren.

```javascript
const persoon = {
    naam: "John",
    leeftijd: 30,
    beroep: "Developer"
}
```

### 1.1.1 JavaScript Objects `toegang`
Je kunt toegang krijgen tot de waarden in een object door gebruik te maken van puntnotatie `.` of vierkante haken `[]`.

```javascript
const persoon = {
    naam: "John",
    leeftijd: 30,
    beroep: "Developer"
}

console.log(persoon.naam); // "John"
console.log(persoon["leeftijd"]); // 30
```

### 1.1.1 JavaScript Objects `toevoegen`, `bijwerken` en `verwijderen`
Je kunt properties toevoegen aan een bestaand object of de waarde van een bestaande property bijwerken.

```javascript
const auto = {
  merk: "Tesla",
  model: "Model S"
};

// Toevoegen van een property
auto.kleur = "rood";
console.log(auto); // { merk: "Tesla", model: "Model S", kleur: "rood" }

// Bijwerken van een property
auto.model = "Model X";
console.log(auto); // { merk: "Tesla", model: "Model X", kleur: "rood" }

// Verwijderen van een property
deconste auto.kleur;
console.log(auto); // { merk: "Tesla", model: "Model X" }
```

### 1.1.2 JavaScript Objects `methods`
Methoden zijn functies die als eigenschappen in een object worden opgeslagen. Ze kunnen worden aangeroepen met de puntnotatie.

```javascript
const calculator = {
    optellen: function(a, b) {
        return a + b;
    }
};

console.log(calculator.optellen(5, 3)); // 8

// ES6 syntax

const rekenmachine = {
    optellen(a, b) {
        return a + b;
    }
};

console.log(rekenmachine.optellen(5, 5)); // 10
```

### 1.1.3 Javascript Objects `this` keyword
Binnen methoden kun je het `this` keyword gebruiken om toegang te krijgen tot andere eigenschappen van hetzelfde object.

```javascript
const persoon = {
    naam: "Bob",
    groeten() {
        console.log(`Hallo, mijn naam is ${this.naam}`);
    }
};

persoon.groeten()
```

### 1.1.4 Javascript Objects `destructuring`
Destructuring is een syntax waarmee je properties kunt uitpakken in afzonderlijke variabelen. Dit kan via de `{}`-notatie.

```javascript
const gebruiker = {
    naam: "Student",
    leeftijd: 25,
    email: "student@windesheim.com"
};

const { naam, leeftijd, email } = gebruiker;
console.log(naam); // "Student"
console.log(leeftijd); // 25
console.log(email); // "student@windesheim.com"
```

Tijdens het destructuring kan je ook default waarden toewijzen.

```javascript
const gebruiker = {
    naam: "Student",
    leeftijd: 25,
    email: "student@windesheim.com"
};

const { naam, leeftijd = 15, email, hobby = "voetbal" } = gebruiker;
console.log(naam); // "Student"
console.log(leeftijd); // 25
console.log(email); // "student@windesheim.com"
console.log(hobby); // "voetbal"
```

### 1.1.4 Javascript Objects `for...in` loop
De `for...in`-loop is een eenvoudige manier om over de eigenschappen van een object te itereren. Deze loop geeft de keys van het object terug.

```javascript
const auto = {
    merk: "Ford",
    model: "Mustang",
    bouwjaar: 1969
};

for (const eigenschap in auto) {
    console.log(`${eigenschap}: ${auto[eigenschap]}`);
}
```

## 2.1 JavaScript Objects oefening
Hieronder enkele opdrachten met JavaScript objecten.

### 2.1.1 JavaScript Objects oefening `basis`
Maak een object `boek` met de eigenschappen `titel`, `auteur`, en `jaar`.

```javascript runner
// Maak het object

console.log(boek);
```

### 2.1.1 JavaScript Objects oefening `toevoegen` en `bewerken`
Voeg de eigenschap `genre` toe aan het object `boek` en update de `jaar` eigenschap.

```javascript runner
// Kopieer hier het object van hierboven

// Voeg genre toe en update jaar naar 2024


console.log(boek);
```

### 2.1.1 JavaScript Objects oefening `methods` en `this`
Voeg een methode `beschrijving` toe aan het object `boek` die de beschrijving van het boek retourneert.

```javascript runner
// Kopieer hier het object van hierboven


console.log(boek); // Output: *titel* is geschreven door *auteur* in het jaar *jaar*.
```

### 2.1.1 JavaScript Objects oefening `destructuring`
Gebruik destructuring om de eigenschappen `titel` en `auteur` van het object `boek` te verkrijgen en print ze.

```javascript runner
const boek = {
    titel: "De Hobbit",
    auteur: "J.R.R. Tolkien",
    jaar: 1951
};

// Destructureer de eigenschappen

// Print de eigenschappen
console.log(titel); // "De Hobbit"
console.log(auteur); // "J.R.R. Tolkien"
```

### 2.1.1 JavaScript Objects oefening `loop`
Gebruik een `for...in` loop om over de eigenschappen van het object `land` te itereren en print zowel de keys als de waarden.

```javascript runner
const land = {
    naam: "Nederland",
    hoofdstad: "Amsterdam",
    bevolking: 17000000
};

// Gebruik de for...in loop

// Output:
// naam: Nederland
// hoofdstad: Amsterdam
// bevolking: 17000000
```