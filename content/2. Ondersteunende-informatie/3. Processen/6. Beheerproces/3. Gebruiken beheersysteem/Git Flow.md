---
title:
  - Git Flow
taxonomie:
  - bg-24.1.Branching-strategiën.OI
  - bg-24.2.Git-Flow.OI
---

## Wat is Git Flow?
Git Flow is een van de populaire [[Branching strategiën]] voor Git, geïntroduceerd door Vincent Driessen in 2010. Het helpt bij het beheren van releases en het organiseren van de ontwikkeling van softwareprojecten. Git Flow gebruikt de volgende branches.
![[git-flow.png]]
De belangrijkste onderdelen van Git Flow:
- **Main Branch**: Bevat de code voor productie. 
- **Develop Branch**: Hier worden alle nieuwe features en verbeteringen samengevoegd voordat ze naar de main branch gaan.
- **Feature Branches**: Voor het ontwikkelen van nieuwe features. Deze worden gemaakt vanaf de develop branch en hiermee samengevoegd wanneer de feature klaar is.
- **Release Branches**: Voorbereiding van een nieuwe release. Hier worden laatste aanpassingen en bugfixes gedaan voordat de code naar de main branch gaat.
- **Hotfix Branches**: Voor snelle fixes van kritieke bugs in de productiesoftware. Deze worden direct vanaf de main branch gemaakt en na de fix met main samengevoegd.

## Waarom gebruik je Git Flow?
De belangrijkste redenen om Git Flow te gebruiken zijn:
**Structuur en Organisatie**: Git Flow biedt je een duidelijke structuur voor het beheren van branches, wat vooral handig is als je met meer ontwikkelaars samenwerkt of complexe taken hebt. Het maakt duidelijk onderscheid tussen verschillende soorten taken (features, releases, hotfixes) en zorgt ervoor dat je weet waaraan je werkt.

**Parallel Ontwikkelen**: Met Git Flow kun je met meerdere ontwikkelaars tegelijkertijd aan verschillende features werken zonder dat je elkaar in de weg te zit. Dit komt doordat elke feature zijn eigen branch heeft, die pas wordt samengevoegd met de develop branch wanneer de feature klaar is.

**Stabiele Releases**: Door gebruik te maken van release branches, kun je ervoor zorgen dat de code in de main branch altijd stabiel en klaar voor productie is. Dit maakt het makkelijker om nieuwe versies van de software uit te brengen zonder onverwachte problemen.

**Hotfixes**: Git Flow maakt het eenvoudig om snel kritieke bugs in de productie op te lossen door hotfix branches te gebruiken. Deze kun je direct vanaf de main branch maken en na de fix snel doorvoeren.

**Samenwerking en CI/CD**: Hoewel Git Flow soms uitdagend kan zijn in combinatie met Continuous Integration/Continuous Deployment (CI/CD), biedt het je een solide basis voor samenwerking en versiebeheer. Het helpt je om gestructureerd en efficiënt te werken .

## Hoe gebruik je Git Flow?
Al je Git Flow wilt gebruiken kun je onderstaande stappen in je project uitvoeren:

1. **Initialiseer Git Flow**: 
a. Ga naar je projectdirectory en voer het volgende commando uit om Git Flow te initialiseren:  
	 ```
	 git flow init 
	 ```
b. Volg de prompts om de standaard branchnamen te accepteren of aan te passen.
	
2. **Maak een Feature Branch**: 
a. Start een nieuwe feature branch vanaf de develop branch: 

```
git flow feature finish naam-van-feature
```

b. Werk aan je feature en commit je wijzigingen zoals gewoonlijk:

```
git add .
git commit -m "Beschrijving van de wijziging"
```

3. **Voltooi een Feature Branch**: 
a. Wanneer je klaar bent met de feature, voltooi je de branch en merge je deze terug naar develop:

```
git flow feature finish naam-van-feature
```
4. Maak een Release Branch:
a. Wanneer je klaar bent om een nieuwe versie uit te brengen, start je een release branch vanaf develop:

```
git flow release start versie-nummer
```
b. Voer laatste bugfixes en aanpassingen door, commit deze, en voltooi de release:
```
git flow release finish versie-nummer
```

5. Maak een hotfix branch:
a. Voor kritieke bugfixes in productie, start je een hotfix branch vanaf main:
```
git flow hotfix start naam-van-hotfix
```

b. Voer de benodigde fixes door, commit deze, en voltooi de hotfix:
```
git flow hotfix finish naam-van-hotfix
```

Deze stappen helpen je om je werk te organiseren en zorgen ervoor dat je altijd een stabiele versie van je project hebt





