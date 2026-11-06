---
name: meta-ads-upload
description: Prepara come bozze in Meta Ads Manager le ads di un set di creatività (video e immagini) su qualunque account. Studia l'account, inventaria i file, abbina le URL, crea una ad per creatività e controlla ad per ad che nome, copy, link e impostazioni siano salvati. Da usare quando Matteo dice "carica queste creatività su Meta", "carica delle creative su Meta" o "prepara le bozze nell'adset". Non pubblica, non crea campagne né audience e non produce ritagli delle immagini (può solo spostare l'inquadratura di un ritaglio automatico per far rientrare il testo).
triggers:
  - "carica queste creatività su Meta"
  - "carica delle creative su Meta"
  - "carica queste creative su Meta"
  - "prepara le bozze in Ads Manager"
  - "fai il setup delle ads in questo adset"
  - "carica le ads nell'adset"
  - "upload questi video su Meta Ads"
  - "set up draft ads from this folder"
  - "upload these creatives to Meta Ads Manager"
prerequisites:
  files:
    - "Link diretto all'account pubblicitario in Ads Manager, dato da Matteo"
    - "Cartelle locali con le creatività da caricare"
  env:
    - "Chrome pilotabile dall'agente, nel browser di Matteo con la sessione Meta già attiva (dichiarato: Matteo, 2026-11-05). Strumento oggi dichiarato: solo Chrome. Da terminale: estensione Claude in Chrome installata con lo stesso account, poi `claude --chrome` oppure `/chrome` in una sessione aperta. Da app desktop: nuova sessione nella stessa cartella dopo l'installazione; se gli strumenti Chrome non compaiono, vale il terminale. Il browser integrato dell'app è un ripiego solo se Matteo vi ha fatto accesso a Meta"
    - "Python 3 per scripts/inventory.py. ffprobe e sips sono facoltativi (durata dei video, dimensioni delle immagini)"
inputs:
  - "Campagna e adset di destinazione, nuovo o esistente"
  - "Fonte del copy: file nuovo, oppure indicazione di dove prenderlo (altre ads dell'account, stesso adset). Se manca, si prende dall'account"
  - "URL di destinazione, se Matteo le fornisce (hanno la precedenza)"
  - "Vincoli del caso (anno nel naming, enhancement richiesti, prodotti da escludere)"
outputs:
  - "Ads in bozza nell'adset indicato, una per creatività"
  - "Report compatto in chat: file validi e bozze, duplicati, correzioni, tabella cartella o prodotto con URL, verifiche fatte, limiti aperti"
ranking_criteria:
  - "Numero di ads create uguale al numero di creatività valide inventariate, con il conteggio preso dall'inventario e non da una lista a video"
  - "Nessuna ad con nome duplicato o con il suffisso - copy"
  - "Ogni ad ha il proprio file, la propria URL di destinazione e il proprio copy, e nessuna punta al file di un'altra"
  - "Nessuna azione di pubblicazione eseguita: ogni ad resta in bozza"
  - "L'audit riporta un esito (ok, anomalia, non verificato) per ogni controllo di ogni ad"
  - "Nessun enhancement o formato attivo che le ads di riferimento dell'account non hanno, salvo richiesta di Matteo"
routing:
  next_skill_suggested: nessuna
  next_skill_condition: "Controllo manuale e pubblicazione sono di Matteo, fuori dalla skill"
stopping_conditions:
  - "Manca il link all'account, la campagna o la cartella delle creatività: pre-flight blocca e chiede"
  - "Stato richiesto diverso da bozza: si ferma, la pubblicazione non fa parte della skill"
  - "Chrome non è disponibile o la sessione Meta richiede il login: si ferma, lo dice e indica come attivare Chrome da terminale (`claude --chrome` o `/chrome`), non inserisce credenziali (dichiarato: Matteo, 2026-11-05)"
  - "Prodotto discordante tra cartella, file e contenuto, o URL ambigua: si ferma su quella riga e chiede"
  - "Copy non coerente con le creatività: si ferma e chiede"
  - "Naming dell'account non ricavabile: chiede a Matteo la struttura in chat"
  - "Account senza ads di riferimento: studia comunque e chiede conferma prima di creare"
preflight_check: enabled
---

# Meta Ads Upload

## Purpose

Trasforma una cartella di creatività in ads in bozza dentro un adset di Meta Ads
Manager, già coerenti con l'account, così che Matteo faccia solo il controllo
manuale e la pubblicazione.

## When to use

- Matteo ha creatività pronte (video o immagini) e vuole le ads in bozza su un
  account che ha già altre ads.
- Il lavoro è sempre lo stesso: cambiano naming, enhancement attivi e copy da
  account ad account, e vengono dallo studio dell'account (`dichiarato: Matteo`).

**NON usare quando**:

- Si deve pubblicare, fare preview to publish o attivare ads: fuori dalla
  skill (`dichiarato: Matteo`).
- Si crea una campagna, un'audience o un setup tecnico nuovo.
- Mancano le creatività finite. Per i brief ai grafici vale `landi-static-ads-brief`.
- Si tratta di un account o di cartelle di un altro cliente non indicati da Matteo.

## Prerequisites (pre-flight check)

```
IF link account assente           THEN STOP, chiedi
IF campagna o cartelle assenti    THEN STOP, chiedi
IF stato richiesto != bozza       THEN STOP, spiega che la skill non pubblica
IF Chrome non disponibile         THEN STOP, dillo e richiama il comando: scrivi a Matteo di lanciare `/chrome` nella sessione (o di aprirla con `claude --chrome`), poi riprendi
IF file sopra 10 MB               THEN avvisa subito: il tool di upload non li carica. Chiedi a Matteo di caricarli nella libreria media prima di iniziare
IF pagina di login Meta           THEN STOP, chiedi a Matteo di accedere. Mai credenziali
IF errore di accesso su profilo   THEN ricarica la pagina. Mai toccare permessi
```

## Inputs

Vedi frontmatter. Cartelle cliente: non si cerca fuori da quelle indicate da
Matteo.

## Regole trasversali

- **Bozza sempre.** Niente "Publish", "Preview to publish" o passaggi che
  possano pubblicare. Anche se l'interfaccia li propone. Uscendo dall'editor
  dopo modifiche si sceglie "Save draft" (`dichiarato: Matteo, 2026-11-05`):
  chiudere con la X ha pubblicato 3 ads in un caso reale. Vedi
  `references/comportamenti-interfaccia.md`.
- **Solo Single media, nient'altro** (`dichiarato: Matteo, 2026-11-05`). Product
  browsing spento, Carousel e Collection spenti. Dettaglio in
  `references/impostazioni-ad.md`.
- **Interazione solo in chat, poche parole.** Report e domande in chat, in tabelle
  e bullet. Nessun file di report.
- **Lettura lean del browser.** Per ogni ciclo leggi solo nodi visibili e
  interattivi, filtrati per etichetta o ruolo. Mai la pagina intera, mai
  screenshot a ogni passo. Dettaglio in `references/comportamenti-interfaccia.md`.
- **Non attivare ciò che le ads di riferimento non hanno** (`dichiarato:
  Matteo`). Non toccare audience né setup tecnici.
- **Verificato solo ciò che è stato riletto dopo il salvataggio.** Un controllo
  non fatto si scrive "non verificato".

## Steps

### 1. Perimetro

```
REGISTRA in 6 righe: account | campagna | adset (nuovo|esistente) | cartelle | fonte copy | URL fornite
IF adset nuovo    THEN duplica un adset di riferimento della campagna e cambia solo il nome (audience, ottimizzazione, tracciamento invariati). Adset nuovo solo se Matteo lo specifica (dichiarato: Matteo, 2026-11-05)
IF adset non indicato come nuovo THEN usa l'esistente
IF fonte copy assente THEN fonte = ads dell'account (vedi passo 5)
```

### 2. Studio dell'account, sola lettura

Dettaglio in [studio-account.md](references/studio-account.md).

```
LEGGI campagna, più adset e più ads pertinenti. NON modificare nulla
ESTRAI profilo: naming | pagina FB | profilo IG | CTA | destinazione | enhancement attivi | formati | tracciamento
IF ads di riferimento assenti  THEN studia comunque, chiedi conferma
IF naming non ricavabile       THEN chiedi la struttura in chat
```

### 3. Inventario e deduplica

Dettaglio in [inventario-e-url.md](references/inventario-e-url.md).

```
ESEGUI scripts/inventory.py <cartelle>   # tabella file, gruppo, formato, hash
COSTRUISCI matrice: Path | File | Prodotto | Versione | Media | URL | Naming | Stato
IF segnali di prodotto discordanti  THEN STOP su quella riga
IF hash uguale                      THEN duplicato esatto, segnala
IF solo il prodotto uguale          THEN NON è duplicato
CONTA creatività valide dall'inventario. Totale atteso = quel numero
```

### 4. URL

```
IF URL fornita THEN usa quella
ELSE cerca pagina prodotto o collezione sul sito del brand, aprila, verifica prodotto e variante
IF più prodotti nel video THEN pagina di collezione pertinente
IF ambigua THEN chiedi
CONTROLLA copy, headline, description: nessun prodotto o promessa incompatibili con la destinazione
```

### 5. Creazione delle bozze

Dettaglio in [impostazioni-ad.md](references/impostazioni-ad.md).

```
PER OGNI creatività valida:
  crea ad con nome unico dal naming dell'account. RIMUOVI "- copy"
  carica i file dalla cartella indicata da Matteo con il metodo di references/comportamenti-interfaccia.md (copia nella cartella della sessione, input file intercettato, tool di upload); se non riesce, chiedi a Matteo di caricarli nella libreria media e prendili da lì. VERIFICA che sia applicato, non solo selezionato
  assegna URL, testo principale, headline, description
IF copy mancante          THEN prendilo dalle ads di riferimento (ricorrente, o la variante indicata)
IF copy incoerente col file THEN STOP, chiedi
```

SBAGLIATO: "Il campo Website URL è giusto, quindi la ad ha la destinazione
giusta."
GIUSTO: "Website URL ed eventuali Source URL sono due campi. Si controllano
entrambi, e un valore ereditato discordante si segnala anche se il clic atterra
bene."

### 6. Impostazioni

```
FORMATO = solo "Single image or video" (o "Single media"), nient'altro
SPEGNI Product browsing (Personalized destinations deve essere 0/4)
SPEGNI Carousel | Collection | Video slideshow | varianti prodotto o app store (Format display options deve essere 1/3)
SPEGNI prodotti, media correlati, tag prodotto ereditati
MANTIENI solo gli enhancement attivi nelle ads di riferimento. Tutto il resto spento
IGNORA i suggerimenti "Apply now"
Add-on: solo se già nell'account
CONTROLLA ogni gruppo di posizionamenti: il file previsto, non quello della bozza duplicata
IF ritaglio automatico taglia il testo più grande  THEN trascina l'inquadratura leggermente in alto o in basso per farlo rientrare nella safe zone. Se non basta, segnala come anomalia
```

### 7. Anti-bug Meta

Dettaglio in [comportamenti-interfaccia.md](references/comportamenti-interfaccia.md).

```
DOPO ogni modifica  ATTENDI che il pannello mostri il valore nuovo
DOPO cambio URL/sorgente  RICONTROLLA i formati: Meta può riattivare carousel o slideshow
IF riepilogo != dettaglio  THEN fidati del dettaglio e riapri
RICARICA (hard reload) le ads corrette e verifica che il salvataggio persista
DOPO il ricarico  RILEGGI CTA e Website URL: possono tornare "See details" e comparire con ?fbclid=fbclid in coda
NON usare Escape nell'editor: apre "Publish draft items?" e chiude l'editor
IF Source URL torna al valore ereditato  THEN documenta, non dichiarare risolto
```

### 8. Audit e report

Dettaglio in [audit-e-report.md](references/audit-e-report.md).

```
PER OGNI ad: esegui la checklist dell'audit. Esito: ok | anomalia | non verificato
RICARICA le ads corrette e ripeti i controlli che Meta può aver cambiato
CONFRONTA inventario e ads create nell'adset
CONSEGNA il report in chat. Ads restano in bozza
```

SBAGLIATO: "L'anteprima mostra il video giusto, quindi tutti i posizionamenti
sono a posto."
GIUSTO: "L'anteprima principale non prova gli altri gruppi di posizionamenti. Si
controlla il file in ognuno, oppure si scrive non verificato."

## Outputs

Report compatto in chat con: file validi, bozze create, duplicati, correzioni,
tabella cartella o prodotto con URL, esito per creatività (file, nome ad,
prodotto, URL, stato, anomalie), verifiche non fatte. Nessun file scritto.

## Quality checklist

- [ ] Nessuna azione di pubblicazione eseguita
- [ ] Ads create uguali alle creatività valide dell'inventario
- [ ] Nomi unici, nessun - copy, naming come nell'account
- [ ] URL, copy, headline e description coerenti con ogni file
- [ ] Single media e nient'altro: Product browsing spento, Format display options 1/3
- [ ] Nessun formato, prodotto o enhancement non richiesto
- [ ] Uscita dall'editor con "Save draft", mai con Publish. Nomi unici riletti nella lista ads
- [ ] Ad sources a 0 e "Text improvements" spento
- [ ] Ogni gruppo di posizionamenti controllato
- [ ] Ads corrette ricaricate e controlli ripetuti
- [ ] Controlli non fatti scritti come non verificati
- [ ] Punti ancora da verificare con Matteo elencati nel report

## Next steps

Matteo controlla le bozze in Ads Manager e pubblica. Nessuna skill a valle.

## References

- [studio-account.md](references/studio-account.md): cosa si ricava dall'account prima di creare
- [inventario-e-url.md](references/inventario-e-url.md): matrice, deduplica e abbinamento delle URL
- [impostazioni-ad.md](references/impostazioni-ad.md): single media, enhancement, posizionamenti
- [comportamenti-interfaccia.md](references/comportamenti-interfaccia.md): attese, riattivazioni di Meta, lettura lean
- [audit-e-report.md](references/audit-e-report.md): checklist ad per ad e formato del report
- [punti-da-verificare.md](references/punti-da-verificare.md): campi che Matteo non ha definito
- [docs/provenance-schema.md](../../docs/provenance-schema.md): tag di provenienza
- [docs/anti-ai-slop-writing-standard.md](../../docs/anti-ai-slop-writing-standard.md): standard di scrittura per copy e messaggi

Made in Landi Brain · [Matteo Landi](https://www.linkedin.com/in/matteolandidigital)
