---
title: 1. Uitleg bewerkingen op getallen
taxonomie:
  - ib-19.2.Talstelsels.OI
---

## Wat zijn bewerkingen op getallen?

Bewerkingen op getallen zijn wiskundige handelingen die je op getallen
kunt uitvoeren. De meest bekende bewerkingen zijn  optellen,
aftrekken, vermenigvuldigen en delen.

In de wiskunde en informatica wordt ook vaak gebruik gemaakt van:

- **floor** : afronden naar beneden
- **ceil** : afronden naar boven
- **div** : gehele deling
- **mod** / **modulo** : rest van een deling

## Hoe zitten **floor** en **ceil** in elkaar?

Bij een floor wordt een getal naar beneden afgerond, bij een ceil wordt een getal naar boven afgerond.

Voor floor gebruiken we de tekens $\lfloor~\rfloor$, voor ceil
gebruiken we de tekens $\lceil~\rceil$.

Voorbeelden:

$\begin{array}{rcl}
\lfloor 3\rfloor & = & 3 \\
\lceil 3\rceil & = & 3 \\
\lfloor 3.1\rfloor & = & 3 \\
\lceil 3.1\rceil & = & 4 \\
\lfloor -3.1\rfloor & = & -4 \\
\lceil -3.1\rceil & = & -3
\end{array}$

> [!warning] Let op!
> Negatieve getallen worden *naar beneden* afgerond
> en niet "naar het nulpunt". Je hebt misschien de neiging te denken
> dat $\lfloor -8.5\rfloor=-8$, maar $\lfloor -8.5\rfloor=-9$.

## Hoe zitten **div** en **mod** in elkaar?

De operaties **div** en **mod** passen we alleen toe op gehele getallen.

De bewerking **div** is een *gehele deling*. Hierbij wordt bij een
deling alleen het gehele getal behouden, de rest wordt genegeerd. We
kunnen stellen dat $7~\textrm{\textbf{div}}~3 = 2$, want 3 past 2x in
7. De rest (1) wordt genegeerd.

Voorbeelden:
$\begin{array}{rcl}
7~\textrm{\textbf{div}}~3 & = & 2\\
17~\textrm{\textbf{div}}~5 & = & 3\\
15~\textrm{\textbf{div}}~5 & = & 3\\
123456~\textrm{\textbf{div}}~10 & = & 12345
\end{array}$

De bewerking **modulo** (of kortweg **mod**) is de rest van een
deling. Het is dus de rest die overblijft na het uitvoeren van een
**div**.

Voorbeelden:
$\begin{array}{rcl}
7~\textrm{\textbf{mod}}~3 & = & 1\\
17~\textrm{\textbf{mod}}~5 & = & 2\\
15~\textrm{\textbf{mod}}~5 & = & 0\\
123456~\textrm{\textbf{mod}}~10 & = & 6
\end{array}$

> [!TIP]- Achtergrond (geen lesstof)
> Gegeven de volgende stelling:
> $$\forall x,n\in\Bbb{N} : \exists q,r\in\Bbb{N} :
> r< n \wedge q\cdot n + r = x$$
> 
> Hier staat: voor alle natuurlijke getallen (gehele getallen $\geq0$)
> $x$ en $n$ bestaan natuurlijke getallen $q$ en $r$, waarbij $r$
> kleiner is dan $n$ en $q\cdot n + r = x$.
> 
> In de stelling hierboven is $q$ de **div** en $r$ is de **mod**.


[Toelichting van het onderwerp]

> [!TIP] Casus
> [Een voorbeeld casus, enkel theorie geen code voorbeeld]


## Hoe gebruik je [onderwerp]?
[Tekst over je overwerp en wanneer je het zou gebruiken. Ook eventuele alternatieven benoemen en daar dan verwijzingen naar toevoegen]

> [!TIP] Casus
>[Duidelijke casus met een lijst van concrete eisen. Maak er eerst een verhaaltje van en daarna pas de lijst met eisen]

**Mogelijke uitwerking van de casus**
```csharp
[Mogelijke uitwerking van de casus]
```

[Mogelijk een extra diagram zoals een flowchart of sequentiediagrammen. Doe dit in mermaid]

Indien bronnen:
> [!info] Bronnen
> Bron: link

---

> Volgende stap: [verwijzing naar PI]
