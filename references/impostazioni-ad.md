---
Origine: `dichiarato [Matteo, testo incollato in chat e risposte all'intervista,
2026-10-29]`. La regola sugli enhancement è un'inferenza da due sue frasi,
marcata sotto.
---

# Impostazioni di ogni ad

## Formato: solo Single media, nient'altro

Regola (`dichiarato: Matteo, 2026-11-05`: "togli product browsing, e lascia
esclusivamente single media"):

```
ATTIVO   solo "Single image or video" (o "Single media", come scrive l'interfaccia)
SPENTO   Carousel | Collection | Video slideshow | varianti con prodotti o dettagli di app store
SPENTO   Product browsing
SPENTO   prodotti, media correlati, tag prodotto, ogni fonte che aggiunge prodotti o link non richiesti
```

I tag prodotto e i media correlati ereditati da altre ads si rimuovono sempre.

### Dove si spegne (`inferito`, provato su un caso reale, 2026-11-05)

Il riscontro finale è sempre sulla singola ad, dopo il ricarico:

- **Product browsing**: sezione "Personalized destinations", deve risultare
  `(0/4)`. In modifica massiva ("Edit each ad", voce "Product browsing") si
  toglie la spunta "Use product browsing to personalize buyer journey" su
  "Edit all selected ads" e si controlla ogni riga.
- **Carousel e Collection**: sezione "Ad experiences", riga "Format display
  options", pulsante Edit. Nel pannello Carousel si tolgono "Show products" e
  "Show app store details"; nel pannello Collection "Show products" e "Show
  site links". Ogni pannello deve mostrare `0 of 2 enabled`. In Single media il
  collage "Show mixed media" resta spento. Esito atteso: "Format display
  options (1/3)", con acceso solo Single media. Il pannello non compare nella
  vista con più ads selezionate: si fa ad per ad.
- **Duplicazione**: nella finestra "Duplicate your ad" si toglie la spunta
  "Add relevant products to this ad" prima di continuare.
- **Raccomandazioni pre-spuntate** (`dichiarato: Matteo, 2026-11-05`: "quando
  vedi quei suggerimenti despuntali"): nei dialog di duplicazione di adset e di
  ad Meta propone raccomandazioni già spuntate (Advantage+ sull'audience,
  conversion location, prodotti accanto ai media). Si tolgono tutte prima di
  Continue o Duplicate. Dopo il clic il dialog si sposta e il pulsante cambia
  nome: rileggere la posizione prima di cliccare.
- **Suggerimenti** come "8% lower Cost per Action (CPA) by showing products": si
  ignorano, vale "Apply now" non cliccato.
- **Ad sources** (Site links, Products): si spengono entrambi
  (`dichiarato: Matteo, 2026-11-05`: "si spegni"). Sezione "Ad experiences",
  riga "Ad sources", pulsante Edit. Esito atteso: 0 attivi.

## Enhancement

Regola (`dichiarato: Matteo, 2026-11-05`, confermata: "sì esatto"):

```
ATTIVI = gli enhancement già attivi nelle ads di riferimento dell'account
         (di solito solo "Relevant comments" ed "Enhance CTA")
SPENTI = ogni altro enhancement e ogni generazione con AI
IF Matteo ne chiede uno esplicitamente THEN attivalo per quel caso
```

Precisazioni (`dichiarato: Matteo, 2026-11-05`): "Text improvements" resta
spento. "Video touch-ups" può restare attivo.

Le frasi: "enhancements attivi (di solito solo relevant comments e cta)" e "non
attivare cose che non ci siano nelle altre ads a meno che non sia richiesto".

## Suggerimenti di Meta

I suggerimenti con pulsante "Apply now" non sono impostazioni attive. Si
ignorano. Non si applicano perché compaiono nel pannello.

## Browser add-on

Non si aggiungono, salvo che l'account li usi già nelle ads di riferimento e il
caso li richieda.

## Setup tecnico

Audience, ottimizzazione, attribuzione e tracciamento dell'adset non si
cambiano (`dichiarato: Matteo`).

## File per posizionamento

```
VIDEO verticale 9:16   già valido per tutti i posizionamenti (9:16, 1:1, 4:5)
VIDEO su orizzontale   il warning di Meta si ignora
```

Immagini, versioni già pronte nelle cartelle (`dichiarato`). La skill non
ritaglia.

| Posizionamenti | File atteso |
|---|---|
| Feed | 1:1 e 4:5 |
| Verticali (storie, reels e simili) | 9:16 |
| Orizzontale | Ritaglio che non taglia il testo più grande dell'ad; se possibile mostra il prodotto o parte di esso |

Priorità nel formato orizzontale (`dichiarato`): non tagliare il testo più
grande dell'ad.

```
IF manca l'1:1 THEN lascia il 4:5 (di solito ha la safe zone per l'1:1) e scrivi la riga nel report
IF il ritaglio automatico taglia il testo più grande THEN trascina l'inquadratura leggermente in alto o in basso per far rientrare il testo nella safe zone. Se non basta, segnala come anomalia. Non produrre file ritagliati
```

Le due regole sono `dichiarato: Matteo, 2026-11-05` ("sì" sull'1:1; "puoi draggare leggermente in alto o basso l'immagine per far rientrare il testo nella safe zone, se puoi fallo").

### Immagini: più formati nella stessa ad (`verificato`, 2026-11-05)

Nell'editor attuale "Customize media" > Crop non ha Replace: offre solo
"Original" e un ritaglio manuale che taglia l'immagine, e il pannello
Placements serve solo a escludere posizionamenti. Una ad statica con più file
(4:5, 1:1, 9:16, 1.91:1 se esiste) si compone così, dal media picker ("Change
selections" o "Edit media"):

```
PASSO Media     seleziona insieme tutti i file della stessa creatività
                Meta li riconosce come "Image group" (variazioni della stessa immagine) e assegna il file giusto a ogni posizionamento
                nel riepilogo in basso compare un solo gruppo, con "3 variations"
PASSI Text, Image generation, Video generation, Enhancements, Translation
                nessuna selezione, nessuna lingua, enhancement spenti. Poi Done
IF manca un formato (es. 1.91:1)  THEN resta il ritaglio automatico e si scrive nel report come non verificato
```

Per togliere un gruppo dalla selezione: riepilogo in basso, clic sul gruppo,
cestino, Confirm. Per una seconda creatività conviene duplicare la prima ad e
cambiare solo il gruppo di media.

Alla fine il crop di ogni ad si controlla a vista: il testo grande non deve
essere tagliato.

## Gruppi di posizionamenti

Meta può conservare il video della bozza duplicata in alcuni gruppi anche quando
l'anteprima principale mostra quello nuovo. Il file previsto deve comparire in
ogni gruppo pertinente.

SBAGLIATO: "Nel gruppo feed c'è il file giusto, quindi la ad è a posto."
GIUSTO: "Il file previsto compare nel gruppo feed, nel gruppo verticale e negli
altri gruppi pertinenti, uno per uno."

## Testi

- Inserisci testo principale, headline e description.
- Rileggi i valori salvati nella singola ad, non quelli digitati.

Made in Landi Brain · [Matteo Landi](https://www.linkedin.com/in/matteolandidigital)
