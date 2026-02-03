AgriTech4 – Project Work

Questo repository contiene il codice sorgente e il materiale di supporto del Project Work AgriTech4, sviluppato per la facoltà di informatica per le aziende digitali Università Telematica Pegaso.

Il progetto riguarda la realizzazione di un middleware asincrono basato su broker di messaggistica, applicato a uno scenario agri-tech per il monitoraggio e il controllo di processi agricoli simulati.

Struttura del progetto

- src/
  Codice sorgente del middleware
  - common/
    Configurazione e funzioni comuni
  - producer/
    Simulazione dei sensori
  - consumer/
    Consumer di monitoraggio
  - consumer/
    Consumer di controllo
  - consumer/
    Consumer attuatore

- dashboard/
  Dashboard di visualizzazione dei dati

- screenshot/
  Screenshot e materiale di supporto

- requirements.txt
  Dipendenze Python

Descrizione generale

Il sistema simula un ambiente agricolo in cui i sensori producono dati di telemetria, elaborati da diversi componenti software che comunicano tramite messaggi asincroni. La comunicazione asincrona consente di mantenere i componenti disaccoppiati e modulari.

Note

Il progetto ha finalità didattiche ed è di visibilità pubblica. I dati utilizzati sono simulati e non provengono da sensori reali.

Autore

Nicola Regoli
