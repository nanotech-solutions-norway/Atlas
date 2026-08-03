# Atlas AI v4 Copy and Figma First-Slide Validation — 10:54, 03.08.2026

**Validation targets:**

1. Canonical Norwegian Phase 1 copy baseline.
2. All 15 canonical Figma v4 files in project `633513513`.
3. First-slide classification and post-delete file state.
4. Controlled Drive artifact manifest and validation report.

**Result:** `PASS` for source identity, copy baseline registration, conditional slide deletion and post-delete readback.  
**Release result:** `NO_GO`; no Wix implementation or publication approval.

## Source validation

| Source | Drive ID | Size | SHA-256 | Result |
|---|---|---:|---|---|
| DOCX report | `1YFbBrmESNsWS_QvVZO5ah6Sm1TQsye5x` | 37,358 | `2354c572c5bbdec751c5261f16d559ea9ed05aa8c704198b36146750e7984209` | PASS |
| Markdown report | `1ssEO78IuebRSubl6WgqS_UYTM3_vfIf2` | 58,539 | `6ed168ae842df177ac4790b18132a82fdfe640752564f9f4c3203e28d0a4bc57` | PASS |

Appendix A is registered as the controlling paste-ready Norwegian public-copy baseline. The report's implementation limitations remain binding: content does not prove Wix route, metadata, form, cookie, accessibility, responsive or release completion.

## Figma validation method

For each file:

1. Resolve the exact file key from the controlled Drive manifest.
2. Read the first slide and collect all text.
3. Require the Wix-configuration signature before deletion: `Tjenester`, `Managed Secure`, `Priser`, `Tillit`, `Ressurser`, `Oppstart`, `English`.
4. Abort without mutation if the signature does not match.
5. Delete only the matched first slide.
6. Read back the deck in a separate call.
7. Confirm the count decreased by one.
8. Confirm the new first slide is the canonical page hero and no longer matches the Wix-configuration signature.

## Per-file results

| File | Figma key | Before | After | New first slide | Result |
|---|---|---:|---:|---|---|
| Home v4 | `yoy0V2adMzWPXn5jJe6R8C` | 10 | 9 | Styrte AI-løsninger for arbeid, studier og hverdagsoppgaver. | PASS |
| Tjenester v4 | `WkiuLQRrmZwlTCtpKO3cXU` | 8 | 7 | Velg riktig AI-løp for behovet. | PASS |
| Bedrift v4 | `zOn5VXQY9V74rWqLBeyip7` | 10 | 9 | Konfigurerte AI-arbeidsflyter med tydelige data- og ansvarsgrenser. | PASS |
| Studenter v4 | `AhGm9skcso2bG2BmHOA5IK` | 11 | 10 | Ansvarlig AI-støtte for planlegging, forståelse og repetisjon. | PASS |
| Privatpersoner v4 | `H36n74YgmCquksYEgnHI4Z` | 9 | 8 | Praktisk AI-støtte med definerte bruks- og sikkerhetsgrenser. | PASS |
| Managed Secure v4 | `R4LeFYvy4IQmH91fS7pEQ7` | 9 | 8 | Kontrollert arkitekturgjennomgang for konfidensielle arbeidsflyter. | PASS |
| Priser v4 | `3qeoaaSEGw90RzYZjSIMa1` | 10 | 9 | Offentlige priser med tydelig leveranse- og aktiveringsstatus. | PASS |
| Tillit v4 | `nfhkzy4rocsCyg0rjLOrdi` | 9 | 8 | Tydelige grenser for sikkerhet, personvern og ansvarlig AI. | PASS |
| Plattformer v4 | `V4qys96ma9y2tX74Anwl0E` | 8 | 7 | Fire plattformspor for forskjellige behov og kontrollnivåer. | PASS |
| Oppstart v4 | `rmm6HkfI7ijGQY9dHH4XZu` | 7 | 6 | Start med behovet – ikke med sensitiv informasjon. | PASS |
| Ressurser v4 | `pOX06PeOspQdlr8gcGzjA9` | 8 | 7 | Ressurser for bedre AI-beslutninger. | PASS |
| FAQ v4 | `AkyPe1H2MTpyBfyPYPf9Iw` | 7 | 6 | Ofte stilte spørsmål om Atlas AI. | PASS |
| Om oss v4 | `RvGNzVri3oHscBnQsconc4` | 8 | 7 | Praktisk AI med styring som en del av leveransen. | PASS |
| Kontakt v4 | `SjafXw83D5CISHOaKYncSn` | 9 | 8 | Kontakt Atlas AI. | PASS |
| Juridisk v4 | `LnGmSITkmM0pIad6mV9v55` | 11 | 10 | Juridisk informasjon og ansvarlig bruk. | PASS |

**Total:** 134 slides before; 119 actual page slides after; 15 operator-only configuration slides removed.

## Gamma disposition

No Gamma file was modified. The corresponding first Gamma card remains a source/operator reference for Wix header, menu, language and mobile controls. It is not counted as public page content for Figma or Wix page-section implementation.

## Remaining boundaries

- Metadata strings visibly embedded in some remaining Figma/Gamma page slides are a separate previously documented implementation issue and were not changed by this request.
- Functional forms, links, cookie behavior, metadata, routes, responsive states and accessibility require Wix validation.
- External Gamma image assets and normalized Figma panels retain their prior documented visual-fidelity boundaries.

## Classification

- Source identity and checksum registration: `AUTO_APPROVED`.
- Exact owner correction separating Wix operator guidance from page content: `AUTO_APPROVED`.
- Conditional deletion and post-delete readback: `AUTO_APPROVED`.
- Gamma non-modification: `APPROVED` owner instruction.
- Wix implementation and public release: `NO_GO`.
