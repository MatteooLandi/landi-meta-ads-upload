---
Origine: intervista `landi-skill-builder` del 2026-10-29. Matteo ha chiesto di procedere in
autonomia e di segnalare come "da verificare" ciò che mancava. Ogni voce sotto è una
proposta mia, `inferito`, finché Matteo non risponde.
---

# Punti da verificare con Matteo

Ogni punto vale come regola provvisoria. Quando Matteo conferma o corregge, la
regola passa nel reference che la riguarda e la voce esce da qui.

## 1. Se Chrome non è disponibile

- **Di cosa si tratta**: `SKILL.md`, `stopping_conditions`, terza voce.
- **Perché serve il suo parere**: decide se la skill si ferma o ha un ripiego.
- **Proposta**: la skill si ferma e lo dice. Matteo ha detto che oggi esiste
  solo Chrome e che in futuro potranno esserci MCP o API Meta.

## 2. Login a Meta

- **Di cosa si tratta**: pre-flight, riga sulla pagina di login.
- **Perché serve il suo parere**: Matteo non ha detto se parte con la sessione
  già attiva.
- **Proposta**: la skill apre il link all'account. Se vede il login si ferma e
  chiede a Matteo di accedere. Non inserisce mai credenziali.

## 3. Creare un adset nuovo

- **Di cosa si tratta**: passo 1 di `SKILL.md`, riga "adset nuovo".
- **Perché serve il suo parere**: Matteo ha detto che l'adset può essere nuovo
  o esistente, senza dire come lo crea.
- **Proposta**: duplicare un adset di riferimento della campagna, cambiare solo
  il nome, e lasciare il resto invariato (audience, ottimizzazione, tracciamento).

## 4. Immagine 1:1 mancante

- **Di cosa si tratta**: `impostazioni-ad.md`, sezione "File per posizionamento".
- **Perché serve il suo parere**: ha detto che il 4:5 ha di solito la safe zone
  per l'1:1, non cosa fa la skill quando manca l'1:1.
- **Proposta**: lasciare il 4:5 e scrivere una riga nel report.

## 5. Ritaglio orizzontale che taglia il testo

- **Di cosa si tratta**: `impostazioni-ad.md`, stessa sezione.
- **Perché serve il suo parere**: ha dato la priorità (non tagliare il testo più
  grande) e ha detto che i formati arrivano già pronti.
- **Proposta**: la skill non produce ritagli. Se il ritaglio automatico taglia il
  testo più grande, lo segnala come anomalia.

## 6. Enhancement

- **Di cosa si tratta**: `impostazioni-ad.md`, sezione "Enhancement".
- **Perché serve il suo parere**: la regola nasce da due sue frasi, non da una
  sola regola detta.
- **Proposta**: restano attivi solo gli enhancement presenti nelle ads di
  riferimento dell'account.

## 7. Nome della skill

- **Di cosa si tratta**: `meta-ads-upload`, nome di cartella e di `name`.
- **Perché serve il suo parere**: il nome deve essere suo.
- **Proposta**: tenerlo, oppure indicare quello che usa lui.

## 8. Frasi di attivazione

- **Di cosa si tratta**: `triggers` in `SKILL.md`.
- **Perché serve il suo parere**: le frasi vere sono quelle che usa lui.
- **Proposta**: le sette frasi attuali, scritte da me.

## 9. Lettura lean del browser

- **Di cosa si tratta**: `comportamenti-interfaccia.md`, ultima sezione.
- **Perché serve il suo parere**: il risparmio di token è un obiettivo suo e non
  è misurato.
- **Proposta**: provarla sul primo caso reale e misurare i token con e senza.

## 10. Raggruppamento dei formati delle immagini

- **Di cosa si tratta**: `scripts/inventory.py`, colonna Gruppo.
- **Perché serve il suo parere**: il raggruppamento dal nome dei file è
  un'euristica sui suoi nomi reali, che non ho visto.
- **Proposta**: provarla sulla prima cartella vera e correggere i token.

## 11. Esempio reale di adset fatto bene

- **Di cosa si tratta**: definizione di "risultato buono".
- **Perché serve il suo parere**: Matteo non ha un esempio sotto mano.
- **Proposta**: tenere la checklist di `audit-e-report.md` come criterio, e
  aggiungere l'esempio quando capita un caso reale.

## 12. Caso reale di prova

- **Di cosa si tratta**: Fase 6 dell'intervista.
- **Perché serve il suo parere**: nessun caso di prova è stato scelto.
- **Proposta**: il primo caricamento reale fa da prova, con me che registro cosa
  si rompe.

Made in Landi Brain · [Matteo Landi](https://www.linkedin.com/in/matteolandidigital)
