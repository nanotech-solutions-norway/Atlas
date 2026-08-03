# ATLAS PROJECT LOG UPDATE PACK — Copy Baseline and Figma Slide Removal — 10:54, 03.08.2026

**Project:** Atlas Website / Atlas AI  
**Task:** Register the validated Norwegian website-copy report as the controlling public-copy baseline, remove the non-page Wix configuration slide from all canonical Figma v4 files, validate the resulting decks, and synchronize manifests, validation records and active controls.  
**Release state:** `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.

## Timestamp

10:54, 03.08.2026 Europe/Oslo.

## Issue or mistake observed

1. The first slide in all 15 canonical Figma v4 files contained global Wix header, navigation, language-selector and mobile-menu configuration guidance rather than actual public page content.
2. Earlier Figma slide counts therefore included one operator-only configuration slide per file.
3. The complete 18:21 Norwegian website-copy report had been used for Gamma/Figma generation and validation but was not yet fully registered as the current active public-copy baseline in the repository overview and copy-control files.
4. An initial Figma write attempted to call `saveVersionHistoryAsync`, which is unsupported in the current `use_figma` execution environment.

## Root cause

- Report/Gamma component instructions and actual page sections were transferred through the same card/slide pipeline.
- Artifact topology was treated as page topology without an explicit operator-guidance boundary.
- Earlier active-source copy controls contained representative samples rather than the complete validated Appendix A authority statement.
- General Plugin API capability was assumed to be available in the constrained connector runtime without a runtime capability check.

## Corrective rules

1. Shared header, menu, language and mobile-control instructions are Wix operator configuration guidance, not standalone public page sections.
2. Every Figma page deck must begin with the canonical page hero/H1.
3. Delete a first slide only after its text matches the Wix configuration signature.
4. Validate every deletion in a separate readback call and confirm the new first slide and reduced count.
5. Register report source files by stable Drive ID, size and checksum.
6. Use Appendix A as the exact Norwegian public-copy baseline while preserving newer explicit owner decisions and approved legal, commercial, security and release controls.
7. Do not modify Gamma where the owner explicitly instructs that Gamma should remain unchanged.
8. Do not call unsupported version-history APIs in `use_figma`; return all affected node IDs and perform independent post-write readback.

## Evidence and sources

- DOCX Drive ID `1YFbBrmESNsWS_QvVZO5ah6Sm1TQsye5x`.
- Markdown Drive ID `1ssEO78IuebRSubl6WgqS_UYTM3_vfIf2`.
- Markdown SHA-256 `6ed168ae842df177ac4790b18132a82fdfe640752564f9f4c3203e28d0a4bc57`.
- DOCX SHA-256 `2354c572c5bbdec751c5261f16d559ea9ed05aa8c704198b36146750e7984209`.
- Controlled Drive artifact manifest `1JR8seQkIw11O2AAEwBsQF2hxV3hSSYluwvrde5d6f_8`.
- Drive validation report `1xOG4BOZbOzR7XwL4n1a0sbcRvEg6y1AekuKGw2fzIYE`.
- Drive log mirror `1YKDGzpjw2q1uXTd6aHaD6nBHygioSVIyFRRazqbM_dg`.
- Drive source-register mirror `1NPpT696lyDFrzJ4pQZtXfZ_0aoE-VBXJnBywVXGj614`.
- Live Figma Plugin API inspection, conditional deletion and post-delete readback for all 15 files.

## Action taken

- Removed the first slide from all 15 canonical Figma v4 files.
- Reduced total Figma page-slide count from 134 to 119.
- Confirmed each new first slide is the canonical page hero/H1.
- Left all Gamma drafts unchanged.
- Updated repository README and the active copy/route/terminology control.
- Added the 03.08 active-source copy baseline and index.
- Added decision, error, validation, source-register and report-integrity records.
- Updated the Drive artifact manifest and appended the correction to the Drive validation report.
- Created Drive mirrors for the project log and source/artifact register in the controlled report folder.
- Registered the source report pair and preserved all release locks.

## Figma count changes

| File | Before | After |
|---|---:|---:|
| Home v4 | 10 | 9 |
| Tjenester v4 | 8 | 7 |
| Bedrift v4 | 10 | 9 |
| Studenter v4 | 11 | 10 |
| Privatpersoner v4 | 9 | 8 |
| Managed Secure v4 | 9 | 8 |
| Priser v4 | 10 | 9 |
| Tillit v4 | 9 | 8 |
| Plattformer v4 | 8 | 7 |
| Oppstart v4 | 7 | 6 |
| Ressurser v4 | 8 | 7 |
| FAQ v4 | 7 | 6 |
| Om oss v4 | 8 | 7 |
| Kontakt v4 | 9 | 8 |
| Juridisk v4 | 11 | 10 |

## Validation performed

- Source pair metadata and checksums verified.
- All 15 first slides inspected before mutation.
- All 15 deletions passed the required configuration signature.
- The unsupported version-history call failed atomically and caused no partial deletion.
- All 15 decks read back after successful deletion.
- Every deck count decreased by one.
- Every new first slide is the expected canonical page hero.
- No deck still begins with the Wix configuration signature.
- Gamma non-modification confirmed by scope; no Gamma write action was executed.
- Drive manifest, validation report, project log and source register were read back after update.

## Unresolved items

- Wix route, metadata, responsive, accessibility, form, cookie and internal-link implementation still require separate validation.
- Some page artifacts still visibly contain implementation metadata or drafting labels previously identified in the copy validation.
- External Gamma images and normalized Figma panel fidelity retain their existing documented boundaries.
- The Kontakt image-pack card-title `v5` naming variance remains separate and unresolved.
- Public release remains blocked pending exact candidate validation and explicit GO.

## Classification

- Exact owner correction and report baseline: `APPROVED`.
- Verified source integrity, conditional deletion, count correction and post-delete readback: `AUTO_APPROVED`.
- Figma connector limitation and corrected workflow: `AUTO_APPROVED`.
- Legal/transaction implementation and public availability: `PENDING_REVIEW` / `NO_GO`.
