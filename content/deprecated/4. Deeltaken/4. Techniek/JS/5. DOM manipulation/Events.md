---
title: JavaScript Events
tags:
  - JS/Events
  - page
difficulty: 2
---

# 1. JavaScript Evenementen (Events)
Evenementen in JavaScript zijn acties die plaatsvinden in de browser, zoals klikken, het laden van een pagina, en invoer van de gebruiker. Ze vormen de kern van de interactie tussen de gebruiker en de webpagina.

## 1.1 Events: types
Hieronder een lijst met veelvoorkomende event types. Voor een volledige lijst bekijk de [MDN docs](https://developer.mozilla.org/en-US/docs/Web/Events).

### Type: click
`click`: Wordt geactiveerd wanneer een element wordt aangeklikt.
```javascript
document.querySelector("button").addEventListener("click", () => {
  console.log("Button is geklikt");
});
```

### Type: load
`load`: Wordt geactiveerd wanneer de volledige pagina inclusief alle afhankelijkheden (zoals afbeeldingen en stylesheets) is geladen.
```javascript
window.addEventListener("load", () => {
  console.log("Pagina volledig geladen");
});
```

### Type: DOMContentLoaded
`DOMContentLoaded`: Wordt geactiveerd wanneer het HTML-document volledig is geladen en geparseerd, zonder te wachten op stylesheets, afbeeldingen, enz.
```javascript
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM volledig geladen en geparseerd");
});
```

### Type: input
`input`: Wordt geactiveerd wanneer de waarde van een `<input>`, `<textarea>`, of `<select>` element verandert.
```javascript
document.querySelector("input").addEventListener("input", (event) => {
  console.log(`Nieuwe waarde: ${event.target.value}`);
});
```

### Type: submit
`submit`: Wordt geactiveerd wanneer een formulier wordt ingediend.
```javascript
document.querySelector("form").addEventListener("submit", (event) => {
  event.preventDefault(); // voorkomt het versturen van het formulier
  console.log("Formulier ingediend");
});
```

### Type: mouseover
`mouseover`: Wordt geactiveerd wanneer de muis over een element beweegt.
```javascript
document.querySelector("div").addEventListener("mouseover", () => {
  console.log("Muis over element");
});
```

### Type: keydown
`keydown`: Wordt geactiveerd wanneer een toets wordt ingedrukt.
```javascript
document.addEventListener("keydown", (event) => {
  console.log(`Toets ingedrukt: ${event.key}`);
});
```

## 1.2 Event Propagation (bulling/capturing)
**Event propagation** bepaalt hoe gebeurtenissen zich verspreiden door de DOM. Er zijn twee belangrijke fasen.

### Bubbling
In **bubbling** (opborrelen) verspreidt het evenement zich van het doelwit element naar boven, door de hiërarchie van voorouders tot de root (meestal `document`).
```javascript
<div id="parent">
  <button id="child">Klik mij</button>
</div>

<script>
  document.getElementById("parent").addEventListener("click", () => {
    console.log("Parent geklikt");
  });

  document.getElementById("child").addEventListener("click", (event) => {
    console.log("Child geklikt");
  });
</script>
```

Als je op de `button` klikt, zie je eerst "Child geklikt", gevolgd door "Parent geklikt". Dit komt omdat het `click`\-evenement van het `button` element naar het `div` element opborrelt.

### Capturing
In **capturing** (vastleggen) verspreidt het evenement zich van de root naar het doelwit element. Dit gebeurt vóór het bubbling.

```javascript
<div id="parent">
  <button id="child">Klik mij</button>
</div>

<script>
  document.getElementById("parent").addEventListener("click", () => {
    console.log("Parent geklikt");
  }, true); // true voor capturing

  document.getElementById("child").addEventListener("click", (event) => {
    console.log("Child geklikt");
  });
</script>
```

In dit geval, als je op de `button` klikt, zie je "Parent geklikt" vóór "Child geklikt". Dit komt omdat capturing de gebeurtenis eerst van boven naar beneden verspreidt.

## 1.3 Event Delegation
**Event delegation** is een techniek waarbij je één enkele event listener gebruikt om gebeurtenissen af te handelen voor meerdere elementen. Dit doe je door gebruik te maken van event propagation.

> **Let op**: in JavaScript bedoelen we iets heel anders met event delegation dan in bijvoorbeeld C#. In JavaScript is het dus **niet** een type dat een referentie naar een methode houdt.

We gebruiken event delegation in JavaScript om het aantal event listeners lager te houden en om makkelijker dynamisch toegevoegde elementen te beheren.

```javascript
<ul id="lijst">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>

<script>
  document.getElementById("lijst").addEventListener("click", (event) => {
    if (event.target.tagName === "LI") {
      console.log(`Geklikt op ${event.target.textContent}`);
    }
  });
</script>
```

In dit voorbeeld wordt een enkele event listener toegevoegd aan de `ul`. Wanneer een `li` wordt aangeklikt, wordt de event handler getriggerd en kan je controleren of de klik plaatsvond op een `li`.

## 1.4 Events voorkomen
**preventDefault()** wordt gebruikt om de standaardactie te voorkomen die normaal optreedt bij bepaalde evenementen, zoals het versturen van een formulier of het volgen van een link.

```javascript
<a href="https://example.com" id="mijnLink">Ga naar voorbeeld</a>

<script>
  document.getElementById("mijnLink").addEventListener("click", (event) => {
    event.preventDefault(); // voorkomt het volgen van de link
    console.log("Link geklikt maar niet gevolgd");
  });
</script>
```
