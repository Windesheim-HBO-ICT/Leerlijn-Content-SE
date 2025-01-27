---
title: Hier een titel beginnend met 1. Onderwerp
taxonomie:
  - "[taxco]"
draft: true
---

> Meer informatie over [verwijzing naar OI]

## Opdracht [nummer]
[Korte introductie tekst]

### Specificaties
- [Eis waar de opdracht aan moet voldoen, duidelijk geformuleerd]
- [Tweede eis waar de opdracht aan moet voldoen, duidelijk geformuleerd]

### Verwachte output:
Als `[variabel] = [waarde]`, komt in de console:
```
[Output in de console]
```
Als `[variabel] = [waarde]`, komt in de console:
```
[Output in de console]
```

### Nu jij:
``` csharp runner
[Hier code die de student moet schrijven, geef ze een basis en extra elementen zoals Usings al. Opdracht 1 meer geven, opdracht 10 minder]
``` 

> [!info]- Mogelijke uitwerking
> ``` csharp
> [Hier een mogelijke uitwerking van de casus. Houdt rekening met de lesstof die al zijn gegeven en dat het duidelijk genoeg is]
> [Code is niet uitvoerbaar via de coderunner, maar moet wel een codeblock zijn]
> ```

---
## Opdracht 1
Zet de volgende casus om naar een if-else block.

### Specificaties:
- Maak een variabel `age` aan.
- Als de waarde van het variabel `age` groter of gelijk is aan `18` moet het volgende in de console komen te staan: "Toegang verleend tot de content." .
- Als de waarde van het variabel `age` kleiner is dan `18`, moet het in de console komen te staan: "Toegang geweigerd. Leeftijdsrestrictie: 18+".

### Verwachte output:
Als `age = 18`, komt in de console:
```
Toegang verleend tot de content.
```
Als `age = 17`, komt in de console:
```
Toegang geweigerd. Leeftijdsrestrictie: 18+
```

### Nu jij:
```csharp runner
using System;

int age = 
if (){

} else {

}
``` 

> [!info]- Mogelijke uitwerking
> ``` csharp
> using System;
> 
> int age = 16;
> if (age >= 18){
>    Console.WriteLine("Toegang verleend tot de content.");
> }
> else {
>    Console.WriteLine("Toegang geweigerd. Leeftijdsrestrictie: 18+");
>}
> ```
