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

## Uscire dall'editor: solo Save draft (un caso reale, 2026-11-05)

Dopo modifiche alle bozze, chiudere l'editor con la X in alto a sinistra ha
mostrato "Publishing 1 of 3" e poi "3 ads were published": le ads sono
risultate attive. La schermata di scelta non è stata vista. La skill non
pubblica mai, quindi:

```
QUANDO esci dall'editor dopo modifiche  compare una schermata: scegli "Save draft"
NON premere "Publish", "Preview to publish" né altro pulsante di pubblicazione
```

Uscita senza pubblicare (`dichiarato: Matteo, 2026-11-05`: "basta che fai save
draft senza cliccare publish quando esce la schermata"). Se la schermata non
compare e parte "Publishing", si dice subito in chat e si propone di mettere le
ads in pausa. La pausa non si fa senza il suo ok.

Matteo autorizza la skill a uscire dall'editor con "Save draft" a fine lavoro
(`dichiarato: Matteo, 2026-11-05`: "prossima volta esci tu dall'editor con save
draft"). Se la sessione nega comunque il clic sulla X, ci si ferma e si spiega,
senza aggirare il blocco.

## Caricare i file da disco

Matteo vuole che sia la skill a caricare i file dalla cartella indicata
(`dichiarato: Matteo, 2026-11-05`: "vorrei andassi tu nella cartella in
download per caricare i file"). Meta crea l'input file solo al clic su
"Upload", e il selettore nativo è una finestra del browser: il controllo
desktop tiene i browser in sola lettura (niente clic né tasti), quindi quel
selettore non si pilota. Il metodo che funziona non lo usa (`verificato`,
2026-11-05, 6 file in un passaggio):

```
COPIA   i file della cartella indicata da Matteo nella cartella temporanea della sessione (il tool di upload legge solo cartelle della sessione)
PAGINA  nel media picker, prima del clic su Upload, esegui in pagina lo snippet sotto: l'input file resta nel documento e il selettore nativo non si apre
CLIC    su "Upload"
CERCA   l'input file creato (ricerca "file input") e passa tutti i file al tool di upload in una sola chiamata
POI     i file compaiono nella libreria già selezionati: togli quelli che non servono alla ad
IF non riesce  THEN dillo e chiedi a Matteo di caricare i file nella libreria media dell'account, scheda Account
```

```js
const orig = HTMLInputElement.prototype.click;
HTMLInputElement.prototype.click = function () {
  if (this.type === 'file') { document.body.appendChild(this); return; }
  return orig.apply(this, arguments);
};
```

Nella libreria ci sono file di campagne vecchie con lo stesso nome (`1.png`,
`2.png`). Si riconoscono quelli nuovi per dimensione e per posizione (i più
recenti compaiono per primi) e si controlla l'anteprima prima di confermare. Un
clic sulla miniatura può solo passare il mouse: la selezione è avvenuta quando
sotto compare "1 selected".

## Nome della ad (`inferito`, 2026-11-05)

- La modifica massiva "Edit each ad" > Name con un campo per ad funziona, se si
  clicca fuori dal campo prima di salvare.
- Nell'editor il campo "Ad name" può non aggiornarsi passando da una bozza
  all'altra, e un valore impostato da tool può non restare. Il riscontro vero è
  la lista ads, non il campo.
- Dopo ogni rinomina si rilegge la lista e si controlla che i nomi siano
  unici e che ciascuno corrisponda alle sue immagini. Una rinomina fatta a
  vista ha creato due ads con lo stesso nome.

## Modifica di più ads insieme

Selezionando più bozze nella barra laterale ("Your edits will apply to 3 ads")
si cambiano insieme voci come Product browsing. Il pannello Format display
options e il nome richiedono la singola ad o "Edit each ad".

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
