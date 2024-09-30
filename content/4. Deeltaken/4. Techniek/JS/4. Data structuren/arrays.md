---
title: JavaScript arrays
tags:
  - JS/Arrays
  - page
difficulty: 2
---

# 1 JavaScript Arrays
In JavaScript is een array een datatype waarmee je een verzameling van meerdere waarden kunt opslaan. Arrays kunnen elementen van verschillende typen bevatten, zoals getallen, strings, objecten, of zelfs andere arrays.

## 1.1 JavaScript Arrays `basis`
Arrays kunnen worden gedefinieerd met vierkante haken `[]` en kunnen verschillende soorten waarden bevatten.

```javascript
let getallen = [1, 2, 3, 4];
let namen = ["Alice", "Bob", "Charlie"];
let mix = [42, "Hallo", true];
```

Je kunt ook een lege array definiëren en later vullen:

```javascript
let legeArray = [];
```

## 1.2 JavaScript Arrays `methoden`
Hieronder worden enkele array methoden behandeld. Dit zijn echter niet alle methoden die beschikbaar zijn op een array. Voor alle methode kijk dan op de [Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods) documentatie.

### 1.2.1 JavaScript array methoden `push`
Met de `push` methode voeg je een of meer elementen toe aan het einde van een array.

```javascript
const getallen = [1, 2, 3];
getallen.push(4);
console.log(getallen); // [1, 2, 3, 4]
```

### 1.2.2 JavaScript array methoden `pop`
Met de `pop` methode verwijder je het laatste element van een array en retourneer je dit element.

```javascript
const getallen = [1, 2, 3];
const laatsteGetal = getallen.pop();
console.log(laatsteGetal); // 3
console.log(getallen); // [1, 2]
```

### 1.2.3 JavaScript array methoden `shift`
Met de `shift` methode verwijder je het eerste element van een array en retourneer je dit element.

```javascript
const getallen = [1, 2, 3];
const eersteGetal = getallen.shift();
console.log(eersteGetal); // 1
console.log(getallen); // [2, 3]
```

### 1.2.4 JavaScript array methoden `unshift`
Met de `unshift` methode voeg je een of meer elementen toe aan het begin van een array.

```javascript
const getallen = [2, 3];
getallen.unshift(1);
console.log(getallen); // [1, 2, 3]
```

### 1.2.5 JavaScript array methoden `map`
Met de `map` methode maak je een nieuwe array door een functie toe te passen op elk element van de originele array. De originele array blijft ongewijzigd.

```javascript
const getallen = [1, 2, 3];
const verdubbeld = getallen.map(function(getal) {
  return getal * 2;
});
console.log(verdubbeld); // [2, 4, 6]
```

### 1.2.6 JavaScript array methoden `filter`
Met de `filter` methode maak je een nieuwe array door elementen te selecteren die voldoen aan een bepaalde voorwaarde. De originele array blijft ongewijzigd.

```javascript
const getallen = [1, 2, 3, 4];
const evenGetallen = getallen.filter(function(getal) {
  return getal % 2 === 0;
});
console.log(evenGetallen); // [2, 4]
```

### 1.2.7 JavaScript array methoden `reduce`
Met de `reduce` methode kun je de elementen van een array reduceren tot een enkele waarde door een functie toe te passen die telkens twee elementen combineert. Dit kan bijvoorbeeld gebruikt worden om de som of het product van alle elementen te berekenen.

```javascript
const getallen = [1, 2, 3, 4];
const som = getallen.reduce(function(totaal, getal) {
  return totaal + getal;
}, 0);
console.log(som); // 10
```

### 1.2.8 JavaScript array methoden tips
In het hoofdstuk over functions hebben we anonymous en arrow-functions besproken. Deze kunnen ook gebruikt worden met array methode. Zie hieronder een voorbeeld met dit soort functies in combinatie met array methoden map, filter en reduce.

**Voorbeeld**

```javascript
const getallen = [1, 2, 3, 4];
const verdubbeld = getallen.map(function(getal) {
  return getal * 2;
});

const evenGetallen = getallen.filter(function(getal) {
  return getal % 2 === 0;
});

const som = getallen.reduce(function(totaal, getal) {
  return totaal + getal;
}, 0);

console.log(verdubbeld); // [2, 4, 6, 8]
console.log(evenGetallen); // [2, 4]
console.log(som); // 10
```

Dit kan herschreven worden naar:

```javascript
const getallen = [1, 2, 3, 4];
const verdubbeld = getallen.map(getal => getal * 2);

const evenGetallen = getallen.filter(getal => getal % 2 === 0);

const som = getallen.reduce((totaal, getal) => totaal + getal, 0);

console.log(verdubbeld); // [2, 4, 6, 8]
console.log(evenGetallen); // [2, 4]
console.log(som); // 10
```


## 1.3 Oefening JavaScript arrays
Hieronder staan enkele oefeningen met array maken en enkele methoden.

### 1.3.1 Oefening JavaScript Array
Maak een array `dagen` met de dagen van de week en print deze naar de console.

```javascript runner

console.log(dagen)
```

### 1.3.2 Oefening JavaScript Array methode `push` 
Voeg drie films toe aan de `favorieteFilms` array met behulp van de `push` methode.

```javascript runner
const favorieteFilms = ["Inception", "The Matrix", "Interstellar"];

// Voeg films toe

console.log(favorieteFilms);
```

### 1.3.3 Oefening JavaScript Array methode `pop`
Verwijder het laatste element uit de array `favorieteFilms` en print de verwijderde film en de bijgewerkte array.

```javascript runner
const favorieteFilms = ["Inception", "The Matrix", "Interstellar"];

// Verwijder de laatste film


console.log(verwijderdeFilm); // "Interstellar"
console.log(favorieteFilms); // ["Inception", "The Matrix"]
```
### 1.3.4 Oefening JavaScript Array methode `shift`
Verwijder het eerste element uit de array `favorieteFilms` en print de verwijderde film en de bijgewerkte array.

```javascript runner
const favorieteFilms = ["Inception", "The Matrix", "Interstellar"];

// Verwijder de eerste film

console.log(verwijderdeFilm); // "Inception"
console.log(favorieteFilms); // ["The Matrix", "Interstellar"]

```
### 1.3.5 Oefening JavaScript Array methode `unshift`
Voeg een nieuwe film toe aan het **begin** van de array `favorieteFilms` en print de bijgewerkte array.

```javascript runner
const favorieteFilms = ["The Matrix", "Interstellar"];

// Voeg een film toe aan het begin

// Print de array
console.log(favorieteFilms); // ["Blade Runner", "The Matrix", "Interstellar"]

```
### 1.3.6 Oefening JavaScript Array methode `map`
Gebruik de `map` methode om een array `nummers` te delen en print de nieuwe array.

```javascript runner
const nummers = [2, 7, 4, 6, 8, 9, 11];

// Deel de nummers


// Print de nieuwe array
console.log(gedeeeld); // [1, 3.5, 2, 3, 4, 4.5, 5.5]
```

### 1.3.7 Oefening JavaScript Array methode `filter`
Gebruik de `filter` methode om een array `nummers` te filteren zodat alleen oneven getallen overblijven en print de nieuwe array.


```javascript runner
const nummers = [2, 7, 4, 6, 8, 9, 11];

// filter de nummers

// Print de nieuwe array
console.log(oneven); // [7, 9, 11]
```
### 1.3.8 Oefening JavaScript Array methode `reduce`
Gebruik de `reduce` methode om de som van de getallen in de array `nummers` te berekenen en print de som.

```javascript runner
const nummers = [2, 7, 4, 6, 8, 9, 11];

// bereken de som

// Print de som
console.log(som); // 47
```