# FAQ v1.1 CMS Replacement Sections Validation — 13:42, 28.07.2026

## Scope

Validate the attached nine-card FAQ v1.1 final draft against the hardened Phase 1 FAQ CMS working inventory, then create only the Gamma cards that require replacement.

## Authority and evidence

- Explicit owner instruction, 28.07.2026.
- Attached final FAQ v1.1 PDF and PPTX, nine cards.
- Canonical decisions `ATL-DEC-20260727-032` and `ATL-DEC-20260728-033`.
- Canonical validations `ATL-VAL-20260728-064` and `ATL-VAL-20260728-065`.
- Authenticated Wix readback of `AtlasFAQs`: 14 active Bokmål Phase 1 working records, content version `FAQ-PHASE1-v0.9.0-20260728`.
- `AtlasFAQsPublic` remains empty; no working record is public or schema eligible.

## Comparison result

The final FAQ draft contained the original eight-topic content structure. The updated working inventory contains fourteen reciprocal topics and materially changes or expands cards 2–8.

### Cards not replaced

1. `Atlas AI · FAQ` cover — positioning remains compatible.
2. `Finner du ikke svaret?` closing card — internal routing and release disclaimer remain compatible.

### Cards requiring replacement

| Existing final card | Reason | Replacement Gamma |
|---|---|---|
| Finn svar før du deler detaljer | Topic navigation omitted new usage, privacy, provider-data and responsible-AI categories | `FAQ v1.1 - Finn svar før du deler detaljer` |
| Fire raske svar | Three quick answers required exact CMS wording updates | `FAQ v1.1 - Fire raske svar` |
| Hvilket spor passer deg? | Student 16–17 control model and consumer-safety boundary were expanded | `FAQ v1.1 - Hvilket spor passer deg?` |
| Hva er Atlas AI? | Audience answer required exact age, payer, identity, privacy and availability wording | `FAQ v1.1 - Hva er Atlas AI?` |
| Plattformer og kostnader | New usage-cap topic and revised provider/cost wording required a replacement | `FAQ v1.1 - Plattformer, kostnader og bruksrammer` |
| Data og Managed Secure | Confidential-data and Managed Secure wording changed; content remained too dense for all new trust topics | `FAQ v1.1 - Data og Managed Secure` |
| Data/trust gap | GDPR claims, processing location, model-training configuration and AI-output limits were absent | `FAQ v1.1 - Personvern, leverandørdata og KI-resultater` |
| Studier og oppstart | Consumer-safety FAQ was absent and student copy changed | `FAQ v1.1 - Studenter og privatpersoner` |
| Studier og oppstart | Onboarding wording and sequence required an independent replacement card | `FAQ v1.1 - Hvordan kommer jeg i gang med Atlas AI?` |

## Created Gamma replacement cards

1. [FAQ v1.1 - Finn svar før du deler detaljer](https://gamma.app/docs/FAQ-v11-Finn-svar-fr-du-deler-detaljer-ql55nkw211wmk4k)
2. [FAQ v1.1 - Fire raske svar](https://gamma.app/docs/FAQ-v11-Fire-raske-svar-xgqnevhc1ahbb7l)
3. [FAQ v1.1 - Hvilket spor passer deg?](https://gamma.app/docs/FAQ-v11-Hvilket-spor-passer-deg-7g4uditcgbwodfs)
4. [FAQ v1.1 - Hva er Atlas AI?](https://gamma.app/docs/FAQ-v11-Hva-er-Atlas-AI-ikjpfwkygc4moog)
5. [FAQ v1.1 - Plattformer, kostnader og bruksrammer](https://gamma.app/docs/FAQ-v11-Plattformer-kostnader-og-bruksrammer-4k1meq1k1x2ntdj)
6. [FAQ v1.1 - Data og Managed Secure](https://gamma.app/docs/FAQ-v11-Data-og-Managed-Secure-y5jttt5hlrnjq6z)
7. [FAQ v1.1 - Personvern, leverandørdata og KI-resultater](https://gamma.app/docs/FAQ-v11-Personvern-leverandrdata-og-KI-resultater-10eds9j3q4vc8wm)
8. [FAQ v1.1 - Studenter og privatpersoner](https://gamma.app/docs/FAQ-v11-Studenter-og-privatpersoner-ehgxoydgwr838eh)
9. [FAQ v1.1 - Hvordan kommer jeg i gang med Atlas AI?](https://gamma.app/docs/FAQ-v11-Hvordan-kommer-jeg-i-gang-med-Atlas-AI-wf4apk41j99pw6c)

## Validation

| Check | Result |
|---|---|
| Exact naming convention | PASS — every title starts `FAQ v1.1 -` and ends with the section/card title |
| Target folder | PASS — `Atlas AI - Contact` |
| Replacement-only scope | PASS — no full FAQ site recreated; unchanged cover and closing card were not duplicated |
| Gamma structure | PASS — nine separate one-card decks |
| Theme and geometry | PASS — Icebreaker, 16:9 |
| CMS topic coverage | PASS — all fourteen Bokmål working topics are represented across the replacements |
| Exact CMS claim boundaries | PASS — age, payer/identity/privacy, usage caps, no automatic chargeable overage, low-risk forms, Managed Secure, GDPR qualification, location, model training, AI-output, student and consumer safety boundaries included |
| Public collection effect | NONE — no CMS promotion or Wix Studio mutation |
| Public release | NO_GO |

## Implementation mapping

The original seven replaceable final cards become nine cards because two dense cards are split:

- Existing `Data og Managed Secure` is replaced by:
  - `Data og Managed Secure`
  - `Personvern, leverandørdata og KI-resultater`
- Existing `Studier og oppstart` is replaced by:
  - `Studenter og privatpersoner`
  - `Hvordan kommer jeg i gang med Atlas AI?`

The revised assembled FAQ candidate therefore contains eleven cards: the unchanged cover, nine replacements and the unchanged closing card.

## Remaining work

1. Assemble and rank the eleven-card FAQ candidate.
2. Confirm final copy and reciprocal English parity.
3. Complete claims, privacy/legal, provider, commercial, student and consumer-safety review.
4. Transfer the selected candidate to Figma and validate responsive geometry and accessible interaction.
5. Create Wix Studio locale pages and bind only to `AtlasFAQsPublic`.
6. Promote only exact approved CMS records after all gates pass.
7. Run accessibility, route, canonical, hreflang, metadata, performance and release acceptance tests.

## Classification and release state

- Draft creation, current CMS comparison, replacement mapping and Gamma readback: `AUTO_APPROVED`.
- Final copy, English parity, Figma/Wix implementation, CMS promotion and release: `PENDING_REVIEW / NO_GO`.
- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
