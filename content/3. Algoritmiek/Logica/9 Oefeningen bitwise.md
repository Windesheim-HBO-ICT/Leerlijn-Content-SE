---
title: 9. Oefeningen bitwise
taxonomie:
  - ib-19.2.Logica.DT
tags:
 - Bitwise
---

> Meer informatie over [[7. Uitleg bitwise|bitwise logica]]

## Opdracht 1
Leer bitwise AND gebruiken om te bepalen of een getal even is.

### Specificaties
- Maak een variabele `number` aan.
- Gebruik een bitwise AND (`&`) om te controleren of `number` even is (laatste bit = 0).

### Verwachte output
Als `number = 6`, komt in de console:
```
Het getal is even.
```

Als `number = 5`, komt in de console:
```
Het getal is oneven.
```

### Nu jij
```csharp
using System;  

int number = ________;  

if ((number & 1) == ________)
{     
	Console.WriteLine("Het getal is even."); 
} 
else 
{     
	Console.WriteLine("Het getal is oneven."); 
}
```

> [!INFO] - Mogelijke uitwerking
> ```csharp
> using System; 
> 
> int number = 6; 
>  
> if ((number & 1) == 0) 
> {     
> 	 Console.WriteLine("Het getal is even."); 
> } 
> else 
> {     
> 	 Console.WriteLine("Het getal is oneven."); 
> }

---

## Opdracht 2
Controleer of het 3e bit van een getal aan staat.

### Specificaties
- Gebruik bitwise AND (`&`) om te controleren of het derde bit (van rechts, waarde 4) van een getal `x` is ingesteld.
- Toon een aangepaste boodschap in de console.

### Verwachte output
Als `x = 5`, komt in de console:
```
Het derde bit staat AAN.
```

Als `x = 2`, komt in de console:
```
Het derde bit staat UIT.
```

### Nu jij
```csharp
using System; 

int x = _________;  

if ((x & 4) == _________)
{     
	Console.WriteLine("Het derde bit staat AAN."); 
} 
else 
{     
	Console.WriteLine("Het derde bit staat UIT."); 
}
```

> [!info]- Mogelijke uitwerking
> ```csharp
> using System; 
> 
> int x = 5; 
> if ((x & 4) == 4) 
> {     
> 	Console.WriteLine("Het derde bit staat AAN."); 
> } 
> else 
> {     
> 	Console.WriteLine("Het derde bit staat UIT."); 
> }
> ```

---

## Opdracht 3
Gebruik bitwise OR om rechten samen te voegen.

### Specificaties
- Maak twee variabelen: `leesRecht = 1`, `schrijfRecht = 2`.
- Voeg de rechten samen in `rechten` met de `|` operator.

### Verwachte output
Als `rechten = leesRecht | schrijfRecht`, komt in de console:
```
Gebruiker heeft lees- en schrijfrechten.
```

### Nu jij
```csharp
using System;

int leesRecht = 1;
int schrijfRecht = 2; 
int rechten = _________;  
if ((rechten & leesRecht) != _________ && (rechten & schrijfRecht) != _________) 
{     
	Console.WriteLine("Gebruiker heeft lees- en schrijfrechten."); 
}
else 
{
	Console.WriteLine("Gebruiker heeft geen lees- en schrijfrechten.");
}
```

> [!info]- Mogelijke uitwerking
> ```csharp
> using System; 
> 
> int leesRecht = 1; 
> int schrijfRecht = 2; 
> int rechten = leesRecht | schrijfRecht;  
> if ((rechten & leesRecht) != 0 && (rechten & schrijfRecht) != 0)
> {     
> 	 Console.WriteLine("Gebruiker heeft lees- en schrijfrechten."); 
> }
> else 
> {
> 	Console.WriteLine("Gebruiker heeft geen lees- en schrijfrechten");
> }
> ```

---

## Opdracht 4
Gebruik bitwise XOR om verschil tussen bits te tonen.

### Specificaties
- Vraag twee getallen `a` en `b`.
- Gebruik de `^` operator om verschilbits te berekenen.
- Print het resultaat.

### Verwachte output
Als `a = 6`, `b = 3`, komt in de console:
```
Verschilbits: 5
```

### Nu jij
```csharp
using System;  

int a = _________; 
int b = _________; 
int verschil = a ^ b;  

Console.WriteLine("Verschilbits: " + verschil);
```

> [!info]- Mogelijke uitwerking
> ```csharp
> using System;
> 
> int a = 6;
> int b = 3;
> int verschil = a ^ b;
> 
> Console.WriteLine("Verschilbits: " + verschil);
> ```

---

## Opdracht 5
Gebruik bitwise shift om te vermenigvuldigen en delen.

### Specificaties
- Maak een variabele `n` aan.
- Gebruik `n << 1` om met 2 te vermenigvuldigen.
- Gebruik `n >> 1` om door 2 te delen.

### Verwachte output
Als `n = 4`, komt in de console:
```
4 x 2 = 8  
4 / 2 = 2
```

### Nu jij
```csharp
using System;

int n = _________;

Console.WriteLine(n + " x 2 = " + (n << 1));
Console.WriteLine(n + " / 2 = " + (n >> 1));
```

> [!info]- Mogelijke uitwerking
> ```csharp
> using System;
> 
> int n = 4;
> Console.WriteLine(n + " x 2 = " + (n << 1));
> Console.WriteLine(n + " / 2 = " + (n >> 1));
> ```

---

## Opdracht 6  Hoofdletters en kleine letters kunnen switchen
Gebruik bitwise operaties om de hoofdletters en kleine letters van een karakter aan te passen.

### Specificaties
- Gebruik een karakter `ch`.
- Maak gebruik van bitwise operators om:
	- de kleine letter van `ch` te tonen
	- de hoofdletter van `ch` te tonen
	- de case te wisselen van `ch`

### Verwachte output  
Als `ch = 'A'`, komt in de console:
```
Lowercase: a  
Uppercase: A  
Wissel case: a
```

Als `ch = 'z'`, komt in de console:
```
Lowercase: z  
Uppercase: Z  
Wissel case: Z
```

### Nu jij
```csharp
using System;

char ch = _________; // bv. 'A'

char lower = (char)(ch | 32);
char upper = (char)(ch & ~32);
char toggled = (char)(ch ^ 32);

Console.WriteLine("Lowercase: " + lower);
Console.WriteLine("Uppercase: " + upper);
Console.WriteLine("Wissel case: " + toggled);
```

> [!info]- Mogelijke uitwerking
> ```csharp
> using System;
> 
> char ch = 'A';
> 
> char lower = (char)(ch | 32);
> char upper = (char)(ch & ~32);
> char toggled = (char)(ch ^ 32);
> 
> Console.WriteLine("Lowercase: " + lower);
> Console.WriteLine("Uppercase: " + upper);
> Console.WriteLine("Wissel case: " + toggled);
> ```