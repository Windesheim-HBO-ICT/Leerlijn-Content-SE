---
title: JavaScript errors
tags:
  - JS/Errors
  - page
difficulty: 2
---

# 1. JavaScript Errors
**Error objects** in JavaScript worden gebruikt om foutmeldingen te representeren. Deze objecten kunnen informatie bevatten zoals het foutbericht, de naam van de fout, en waar de fout is opgetreden. Het gebruik van error objects helpt bij het debuggen en afhandelen van fouten in je code.

## 1.1 JavaScript Errors `basis`
Dit hoofdstuk gaat over errors, custom errors, built-in error types en het afhandelen van errors

### Voorbeeld: Error object
Je kunt een fout creëren met de `Error` constructor let hierbij op het `new` keyword.

```javascript
try {
  throw new Error("Er is iets misgegaan!");
} catch (error) {
  console.log(error.name);    // "Error"
  console.log(error.message); // "Er is iets misgegaan!"
  console.log(error.stack);   // Stack trace van de fout
}
```

### Voorbeeld: Custom Error object
Je kunt een aangepaste fout creëren door een nieuwe foutklasse te definiëren:

```javascript
class CustomError extends Error {
  constructor(message) {
    super(message);
    this.name = "CustomError";
  }
}

try {
  throw new CustomError("Dit is een aangepaste fout!");
} catch (error) {
  console.log(error.name);    // "CustomError"
  console.log(error.message); // "Dit is een aangepaste fout!"
}
```

## 1.2 JavaScript Errors `built-in types`
Dit hoofdstuk gaat over de built-in error types.

### SyntaxError

```javascript
try {
  eval("console.log('Hello)");
} catch (error) {
  console.log(error.name);    // "SyntaxError"
  console.log(error.message); // "Invalid or unexpected token"
}
```

### ReferenceError

```javascript
try {
  console.log(onbekendeVariabele);
} catch (error) {
  console.log(error.name);    // "ReferenceError"
  console.log(error.message); // "onbekendeVariabele is not defined"
}
```

### TypeError

```javascript
try {
  null.foo();
} catch (error) {
  console.log(error.name);    // "TypeError"
  console.log(error.message); // "Cannot read property 'foo' of null"
}
```

### RangeError

```javascript
try {
  const getal = 1;
  getal.toPrecision(500);
} catch (error) {
  console.log(error.name);    // "RangeError"
  console.log(error.message); // "toPrecision() argument must be between 1 and 100"
}
```

### URIError

```javascript
try {
  decodeURIComponent("%");
} catch (error) {
  console.log(error.name);    // "URIError"
  console.log(error.message); // "URI malformed"
}
```

## 2 Oefeningen
Hieronder enkele oefeningen betreffende errors.

### Oefening 1: Basis
Gooi een eenvoudige fout met het bericht `"Dit is een fout!"` en vang het op met een `try-catch`\-blok. Log de naam en het bericht van de fout.

```javascript runner
try {
} catch (error) {
  console.log(error.name);    // Verwacht: "Error"
  console.log(error.message); // Verwacht: "Dit is een fout!"
}
```

### Oefening 2: Built-in error type
Schrijf een `try-catch`\-blok dat een `ReferenceError` opvangt als je probeert een niet-bestaande variabele te loggen.

```javascript runner
try {
  // Probeer een niet-bestaande variabele te loggen
} catch (error) {
  console.log(error.name);    // Verwacht: "ReferenceError"
  console.log(error.message); // Verwacht: "onbestaandeVariabele is not defined"
}
```

### Oefening 1: Custom error
Maak een aangepaste fout genaamd `ValidationError` met een bericht `"Ongeldige invoer"`. Gooi deze fout als de input `"test"` is en vang de fout op.

```javascript runner
// Maak hier de class

function controleerInput(input) {
  if (input === "test") {
    // throw hier de error
  }
  return "Input is geldig";
}

try {
  console.log(controleerInput("test"));
} catch (error) {
  console.log(`${error.name}: ${error.message}`); // Verwacht: "ValidationError: Ongeldige invoer"
}
```

