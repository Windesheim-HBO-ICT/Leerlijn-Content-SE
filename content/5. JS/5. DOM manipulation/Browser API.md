---
title: Browser Object Model (BOM)
tags:
  - HTML/BOM
difficulty: 2
---

# 1. Browser Object Model (BOM)
Het **Browser Object Model (BOM)** biedt toegang tot browser-specifieke objecten en functionaliteiten die geen deel uitmaken van de core JavaScript-taal maar wel essentieel zijn voor interactie met de webpagina en de browseromgeving.

## 1.1 Browser objecten
Hieronder een lijst van browser objecten.

### Object: window
Het **`window` object** is het globale object in de browser. Het vertegenwoordigt het browservenster en omvat methoden, eigenschappen, en objecten die je kunt gebruiken om met de browser te werken. Het window object heeft verschillende properties. Hieronder worden enkele voorbeelden gegeven. Voor meer informatie bekijk de [MDN docs](https://developer.mozilla.org/en-US/docs/Web/API/Window).

`window.innerWidth` en `window.innerHeight`: Geven de breedte en hoogte van het browservenster in pixels
```javascript
console.log(window.innerWidth, window.innerHeight);
```

`window.location`: Bevat informatie over de huidige URL van het document.
```javascript
console.log(window.location.href);
```

Het window object heeft ook enkele methoden bijvoorbeeld `open()`. Dit opent een nieuw venster of window.
```javascript
window.open("https://example.com", "_blank"); // Opent een nieuwe tab met de opgegeven URL
```

### Object: document
Het `document` object vertegenwoordigt de DOM en biedt methoden en eigenschappen om HTML-elementen te manipuleren bijvoorbeeld het ophalen van het eerste element op dat overeenkomt met een CSS-selector.

```javascript
const element = document.querySelector(".mijnClass");
```

Of een nieuw element aanmaken:
```javascript
const nieuwElement = document.createElement("div");
```

### Object: navigator
Het `navigator` object biedt informatie over de browser en het systeem van de gebruiker. Veelgebruikte properties hiervan is de userAgent en language property.

`navigator.userAgent`: Bevat een string met informatie over de browser.
```javascript
console.log(navigator.userAgent);
```

`navigator.language`: Geeft de voorkeurstaal van de browser.
```javascript
console.log(navigator.language);
```

### Object: History
Het `history` object biedt methoden om door de sessiegeschiedenis van de browser te navigeren.

`history.back()`: Gaat terug naar de vorige pagina.
```javascript
history.back();

```

`history.forward()`: Gaat naar de volgende pagina in de geschiedenis.
```javascript
history.forward();
```

`history.go()`: Navigeert naar een specifieke pagina in de geschiedenis.
```javascript
history.go(-1); // Gaat één pagina terug
```

## 1.2 LocalStorage / SessionStorage
**LocalStorage** en **sessionStorage** zijn Web Storage API's waarmee je gegevens kunt opslaan in de browser.


### LocalStorage
**localStorage** slaat gegevens op die beschikbaar blijven na het sluiten van de browser. Gegevens blijven bestaan totdat ze expliciet worden verwijderd.

`Opslaan`
```javascript
localStorage.setItem("gebruikersnaam", "Alice");
```

`Ophalen`
```javascript
const gebruikersnaam = localStorage.getItem("gebruikersnaam");
```

`Verwijderen`
```javascript
localStorage.removeItem("gebruikersnaam");
```

`Alles Wissen`
```javascript
localStorage.clear();
```

### Session storage
**sessionStorage** slaat gegevens op die alleen beschikbaar zijn gedurende de huidige sessie. Gegevens verdwijnen zodra de browser of tabblad wordt gesloten.

`Opslaan`
```javascript
sessionStorage.setItem("sessieId", "12345");
```

`Ophalen`
```javascript
const sessieId = sessionStorage.getItem("sessieId");
```

`Verwijderen`
```javascript
sessionStorage.removeItem("sessieId");
```

`Alles Wissen`
```javascript
sessionStorage.clear();
```



