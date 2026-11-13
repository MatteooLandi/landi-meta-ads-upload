<!-- Copia sincronizzata di landi-brain docs/provenance-schema.md (Brain bc06fd6, 2026-11-13). La versione canonical sta nel Brain: quando differiscono vince quella. I rimandi ad altri file del Brain non sono inclusi in questo repository. -->

# Provenance schema

Schema unico di classificazione dell'origine di ogni informazione dentro il
Brain e dentro i brand cliente. Attivo in **tutte le skill** che leggono,
scrivono o sintetizzano informazioni.

## Livelli

| Tag | Significato | Requisito minimo |
|---|---|---|
| `[verificato]` | Letto da fonte primaria accessibile o account collegato | URL/riferimento verificabile + contenuto della fonte davvero supporta il claim |
| `[dichiarato]` | Affermato dal cliente o da fonte interessata | Nome della fonte + data della dichiarazione |
| `[inferito]` | Conclusione AI basata su evidenze | Almeno 2 evidenze citate + spiegazione della catena inferenziale |
| `[sconosciuto]` | Origine o supporto insufficienti | Segnalato esplicitamente, non nascosto |

## Regola di comportamento

1. **Provenienza evidente**: la skill classifica automaticamente
2. **Provenienza ambigua**: la skill chiede all'utente
3. **Provenienza mancante**: resta `[sconosciuto]`, mai promosso senza evidenza
4. **Correzione utente**: prevale sempre
5. **Verifica cliente**: se la fonte è il cliente stesso, si verifica che il
   cliente lo abbia **dichiarato**, non che sia vero. Il cliente parla → tag
   `[dichiarato]`. Solo verifica indipendente promuove a `[verificato]`

## Formato in-line

Il tag e la fonte si separano con i due punti: `[dichiarato: fonte, data]`. I tag scritti prima del 2026-09-15 con il trattino lungo restano validi per l'audit, ma nei file nuovi il trattino lungo è vietato dallo standard anti AI-slop.

Ogni claim, dato, quote, statistica va marcato. Formati ammessi:

```markdown
Il prodotto costa 49€ [dichiarato: cliente onboarding 2026-08-22].

Studies show barrier repair after 4 weeks [verificato: Dermatol Ther 2024,
doi.org/xxx].

L'audience over-40 preferisce claim "sostenibili" [inferito: cross-source
Reddit + Amazon 2026-08].

Numero clienti attivi: [sconosciuto: chiedere in follow-up].
```

## Dove va applicato

Obbligatorio in questi file di brand-context:

- `positioning.md` — ogni claim di value prop, competitor, differenziazione
- `buyer-personas.md` — ogni tratto demografico, pain, obiezione
- `verbatim.md` — ogni quote deve avere source (verificato se link, dichiarato
  se cliente, sconosciuto se anonimo)
- `learnings.md` — ogni pattern con evidenze (verificato/inferito), mai
  dichiarato senza altre fonti
- Output di `outputs/research/*.md` — ogni pattern e verbatim tagged
- Output di `outputs/analysis/*.md` — root cause, ipotesi, conclusioni

Opzionale ma consigliato:

- `tone-of-voice.md` — soprattutto per esempi frasi (dichiarato dal cliente
  vs verificato su asset esistenti)
- `resources.md` — quali asset sono verificati esistenti vs dichiarati
  disponibili

## Promozione fra livelli

Un tag può essere promosso quando:

- `[sconosciuto]` → `[dichiarato]`: cliente/fonte fornisce dichiarazione
- `[dichiarato]` → `[verificato]`: fonte terza indipendente conferma
- `[inferito]` → `[verificato]`: nuova evidenza primaria conferma direttamente
- `[verificato]` → `[dichiarato]`: se la fonte primaria diventa non
  raggiungibile o è smentita (declassamento)

Ogni promozione/declassamento va registrato con:

```markdown
[verificato: Dermatol Ther 2024, doi.org/xxx]
<!-- promosso da [inferito] il 2026-09-01 dopo cross-check paper -->
```

## Anti-pattern

- Non promuovere `[dichiarato]` a `[verificato]` solo perché "è plausibile"
- Non usare `[verificato]` per contenuto AI-generated non verificato manualmente
- Non lasciare claim senza tag (crea drift silenzioso)
- Non seppellire `[sconosciuto]` in note a piè di pagina — deve essere visibile
- Non fondere claim di livelli diversi in una frase unica (perde tracciabilità)

## Skill che devono applicarlo

Tutte le skill che generano o modificano contenuto brand:

- `onboard-client` — default `[ONBOARDING - da validare]` = `[dichiarato]`
  con nota temporale
- `import-existing-brand` — mantiene tag della fonte importata; se mancante,
  `[sconosciuto]`
- `research-*` — ogni verbatim = `[verificato]` (con URL) o
  `[sconosciuto]`. Pattern = `[inferito]`
- `build-positioning` — ogni claim rispetta i tag delle fonti a monte, non
  li promuove implicitamente
- `build-buyer-personas` — stesso principio
- `build-visual-dna` — palette/font sono `[verificato]` se da brand book,
  `[dichiarato]` se da cliente in call
- `root-cause-analysis` — ogni "perché" ha evidence tagged
- `update-learnings` — Pattern entra solo se supportato da `[verificato]`
  o `[inferito]` con ≥2 fonti
- `bundle-for-external` — mantiene tag anche nell'export

## Checker automatico (futuro)

`brain-audit` (skill in roadmap) verificherà:

- % claim senza tag → segnala se > 5%
- % claim `[sconosciuto]` → informativo
- Contraddizioni fra tag (stesso claim tagged diversi in file diversi)
- Fonti `[verificato]` con URL non raggiungibile

## Reference file portatile

Per skill che vivono in pacchetti autonomi (research-pack,
landi-video-scriptwriter), esiste copia sincronizzata in:

- `skills/research-pack/CONVENTIONS/provenance.md`
- `skills/landi-video-scriptwriter/CONVENTIONS/provenance.md` (da aggiungere
  quando si aggiorna quel pack)

Il presente file resta la versione **canonical**. Ogni pack sincronizza al
proprio ritmo. Quando differiscono, canonical vince.
