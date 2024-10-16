---
title: Geolocation API
taxonomie: None
tags:

---### Geolocation API
De **Geolocation API** biedt toegang tot de geografische locatie van de gebruiker, mits toestemming wordt gegeven.

**Locatie opvragen**
```javascript
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition((positie) => {
    console.log(`Breedtegraad: ${positie.coords.latitude}`);
    console.log(`Lengtegraad: ${positie.coords.longitude}`);
  }, (fout) => {
    console.error(`Foutcode: ${fout.code}, Bericht: ${fout.message}`);
  });
} else {
  console.log("Geolocatie niet ondersteund door deze browser");
}
```

**Instellingen**

Je kunt opties zoals `timeout` (maximale wachttijd voor een antwoord) en `maximumAge` (maximum leeftijd van een opgeslagen positie) instellen.
```javascript
navigator.geolocation.getCurrentPosition(succesCallback, errorCallback, {
  timeout: 10000,
  maximumAge: 60000,
  enableHighAccuracy: true
});
```

