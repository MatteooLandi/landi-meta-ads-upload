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

Dopo il ricarico, in un caso reale (`verificato`, 2026-11-06), su ads con
destinazione Website la CTA scelta era tornata a "See details" e la Website URL
aveva in coda `?fbclid=fbclid` (Meta lo scrive aprendo l'anteprima del link).

```
DOPO il ricarico  RILEGGI CTA e Website URL di ogni ad
IF CTA tornata a "See details"  THEN reimposta la CTA voluta
IF URL con ?fbclid=fbclid in coda  THEN riscrivi l'URL pulita e riverifica
```

## Escape nell'editor (`verificato`, 2026-11-06)

Premere Escape nell'editor apre il dialogo "Publish draft items?" e chiude
l'editor.

```
NON usare Escape nell'editor. Per chiudere un popover clicca in un'area vuota
IF compare "Publish draft items?"  THEN chiudi con "Close", mai con Publish
```

## Duplicare una ad con destinazione Website (`verificato`, 2026-11-06)

Il dialogo di duplicazione pre-spunta raccomandazioni come "Add an image".
Togli la spunta prima di confermare, in coerenza con Single media e con "non
attivare ciò che le ads di riferimento non hanno".

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

## Creatività su Google Drive (`inferito`, una sessione del 2026-11-12)

Base: una proposta di un progetto cliente, un solo caso su un solo output. Se le
creatività stanno in una cartella Drive, l'agente non le scarica né con il
connettore Drive né con `curl`. Il Chrome di Matteo è già connesso a Drive.

```
IF le creatività stanno su Drive  THEN apri il link di download di ogni file in una scheda Chrome, poi sposta i file scaricati in una cartella pulita
POI   usa quella cartella come cartella indicata da Matteo (metodo "Caricare i file da disco")
IF il download non parte  THEN dillo e chiedi a Matteo di scaricare i file nella cartella Download
```

## Più browser collegati all'estensione (`inferito`, stessa sessione)

Con più browser collegati all'estensione Claude in Chrome, il primo può non
rispondere.

```
IF lo strumento Chrome non risponde e risultano più browser collegati  THEN prova l'altro browser prima di dichiarare Chrome non disponibile
```

## Dialogo dei media: si chiude solo con Done (`inferito`, stessa sessione)

Nel dialogo dei media, premere Esc lo chiude senza applicare le modifiche fatte
nei passi successivi (Text, Enhancements e gli altri). Vale la regola già scritta
per l'editor: Esc non si usa.

```
NEL dialogo dei media  CHIUDI sempre con Done, mai con Esc
DOPO Done  RIAPRI il dettaglio della ad e verifica che le selezioni siano rimaste
```

## Dopo il cambio dei media: Meta riattiva formati e tag (`inferito`, stessa sessione)

Sostituendo video con immagini (`verificato`, 2026-11-27) Meta riattiva anche Format display options 3/3 (Carousel e Collection), Advantage+ creative enhancements (Add overlays, Visual touch-ups) ed Essential enhancements. Rifai la pulizia e rileggi i contatori.

Dopo aver cambiato i media, Meta può riattivare Carousel, Collection e i tag
prodotto. Con i tag prodotto attivi, l'interruttore Product browsing resta
bloccato su On e non si spegne finché i tag non sono tolti.

```
DOPO il cambio dei media  CONTROLLA Format display options (deve essere 1/3), Product browsing (Personalized destinations 0/4) e i tag prodotto
IF Product browsing resta bloccato su On  THEN togli prima i tag prodotto, poi spegni Product browsing e riverifica
```

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

Limite del tool di upload: 10 MB per chiamata (`verificato`, 2026-11-06, video
da 94 e 145 MB rifiutati). I video verticali 4K lo superano quasi sempre, e il
fetch da un server locale è bloccato dalla pagina Meta. Non si aggira. Un invio a
blocchi non è stato provato e non fa parte della skill: l'unica via verificata è
il caricamento manuale nella libreria.

```
NEL pre-flight, SE un file supera 10 MB  AVVISA subito e chiedi a Matteo di caricarlo nella libreria media prima di iniziare, poi prendilo da lì
```

Senza un media già scelto, l'editor non permette di inserire i testi della ad:
conviene far caricare i file prima di compilare.

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

Le modifiche valgono per tutte le ads selezionate (`verificato`, 2026-11-06):
se un valore deve differire da ad a ad (testo, destinazione, CTA), seleziona
una ad per volta.

## Bozze in altri adset: copia e incolla (2026-11-27, `verificato`)

- Il Duplicate rapido copia solo nello stesso adset. Per portare bozze in altri
  adset: seleziona le bozze, Cmd+C; apri la scheda Ad sets, seleziona uno o più
  adset di destinazione, Cmd+V. Meta crea una copia per ogni adset selezionato.
- Gli appunti restano nella pagina aperta. Un cambio URL o un ricarico li svuota
  e Meta risponde "You haven't copied any items". Copia e incolla nella stessa
  sessione.
- Cmd+V nella vista Ads apre "Duplicate your ads": con Cancel si chiude senza
  copiare.
- Le copie restano bozze. Il nome finisce con " - Copy" e va corretto.

## Nomi e date in modifica multipla (2026-11-27, `verificato`)

- Il nome digitato nell'editor singolo può non salvarsi. Rileggi la lista ads
  dopo il ricarico.
- Nella tabella multipla i valori si digitano con i tasti. Quelli impostati da
  script non restano.
- Data di fine: "Edit all selected ads", poi Ongoing, poi End on, data, ora. Ore,
  minuti e AM/PM si impostano per segmento (Backspace e digita; ArrowUp o
  ArrowDown per cambiare AM/PM). Dopo il salvataggio riapri il pannello e leggi
  la data di ogni ad.
- Website URL: un valore impostato in "Edit all selected ads" vale per tutte.
  Controlla ogni gruppo di posizionamenti dal menu a tendina.

## Batch del browser

Un batch con più di circa quindici azioni, o con attese lunghe, può non
rispondere. Spezzalo in blocchi corti e rileggi lo stato dopo ogni blocco.

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
