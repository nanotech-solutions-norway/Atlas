# ATLAS PROJECT LOG UPDATE PACK — Tillit v4 Figma reconciliation — 16:35, 10.08.2026

## Session / task

Reconcile and validate the existing `Tillit v4` Figma Slides deck against the supplied Gamma-derived PDF/PPTX exports and the owner-approved Atlas Home/Tjenester v4.1 Figma configuration, including the approved source-specific body/list line-spacing rule.

## Scope

- **Figma target:** `https://www.figma.com/slides/ZgbIXGcKgtQw9eI0hgA066/Tillit-v4`
- **Exact Figma file key:** `ZgbIXGcKgtQw9eI0hgA066`
- **Figma project reference:** `https://www.figma.com/files/project/634220422`
- **Gamma source:** `https://gamma.app/docs/3igs67bh9d1wv0e`
- **Supplied exports:** `Tillit-v4.pdf`, `Tillit-v4.pptx`
- **Slides:** 8
- **Scope type:** design/content handoff only.
- **Excluded:** Gamma mutation, Wix mutation, responsive/runtime acceptance, checkout/payment activation, production availability and public release.

The Figma connector cannot authoritatively enumerate every file in project folder `634220422`. This validation therefore applies only to the exact supplied Figma file key above and does not claim folder-wide completeness.

## Authority / baseline

Canonical GitHub `main` was re-read immediately before task write-back at:

- `7d44a17d854d4d6ab680d6c733ddef02d8ec0ddb`

The controlled Google Drive document `ATLAS Figma Adjustment and Website-Draft Preparation Standard — 23:05, 04.08.2026` is classified `CANONICAL` and was applied together with the current operator instruction.

Source authority remained:

1. explicit current operator instruction;
2. approved/canonical Atlas governance and design rules;
3. current live Figma implementation evidence;
4. supplied Gamma/PDF/PPTX evidence;
5. controlled prior validation handoffs;
6. labelled inference.

No lower-authority source was allowed to silently override a higher-authority approved rule.

## Source inspection

### PDF

The eight-page PDF was rendered and visually inspected page by page before mutation, including the two photographic split layouts, six-card third-party boundary layout, numbered principle layout, responsibility split panel, process diagram, eight-step detail layout and four-card closing framework.

### PPTX

The PPTX was inspected programmatically for:

- 1920 × 1080-equivalent canvas dimensions;
- exact copy and deliberate line breaks;
- source font families, sizes and paragraph spacing;
- text-box geometry and principal margins;
- card/panel/callout geometry;
- fills, strokes and mechanically imported radii;
- raster CTA/card surfaces;
- image dimensions and crop intent.

Source-specific body, list and box spacing was preserved independently from the 118% principal-heading rule.

## Issues observed

1. Imported Figma typography used `Inter` instead of the approved `Roboto Slab` / `Roboto` pairing.
2. Non-hero principal headings ranged from approximately 32–64 px rather than the approved 50 px / 118% rule.
3. Slide 1 CTA controls were raster image-filled frames rather than editable controls.
4. Slide 2 used six raster image-backed card surfaces rather than editable Atlas cards.
5. Several source shapes retained mechanically scaled rounded corners substantially above the approved radius taxonomy, including:
   - Slide 4 number badges and warning callout;
   - Slide 5 left responsibility panel (~127.7 px);
   - Slide 8 four framework cards (~31.9 px) and bottom callout (~24.1 px).
6. Slide 4 warning icon, Slide 5 arrow icons and Slide 8 information icon used `CROP` despite being line/pictographic assets.
7. Slide 6 principal heading was only 32 px in the imported deck and required controlled geometry adjustment to accommodate the canonical 50 px / 118% treatment without disturbing the dense source diagram.
8. Slide 7 imported step numbers lost the source leading zeroes, displaying `1–8` rather than `01–08`.
9. Atlas source/status/validation metadata were absent from the deck.

## Root cause

The deck had been mechanically transferred from Gamma/PPTX into Figma Slides. Copy, placement and imagery were substantially retained, but export-specific Inter typography, rasterized controls/card surfaces, mechanically scaled radii, image scale modes and one numbering representation were inherited from the import rather than normalized to the approved Atlas Figma contract.

## Corrective rules applied

1. Hero principal heading remains `Roboto Slab Regular`, 64 px / 104%.
2. Every non-hero principal page/section heading uses `Roboto Slab Regular`, 50 px / 118%.
3. The 118% rule applies only to principal non-hero headings.
4. Body, list, box, diagram and supporting text follows source-specific PPTX spacing.
5. `Roboto Slab` is used for display/card headings; `Roboto` for body copy, labels and controls.
6. Standard content cards/panels/callouts use 6 px radius; labels/CTAs/small badge controls use 4 px; full backgrounds remain 0 px.
7. Raster CTA controls and raster content-card surfaces are reconstructed as editable Figma structures.
8. Photography/source diagrams retain source `CROP` intent; line/pictographic icons use `FIT`.
9. Source-specific specialist geometry is preserved when the PPTX establishes an intentional exception to the global 32 px rhythm/padding default.
10. Copy, claim boundaries and release wording remain unchanged unless explicitly approved by the operator.

## Figma corrections completed

### Slide 1 — hero

- Hero heading converted to `Roboto Slab Regular`, 64 px / 104%.
- Hero body converted to `Roboto Regular`, 25.3333 px / 133%.
- Rebuilt both source CTAs as editable Figma frames + text:
  - `Les rammeverket`
  - `Kontakt Atlas`
- CTA radius normalized to 4 px.
- Hero photography retained as `CROP`.

### Slide 2 — third-party technology boundary

- Principal heading normalized to 50 px / 118%.
- Intro/body uses source 24 px / 129% with the source paragraph gap retained.
- Rebuilt all six raster card-background images as editable Atlas card structures.
- Each card now uses:
  - white editable surface;
  - neutral `#D8D4D4` 1 px border;
  - 6 px radius;
  - source-faithful 12 px vertical blue gradient accent (`#476FD6` → `#1C3F99`).
- Card headings use `Roboto Slab`, 29.3333 px / 104%.
- Card bodies use `Roboto`, 24 px / 129%.

### Slide 3 — data boundary

- Principal heading normalized to 50 px / 118%.
- Preserved the source-visible line break after `per`.
- Body uses 25.3333 px / 133%.
- Data-centre photograph retained as `CROP`.

### Slide 4 — data-handling principles

- Principal heading normalized to 50 px / 118%.
- Intro/body/callout text uses 25.3333 px / 133%.
- Number badges normalized to 4 px radius and retain source 38.6667 px number typography.
- Item headings use `Roboto Slab`, 32 px / 104%.
- Warning callout normalized to 6 px radius.
- Warning pictogram changed from `CROP` to `FIT`.
- Preserved the source-specific 1807.65625 px intro width.

### Slide 5 — human decision responsibility

- Left blue panel normalized from approximately 127.7 px radius to 6 px.
- Principal heading normalized to 50 px / 118% with the source-visible two-line break preserved.
- Left body uses 25.3333 px / 133% with the source paragraph gap retained.
- Supporting heading uses `Roboto Slab`, 32 px / 104%.
- Six right-hand statements were corrected to source semantics: bold lead phrase + regular explanatory text.
- All six arrow pictograms changed from `CROP` to `FIT`.

### Slide 6 — public-claim assessment diagram

- Principal heading normalized from 32 px to 50 px / 118%.
- The heading wrapper was moved to `y=54` and resized to 59 px high so the canonical heading fits without interfering with the source diagram or intro.
- Intro/footer retain their source-specific 12 px / 100% treatment.
- Four diagram labels use `Roboto Slab`, 37.3333 px / 104%.
- The dense source diagram remains a controlled `CROP` image exception and was not raster-to-vector reconstructed.

### Slide 7 — detailed eight-step review

- Principal heading normalized to 50 px / 118%.
- Restored exact source numbering `01` through `08` using `Roboto Slab Light`, 22.6667 px / 100%.
- Step headings use `Roboto Slab`, 28 px / 104%.
- Step bodies use `Roboto`, 22.6667 px / 126%.
- Source divider geometry retained.

### Slide 8 — responsible-AI framework

- Principal heading normalized to 50 px / 118%.
- Intro/card/callout body text uses 25.3333 px / 133%.
- Four framework headings use `Roboto Slab`, 32 px / 104%, preserving the source emoji labels.
- Four card radii normalized from approximately 31.9 px to 6 px.
- Bottom callout radius normalized from approximately 24.1 px to 6 px.
- Bottom information icon changed from `CROP` to `FIT`.

## Source-specific layout exceptions recorded

The global 32 px rhythm/padding remains the Atlas default. The following specialist layouts preserve explicit PPTX-established geometry rather than being silently normalized:

- Slide 2 accent-strip third-party cards, including source text inset;
- Slide 4 1807.65625 px intro width and numbered-principle arrangement;
- Slide 5 split responsibility panel and source text inset;
- Slide 6 dense infographic composition;
- Slide 8 framework-card source inset.

These exceptions retain source design intent while still applying canonical typography, radius, editability and image-treatment controls.

## Content contradiction preserved for review

The supplied source on Slide 4 is titled `Syv prinsipper for datahåndtering`, while the slide itself contains only four numbered principles (`1–4`) before the warning callout. Both the attached PDF/PPTX and the live Figma source show the same state.

This task did **not** invent or add principles 5–7. The source was preserved exactly because public copy/content changes require a higher-authority content decision.

- **Classification:** `PENDING_REVIEW` content inconsistency.
- **Recommended next action:** confirm whether the title should become `Fire prinsipper for datahåndtering` or whether three additional approved principles are missing from the source.

## Validation result

A separate expected-baseline validator was executed after all design mutations.

**Result:** `PASS_DESIGN_AND_CONTENT_HANDOFF`

| Control | Result |
|---|---:|
| Slide count/order | 8/8 `PASS` |
| Canvas | 8/8 at 1920×1080 `PASS` |
| Expected visible text nodes | 87/87 `PASS` |
| Exact controlled copy by node ID | 87/87 `PASS` |
| Hero principal heading | 64 px / 104% `PASS` |
| Non-hero principal headings | Slides 2–8 at 50 px / 118% `PASS` |
| Source-specific body/list/diagram spacing | `PASS` |
| Source-specific paragraph gaps | Slides 2 and 5 `PASS` |
| Font-family violations | 0 `PASS` |
| Missing fonts | 0 `PASS` |
| Unexplained visible radius > 6 px | 0 `PASS` |
| Raster CTA controls remaining | 0 `PASS` |
| Raster Slide-2 card surfaces remaining | 0 `PASS` |
| Image-bearing nodes | 11/11 `PASS` |
| Image hashes | 11/11 non-empty `PASS` |
| Image modes | 3 source photo/diagram `CROP`; 8 pictographic icons `FIT` `PASS` |
| Image clipping/opacity/transform/positive geometry | 11/11 `PASS` |
| Visible nodes outside slide bounds | 0 `PASS` |
| Text truncation findings | 0 `PASS` |
| Literal duplicate-bullet text | 0 `PASS` |
| Atlas source metadata | 8/8 `PASS` |
| Rendered page-by-page visual QA | 8/8 `PASS` |

## Final Figma metadata

All eight slides now carry:

- Gamma source: `https://gamma.app/docs/3igs67bh9d1wv0e`
- Source PDF: `Tillit-v4.pdf`
- Source PPTX: `Tillit-v4.pptx`
- Status: `PASS_DESIGN_AND_CONTENT_HANDOFF`
- Deterministic validation: `PASS`
- Rendered visual QA: `PASS_8_OF_8`
- Validated at: `16:35, 10.08.2026 Europe/Oslo`

## Final classification

`PASS_DESIGN_AND_CONTENT_HANDOFF`

This classification applies only to the exact eight-slide Figma design/content handoff assessed above.

It does **not** imply:

- Wix implementation;
- responsive/runtime validation;
- checkout/payment activation;
- production availability;
- public release.

Public release remains `NO_GO` until the controlling runtime and release gates pass.

## Classification of this update

- Exact operator-directed Figma correction, validated typography/geometry/radius/image/control fixes, source line-break restoration, numbering correction and non-sensitive QA improvements: `AUTO_APPROVED`.
- Slide 4 `Syv prinsipper` / four visible principles content inconsistency: `PENDING_REVIEW`.
- Commercial, legal, provider-policy, safety-posture, production-availability and public-release decisions: unchanged.
