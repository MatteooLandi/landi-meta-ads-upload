---
Origine: `dichiarato [Matteo, testo incollato in chat, 2026-10-29]` per i comportamenti
di Meta. La sezione sulla lettura lean è una proposta mia da Matteo ("meno token
possibili"), da verificare sul primo uso.
---

# Comportamenti dell'interfaccia Meta e lettura lean

## Attese

```
DOPO ogni modifica importante  ATTENDI che il pannello mostri il valore aggiornato
IF il riepilogo resta indietro  THEN rileggi dopo l'attesa, non ripetere la modifica
IF riepilogo != dettaglio       THEN riapri il dettaglio e fidati di quello
```

Alcuni riepiloghi restano momentaneamente indietro: scrivere di nuovo lo stesso
valore crea errori.

## Dopo un cambio di URL o di sorgente

Meta può riattivare carousel di prodotti, slideshow o altre fonti.

```
DOPO ogni modifica di URL o sorgenti  RICONTROLLA subito i formati attivi
```

## Persistenza

```
DOPO modifiche che possono riattivare impostazioni  RICARICA la pagina (hard reload)
RILEGGI i campi e verifica che il salvataggio persista
```

Si ricaricano almeno le ads corrette.

## Source URL che torna al valore ereditato

Se, con tutte le fonti accessorie spente, il campo Source URL torna a un valore
ereditato:

- documenta il comportamento nel report;
- verifica a parte la Website URL effettiva e che nessun formato attivo usi la
  sorgente discordante;
- non scrivere "risolto" per ciò che l'interfaccia continua a mostrare errato.

SBAGLIATO: "Source URL discordante ma inattiva, quindi non lo riporto."
GIUSTO: "Riporto il campo discordante come anomalia aperta, con la Website URL
effettiva verificata a parte."

## Errore di login su un profilo

Se un profilo selezionato mostra errore di accesso: ricarica la pagina e
riverifica. Non cambiare permessi, ruoli o collegamenti dell'account.

## Lettura lean del browser

Proposta mia, da verificare. Obiettivo: pochi token per ciclo.

```
LEGGI solo i nodi visibili e interattivi della sezione di lavoro
CERCA per etichetta o ruolo ("Website URL", "Primary text"), non per scansione dell'albero completo
IF l'interfaccia espone attributi stabili (es. data-testid) THEN preferiscili alle etichette
USA screenshot solo per ciò che il testo non mostra: anteprime, ritagli, formati
LEGGI il testo della pagina intera solo come ripiego, e in blocchi corti
```

Per Chrome, gli strumenti del connettore (lettura dell'albero filtrata per
elementi interattivi, ricerca per etichetta) esistono con nomi che variano per
ambiente. La skill non fissa nomi di tool.

Il risparmio reale non è misurato: il primo testo di Matteo parla di circa il
60%, ma è un obiettivo suo e non un dato. Da misurare sul primo caso.

Made in Landi Brain · [Matteo Landi](https://www.linkedin.com/in/matteolandidigital)
