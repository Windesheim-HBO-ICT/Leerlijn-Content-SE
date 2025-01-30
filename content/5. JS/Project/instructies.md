---
title: Project instructies
tags:
  - Project
difficulty: 3
---

# 1. JavaScript Project
Ter afsluiting van de JavaScript deeltaken gaan jullie een todo-lijst app maken. Dit gaan we doen met Web Components. Het project gaat in op het gebruik van verschillende aspecten zoals behandeld in de deeltaken. Informatie over Web Components kan je [hier](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) vinden.

## Opzet project
Voor dit project wordt er aangeraden om Visual Studio Code te gebruiken met de [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) plugin. 

### Structuur
Voor dit project wordt verwacht dat je de code als componenten maakt, die elk verantwoordelijk is voor een deel van de logica. Om je hier bij te helpen raden we je aan de volgende structuur aan te houden.

```
app/
├── index.html
├── style.css
├── script.js
└── components/
    ├── todo-app.js
    ├── todo-list.js
    ├── todo-item.js
    └── todo-filter.js
```

## Requirements
Hieronder de lijst met requirements waar de app aan moet voldoen.

***ToDo Lijst Component***
- De app moet een `todo-list` Web Component bevatten dat alle taken weergeeft.
- Het component moet taken kunnen toevoegen, verwijderen, en markeren als voltooid.
- Elke taak wordt weergegeven als een `todo-item` Web Component met een checkbox en verwijderknop.
- Gebruik Shadow DOM om de stijlen van de componenten te isoleren.

***Taken Beheren met Local storage***
- De app moet de taken persistent opslaan in de browser via Local Storage, zodat ze bij een herlaad van de pagina behouden blijven.
- De `todo-list` component moet bij het laden van de pagina taken inlezen uit Local Storage en weergeven.
- Veranderingen in de takenlijst (zoals toevoegen of verwijderen) moeten automatisch worden opgeslagen in Local Storage.

***Asynchrone data-opslag en ophalen met promises***
- De interactie met Local Storage moet worden afgehandeld via een wrapper met Promises, om asynchrone operaties te simuleren en uitbreidbaarheid naar echte API-calls mogelijk te maken.
- Bij het opslaan of ophalen van taken uit Local Storage moet de app gebruik maken van Promises, waarbij successen en fouten op de juiste manier worden afgehandeld.

***Event-Driven architectuur***
- De `todo-list` component moet Event Listeners gebruiken om te reageren op gebruikersacties, zoals het toevoegen van een taak, het verwijderen van een taak, en het markeren van een taak als voltooid.
- Elk `todo-item` moet zijn eigen Event Listeners hebben voor acties zoals het aanvinken van de checkbox (om de taak als voltooid te markeren) en het klikken op de verwijderknop.
- Gebeurtenissen die plaatsvinden in een `todo-item` moeten naar de `todo-list` worden gebubbeld zodat de lijst correct wordt bijgewerkt.

***Taak filteren en sorteren***
- De app moet gebruikers de mogelijkheid bieden om taken te filteren op status (alle, voltooid, onvoltooid).
- De filteropties moeten worden weergegeven in een apart Web Component (`todo-filter`) en moeten via Event Listeners wijzigingen doorgeven aan de `todo-list`.
- Taken moeten gesorteerd kunnen worden op basis van hun status of aanmaakdatum, met ondersteuning voor zowel oplopende als aflopende sortering.

## Code 
Vind hieronder de beginsituaties voor de bestanden. Dit helpt je een beetje op weg.

***index.html***
```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>To-Do App</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <todo-app></todo-app>
    <todo-filter></todo-filter>
    <script type="module" src="./components/todo-app.js"></script>
  </body>
</html>
```

***todo-app.js***
```javascript
import './todo-list.js';
import './todo-filter.js';

class TodoApp extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = `
      <todo-list></todo-list>
    `;
  }
}

customElements.define('todo-app', TodoApp);
```

***todo-list.js***
```javascript
import './todo-item.js';

class TodoList extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = `
      <style>
        ul {
          list-style: none;
          padding: 0;
        }
      </style>
      <ul></ul>
      <input type="text" placeholder="Nieuwe taak..." id="new-todo">
      <button id="add-todo">Toevoegen</button>
    `;
    this.currentFilter = 'all'; // Standaard filter
  }
}

customElements.define('todo-list', TodoList);
```

***todo-item.js***
```javascript
class TodoItem extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = `

    `;
  }

}

customElements.define('todo-item', TodoItem);
```

***todo-filter.js***
```javascript
class TodoFilter extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = `
    `;
  }
}

customElements.define('todo-filter', TodoFilter);
```

