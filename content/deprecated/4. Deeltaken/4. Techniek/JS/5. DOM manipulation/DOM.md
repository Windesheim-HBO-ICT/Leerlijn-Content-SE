---
title: Document Object Model (DOM)
tags:
  - HTML/DOM
  - page
difficulty: 2
---

# 1. Het Document Object Model (DOM)
Het **Document Object Model (DOM)** is een programmeerinterface voor HTML en XML-documenten. Het representeert de pagina als een boomstructuur (tree structure) waarin elk onderdeel van de pagina een object is dat gemanipuleerd kan worden met een programmeertaal zoals JavaScript.

## 1.1 DOM: Wat is het?
Het DOM geeft een gestructureerde representatie van het document en definieert hoe het document kan worden veranderd. Het is essentieel voor dynamische interactie op webpagina's, zoals het updaten van de inhoud, het aanpassen van stijlen, en het reageren op gebruikersgebeurtenissen.

Een eenvoudig voorbeeld van een HTML-document en de bijbehorende DOM-tree:

```html
<html>
<head>
  <title>Mijn Pagina</title>
</head>
<body>
  <h1>Welkom</h1>
  <p>Dit is een paragraaf.</p>
</body>
</html>
```

## 1.2 Dom: Operaties
Hier zijn enkele van de meest gebruikte operaties voor het manipuleren van het DOM met JavaScript:

### 1.2.1 Elementen selecteren
`document.getElementById(id)`: Selecteert een element op basis van zijn ID.
```javascript
const header = document.getElementById("mijnHeader");
```

`document.getElementsByClassName(className)`: Selecteert elementen op basis van hun class naam. Retourneert een HTMLCollection.

```javascript
const fotos = document.getElementsByClassName("foto");
```
> **Let op**: dit returned een HTMLCollection. Veranderingen in de DOM reflecteerd zich meteen in de array. Bijvoorbeeld: je haalt een class `foto` weg van 1 van de elementen wordt deze ook verwijderd uit de HTMLCollection.

`document.getElementsByTagName(tagName)`: Selecteert elementen op basis van hun tag.
```javascript
const paragrafen = document.getElementsByTagName("p");
```

`document.querySelector(selector)`: Selecteert het eerste element dat overeenkomt met de CSS-selector.
```javascript
const eersteParagraaf = document.querySelector("p");
```

`document.querySelectorAll(selector)`: Selecteert alle elementen die overeenkomen met de CSS-selector. Retourneert een NodeList (lijkt op een array).
```javascript
const alleParagrafen = document.querySelectorAll("p");
```

### 1.2.2 Inhoud manipuleren
`element.textContent`: Leest of schrijft de tekstinhoud van een element.
```javascript
const paragraaf = document.querySelector("p");
paragraaf.textContent = "Nieuwe tekst.";
```

`element.innerHTML`: Leest of schrijft de HTML-inhoud van een element.
```javascript
const container = document.querySelector("#container");
container.innerHTML = "<p>Nieuwe <b>inhoud</b></p>";
```

> **Let op**: get gebruik van `innerHTML` opent zich wel op tot security risico's. Zorg er altijd voor dat je de HTML sanitized. Om HTML toe te voegen zonder overschrijven gebruik `insertAdjacentHTML()`.

### Attributen beheren
`element.getAttribute(attributeName)`: Haalt de waarde van een attribuut op.
```javascript
const link = document.querySelector("a");
const href = link.getAttribute("href");
```

`element.setAttribute(attributeName, value)`: Stelt de waarde van een attribuut in.
```javascript
const link = document.querySelector("a");
link.setAttribute("href", "https://example.com");
```

`element.removeAttribute(attributeName)`: Verwijdert een attribuut.
```javascript
const link = document.querySelector("a");
link.removeAttribute("href");
```

### Elementen toevoegen, verwijderen en verplaatsen
`document.createElement(tagName)`: Maakt een nieuw element aan.
```javascript
const nieuwParagraaf = document.createElement("p");
nieuwParagraaf.textContent = "Dit is een nieuw element.";
```

`element.appendChild(child)`: Voegt een nieuw kindelement toe aan een element.
```javascript
const nieuwParagraaf = document.createElement("p");
document.body.appendChild(nieuwParagraaf);
```

`element.removeChild(child)`: Verwijdert een kindelement.
```javascript
document.body.removeChild(nieuwParagraaf);
```

`element.insertBefore(newNode, referenceNode)`: Voegt een nieuw kindelement in vóór een referentie-element.
```javascript
const nieuwParagraaf = document.createElement("p");
const referentieParagraaf = document.querySelector("p");
document.body.insertBefore(nieuwParagraaf, referentieParagraaf);
```

### Events
**Evenementen** (events) zijn acties die gebeuren op de pagina (zoals klikken, invoer, enz.). Je kunt evenementen afhandelen door **event listeners** toe te voegen.

`element.addEventListener(event, callback)`: Voegt een event listener toe aan een element.
```javascript
const knop = document.querySelector("button");
knop.addEventListener("click", () => {
  alert("Knop is geklikt!");
});
```

`element.removeEventListener(event, callback)`: Verwijdert een event listener van een element.
```javascript
const callback = () => {
  alert("Knop is geklikt!");
};

knop.addEventListener("click", callback);
knop.removeEventListener("click", callback);
```