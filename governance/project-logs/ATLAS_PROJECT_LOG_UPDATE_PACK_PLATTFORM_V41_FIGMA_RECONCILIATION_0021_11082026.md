# ATLAS PROJECT LOG UPDATE PACK — Plattform v4.1 Figma reconciliation — 00:21, 11.08.2026

## Session / task

Review the supplied `Plattform v4.1.pdf` and `Plattform v4.1.pptx` exports from Gamma document `rc0oemzx7wyufxl`, reconcile the existing `Plattform v4.1` Figma Slides file against the owner-approved Atlas Home/Tjenester v4.1 Figma adjustment standard, modify the exact file in place, and validate the complete eight-slide design/content handoff.

## Scope

- **Figma target:** `https://www.figma.com/slides/qGGeQPTVxJnqOu2WnRwvR6/Plattform-v4.1`
- **Exact Figma file key:** `qGGeQPTVxJnqOu2WnRwvR6`
- **Project-folder URL supplied in the current operator instruction:** `https://www.figma.com/files/project/63422042222`
- **Previously controlled Atlas v4.1 project reference:** `https://www.figma.com/files/project/634220422`
- **Gamma source:** `https://gamma.app/docs/rc0oemzx7wyufxl`
- **Supplied exports:** `Plattform v4.1.pdf`, `Plattform v4.1.pptx`
- **Slides:** 8
- **Scope type:** design/content handoff only.
- **Excluded:** Gamma mutation, Wix mutation, responsive/runtime acceptance, checkout/payment activation, production availability and public release.

The current operator-supplied project-folder ID differs from the previously controlled Atlas v4.1 folder reference. The Figma connector cannot authoritatively enumerate all files in a project folder or prove current project membership for an existing file. No folder ID was silently substituted or treated as authoritative. This validation therefore applies only to the exact supplied Figma file key and does not claim folder-wide completeness. The folder-reference discrepancy remains `PENDING_REVIEW` as evidence/organisation state only; it does not affect the validated file itself.

## Authority / baseline

Canonical GitHub `main` was re-read immediately before write-back at:

- `7d44a17d854d4d6ab680d6c733ddef02d8ec0ddb`

Applied sources, in controlling order:

1. current explicit operator instruction;
2. approved/canonical Atlas governance and design rules;
3. current live Figma implementation evidence;
4. supplied Gamma/PDF/PPTX evidence;
5. controlled Drive standards and prior validated handoffs;
6. labelled inference only where unavoidable.

The controlled Drive document `ATLAS Figma Adjustment and Website-Draft Preparation Standard — 23:05, 04.08.2026` is classified `CANONICAL` and was applied, including the saved 05.08.2026 defaults for typography, radii, image treatment, source-specific layout exceptions and validation.

## Source inspection

### PDF

The eight-page PDF was rendered and visually inspected page by page. The source establishes:

1. split hero with right-side workplace image and two CTA controls;
2. four platform-route cards;
3. Track A explanatory section with three arrow/item rows;
4. Track B split blue panel plus four contribution cards;
5. Track C split server-room image plus warning callout;
6. Track D dense specialist layout with a large multi-engine illustration and public start-price copy;
7. nine platform-selection criteria with six icons and three lower cards;
8. closing photographic section with two CTA controls.

### PPTX

The PPTX was inspected for canvas dimensions, text and paragraph structure, source typography, line/paragraph spacing, frame/card/callout geometry, fills, strokes, radii, embedded image placement and crop intent.

The PPTX uses the Gamma source geometry that maps to the controlled 1920×1080 Figma canvas. Source-specific body/list spacing and specialist geometry were preserved independently from the canonical principal-heading rule.

## Issues observed before correction

1. All live Figma text used `Inter` rather than the approved `Roboto Slab` / `Roboto` pairing.
2. Non-hero principal headings used inconsistent source/import sizes, including 64 px, 56 px and approximately 34.67 px, rather than the approved 50 px / 118% rule.
3. Slide 1 and Slide 8 CTA controls were raster image-filled frames rather than editable controls.
4. Slide 4 used four raster image-backed contribution-card surfaces rather than editable Atlas cards.
5. Mechanically scaled radii were inherited from the import, including approximately:
   - Slide 2 route cards: 24.81 px;
   - Slide 4 blue panel: 78.66 px;
   - Slide 5 warning callout: 24.10 px;
   - Slide 7 lower cards: 27.69 px.
6. Category-label outlines on several slides carried mechanically scaled values above the approved 4 px control radius.
7. Line/pictographic assets on Slides 3, 5 and 7 used `CROP` rather than `FIT`.
8. Slide 6 principal heading was approximately 34.67 px and its imported heading frame was too shallow for the approved 50 px / 118% treatment.
9. Atlas source/status/validation metadata were absent.
10. After the first full render, Slide 1's 64 px Roboto Slab hero heading wrapped to three lines because Figma's font metrics were slightly wider than the supplied source render, despite the approved size and source frame being retained.

## Root cause

The deck was mechanically transferred from Gamma/PPTX into Figma Slides. Copy, order, imagery and principal source geometry were substantially retained, but export/import typography, rasterized controls/content containers, mechanically scaled corner values, image scale modes and font-metric wrapping were not normalized to the owner-approved Atlas Figma contract.

## Corrective rules applied

- Hero principal heading retains the approved/source 64 px treatment; source render determines intended wrap.
- Non-hero principal headings use `Roboto Slab Regular`, 50 px, 118% line height.
- Supporting/card headings retain their source-specific hierarchy rather than being forced to 50 px.
- Body, list and box text uses `Roboto` with source-specific line height and paragraph spacing.
- Standard cards/panels/callouts use 6 px radius.
- Category labels and CTA controls use 4 px radius.
- Photography and the Slide 6 specialist illustration retain `CROP`; line/pictographic icons use `FIT`.
- Raster CTA controls and raster content-card surfaces are rebuilt as editable Figma structures.
- Source-specific split/dense layouts are preserved where the PPTX establishes intentional geometry.
- Public price copy is preserved exactly and remains separate from activation or release status.

## Figma corrections completed

### Slide 1 — hero

- Replaced Inter with Roboto Slab / Roboto.
- Hero heading retained at 64 px / 104%.
- Preserved the intended two-line source render using the exact visible wording and a controlled `-1.5%` Figma letter-spacing compensation. The source frame width and hero font size were not changed.
- Hero body uses source 25.3333 px / 133% line height.
- Rebuilt both raster CTA controls as editable frames + text:
  - `Start en plattformvurdering`;
  - `Les mer om Atlas`.
- CTAs use 4 px radius; primary uses Atlas blue and secondary uses white fill with blue border.
- Right-side photograph retained as `CROP`.

### Slide 2 — platform route selection

- Principal heading corrected to 50 px / 118%.
- Intro body uses 25.3333 px / 133%.
- Route headings use Roboto Slab; route descriptions use Roboto.
- All four route-card radii corrected from approximately 24.81 px to 6 px.
- Source 2×2 geometry and blue fill retained.

### Slide 3 — Track A

- Category label uses Roboto and 4 px outline radius.
- Principal heading corrected to 50 px / 118%.
- Two-paragraph body uses 25.3333 px / 133%, including the source-established paragraph separation.
- `Atlas bidrar med:` and supporting hierarchy converted to Roboto Slab / Roboto.
- All three arrow/pictographic assets changed from `CROP` to `FIT`.

### Slide 4 — Track B

- Category label uses 4 px radius.
- Principal heading corrected to 50 px / 118%.
- Blue explanatory panel radius corrected from approximately 78.66 px to 6 px.
- Source paragraph spacing retained.
- Rebuilt all four raster contribution-card surfaces as editable cards:
  - white fill;
  - `#D8D4D4` border;
  - 6 px card radius;
  - 12 px Atlas blue vertical gradient accent strip.
- Original text content and card placement retained.

### Slide 5 — Track C

- Category label corrected to 4 px radius.
- Principal heading corrected to 50 px / 118% with the source-visible two-line treatment.
- Two-paragraph body uses source 25.3333 px / 133% spacing.
- Warning callout radius corrected from approximately 24.10 px to 6 px.
- Warning icon changed from `CROP` to `FIT`.
- Server-room photograph retained as `CROP`.

### Slide 6 — Track D

- Preserved the intentionally dense specialist layout and source-specific small body/pricing hierarchy.
- Principal heading corrected to 50 px / 118%.
- Heading wrapper geometry increased only enough to contain the approved title without clipping; image and body start positions were preserved.
- Body retained source 13.3333 px / 103% line height and source paragraph separation.
- `159K`, `Fra kr ekskl. MVA`, and `Research Multi-Engine startpris, pluss forbruksbasert kostnad` were preserved exactly; no pricing decision was created.
- Category label corrected to 4 px radius.
- Specialist illustration retained as `CROP`.

### Slide 7 — selection criteria

- Principal heading corrected to 50 px / 118%.
- Source-specific 1807.65625 px intro width and offset retained as an explicit specialist-layout exception.
- Criterion headings use Roboto Slab 28 px / 104%; descriptions use Roboto 22.6667 px / 125%.
- All six pictographic assets changed from `CROP` to `FIT`.
- Three lower card radii corrected from approximately 27.69 px to 6 px.

### Slide 8 — closing CTA

- Principal heading corrected to 50 px / 118%.
- Two-paragraph body uses source 25.3333 px / 133% spacing.
- Rebuilt both raster CTA controls as editable frames + text:
  - `Start en plattformvurdering`;
  - `Ta kontakt med Atlas`.
- CTAs use 4 px radius.
- Full-width closing photograph retained as `CROP`.

## Validation result

A separate expected-baseline validator was executed after all design mutations and after the final Slide 1 rendered-wrap correction.

**`PASS_DESIGN_AND_CONTENT_HANDOFF`**

- Slide count/order: **8/8 PASS**.
- Canvas: **8/8 at 1920×1080 PASS**.
- Visible Figma text nodes after editable CTA reconstruction: **64/64 expected PASS**.
- Supplied PPTX visible text: **60/60 source text blocks preserved**, with visual wrapping controlled where needed.
- PDF-visible CTA labels: **4/4 preserved exactly**.
- Hero principal heading: **64 px / 104% PASS**, with source-render two-line wrap restored without changing font size or source frame width.
- Non-hero principal headings: **7/7 at 50 px / 118% PASS**.
- Source-specific body/list/box line-height and paragraph-spacing treatment: **PASS**.
- Font-family violations: **0 PASS**.
- Missing fonts: **0 PASS**.
- Visible out-of-bounds nodes: **0 PASS**.
- Unexplained visible box radii above 6 px: **0 PASS**.
- Raster CTA controls remaining: **0 PASS**.
- Raster Slide-4 content-card surfaces remaining: **0 PASS**.
- Image-bearing nodes: **14/14 PASS**.
- Image hashes: **14/14 non-empty PASS**.
- Image treatment: **4 CROP** photographic/specialist assets and **10 FIT** pictographic assets PASS.
- Image opacity, clipping, positive geometry and slide-bound containment: **14/14 PASS**.
- Literal duplicate-bullet text: **0 PASS**.
- Atlas source/status metadata: **8/8 PASS**.
- Rendered visual QA: **8/8 PASS**.

The corrected deck now stores on all eight slides:

- Gamma source: `https://gamma.app/docs/rc0oemzx7wyufxl`
- Source PDF: `Plattform v4.1.pdf`
- Source PPTX: `Plattform v4.1.pptx`
- Status: `PASS_DESIGN_AND_CONTENT_HANDOFF`
- Deterministic validation: `PASS`
- Rendered visual QA: `PASS_8_OF_8`
- Validated at: `00:21, 11.08.2026 Europe/Oslo`
- Standard: `ATLAS Figma Adjustment and Website-Draft Preparation Standard`

## Provider / workflow limitations and errors observed

1. **Project-folder inventory limitation.** Figma does not provide an authoritative global project-folder inventory/membership read for existing files through the current connector. The supplied folder-ID discrepancy therefore cannot be resolved by inference.
2. **Recoverable duplicate/version limitation.** The current connector did not expose a supported file-history duplicate/version operation for this exact existing Slides file. The complete pre-edit inventory plus supplied PDF/PPTX exports were retained as recovery evidence.
3. **Read-only reference extraction syntax error.** One initial read-only `use_figma` script used to extract a previously validated Atlas card precedent contained a JavaScript syntax error. Figma execution is atomic; the failed script made no design mutation. The script was corrected before the reference was used and the subsequent read succeeded. This is workflow evidence only, not a design defect.

## Unresolved items

- Confirm whether the current operator-intended Atlas v4.1 project folder is `63422042222` or the previously controlled `634220422`. This is an organisational/reference correction and must not be silently inferred.
- No other content/design discrepancy remains within the exact eight-slide assessed scope.
- Wix implementation, responsive/runtime validation and public release remain separate workstreams.

## Release boundary

This design/content handoff pass does **not** imply:

- Wix implementation;
- responsive/runtime acceptance;
- checkout/payment activation;
- Atlas-administered Track C general availability;
- production readiness;
- public release.

Existing Atlas release locks remain unchanged and public release remains `NO_GO` until the controlling runtime/release gates pass.

## Classification of this update

- Exact operator-directed Figma correction, validated design fixes, editability fixes, source-specific spacing/wrap treatment, image-treatment corrections and non-sensitive quality-control evidence: **`AUTO_APPROVED`**.
- Project-folder ID discrepancy: **`PENDING_REVIEW`** until the owner confirms the intended folder reference.
- Commercial/pricing policy changes: **none created**.
- Legal/provider-policy/safety-posture changes: **none created**.
- Production availability and public release: **unchanged / `NO_GO`**.
