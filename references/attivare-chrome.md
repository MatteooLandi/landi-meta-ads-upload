---
Origine: proposta di un progetto cliente del 2026-11-05 (un caso su un solo output),
approvata da Matteo il 2026-11-20 (`dichiarato`). La formulazione è `inferito`.
---

# Chrome non disponibile: guida passo per passo

Succede quando la skill gira in una chat dell'app Claude Desktop: lì gli strumenti
Chrome non sono caricati. Il comando `/chrome` e `claude --chrome` esistono solo in
una sessione Claude Code. Chi legge una schermata `/chrome` di un'altra sessione la
scambia facilmente per quella della chat.

```
SE gli strumenti Chrome mancano  CONTROLLA prima i connettori della sessione (stato e riconnessione)
IF dopo il controllo mancano ancora  THEN dillo subito: "questa chat dell'app non ha Chrome"
POI   indica dove aprire la sessione giusta e consegna la richiesta già pronta, con account e cartella
```

## Cosa dire a Matteo, in chat

1. Questa chat non può pilotare Chrome. Serve una sessione Claude Code con Chrome.
2. Dove aprirla: nell'app Claude Desktop, scheda Code, nel pannello Terminale
   dell'app, nella cartella del progetto. Si scrive `claude --chrome`. Se la
   sessione è già aperta, si scrive `/chrome`.
3. Prerequisiti: estensione Claude in Chrome installata con lo stesso account
   Claude, Chrome aperto con l'accesso a Meta già fatto.
4. La richiesta da incollare nella nuova sessione (la skill compila i campi con i
   dati già detti in chat):

```text
Usa la skill meta-ads-upload.
Account pubblicitario: <link diretto all'account in Ads Manager>
Campagna e adset: <nome, nuovo o esistente>
Cartella delle creatività: <percorso della cartella>
Cartella del progetto: <percorso del progetto in cui aprire la sessione>
Stato: bozza.
```

Il Terminale è un ripiego e la skill dice perché: serve perché solo una sessione
Claude Code carica gli strumenti Chrome. Non esiste ancora una via dall'interfaccia
dell'app per questo (`sconosciuto`: da ricontrollare quando l'app cambia).
