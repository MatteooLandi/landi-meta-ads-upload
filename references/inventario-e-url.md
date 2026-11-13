---
Origine: `dichiarato [Matteo, testo incollato in chat, 2026-10-29]`. Raggruppamento dei
formati delle immagini e uso dell'hash: proposta mia, da verificare.
---

# Inventario, deduplica e URL

## Script

`scripts/inventory.py <cartella> [<cartella> ...]` produce una tabella compatta.
Non usa l'AI: scansione, hash e dimensioni sono meccanici.

```
python3 <cartella della skill>/scripts/inventory.py <cartella> [--video-subdir Export]
```

Colonne: `Path | File | Tipo | WxH | Rapporto | Durata | SHA256 | Gruppo | DupDi`.

- **Video**: contano solo i file dentro la sottocartella indicata da
  `--video-subdir` (esempio dichiarato: `Export`, cioè i file editati). Gli altri
  video sono scartati e l'elenco degli scartati si stampa a parte.
- **Immagini**: contano tutti i file immagine.
- **Duplicati**: `DupDi` riporta il primo file con lo stesso SHA256.
- **Gruppo**: chiave ricavata dal nome tolti i token di formato (1x1, 4x5, 9x16,
  1080x1350...). File con lo stesso gruppo sono versioni di formato della stessa
  creatività. È un'euristica: l'agente conferma il raggruppamento.

## Matrice

Una riga per creatività (gruppo), non per file:

| Path | File | Prodotto | Versione | Media | URL | Naming | Stato |
|---|---|---|---|---|---|---|---|

Stato: `da fare | creata | verificata | anomalia | STOP`.

## Prodotto e versione

```
RICONOSCI prodotto da: nome cartella + nome file + contenuto visivo
IF i tre segnali sono discordanti THEN STOP su quella riga e chiedi
IF due file hanno stesso prodotto ma versione diversa THEN due creatività, non duplicato
IF hash identico con nomi diversi THEN duplicato esatto: una sola ad, segnalalo nel report
```

Il contenuto visivo si controlla su un fotogramma o sull'immagine. Non si
decide dal solo nome del file.

## Totale atteso

Il totale atteso di ads è il numero di creatività valide dell'inventario. Non si
deduce dalle righe visibili in Ads Manager: l'elenco può essere virtualizzato o
paginato.

SBAGLIATO: "Nell'elenco vedo 12 ads, quindi ne mancano 3 rispetto alle 15
creatività."
GIUSTO: "L'inventario ha 15 creatività valide. Per contare le ads nell'adset
scorro o filtro l'elenco finché il conteggio non cambia più."

## URL

```
IF Matteo ha dato le URL THEN usale, hanno la precedenza
ELSE cerca pagina prodotto o collezione sul sito del brand
     CONFRONTA cartella, file, prodotto mostrato
IF il video mostra più prodotti THEN pagina di collezione pertinente
IF prodotto o pagina restano ambigui THEN chiedi l'URL
APRI la pagina. VERIFICA prodotto, variante e destinazione
```

Tabella da consegnare in chat:

| Cartella o prodotto | URL | Verificata |
|---|---|---|

## Website URL e Source URL

- **Website URL**: destinazione effettiva del clic.
- **Source URL**: usata dalle funzioni creative. Può restare ereditata e inattiva.
- Non scambiare un campo sorgente ereditato con il link su cui atterra il clic.
- Un campo ereditato discordante si segnala anche se non è attivo.

## Coerenza del testo con la destinazione

Copy, headline e description non citano prodotti, promesse o link incompatibili
con la destinazione. Se li citano: STOP e chiedi, non riscrivere.

Made in Landi Brain · [Matteo Landi](https://www.linkedin.com/in/matteolandidigital)
