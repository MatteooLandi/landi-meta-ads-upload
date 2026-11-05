---
Origine: intervista `landi-skill-builder` del 2026-10-29. Matteo ha risposto ai dodici
punti il 2026-11-05. I punti 1-8 e 11 sono confermati e passati nei reference.
Restano due prove da fare sul primo caso reale e la prova di fine bozza.
---

# Punti ancora aperti

## Confermati il 2026-11-05 (`dichiarato: Matteo`)

- **Chrome non disponibile:** la skill si ferma e indica l'attivazione da terminale
  (`claude --chrome` o `/chrome`). Passato in `SKILL.md`.
- **Login a Meta:** la sessione è già attiva perché la skill usa il browser di Matteo.
- **Adset nuovo:** si duplica un adset di riferimento e si cambia il nome, ma solo se
  Matteo lo specifica. Altrimenti si usa l'esistente. Passato nel passo 1.
- **Immagine 1:1 mancante:** si lascia il 4:5 e si scrive una riga nel report.
- **Ritaglio che taglia il testo:** si trascina leggermente l'inquadratura in alto o in
  basso per far rientrare il testo nella safe zone. Se non basta, anomalia.
- **Enhancement:** restano attivi solo quelli delle ads di riferimento.
- **Nome e attivazione:** `meta-ads-upload` va bene. La skill si attiva anche con
  "carica delle creative su Meta". Frasi aggiunte nei `triggers`.
- **Esempio di adset fatto bene:** si usa la checklist di `audit-e-report.md`.

## Da misurare sul primo caso reale (`inferito`, Matteo ha detto sì)

### Lettura lean del browser

- **Di cosa si tratta**: `comportamenti-interfaccia.md`, ultima sezione.
- **Cosa resta**: il risparmio di token non è misurato.
- **Proposta**: misurare i token con e senza sul primo caricamento.

### Raggruppamento dei formati delle immagini

- **Di cosa si tratta**: `scripts/inventory.py`, colonna Gruppo.
- **Cosa resta**: il raggruppamento dal nome dei file è un'euristica, mai provata su
  nomi reali.
- **Proposta**: correggere i token sulla prima cartella vera.

## Caso reale di prova

Nessun caso scelto. Matteo ha detto di mettere online la skill senza prova
(2026-11-05). Il primo caricamento reale fa da prova e si registra cosa si rompe.

Made in Landi Brain · [Matteo Landi](https://www.linkedin.com/in/matteolandidigital)
