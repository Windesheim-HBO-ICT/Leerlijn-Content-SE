---
title: 2. JavaScript scope en closures
tags:
  - JS/scope-closures
  - page
difficulty: 2
---

# 1 JavaScript scope en closures
In JavaScript is de scope de context waarin variabelen, functies, en objecten toegankelijk zijn. Een closure is een functie die toegang heeft tot de scope van een buitenliggende functie, zelfs nadat die buitenliggende functie is uitgevoerd. Deze concepten zijn essentieel om te begrijpen hoe variabelen werken en worden gebruikt in JavaScript.

## 1.1 Scope: `global`
Variabelen die buiten elke functie of blok zijn gedeclareerd, bevinden zich in de globale scope. Ze zijn toegankelijk vanuit elk deel van het bestand.

```javascript
const globaleVariabele = "Ik ben globaal!";

function toonGlobaal() {
  console.log(globaleVariabele); // Toegang tot de globale variabele
}

toonGlobaal(); // "Ik ben globaal!"
console.log(globaleVariabele); // "Ik ben globaal!"
```

## 1.1.1 Scope: `function`
Variabelen gedeclareerd binnen een functie zijn alleen toegankelijk binnen die functie. Dit wordt function scope genoemd.

```javascript
function toonLokaal() {
  let lokaleVariabele = "Ik ben lokaal!";
  console.log(lokaleVariabele); // Toegang tot de lokale variabele
}

toonLokaal(); // "Ik ben lokaal!"
console.log(lokaleVariabele); // ReferenceError: lokaleVariabele is not defined
```

## 1.1.1 Scope: `block`
Variabelen gedeclareerd met `let` of `const` binnen een blok (bijvoorbeeld binnen een `if`-statement of een `for`-loop) zijn alleen toegankelijk binnen dat blok. Dit wordt block scope genoemd.

```javascript
if (true) {
  let blockVariabele = "Ik ben in een blok!";
  console.log(blockVariabele); // Toegang tot de block-variabele
}

console.log(blockVariabele); // ReferenceError: blockVariabele is not defined
```

## 1.2 Closures
Een closure ontstaat wanneer een functie toegang heeft tot de scope van een buitenliggende functie, zelfs nadat die buitenliggende functie is voltooid. Dit stelt de functie in staat om "privé" variabelen en parameters te onthouden en ermee te werken.

```javascript
function buiten() {
  let binnenVariabele = "Ik ben binnen!";
  
  function binnen() {
    console.log(binnenVariabele); // Toegang tot binnenVariabele van buiten
  }
  
  return binnen;
}

let mijnClosure = buiten();
mijnClosure(); // "Ik ben binnen!"
```
**Uitleg**
- De functie `buiten` declareert een lokale variabele `binnenVariabele` en retourneert een functie `binnen`.
- De functie `binnen` is een closure die toegang heeft tot de variabele `binnenVariabele` van de buitenliggende functie `buiten`, zelfs nadat `buiten` is voltooid.
- Wanneer `mijnClosure` wordt aangeroepen, heeft het nog steeds toegang tot `binnenVariabele`.

## 1.2.1 Closures: praktisch gebruik
Closures worden vaak gebruikt voor het maken van functies die 'privégegevens' onthouden, zoals functions die waarde bijhouden.

```javascript
function teller() {
  let count = 0;
  
  return function() {
    count++;
    return count;
  };
}

let mijnTeller = teller();
console.log(mijnTeller()); // 1
console.log(mijnTeller()); // 2
console.log(mijnTeller()); // 3
```

**Uitleg**
- De functie `teller` retourneert een functie die de waarde van `count` met 1 verhoogt en deze teruggeeft.
- De variabele `count` blijft bewaard in de closure, waardoor elke aanroep van `mijnTeller` de waarde van `count` verhoogt en onthoudt.

# 2 Oefeningen JavaScript scope en closures
Hieronder staan enkele oefeningen betreffende scope en closures.

## 2.1 Oefening JavaScript scope `global`
Maak een globale variabele `basis` en een functie `vermenigvuldig` die deze variabele met een argument vermenigvuldigt en het resultaat teruggeeft.

```javascript runner

console.log(vermenigvuldig(2)); // 10
console.log(vermenigvuldig(4)); // 20
```

## 2.2 Oefening JavaScript scope `function`
Schrijf een functie `grootsteVanTwee` die twee getallen neemt en het grootste getal teruggeeft. Gebruik lokale variabelen binnen de functie.


```javascript runner

console.log(grootsteVanTwee(3, 7)); // 7
console.log(grootsteVanTwee(10, 5)); // 10
```

## 2.3 Oefening JavaScript scope `block`
Schrijf een functie `isEven` die een getal neemt en `true` teruggeeft als het even is, anders `false`. Gebruik een variabele met block scope om de status bij te houden.


```javascript runner

console.log(isEven(4)); // true
console.log(isEven(7)); // false
```


## 2.4 Oefening JavaScript closures
Schrijf een functie `maakVermenigvuldiger` die een getal (`factor`) accepteert en een functie retourneert die een ander getal met deze `factor` vermenigvuldigt.

```javascript runner

const vermenigvuldigerMet5 = maakVermenigvuldiger(5);
console.log(vermenigvuldigerMet5(3)); // 15
console.log(vermenigvuldigerMet5(4)); // 20

const vermenigvuldigerMet10 = maakVermenigvuldiger(10);
console.log(vermenigvuldigerMet10(2)); // 20
console.log(vermenigvuldigerMet10(3)); // 30
```
