---
title: Fetch API
taxonomie: None
tags:

---### Fetch API
De **Fetch API** biedt een eenvoudige en krachtige manier om HTTP-aanvragen te doen. **Async/await** maakt het werken met asynchrone operaties intuïtiever door de code er synchrone uit te laten zien. Dit verhoogt de leesbaarheid en vereenvoudigt de foutafhandeling.

**GET**
Een GET-aanvraag haalt gegevens van een server op.

```javascript
// Asynchrone functie om gegevens op te halen
async function fetchData() {
  try {
    const response = await fetch("https://api.example.com/data");

    // Controleer of het antwoord succesvol was
    if (!response.ok) {
      throw new Error(`Netwerk antwoord was niet oké: ${response.statusText}`);
    }

    // Verwerk het antwoord als JSON
    const data = await response.json();
    console.log(data);

  } catch (error) {
    console.error("Er was een probleem met de fetch-operatie:", error);
  }
}

fetchData();
```

**POST**
Een POST-aanvraag verstuurt gegevens naar een server.
```javascript
// Asynchrone functie om gegevens te versturen
async function postData() {
  try {
    const response = await fetch("https://api.example.com/data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        naam: "Alice",
        leeftijd: 25
      })
    });

    // Controleer of het antwoord succesvol was
    if (!response.ok) {
      throw new Error(`Netwerk antwoord was niet oké: ${response.statusText}`);
    }

    // Verwerk het antwoord als JSON
    const data = await response.json();
    console.log("Succes:", data);

  } catch (error) {
    console.error("Fout:", error);
  }
}

postData();
```
