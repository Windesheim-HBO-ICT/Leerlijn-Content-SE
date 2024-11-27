---
title:
  - OTAP
taxonomie:
  - bb-25.1.Volledigheid-ontwikkelstraat.OI
---
## Wat is OTAP?
OTAP staat voor de vier fasen in de softwareontwikkeling. Er wordt ook wel gesproken over een 'OTAP-straat'. De o staat voor ontwikkeling, dit doe je in een ontwikkelomgeving. Zo hebben de andere stakeholders als testers en superusers geen last van functionaliteiten die nog niet klaar zijn. Zodra je hiermee klaar bent kan de software doorgezet worden naar de volgende fase, namelijk de t van Test. Het testen wordt uitgevoerd door de testers in een aparte omgeving, namelijk de testomgeving. Deze omgeving bevat alle componenten die straks ook in het echt nodig zijn, maar met eigen gegevens, zodat de testscenario's kunnen worden uitgevoerd zonder dat de superusers of acceptanten hier last van hebben. Zodra de testfase voorbij is dan kan de software worden doorgezet naar de acceptanten ter acceptatie (daar staat de a dus voor). Dit gebeurd in een acceptatie omgeving. Dit is vaak een kopie van de productieomgeving waarin privacy gevoelige informatie is geanonimiseerd. Als de software acceptabel is kan het naar de laatste fase, namelijk de p van productie. Hierbij wordt de software naar de productieomgeving gebracht en in productie genomen. Kortom de software wordt pas beschikbaar gesteld aan eindgebruikers  zodra het uitgebreid is getest en de opdrachtgever akkoord heeft gegeven.

## Waarom gebruik je OTAP?
Werken volgens de OTAP-straat is heel belangrijk als je software ontwikkelt. Je wilt niet dat de eindgebruiker last heeft van tests of een onvolledige versie van de software te zien krijgt, inclusief mogelijke bugs. Door de OTAP-methode hebben Developers de ruimte en tijd om hun werk te doen en functies uitgebreid te testen voordat de software in productie gaat. Ook kan de opdrachtgever hierdoor feedback geven op de software voordat deze in gebruik wordt genomen.

## Hoe gebruik je OTAP?
Door vier verschillende omgevingen in te richten en die te markeren voor ontwikkeling, test, acceptatie of productie, is je OTAP-straat ingericht. De verschillende omgevingen werken met hun eigen versie van data, maar bij grote systemen ook op hun eigen infrastructuur! In de praktijk worden soms de ontwikkel en testomgeving gecombineerd vanwege de overhead die de testomgeving geeft en de ontwikkelaars het ook goed getest willen hebben (met dezelfde software als die waarmee getest wordt).

Als ontwikkelaar moet je er zelf voor zorgen dat de software wordt overgezet naar de juiste plek. Dan kan geautomatiseerd door tooling te gebruiken of de Visual Studio omgeving hierop aan te passen (b.v. deployment naar Azure kan gemakkelijk vanuit de IDE) . Om dit mogelijk te maken heb je een buildstraat nodig waarmee je je eigen onderdelen kunt bouwen en testen die vervolgens kunt samenvoegen met componenten van je teamgenoten (of andere ontwikkelaars).
Een goed model hiervoor zie je in het onderstaande plaatje:
![[Buildstraat.png]]

De laatste stap in dit proces is deploy. Als alle testen slagen kan de software worden doorgezet naar de testomgeving. Als de software door de testomgeving komt kan het worden doorgezet naar de acceptatieomgeving etc.
C# werk middels xcopy deployment principe. Met andere woorden de software kan eenvoudig vanuit de bin\release map worden gekopieerd naar de juiste plek.
Hoe dit in de praktijk gaat hangt sterk af van de soort omgeving die beschikbaar wordt gesteld als test-, acceptatie- of productieomgeving.