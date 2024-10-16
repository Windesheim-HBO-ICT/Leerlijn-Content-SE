---
title: JavaScript Callbacks
tags:
  - JS/Callbacks
  - page
difficulty: 2
---

# 1 JavaScript Callbacks
In JavaScript zijn **callbacks** functies die als argumenten aan andere functies worden doorgegeven en later worden aangeroepen binnen die andere functie. Callbacks worden vaak gebruikt voor asynchrone operaties zoals tijdsafhankelijke acties of netwerkverzoeken.

## 1.1 JavaScript Callbacks `basis`
Een callback is een functie die wordt doorgegeven aan een andere functie als parameter en vervolgens wordt aangeroepen binnen die functie.

In het onderstaande voorbeeld: 
-  `doeIets` is een functie die een andere functie (`callback`) als parameter accepteert. 
- `mijnCallback` is de callback functie die als argument wordt doorgegeven aan `doeIets`. 
- `doeIets` voert eerst zijn eigen code uit (`Stap 1`) en roept dan de `callback` aan (`Stap 2`).

```javascript
function doeIets(callback) {
  console.log("Stap 1: Iets doen");
  callback(); // Roept de callback functie aan
}

function callbackFunction() {
  console.log("Stap 2: Iets anders doen");
}

doeIets(callbackFunction);
```

## 1.2 JavaScript Callbacks `anoniem`
In plaats van een genaamde functie, kun je een anonieme functie gebruiken als callback.


In het onderstaande voorbeeld maken we gebruik van van een anonieme functie.

```javascript
function doeIets(callback) {
  console.log("Stap 1: Iets doen");
  callback();
}

doeIets(() => {
  console.log("Stap 2: Iets anders doen");
});
```

## 1.3 JavaScript Callbacks `callback hell`
Wanneer callbacks genest worden binnen andere callbacks, kan de code moeilijk te lezen en onderhouden worden. Dit fenomeen wordt vaak "callback hell" genoemd.

```javascript
setTimeout(() => {
  console.log("Stap 1");
  setTimeout(() => {
    console.log("Stap 2");
    setTimeout(() => {
      console.log("Stap 3");
    }, 1000);
  }, 1000);
}, 1000);
```

## 1.4 JavaScript Callbacks `problemen`
- **Inversie van Controle**: Bij callbacks geef je de controle over aan een andere functie, wat kan leiden tot onvoorspelbaar gedrag als de callback niet naar verwachting wordt aangeroepen.
- **Callback Hell**: Kan de code moeilijk leesbaar en onderhoudbaar maken.

## 1.5 JavaScript Callbacks `alternatieven`
Callbacks zijn een basisprincipe in JavaScript, maar moderne technieken zoals **Promises** en **Async/Await** bieden elegantere oplossingen voor asynchrone operaties.

- **Promises**: Een object dat een asynchrone operatie vertegenwoordigt, met methoden om de uitkomst van de operatie af te handelen.
- **Async/Await**: Maakt gebruik van Promises om asynchrone code te schrijven die eruitziet als synchrone code.


