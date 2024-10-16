---
title: JavaScript Promises
tags:
  - JS/Promises
  - page
difficulty: 2
---

# 1 JavaScript Promises
Een **Promise** is een object dat een toekomstige waarde vertegenwoordigt. Het wordt gebruikt voor het omgaan met asynchrone operaties, zoals netwerkverzoeken.

## 1.1 JavaScript Promises `basis`
Een `Promise` is een object dat een toekomstige waarde vertegenwoordigt. Het wordt gebruikt voor het omgaan met asynchrone operaties, zoals netwerkverzoeken. Een `promise` kan zich in 3 toestanden bevinden:
- **Pending** (In afwachting): De initiële toestand, nog niet vervuld of afgewezen.
- **Fulfilled** (Vervuld): De operatie is geslaagd, en de Promise heeft een waarde.
- **Rejected** (Afgewezen): De operatie is mislukt, en de Promise heeft een reden voor de mislukking.

Je kan een promise aanmaken met het `new` keyword.

```javascript
const future = new Promise()
```

Een promise kan zoals hierboven aangegeven slagen of mislukken, dit kan je zelf beheren. Dit wordt gedaan met `callbacks`. Deze worden vaak opgeschreven als `resolve` en `reject`.

```javascript
const succes = true

const future = new Promise((resolve, reject) => {
  if (succes) {
    resolve("Het gaat goed!")
  }

  reject("Er is iets missgeggaan")
})
```

Om het resultaat uit een `Promise` te krijgen moet je gebruik maken van `.then()`/`.catch()` of `async`/`await`. Als je de value wilt krijgen via de then-catch variant moet er een callback worden meegegeven als argument. 

```javascript
const succes = true;

const future = new Promise((resolve, reject) => {
  if (succes) {
    resolve("Operatie geslaagd!");
  }
  reject("Operatie mislukt.");
});

future
  .then((bericht) => {
    console.log(bericht);
  })
  .catch((fout) => {
    console.error(fout);
  });
```


## 1.2 JavaScript Promises `chaining`
Je kunt meerdere Promises aan elkaar schakelen om complexe asynchrone workflows te beheren.

```javascript
let stap1 = () => new Promise((resolve) => resolve("Stap 1 voltooid"));
let stap2 = () => new Promise((resolve) => resolve("Stap 2 voltooid"));
let stap3 = () => new Promise((resolve) => resolve("Stap 3 voltooid"));

stap1()
  .then((resultaat1) => {
    console.log(resultaat1);
    return stap2();
  })
  .then((resultaat2) => {
    console.log(resultaat2);
    return stap3();
  })
  .then((resultaat3) => {
    console.log(resultaat3);
  });
```

## 1.3 JavaScript Promises `async/await`
**Async/Await** biedt syntax sugar bovenop `Promises`, waardoor asynchrone code lijkt op synchrone code. Dit maakt het eenvoudiger te begrijpen en te onderhouden. Bij het gebruik van het `await` keyword, moet de functie zelf asynchroon zijn. Dit kan je declareren door het `async` keyword voor `function` te zetten

```javascript
async function voorbeeld() {
  const future = new Promise((resolve) => {
    setTimeout(() => resolve("Resultaat na 2 seconden"), 2000);
  });

  const resultaat = await future;
  console.log(resultaat);
}

voorbeeld();
```

Anonieme functie variant

```javascript
const voorbeeld = async () => {
  const future = new Promise((resolve) => {
    setTimeout(() => resolve("Resultaat na 2 seconden"), 2000);
  });

  const resultaat = await future;
  console.log(resultaat);
}

voorbeeld();
```

## 1.4 JavaScript Promises `try/catch`
Je kunt fouten afhandelen met **try...catch** in async functies.

```javascript
async function voorbeeld() {
  try {
    const future = new Promise((_, reject) => {
      setTimeout(() => reject("Er ging iets fout"), 2000);
    });

    let resultaat = await future;
    console.log(resultaat);
  } catch (fout) {
    console.error(fout);
  }
}

voorbeeld();
```

# Oefeningen
Hieronder enkele oefeningen betreffende JavaScript Promises.

## 2.1 JavaScript Promises `basis`
Maak een Promise `promiseMetGetal` die een getal na 1 seconde teruggeeft. 

```javascript runner
// Maak hier jouw implementatie van promiseMetGetal

promiseMetGetal
  .then((getal) => {
    console.log(`Het getal is: ${getal}`);
  })
  .catch((fout) => {
    console.error(fout);
  });
```

## 2.2 JavaScript Promises `chaining`
Maak twee Promises `stapA` en `stapB`. `stapA` moet na 1 seconde een bericht geven en `stapB` moet na 1 seconde een ander bericht geven. Gebruik chaining om beide berichten achtereenvolgens te loggen.

```javascript runner
// Maak hier jouw implementatie van stapA

// Maak hier jouw implementatie van stapB

// Roep hier stapA aan en chain de resultaten
```

## 2.3 JavaScript Promises `async/await`
Maak een async functie `doeIets` die een Promise aanroept die na 2 seconden een string teruggeeft. Gebruik `await` om op de Promise te wachten en log de string.

```javascript runner
// Maak hier jouw implementatie van doeIets

doeIets()
```

## 2.4 JavaScript Promises `try/catch`
Maak een async functie `controleer` die een Promise aanroept die na 1 seconde wordt afgewezen met een fout. Gebruik `try...catch` om de fout af te handelen en log een foutmelding.

```javascript runner
// Maak hier jouw jouw implementatie van controleer

controleer()
```




