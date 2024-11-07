---
title: 1. If-Else Structuur
---

## Wat is een If-Else-structuur?
Stel je maakt een programma dat checkt of gebruikers 18 jaar of ouder zijn. 
Als een gebruiker zijn leeftijd heeft ingevuld wil je dit kunnen checken en verschillende acties uitvoeren in het geval dat de gebruiker jonger is of ouder dan 18 is. Hierbij komt de If-Else-structuur goed van pas.

Een *If-Else*-structuur stelt de programmeur in staat om voorwaarden (condities) te controleren en daarop gebaseerde acties uit te voeren. Wanneer een conditie waar (true) is, wordt een specifieke code uitgevoerd; als de conditie niet waar (false) is, wordt alternatieve code uitgevoerd.

## Hoe zit een If-Else-structuur in elkaar?
De *If-Else*-structuur volgt een specifieke opbouw, die begint met een `if`-clausule waarin een conditie wordt gespecificeerd, gevolgd door de bijbehorende actie. Optioneel volgt daarna een `else`-clausule waarin een alternatieve actie kan worden gedefinieerd.

### Codevoorbeeld
```C#
if (conditie_1){
    // code om uit te voeren als de conditie waar is.
}
else{
    // alternatieve code als de conditie niet waar is.
}
```

## Hoe gebruik je een If-Else-structuur?
De causaliteit in een *If-Else*-structuur is eenvoudig: het programma voert een actie uit op basis van de waarheid van een voorwaarde.

### Casus
Stel je schrijft een script dat gebruikersleeftijd controleert. Als de leeftijd 18 of meer is, toont het "Toegang verleend", anders "Toegang geweigerd".
