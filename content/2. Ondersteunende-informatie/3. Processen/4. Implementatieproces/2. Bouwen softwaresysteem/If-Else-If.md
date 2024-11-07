---
title: 2. If-Else-If Structuur
---

## Wat is een If-Else-If-structuur?
Soms moet je een programma maken waarin je meerdere condities wilt controleren. 
Bijvoorbeeld: als je een leeftijdscontrole wilt doen, maar ook wilt checken of iemand een speciale status heeft, zoals student of senior. 
Hierbij gebruik je de *If-Else-If*-structuur.

Een *If-Else-If*-structuur laat toe om meerdere condities achtereenvolgens te controleren en, afhankelijk van de eerste ware conditie, een actie uit te voeren.

## Hoe zit een If-Else-If-structuur in elkaar?
De *If-Else-If*-structuur begint met een `if`-clausule, gevolgd door optionele `else if`-clausules en uiteindelijk een `else`-clausule.

### Codevoorbeeld
```C#
if (conditie_1){
    // code om uit te voeren als de eerste conditie waar is.
}
else if (conditie_2){
    // code als de tweede conditie waar is.
}
else {
    // alternatieve code als geen enkele conditie waar is.
}
```

## Hoe gebruik je een If-Else-If-structuur?
Deze structuur is ideaal wanneer je verschillende condities hebt die niet tegelijkertijd waar kunnen zijn.

### Casus
Stel, een programma controleert leeftijden: "kind" voor <13 jaar, "tiener" voor 13-18, "volwassene" voor >18. 
Dit vereist een *If-Else-If*-structuur voor juiste categorisering.
