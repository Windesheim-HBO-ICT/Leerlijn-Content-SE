---
title: JavaScript Classes
tags:
  - JS/Classes
  - page
difficulty: 2
---

# 1. JavaScript Classes
In JavaScript zijn **classes** een manier om objectgeoriënteerd programmeren (OOP) te ondersteunen. Ze bieden een syntactische suiker over de prototype-gebaseerde overerving en maken het eenvoudiger om objecten en hun methoden te definiëren.

## 1.1 JavaScript Classes
Dit hoofdstuk gaat over errors, custom errors, built-in error types en het afhandelen van errors

### Voorbeeld: Class declaratie
Een class wordt gedefinieerd met het `class` keyword en bevat een constructor-functie voor initiële waardes, en methoden die aan alle instanties van de class beschikbaar zijn. Een class kan aangemaakt worden met het `new` keyword.

```javascript
class Persoon {
  constructor(naam, leeftijd) {
    this.naam = naam;
    this.leeftijd = leeftijd;
  }

  begroet() {
    return `Hallo, mijn naam is ${this.naam} en ik ben ${this.leeftijd} jaar oud.`;
  }
}

const persoon1 = new Persoon("Alice", 25);
console.log(persoon1.begroet()); // "Hallo, mijn naam is Alice en ik ben 25 jaar oud."
```

### Voorbeeld: Methods
Classes kunnen methoden bevatten die acties uitvoeren met de eigenschappen van de class.

```javascript
class Vierkant {
  constructor(zijde) {
    this.zijde = zijde;
  }

  oppervlakte() {
    return this.zijde ** 2;
  }
}

let vierkant = new Vierkant(4);
console.log(vierkant.oppervlakte()); // 16
```

### Voorbeeld: Overerving
**Inheritance** stelt je in staat om een class van een andere class te laten erven, wat betekent dat de eigenschappen en methoden van de basisclass beschikbaar zijn in de afgeleide class. Hiervoor wordt het `extends` keyword gebruikt.

```javascript
class Dier {
  constructor(soort) {
    this.soort = soort;
  }

  maakGeluid() {
    return "Geluid";
  }
}

class Hond extends Dier {
  constructor(naam, ras) {
    super("Hond");
    this.naam = naam;
    this.ras = ras;
  }

  maakGeluid() {
    return "Woef!";
  }

  beschrijf() {
    return `${this.naam} is een ${this.ras} en maakt geluid: ${this.maakGeluid()}}`;
  }
}

let mijnHond = new Hond("Max", "Labrador");
console.log(mijnHond.beschrijf()); // "Max is een Labrador en maakt geluid: Woef!"
```

### Voorbeeld: Private properties / methods
Classes kunnen ook private methoden bevatten. Deze worden aangegeven met een `#`-prefix. Deze moet ook gebruikt worden voor het aanroepen van de variabele.

```javascript
class Vierkant {
  #zijde;

  constructor(zijde) {
    this.#zijde = zijde;
  }

  oppervlakte() {
    return this.#zijde ** 2;
  }
}

const vierkant = new Vierkant(4);
console.log(vierkant.oppervlakte()); // 16
```

### Voorbeeld: Getters / Setters
Je kunt getters en setters gebruiken om toegang te bieden tot private velden.

```javascript
class Cirkel {
  #straal;

  constructor(straal) {
    this.#straal = straal;
  }

  get straal() {
    return this.#straal;
  }

  set straal(nieuweStraal) {
    if (nieuweStraal > 0) {
      this.#straal = nieuweStraal;
    } else {
      throw new Error("De straal moet positief zijn.");
    }
  }

  get diameter() {
    return this.#straal * 2;
  }
}

const cirkel = new Cirkel(5);
console.log(cirkel.diameter); // 10
cirkel.straal = 7;
console.log(cirkel.diameter); // 14
```

### Voorbeeld: Static Methoden
**Static** methoden behoren toe aan de class zelf en niet aan een instantie van de class. Je kunt ze aanroepen zonder een object van de class te maken.

```javascript
class Converter {
  static naarGraden(celsius) {
    return celsius * 9 / 5 + 32;
  }

  static naarCelsius(graden) {
    return (graden - 32) * 5 / 9;
  }
}

console.log(Converter.naarGraden(30)); // 86
console.log(Converter.naarCelsius(86)); // 30
```

## Oefeningen
Hieronder enkele oefeningen betreffende classes.

### Oefening 1: Class aanmaken
- Maak een class `Boek` met de eigenschappen `titel`, `auteur`, en `paginas`. 
- Voeg een methode `beschrijf` toe die een string retourneert met de beschrijving van het boek.

```javascript runner
// Maak de class Boek hier

// Test je code hier
const mijnBoek = new Boek("De Kleine Prins", "Antoine de Saint-Exupéry", 96);
console.log(mijnBoek.beschrijf()); // Verwacht: "Het boek 'De Kleine Prins' is geschreven door Antoine en heeft 96 pagina's."
```

### Oefening 2: Overerving
- Maak een basisclass `Persoon` met de eigenschappen `naam` en `leeftijd`, en een methode `beschrijf`.
- Maak een class `Student` die erft van `Persoon` en een extra eigenschap `studie` heeft. 
- Override de methode `beschrijf` in de `Student` class om ook de studie te vermelden.

```javascript runner
// Maak de basisclass Persoon hier

// Maak de class Student die erft van Persoon hier

// Test je code hier
let student1 = new Student("Emma", 22, "Informatica");
console.log(student1.beschrijf()); // Verwacht: "Dit is Emma, 22 jaar oud. Zij/hij studeert Informatica."
```

### Oefening 4: Private properties
- Maak een class `Persoon` met private velden `#naam` en `#leeftijd`. 
- Voeg getters en setters toe voor `naam` en `leeftijd`, waarbij de setter van `leeftijd` controleert of de leeftijd positief is. 
- Voeg een methode `beschrijf` toe die een string retourneert met de beschrijving van de persoon.

```javascript runner
// Maak de class Persoon hier

// Test je code hier
let persoon1 = new Persoon("Alice", 25);
console.log(persoon1.beschrijf()); // Verwacht: "Dit is Alice, 25 jaar oud."
persoon1.leeftijd = 30;
console.log(persoon1.beschrijf()); // Verwacht: "Dit is Alice, 30 jaar oud."
// persoon1.leeftijd = -5; // Verwacht: Error: "Leeftijd moet positief zijn."

```

### Oefening 5: Static methoden
- Maak een class `MathUtils` met een static methode `som` die twee getallen optelt. 
- Voeg een static methode `product` toe die het product van twee getallen retourneert.

```javascript runner
// Maak de class MathUtils hier

// Test je code hier
console.log(MathUtils.som(3, 4)); // Verwacht: 7
console.log(MathUtils.product(3, 4)); // Verwacht: 12

```


