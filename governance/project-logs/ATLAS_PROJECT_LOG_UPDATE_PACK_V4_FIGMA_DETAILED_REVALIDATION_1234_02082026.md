# ATLAS PROJECT LOG UPDATE PACK — v4 Figma detailed revalidation — 12:34, 02.08.2026

**Project:** Atlas Website / Atlas AI  
**Task:** Revalidate all 15 recently created Phase 1 v4 Figma Slides files against the current Gamma v4 source pack, approved Atlas controls and measurement requirements; move only files that pass.  
**Release state:** `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.

## Sources and authority

- Explicit owner request, 02.08.2026.
- Current canonical GitHub/Drive registers and PR #40 strategy baseline.
- Gamma folder `Atlas AI - Phase 1`: full-page v4 A, full-page v4 B, replacement-sections v4 and final-control replacements v4.
- Atlas AI Technical Drawing and Measurement Report v2.1.
- Later approved Figma v3 transfer-pack typography/spacing profile.
- Live Figma Plugin API readback and rendered screenshots.

Gamma was used as the content/order/source-specific visual reference. Canonical GitHub/Drive remained authoritative for claims, governance and release state. Figma was treated as design evidence.

## Scope

- 15 Figma Slides files.
- 104 slides.
- 48 image placeholders.
- Content, slide count, terminology, controlled claims, typography, palette, margins, safe frame, image-slot geometry, CTA construction, nominal bounds, rendered text bounds and representative screenshot review.

## Confirmed passes

1. All 15 files contain the correct current v4 source copy and expected slide counts.
2. Prices and FAQ include the later final-control replacement wording.
3. All files use the common v4 typography system: Roboto Slab headings and Roboto body/labels.
4. All slides are 1920×1080 with the common 104 px left anchor, 1712 px live width and 48 px outer safe-frame discipline.
5. All 48 placeholders retain x `1240`, y `104`, width `576`, height `872`, canonical v4 names and three-alternative source metadata.
6. No rendered-text overlap or safe-frame defect was found in Hjem, Tjenester, Business, Student, Consumer, Prices, Platform lanes, Trust, Onboarding, Resources, About, Legal, FAQ or Generell kontakt.

## Verified defects and contradictions

### 1. Managed Secure rendered-text overlap — `AUTO_APPROVED` defect evidence

The earlier nominal-bounds validator used `absoluteBoundingBox`. Figma Slides multiline text nodes report a nominal height of 10 px even when rendered text is substantially taller. The prior validator therefore missed visible collisions.

A corrected `absoluteRenderBounds` audit and screenshot review found four collisions:

- Slide `2:2`, `Kontrollområder som må vurderes`:
  - Intro overlaps `01 Identitet og tilgang`.
  - Intro overlaps `05 Hendelseshåndtering`.
- Slide `2:32`, `Før en eventuell leveranse`:
  - The `Atlas dokumenterer` list overlaps `02 Kunden dokumenterer`.
  - The first list also overlaps the second list.

**Corrective rule:** All future Figma Slides text QA must use `absoluteRenderBounds` and rendered screenshots for multiline text. Nominal node height is not sufficient.

### 2. CTA token conflict — `PENDING_REVIEW`

The 13 CTA-bearing files consistently use:

- 62 px button height.
- 23 px label size.
- 24 px inter-button gap.
- 31 px pill radius.
- White fill with 1 px `#CCD5E3` stroke.

The fixed Technical Drawing v2.1 profile specifies 78 px height, 36 px text and 16 px gap. The later approved v3 transfer pack specifies a 4 px button radius. No later approved source explicitly superseding these CTA values was found.

**Result:** The 13 CTA-bearing files are content-correct and visually consistent, but cannot receive unconditional measurement approval until the v4 CTA standard is explicitly resolved. Do not silently treat the pill system as an approved supersession.

## File disposition

| Draft | Scope | Content | Rendered layout | CTA measurement | Final disposition |
|---|---|---|---|---|---|
| Hjem | 2-section v4 | PASS | PASS | N/A | `PASS / UNMOVED` |
| Tjenester | 3-section v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| Business | 5-section v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| Managed Secure | 3-section v4 | PASS | FAIL | N/A | `FAIL_LAYOUT` |
| Student | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| Consumer | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| Prices | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| Platform lanes | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| Trust | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| Onboarding | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| Resources | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| About | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| Legal | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| FAQ | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |
| Generell kontakt | Full v4 | PASS | PASS | Conflict | `CONDITIONAL / PENDING_REVIEW` |

## Figma project placement

Target project: `633513513`.

The available Figma connector can select a project only when creating a new file and exposes no existing-file move operation. Existing validated files were not duplicated or destructively recreated to simulate a move. Consequently:

- No file was moved in this workstream.
- Project membership is not claimed.
- Hjem passes the technical review but remains outside/unverified for the target project because the move path is unavailable.

## Required continuation

1. Correct Managed Secure slides `2:2` and `2:32`, then rerun rendered-bounds and screenshot QA.
2. Resolve the CTA standard explicitly: either approve 62/23/24/r31 as the v4 canonical token set or update the 13 affected files to the controlling measurement profile.
3. Move approved existing files through Figma's file browser into project `633513513` and perform post-move membership readback.
4. Preserve all release locks; no Wix content, publication, checkout, payment, entitlement or release state was changed.

## Classification

- Exact Gamma/Figma content and slide-count findings: `AUTO_APPROVED` evidence.
- Managed Secure rendered-layout defect and corrected validation method: `AUTO_APPROVED`.
- CTA-token supersession decision: `PENDING_REVIEW`.
- Existing-file project relocation: `BLOCKED / PENDING_REVIEW` completion.
- Public availability and release: `NO_GO`.