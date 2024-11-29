---
draft: true
---

Obsidian en Quartz hebben de mogelijkheid om LaTeX-formules in te voegen, hiermee kunnen wetenschappelijke en wiskundige notaties eenvoudig in documenten opgenomen worden.

## Inline LaTeX
Korte formules kunnen binnen een tekstregel weergeven worden. Door dollartekens (`$`) om de formule heen te zetten wordt de tekst binnen de tekens als formule gezien zoals in dit voorbeeld:

```
De reden waarom er maximaal $0.1\micro g\cdot{kg}^{-1}$ PFAS in de grond mag zitten is omdat dit de laagste meetbare hoeveelheid was toen de wet werd aangenomen.
```

Resultaat:

De reden waarom er maximaal $0.1\micro g\cdot{kg}^{-1}$ PFAS in de grond mag zitten is omdat dit de laagste meetbare hoeveelheid was toen de wet werd aangenomen.

Dit voorbeeld is gemaakt met [machten](Latex-Uitdrukkingen#Machten).

## Blok LaTeX
Grotere en complexere formules kunnen niet altijd binnen een stuk tekst, daarom is het ook mogelijk een blok met de formule te maken. dit wordt gedaan door 2 dollartekens (`$$`) om de formule heen te zetten:

```
Om het nulpunt van de parabool te vinden kan de abc-formule toegepast worden:
$$
\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
```

Resultaat:
Om het nulpunt van de parabool te vinden kan de abc-formule toegepast worden:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

Dit voorbeeld is gemaakt met behulp van [machten](Latex-Uitdrukkingen#Machten), [fracties](Latex-Uitdrukkingen#Fracties) en [wortels](Latex-Uitdrukkingen#Wortels).

## Variabelen en nummers
Binnen latex worden accolades (`{}`) gebruikt om aan te geven dat een aantal nummers of variabelen bij elkaar hoort, Als er bijvoorbeeld 2^16 opgeschreven wordt zal LaTeX 2 tot de eerste macht vermenigvuldigd met 6 opschrijven. Dit kan voorkomen worden door de 16 binnen deze haakjes te zetten:

```
$2^16$ is geen hoog getal, daarentegen is $2^{16}$ veel hoger.
```

Resultaat:
$2^16$ is geen hoog getal, daarentegen is $2^{16}$ veel hoger.

## Reken operatoren
De meeste basisoperatoren (+, -, =, <, >) zijn als tekst binnen LaTeX te gebruiken. vermenigvuldiging, niet gelijk aan en deling moeten met een \\ aangegeven worden zoals in het tabel hieronder:

| **Type**          | **Notatie**                   | **Resultaat**               |
| :---------------- | :---------------------------- | :-------------------------- |
| Basisoperatoren   | `$a + b$`                     | $a + b$                     |
| Vermenigvuldiging | `$a \times b$` of `a \cdot b` | $a \times b$ of $a \cdot b$ |
| Niet gelijk aan   | `$a \neq b$`                  | $a \neq b$                  |
| Deling            | `$a \div b$`                  | $a \div b$                  |

> Voor betere leesbaarheid en consistentie is het aangeraden om [fracties](Latex-Uitdrukkingen#Fracties) in plaats van deling te gebruiken, vooral in grotere functies. Dit voorkomt onduidelijkheden en is consistent met de conventies.

## Niet-Latijnse karakters
Er kunnen ook alternatieve symbolen zoals $\pi$ of $\ohm$ gebruikt worden in latex. Deze worden aangegeven door een backslash (`\`) gevolgd door de naam van de letter binnen een LaTeX blok. als de eerste letter van de naam van een Griekse letter een hoofdletter is word de hoofdletter in plaats van de kleine letter gebruikt.

```
Met behulp van LaTeX kunnen symbolen zoals $\aleph$ en $\Delta$ gemakkelijk gebruikt worden!
```

Resultaat:
Met behulp van LaTeX kunnen symbolen zoals $\aleph$ en $\Delta$ gemakkelijk gebruikt worden!

## Lijst van karakters
Door de eerste letter een hoofdletter te maken wordt de hoofdletter gebruikt:
`delta`$\delta$ $\rightarrow$ `Delta` $\Delta$
Dit is niet beschikbaar voor elke letter omdat sommige letters hetzelfde zijn als in het latijns alfabet.

| **Letter** | **Notitie**  | **Resultaat** | **Hoofdletter** |
| :--------- | :----------- | :------------ | :-------------- |
| Alpha      | `$\alpha$`   | $\alpha$      | (Latijns) $A$   |
| Beta       | `$\beta$`    | $\beta$       | (Latijns) $B$   |
| Gamma      | `$\gamma$`   | $\gamma$      | $\Gamma$        |
| Delta      | `$\delta$`   | $\delta$      | $\Delta$        |
| Epsilon    | `$\epsilon$` | $\epsilon$    | (Latijns) $E$   |
| Zeta       | `$\zeta$`    | $\zeta$       | (Latijns) $Z$   |
| Eta        | `$\eta$`     | $\eta$        | (Latijns) $H$   |
| Theta      | `$\theta$`   | $\theta$      | $\Theta$        |
| Iota       | `$\iota$`    | $\iota$       | (Latijns) $I$   |
| Kappa      | `$\kappa$`   | $\kappa$      | (Latijns) $K$   |
| Lambda     | `$\lambda$`  | $\lambda$     | $\Lambda$       |
| Mu         | `$\mu$`      | $\mu$         | (Latijns) $M$   |
| Nu         | `$\nu$`      | $\nu$         | (Latijns) $N$   |
| Xi         | `$\xi$`      | $\xi$         | $\Xi$           |
| Omicron    | `$\omicron$` | $\omicron$    | (Latijns) $O$   |
| Pi         | `$\pi$`      | $\pi$         | $\Pi$           |
| Rho        | `$\rho$`     | $\rho$        | (Latijns) $P$   |
| Sigma      | `$\sigma$`   | $\sigma$      | $\Sigma$        |
| Tau        | `$\tau$`     | $\tau$        | (Latijns) $T$   |
| Upsilon    | `$\upsilon$` | $\upsilon$    | $\Upsilon$      |
| Phi        | `$\phi$`     | $\phi$        | $\Phi$          |
| Chi        | `$\chi$`     | $\chi$        | (Latijns) $X$   |
| Psi        | `$\psi$`     | $\psi$        | $\Psi$          |
| Omega      | `$\omega$`   | $\omega$      | $\Omega$        |


## Uitdrukkingen 
Functies in latex zoals machten en fracties maken gebruik van accolades (`{}`), binnen deze kunnen ook andere uitdrukkingen gezet worden om op deze manier meerdere functies te combineren:

```
$$
T = \sqrt{2\times\frac{Hoogte}{Versnelling}}
$$
```

Resultaat:
$$
T = \sqrt{2\times\frac{Hoogte}{Versnelling}}
$$

### Fracties
Een fractie kan binnen LaTeX aangegeven worden met behulp van de `\frac` tag gevolgd door 2 paar accolades (`{}`). De inhoud van de eerste accolade verschijnt boven de deelstreep terwijl de inhoud van de tweede accolade onder de deelstreep komt.

```
De dichtheid is te berekenen met: $\frac{Gewicht}{Volume}$
```

Resultaat:
De dichtheid is te berekenen met: $\frac{Gewicht}{Volume}$

### Machten
Machten kunnen met behulp van een caret-symbool (`^`) aangegeven worden. Het getal of stuk tekst links wordt het grondtal en de tekst rechts van het symbool wordt de exponent.

```
$2^{16}$
```

Resultaat:
$2^{16}$

### Wortels
Wortels kunnen gemaakt worden met behulp van do `\sqrt` tag, deze zet het getal of stuk tekst binnen de eerstvolgende accolades (`{}`) of getal onder een wortel:

```
$$
\sqrt{15}
$$
```

Resultaat:
$$
\sqrt{15}
$$

Het is ook mogelijk een exponent mee te geven. Deze kan meegegeven worden door binnen vierkante haakjes (`[]`) een getal mee te geven. Deze worden na de tag maar voor de radicand (getal waarvan wortel genomen wordt):

```
$$
\sqrt[4]{256}
$$
```

$$
\sqrt[4]{256}
$$

### Logaritmes
Binnen LaTeX kunnen logaritmes gecreëerd worden met behulp van do `\log` tag. Een basis kan meegegeven worden na een underscore (`_`) voor het argument van het logaritme.

$$
log_{10}(100)
$$

>[!tip] Basis van logaritmes
>
>Probeer altijd een basis mee te geven aan een logaritme. Dit voorkomt verwarring omdat de "standaard" basis 10 of $e$ kan zijn.

### Sommatie en Product
Sommatie en Producten kunnen gemaakt worden met de `\sum` en `\prod` tags. Met behulp van een underscore (`_`) en caret-symbool (`^`) kunnen de term en index respectievelijk aangegeven worden:

```
$$
\sum_{i=0}^{5}i*2
$$

$$
\prod_{i=1}^{5}i*3
$$
```

Resultaat:
$$
\sum_{i=0}^{5}i*2
$$

$$
\prod_{i=1}^{5}i*3
$$

## Matrices
Binnen LaTeX kan een matrix gemaakt worden. dit kan met behulp van de `\begin{matrix}` en `\end{matrix}` tags die om de tekst van de matrix heen gezet worden. 

De inhoud van de matrix wordt aangeven door `&` tussen de waardes op dezelfde rij te zetten en `\\` om een nieuwe rij te beginnen:

```
$$
\begin{matrix}
a & b \\
c & d
\end{matrix}
$$
```

Resultaat:

$$
\begin{matrix}
a & b \\
c & d
\end{matrix}
$$

Ook zijn er verschillende soorten scheidingstekens mogelijk. deze zijn te selecteren door de start en end tags aan te passen:

```
$$
\begin{Bmatrix}
a & b \\
c & d
\end{Bmatrix}
$$
```

Resultaat:

$$
\begin{Bmatrix}
a & b \\
c & d
\end{Bmatrix}
$$

![[matrix_format.png]]

## Inline matrix
Voor kleine matrixes is het ook mogelijk om `{smallmatrix}` te gebruiken. deze matrix past binnen regels tekst:

```
De matrix is: $\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}$
```

Resultaat:

De matrix is: $\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}$

net zoals bij normale matrixes kunnen p, b, B, v en V hiervoor gezet worden om scheidingstekens toe te voegen.

![[inline_matrix_format.png]]

> Leesbaarheid smallmatrix \
> Smallmatrix is niet altijd goed leesbaar, probeer hier voor slechtziende gebruikers rekening mee te houden.

