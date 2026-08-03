# Atlas AI v4 Copy and Figma First-Slide Validation — 10:54, 03.08.2026

**Corrective revalidation:** 11:22, 03.08.2026 Europe/Oslo.  
**Validation targets:**

1. Canonical Norwegian Phase 1 copy baseline.
2. The 15 controlled Figma v4 file keys associated with the Atlas AI v4 workstream.
3. First-slide classification and post-delete file state.
4. Controlled Drive artifact manifest and validation report.

**Result:** `PASS_KNOWN_FILES` for source identity, conditional first-slide deletion, complete remaining-slide presence and separate live readback.  
**Project-folder inventory result:** `LIMITED` because the available Figma connector cannot enumerate an existing project folder or prove project membership.  
**Release result:** `NO_GO`; no Wix implementation or publication approval.

## Corrective owner report and response

At 11:22, 03.08.2026, the owner reported that the v4 drafts appeared completely deleted and instructed that no slide other than the first should be changed.

A new read-only, node-level inspection was immediately run against every controlled file key. No restoration, rollback, regeneration or further Figma mutation was performed because the live files were not empty or corrupted: all 119 expected remaining page slides were present, populated and readable. Reverting the files would have reintroduced the unwanted Wix-configuration slide or risked overwriting intact page content.

The precise cause of the owner’s apparent empty/deleted Figma UI state is not established by the connector evidence. The connector can validate known file keys and their contents, but it cannot provide an authoritative project-folder listing.

## Source validation

| Source | Drive ID | Size | SHA-256 | Result |
|---|---|---:|---|---|
| DOCX report | `1YFbBrmESNsWS_QvVZO5ah6Sm1TQsye5x` | 37,358 | `2354c572c5bbdec751c5261f16d559ea9ed05aa8c704198b36146750e7984209` | PASS |
| Markdown report | `1ssEO78IuebRSubl6WgqS_UYTM3_vfIf2` | 58,539 | `6ed168ae842df177ac4790b18132a82fdfe640752564f9f4c3203e28d0a4bc57` | PASS |

Appendix A is registered as the controlling paste-ready Norwegian public-copy baseline. The report's implementation limitations remain binding: content does not prove Wix route, metadata, form, cookie, accessibility, responsive or release completion.

## Original Figma edit method

For each controlled file:

1. Resolve the exact file key from the controlled Drive manifest.
2. Read the first slide and collect all text.
3. Require the Wix-configuration signature before deletion: `Tjenester`, `Managed Secure`, `Priser`, `Tillit`, `Ressurser`, `Oppstart`, `English`.
4. Abort without mutation if the signature does not match.
5. Delete only the matched first slide.
6. Read back the deck in a separate call.
7. Confirm the count decreased by one.
8. Confirm the new first slide is the canonical page hero and no longer matches the Wix-configuration signature.

An initial script attempted to call the unsupported `saveVersionHistoryAsync` method. That call failed atomically, so it made no file change. The corrected script omitted the unsupported method and returned the deleted slide IDs for audit.

## Per-file corrective live results

| File | Figma key | Before | Current | Current first slide | Remaining content | Result |
|---|---|---:|---:|---|---|---|
| Home v4 | `yoy0V2adMzWPXn5jJe6R8C` | 10 | 9 | Styrte AI-løsninger for arbeid, studier og hverdagsoppgaver. | 9/9 populated | PASS |
| Tjenester v4 | `WkiuLQRrmZwlTCtpKO3cXU` | 8 | 7 | Velg riktig AI-løp for behovet. | 7/7 populated | PASS |
| Bedrift v4 | `zOn5VXQY9V74rWqLBeyip7` | 10 | 9 | Konfigurerte AI-arbeidsflyter med tydelige data- og ansvarsgrenser. | 9/9 populated | PASS |
| Studenter v4 | `AhGm9skcso2bG2BmHOA5IK` | 11 | 10 | Ansvarlig AI-støtte for planlegging, forståelse og repetisjon. | 10/10 populated | PASS |
| Privatpersoner v4 | `H36n74YgmCquksYEgnHI4Z` | 9 | 8 | Praktisk AI-støtte med definerte bruks- og sikkerhetsgrenser. | 8/8 populated | PASS |
| Managed Secure v4 | `R4LeFYvy4IQmH91fS7pEQ7` | 9 | 8 | Kontrollert arkitekturgjennomgang for konfidensielle arbeidsflyter. | 8/8 populated | PASS |
| Priser v4 | `3qeoaaSEGw90RzYZjSIMa1` | 10 | 9 | Offentlige priser med tydelig leveranse- og aktiveringsstatus. | 9/9 populated | PASS |
| Tillit v4 | `nfhkzy4rocsCyg0rjLOrdi` | 9 | 8 | Tydelige grenser for sikkerhet, personvern og ansvarlig AI. | 8/8 populated | PASS |
| Plattformer v4 | `V4qys96ma9y2tX74Anwl0E` | 8 | 7 | Fire plattformspor for forskjellige behov og kontrollnivåer. | 7/7 populated | PASS |
| Oppstart v4 | `rmm6HkfI7ijGQY9dHH4XZu` | 7 | 6 | Start med behovet – ikke med sensitiv informasjon. | 6/6 populated | PASS |
| Ressurser v4 | `pOX06PeOspQdlr8gcGzjA9` | 8 | 7 | Ressurser for bedre AI-beslutninger. | 7/7 populated | PASS |
| FAQ v4 | `AkyPe1H2MTpyBfyPYPf9Iw` | 7 | 6 | Ofte stilte spørsmål om Atlas AI. | 6/6 populated | PASS |
| Om oss v4 | `RvGNzVri3oHscBnQsconc4` | 8 | 7 | Praktisk AI med styring som en del av leveransen. | 7/7 populated | PASS |
| Kontakt v4 | `SjafXw83D5CISHOaKYncSn` | 9 | 8 | Kontakt Atlas AI. | 8/8 populated | PASS |
| Juridisk v4 | `LnGmSITkmM0pIad6mV9v55` | 11 | 10 | Juridisk informasjon og ansvarlig bruk. | 10/10 populated | PASS |

**Total:** 134 slides before; 119 actual page slides after; 15 operator-only configuration slides removed; 119/119 current slides populated.

## Gamma disposition and validation

No Gamma file was modified. The Gamma inventory still contains all 15 newest v4 drafts under the same IDs, URLs and pre-edit update timestamps. The corresponding first Gamma card remains source/operator guidance for Wix header, menu, language and mobile controls.

## Wix disposition and validation

No Wix write action was executed. Current authenticated Wix context still identifies Atlas-AI site ID `1448ccad-68f0-43ea-8f0e-c9d8c0366082` as a Draft Wix Studio site. This Figma correction did not publish or change the Wix site.

## Mandatory destructive-edit safeguard

Before any future Figma deletion or other destructive mutation:

1. Capture the full pre-write slide grid, slide IDs, names, text digest, child count and expected count.
2. Create or verify a recoverable Figma version/duplicate where the connector supports it; if it does not, state that limitation before mutation.
3. Require an exact deletion signature and abort on any mismatch.
4. Mutate only the specifically authorized node IDs.
5. Run a separate post-write readback across every remaining slide.
6. Report the exact per-file before/after counts and all mutated IDs.
7. Never claim project-folder completeness unless project membership itself has been enumerated and read back.
8. Do not roll back an intact file merely to address an unverified project-browser or UI discrepancy.

## Remaining boundaries

- The available connector does not enumerate the target Figma project folder; project membership remains unproven by connector readback.
- Metadata strings visibly embedded in some remaining Figma/Gamma page slides are a separate previously documented implementation issue and were not changed.
- Functional forms, links, cookie behavior, metadata, routes, responsive states and accessibility require Wix validation.
- External Gamma image assets and normalized Figma panels retain their prior documented visual-fidelity boundaries.

## Classification

- Owner instruction that only the first slide may be deleted: `APPROVED`.
- Corrective live audit, non-restoration decision and destructive-edit safeguards: `AUTO_APPROVED`.
- Gamma and Wix non-modification: `APPROVED` scope preservation.
- Project-folder membership: `EVIDENCE_LIMITED`.
- Wix implementation and public release: `NO_GO`.

## Rollback supersession — 11:48, 03.08.2026

The owner subsequently ordered complete rollback and explicitly accepted reintroduction of the Wix configuration slides. That current instruction supersedes the non-restoration disposition above for these 15 files.

A native provider-history rollback could not be executed because the current Figma MCP runtime rejects `triggerUndo` and `saveVersionHistoryAsync`. The operation was therefore completed as controlled content-state restoration:

- one reconstructed Wix configuration slide inserted at position 1 in each controlled file;
- original hero retained at position 2 with its original node ID;
- all 119 existing page slides preserved and populated;
- total restored from 119 to 134 slides;
- independent readback passed for 15/15 files;
- Gamma and Wix remained unchanged.

The controlling result is recorded in `ATLAS_V4_COMPLETE_ROLLBACK_RESTORATION_VALIDATION_1148_03082026.md` as `ATL-VAL-20260803-074`.
