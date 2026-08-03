# ATLAS PROJECT LOG UPDATE PACK — Copy Baseline and Figma Slide Removal — 10:54, 03.08.2026

**Project:** Atlas Website / Atlas AI  
**Task:** Register the validated Norwegian website-copy report as the controlling public-copy baseline, remove the non-page Wix configuration slide from all controlled Figma v4 files, validate the resulting decks, and synchronize manifests, validation records and active controls.  
**Release state:** `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.

## Timestamp

Original operation: 10:54, 03.08.2026 Europe/Oslo.  
Corrective owner-report audit: 11:22, 03.08.2026 Europe/Oslo.

## Issue or mistake observed

1. The first slide in all 15 controlled Figma v4 files contained global Wix header, navigation, language-selector and mobile-menu configuration guidance rather than actual public page content.
2. Earlier Figma slide counts therefore included one operator-only configuration slide per file.
3. The complete 18:21 Norwegian website-copy report had been used for Gamma/Figma generation and validation but was not yet fully registered as the current active public-copy baseline in the repository overview and copy-control files.
4. An initial Figma write attempted to call `saveVersionHistoryAsync`, which is unsupported in the current `use_figma` execution environment. The failed call was atomic and changed nothing.
5. After the successful first-slide deletion, the owner reported that all v4 Figma drafts appeared completely deleted. The connector audit did not confirm that loss: all 15 known files and all 119 expected remaining slides were present and populated.
6. The initial completion wording did not make the Figma project-folder inventory limitation sufficiently prominent. The connector can inspect known file keys but cannot authoritatively enumerate membership in project `633513513`.

## Root cause

- Report/Gamma component instructions and actual page sections were transferred through the same card/slide pipeline.
- Artifact topology was treated as page topology without an explicit operator-guidance boundary.
- Earlier active-source copy controls contained representative samples rather than the complete validated Appendix A authority statement.
- General Plugin API capability was assumed to be available in the constrained connector runtime without a runtime capability check.
- The destructive edit was not preceded by a connector-verifiable immutable backup or duplicate, and the post-edit report did not immediately expose the complete per-file node/count inventory to the owner.
- The exact cause of the owner’s apparent empty/deleted project UI is not proven. It must not be silently attributed to deletion, caching, project membership or another cause without evidence.

## Corrective rules

1. Shared header, menu, language and mobile-control instructions are Wix operator configuration guidance, not standalone public page sections.
2. Every Figma page deck must begin with the canonical page hero/H1.
3. Before a destructive Figma edit, capture the complete slide grid, IDs, names, text digest, child count and expected file count.
4. Create or verify a recoverable version/duplicate where the available connector supports it. When unsupported, state the limitation before mutation.
5. Delete a node only after its text and structural signature match the exact approved target; abort on mismatch.
6. Return every mutated node ID and validate every deletion in a separate, complete readback call.
7. Report exact before/after counts and verify every remaining slide, not only the new first slide.
8. Do not claim project-folder completeness unless membership itself has been enumerated and read back.
9. Do not roll back or regenerate an intact deck merely to address an unverified project-browser/UI discrepancy.
10. Register report source files by stable Drive ID, size and checksum.
11. Use Appendix A as the exact Norwegian public-copy baseline while preserving newer explicit owner decisions and approved legal, commercial, security and release controls.
12. Do not modify Gamma where the owner explicitly instructs that Gamma should remain unchanged.
13. Do not call unsupported version-history APIs in `use_figma`.

## Evidence and sources

- DOCX Drive ID `1YFbBrmESNsWS_QvVZO5ah6Sm1TQsye5x`.
- Markdown Drive ID `1ssEO78IuebRSubl6WgqS_UYTM3_vfIf2`.
- Markdown SHA-256 `6ed168ae842df177ac4790b18132a82fdfe640752564f9f4c3203e28d0a4bc57`.
- DOCX SHA-256 `2354c572c5bbdec751c5261f16d559ea9ed05aa8c704198b36146750e7984209`.
- Controlled Drive artifact manifest `1JR8seQkIw11O2AAEwBsQF2hxV3hSSYluwvrde5d6f_8`.
- Drive validation report `1xOG4BOZbOzR7XwL4n1a0sbcRvEg6y1AekuKGw2fzIYE`.
- Drive log mirror `1YKDGzpjw2q1uXTd6aHaD6nBHygioSVIyFRRazqbM_dg`.
- Drive source-register mirror `1NPpT696lyDFrzJ4pQZtXfZ_0aoE-VBXJnBywVXGj614`.
- Live Figma Plugin API inspection, conditional deletion and independent node-level corrective readback for all 15 files.
- Gamma inventory of all 15 newest v4 drafts, unchanged IDs/URLs/timestamps.
- Authenticated Wix context showing Atlas-AI remains a Draft Studio site.

## Action taken

- Removed exactly the first slide from each of the 15 controlled Figma v4 files after signature matching.
- Reduced total Figma page-slide count from 134 to 119.
- Confirmed each new first slide is the canonical page hero/H1.
- On the owner’s correction, performed a new read-only inventory of every slide in every controlled file.
- Confirmed 119/119 remaining slides are present, readable, populated and retain nonzero child content.
- Performed no rollback, regeneration or additional Figma mutation because the live files already match the approved target state.
- Left all Gamma drafts unchanged and verified the 15 newest v4 Gamma artifacts remain available.
- Made no Wix write and verified the Atlas-AI Wix site remains Draft.
- Updated canonical error and validation records with the owner-reported incident, evidence limitation and stronger destructive-edit safeguards.
- Updated repository README and active copy/route/terminology control.
- Added the 03.08 active-source copy baseline and index.
- Added decision, error, validation, source-register and report-integrity records.
- Updated the Drive artifact manifest and appended the original correction to the Drive validation report.
- Created Drive mirrors for the project log and source/artifact register in the controlled report folder.
- Registered the source report pair and preserved all release locks.

## Figma count changes and corrective confirmation

| File | Before | Current | Corrective state |
|---|---:|---:|---|
| Home v4 | 10 | 9 | 9/9 slides populated; correct hero first |
| Tjenester v4 | 8 | 7 | 7/7 slides populated; correct hero first |
| Bedrift v4 | 10 | 9 | 9/9 slides populated; correct hero first |
| Studenter v4 | 11 | 10 | 10/10 slides populated; correct hero first |
| Privatpersoner v4 | 9 | 8 | 8/8 slides populated; correct hero first |
| Managed Secure v4 | 9 | 8 | 8/8 slides populated; correct hero first |
| Priser v4 | 10 | 9 | 9/9 slides populated; correct hero first |
| Tillit v4 | 9 | 8 | 8/8 slides populated; correct hero first |
| Plattformer v4 | 8 | 7 | 7/7 slides populated; correct hero first |
| Oppstart v4 | 7 | 6 | 6/6 slides populated; correct hero first |
| Ressurser v4 | 8 | 7 | 7/7 slides populated; correct hero first |
| FAQ v4 | 7 | 6 | 6/6 slides populated; correct hero first |
| Om oss v4 | 8 | 7 | 7/7 slides populated; correct hero first |
| Kontakt v4 | 9 | 8 | 8/8 slides populated; correct hero first |
| Juridisk v4 | 11 | 10 | 10/10 slides populated; correct hero first |

## Validation performed

- Source pair metadata and checksums verified.
- All 15 original first slides inspected before mutation.
- All 15 deletions passed the required configuration signature.
- The unsupported version-history call failed atomically and caused no partial deletion.
- All 15 decks read back after successful deletion.
- A second full live audit was run after the owner reported apparent complete deletion.
- Every known file remains accessible.
- Every deck count is exactly original count minus one.
- Every one of the 119 remaining slides has readable text and nonzero child content.
- Every new first slide is the expected canonical page hero.
- No deck begins with the Wix configuration signature.
- Gamma non-modification confirmed by inventory; no Gamma write action was executed.
- Wix non-modification confirmed by authenticated site context; no Wix write action was executed.
- Drive manifest, validation report, project log and source register were read back after the original update.

## Unresolved items

- Figma project-folder membership cannot be authoritatively enumerated through the available connector. The known files are intact, but the project-browser state seen by the owner cannot be fully diagnosed through this interface.
- Wix route, metadata, responsive, accessibility, form, cookie and internal-link implementation still require separate validation.
- Some page artifacts still visibly contain implementation metadata or drafting labels previously identified in the copy validation.
- External Gamma images and normalized Figma panel fidelity retain their existing documented boundaries.
- The Kontakt image-pack card-title `v5` naming variance remains separate and unresolved.
- Public release remains blocked pending exact candidate validation and explicit GO.

## Classification

- Exact owner correction and report baseline: `APPROVED`.
- Verified source integrity, conditional deletion, count correction, full corrective readback and non-restoration decision: `AUTO_APPROVED`.
- Figma connector limitations and corrected destructive-edit workflow: `AUTO_APPROVED`.
- Project membership diagnosis: `EVIDENCE_LIMITED`.
- Legal/transaction implementation and public availability: `PENDING_REVIEW` / `NO_GO`.
