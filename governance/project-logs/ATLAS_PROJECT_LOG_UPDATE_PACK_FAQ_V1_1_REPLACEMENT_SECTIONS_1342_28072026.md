# ATLAS PROJECT LOG UPDATE PACK — FAQ v1.1 Replacement Sections — 13:42, 28.07.2026

## Timestamp

13:42, 28.07.2026 Europe/Oslo

## Session / task

Compare the attached final FAQ v1.1 against the updated Phase 1 Wix FAQ CMS and create only the Gamma sections that require replacement, using exact `FAQ v1.1 - [Section/card title]` naming in the `Atlas AI - Contact` folder.

## Issue or mistake observed

1. The attached final FAQ still reflected the earlier eight-topic content model.
2. The hardened private CMS now contains fourteen active Bokmål topics, including six material additions: usage limits, GDPR claim qualification, processing/storage location, provider training-use configuration, AI-output limitations and consumer-safety boundaries.
3. Two original cards would become unreadable if all new topics were inserted without splitting.

## Root cause

- The final FAQ was exported before the 28.07.2026 CMS hardening and bilingual inventory expansion.
- Earlier content grouped data/trust and student/onboarding topics too tightly for the new fourteen-topic scope.

## Corrective rule

1. Regenerate only cards with material CMS drift.
2. Do not duplicate unchanged cover or closing cards.
3. Use one Gamma deck per replacement card.
4. Use exact file naming `FAQ v1.1 - [Section/card title]`.
5. Preserve the Icebreaker theme and 16:9 card geometry.
6. Split dense cards where needed rather than shrinking important trust, legal or safety text below readable size.
7. Treat private `AtlasFAQs` as the working source and do not promote or bind it publicly.

## Evidence / source

- Attached `FAQ-v11(1).pdf` and `FAQ-v11(1).pptx`, nine-card final draft.
- Authenticated Wix query of active Bokmål `AtlasFAQs` records.
- CMS content version `FAQ-PHASE1-v0.9.0-20260728`.
- Canonical decisions `ATL-DEC-20260727-032` and `ATL-DEC-20260728-033`.
- Canonical validations `ATL-VAL-20260728-064` and `ATL-VAL-20260728-065`.
- Drive hardening addendum and project log dated 13:11, 28.07.2026.

## Action taken

Created nine separate one-card Gamma replacement decks in `Atlas AI - Contact`:

1. `FAQ v1.1 - Finn svar før du deler detaljer`
   - https://gamma.app/docs/FAQ-v11-Finn-svar-fr-du-deler-detaljer-ql55nkw211wmk4k
2. `FAQ v1.1 - Fire raske svar`
   - https://gamma.app/docs/FAQ-v11-Fire-raske-svar-xgqnevhc1ahbb7l
3. `FAQ v1.1 - Hvilket spor passer deg?`
   - https://gamma.app/docs/FAQ-v11-Hvilket-spor-passer-deg-7g4uditcgbwodfs
4. `FAQ v1.1 - Hva er Atlas AI?`
   - https://gamma.app/docs/FAQ-v11-Hva-er-Atlas-AI-ikjpfwkygc4moog
5. `FAQ v1.1 - Plattformer, kostnader og bruksrammer`
   - https://gamma.app/docs/FAQ-v11-Plattformer-kostnader-og-bruksrammer-4k1meq1k1x2ntdj
6. `FAQ v1.1 - Data og Managed Secure`
   - https://gamma.app/docs/FAQ-v11-Data-og-Managed-Secure-y5jttt5hlrnjq6z
7. `FAQ v1.1 - Personvern, leverandørdata og KI-resultater`
   - https://gamma.app/docs/FAQ-v11-Personvern-leverandrdata-og-KI-resultater-10eds9j3q4vc8wm
8. `FAQ v1.1 - Studenter og privatpersoner`
   - https://gamma.app/docs/FAQ-v11-Studenter-og-privatpersoner-ehgxoydgwr838eh
9. `FAQ v1.1 - Hvordan kommer jeg i gang med Atlas AI?`
   - https://gamma.app/docs/FAQ-v11-Hvordan-kommer-jeg-i-gang-med-Atlas-AI-wf4apk41j99pw6c

The original cover and `Finner du ikke svaret?` closing card were not recreated.

## Validation performed

- Current CMS filtered readback: PASS — 14 active Bokmål topics.
- Attached PPTX inspection: PASS — 9 original cards, 16:9.
- Replacement mapping: PASS — cards 2–8 require replacement.
- Exact titles: PASS.
- Folder placement: PASS.
- Separate one-card structure: PASS.
- Icebreaker theme: PASS.
- 16:9 dimensions: PASS.
- Gamma content readback: PASS for all nine cards.
- New topic coverage: PASS.
- Public CMS promotion: NOT PERFORMED.
- Wix Studio mutation: NOT PERFORMED.
- Release effect: NONE / NO_GO.

## Unresolved items

1. Assemble the unchanged cover, nine replacements and unchanged closing card into the eleven-card final candidate.
2. Run the established weighted ranking and select the final sequence.
3. Complete English reciprocal copy and all content/claim/legal/privacy/provider/commercial/student/consumer reviews.
4. Validate Figma geometry, responsive behavior, keyboard interaction and focus states.
5. Create Wix Studio routes and bind only to `AtlasFAQsPublic`.
6. Promote exact approved CMS pairs only after release gates pass.

## Classification

- `AUTO_APPROVED`: source comparison, replacement-only selection, exact naming, Gamma creation and readback.
- `PENDING_REVIEW`: final assembled copy, English parity, Figma/Wix implementation, record promotion and public release.

## Release controls after task

- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
- `AtlasFAQsPublic` remains empty.
- Checkout, payments, production entitlements and public Managed Secure availability remain disabled.
