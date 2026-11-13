# Meta Ads Upload

Skill per Claude Code che prepara in bozza su Meta Ads Manager le ads di un set
di creatività (video e immagini), su qualunque account.

Studia l'account, fa l'inventario dei file, abbina le URL di destinazione, crea
una ad per creatività e controlla ad per ad che nome, copy, link e impostazioni
siano salvati. Non pubblica, non crea campagne né audience.

Nel testo della skill "Matteo" indica la persona che la usa e dà le
indicazioni: chi la lancia prende quel ruolo.

## Stato

BOZZA. La skill non è ancora stata provata su un caso reale: le bozze create
vanno controllate una per una in Ads Manager prima di pubblicare.

## Cosa serve

- Claude Code (terminale o scheda Code dell'app desktop).
- L'estensione Claude in Chrome, installata con lo stesso account Claude, e
  Chrome con l'accesso a Meta già fatto. Da terminale si apre la sessione con
  `claude --chrome` oppure si scrive `/chrome` in una sessione aperta.
- Python 3 per `scripts/inventory.py`. `ffprobe` e `sips` sono facoltativi
  (durata dei video e dimensioni delle immagini).

## Installazione

Clona il repository nella cartella delle skill personali di Claude Code:

```bash
git clone https://github.com/MatteooLandi/landi-meta-ads-upload.git ~/.claude/skills/meta-ads-upload
```

Per gli aggiornamenti:

```bash
git -C ~/.claude/skills/meta-ads-upload pull
```

## Come si usa

In una sessione con Chrome attivo scrivi, per esempio, "carica queste
creatività su Meta". Servono il link all'account pubblicitario, la campagna e
l'adset di destinazione e la cartella con le creatività.

## Struttura

```
SKILL.md                      flusso completo, regole e checklist
references/                   studio dell'account, inventario e URL,
                              impostazioni delle ads, comportamenti
                              dell'interfaccia, audit e report, punti aperti
scripts/inventory.py          inventario meccanico dei file (hash, formati)
CONVENTIONS/                  copie dal Landi Brain: tag di provenienza e
                              standard di scrittura
```

Made in Landi Brain · [Matteo Landi](https://www.linkedin.com/in/matteolandidigital)
