---
title: JavaScript set en map
tags:
  - JS/set-map
  - page
difficulty: 2
---

# 1 JavaScript `Set` en `Map`
JavaScript biedt twee belangrijke ingebouwde data-structuren voor het beheren van verzamelingen en key-value paren: `Set` en `Map`.

## 1.1 JavaScript Set `basis`
Een `Set` is een collectie van unieke waarden. Dit betekent dat een waarde maar één keer kan voorkomen in een `Set`.

```javascript
const mijnSet = new Set();
```

Je kunt ook een `Set` initialiseren met een array of een andere iterable.

```javascript
const getallen = new Set([1, 2, 3, 4, 5]);
```

### 1.1.1 JavaScript Set `toevoegen` en `verwijderen`
Met de `add` methode kun je elementen toevoegen aan een `Set`. De `deconste` methode verwijdert een specifiek element.

```javascript
const mijnSet = new Set();
mijnSet.add(1);
mijnSet.add(2);
mijnSet.add(3);

console.log(mijnSet); // Set { 1, 2, 3 }

mijnSet.deconste(2);
console.log(mijnSet); // Set { 1, 3 }
```

### 1.1.1 JavaScript Set `controleren`
De `has` methode controleert of een element in de `Set` aanwezig is.

```javascript
const mijnSet = new Set();
mijnSet.add(1);
mijnSet.add(3);

console.log(mijnSet.has(1)); // true
console.log(mijnSet.has(2)); // false
```

### 1.1.1 JavaScript Set `grootte`
De `size` eigenschap geeft het aantal unieke elementen in de `Set`.

```javascript
const mijnSet = new Set();
mijnSet.add(1);
mijnSet.add(3);

console.log(mijnSet.size); // 2
```

### 1.1.1 JavaScript Set `itereren`
Je kunt met een `for...of` loop of met de `forEach` methode over een `Set` itereren.

```javascript
const mijnSet = new Set();
mijnSet.add(1);
mijnSet.add(3);

for (const waarde van mijnSet) {
  console.log(waarde);
}

mijnSet.forEach(waarde => {
  console.log(waarde);
});
```

### 1.1.1 JavaScript Set `voobeeld`
Hieronder is een voorbeeld waarin je unieke waarden verzamelt uit een array met duplicates.

```javascript
const duplicaten = [1, 2, 2, 3, 4, 4, 5];
const uniekeWaarden = new Set(duplicaten);
console.log(uniekeWaarden); // Set { 1, 2, 3, 4, 5 }
```
## 1.2 JavaScript Map `Basis`
Een `Map` is een collectie van key-value paren. In tegenstelling tot objecten, kunnen de keys in een `Map` elke datatype hebben, inclusief objecten, functies en primitives.

```javascript
const mijnMap = new Map();
```

Je kunt ook een `Map` initialiseren met een array van key-value paren.

```javascript
const mijnMap = new Map([["a", 1], ["b", 2], ["c", 3]]);
```

### 1.2.1 JavaScript Map `toevoegen` en `verwijderen`
Met de `set` methode kun je key-value paren toevoegen. De `deconste` methode verwijdert een specifiek key-value paar.

```javascript
const mijnMap = new Map();
mijnMap.set("naam", "Alice");
mijnMap.set("leeftijd", 25);

console.log(mijnMap); // Map { 'naam' => 'Alice', 'leeftijd' => 25 }

mijnMap.deconste("leeftijd");
console.log(mijnMap); // Map { 'naam' => 'Alice' }
```

### 1.2.1 JavaScript Map `ophalen`
De `get` methode retourneert de waarde voor een specifieke key.

```javascript
const mijnMap = new Map();
mijnMap.set("naam", "Alice");

console.log(mijnMap.get("naam")); // "Alice"
```

### 1.2.1 JavaScript Map `controle`
De `has` methode controleert of een key in de `Map` aanwezig is.

```javascript
const mijnMap = new Map();
mijnMap.set("naam", "Alice");
mijnMap.set("leeftijd", 25);

console.log(mijnMap.has("naam")); // true
console.log(mijnMap.has("leeftijd")); // false
```

### 1.2.1 JavaScript Map `grootte`
De `size` eigenschap geeft het aantal key-value paren in de `Map`.

```javascript
const mijnMap = new Map();
mijnMap.set("naam", "Alice");
mijnMap.set("leeftijd", 25);

console.log(mijnMap.size); // 2
```

### 1.2.1 JavaScript Map `itereren`
Je kunt met een `for...of` loop of met de `forEach` methode over een `Map` itereren. Je kunt de keys, waarden, of de key-value paren itereren.

```javascript
const mijnMap = new Map([["a", 1], ["b", 2], ["c", 3]]);

// Itereren over key-value paren
for (const [key, value] of mijnMap) {
  console.log(`${key}: ${value}`);
}

// Itereren over keys
for (const key of mijnMap.keys()) {
  console.log(key);
}

// Itereren over waarden
for (const value of mijnMap.values()) {
  console.log(value);
}

// forEach methode
mijnMap.forEach((value, key) => {
  console.log(`${key}: ${value}`);
});
```

## 2 JavaScript Set en Map oefeningen
Hieronder enkele oefenening met `Set` en `Map`

### 2.1.1 JavaScript oefening Set `basis`
Maak een `Set` met de waarden `1`, `2`, `3`, `4`, en `5`. Voeg de waarde `6` toe en verwijder de waarde `3`. Controleer of de `Set` de waarde `4` bevat.

```javascript runner

// Maak een Set

// Voeg waarde 6 toe en verwijder waarde 3

// Controleer op bestaan

// Print de Set
console.log(mijnSet); // Set { 1, 2, 4, 5, 6 }
```

### 2.1.2 JavaScript oefening Set `itereren`
Gebruik een `for...of` loop om de waarden te printen.

```javascript runner
const mijnSet = new Set(["a", "b", "c", "d", "e"]);

// Itereer over de Set
for (const waarde of mijnSet) {
  console.log(waarde);
}
```

### 2.1.4 JavaScript oefening Map `Basis`
Gebruik de al voorgegeven Map. Voeg een key value pair `telefoonnummer` - `0612345678` toe en verwijder de key `leeftijd`. Controleer of de `Map` de key `naam heeft`


```javascript runner
const mijnMap = new Map();
mijnMap.set("naam", "Alice");
mijnMap.set("leeftijd", 25);


// Voeg key value toe

// Verwijder leeftijd

// Controleer op bestaan {naam}

```

### 2.1.5 JavaScript oefening Map `itereren`
Gebruik een `for...of` loop om over de `Map` te itereren.

```javascript runner
const mijnMap = new Map([
  ["naam", "Alice"],
  ["leeftijd", 25],
  ["telefoonnummer", "0612345678"]
]);
```