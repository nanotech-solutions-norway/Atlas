# ATLAS PROJECT LOG UPDATE PACK — Kontakt v4.1 Figma reconciliation — 13:55, 11.08.2026

## Session / task

Review the supplied `Kontakt-v41.pdf` and `Kontakt-v41.pptx` exports from Gamma document `ob03k9wee43in6c`, reconcile the existing `Kontakt v4.1` Figma Slides file against the owner-approved Atlas Home/Tjenester v4.1 configuration, modify the exact existing file in place, and validate the five-slide design/content handoff.

## Scope

- **Figma target:** `https://www.figma.com/slides/MoXhiyG67Lzft1Jo6Xyeej/Kontakt-v41`
- **Exact Figma file key:** `MoXhiyG67Lzft1Jo6Xyeej`
- **Figma project reference:** `https://www.figma.com/files/project/634220422`
- **Gamma source:** `https://gamma.app/docs/ob03k9wee43in6c`
- **Supplied exports:** `Kontakt-v41.pdf`; `Kontakt-v41.pptx`
- **Slides:** five existing slides — `0:20`, `0:22`, `0:23`, `0:24`, `0:25`.
- **Scope type:** Figma design/content handoff only.
- **Excluded:** Gamma mutation, Wix/runtime mutation, production availability and public release.

The Figma connector cannot authoritatively enumerate every file in project folder `634220422`. This validation therefore applies only to the exact supplied file key and is not a folder-wide completeness certification.

## Authority / baseline

Execution followed the current operator instruction, the canonical Atlas source-authority hierarchy, the CANONICAL `ATLAS Figma Adjustment and Website-Draft Preparation Standard`, the validated Home v4.1 and Tjenester v4.1 precedents, the current live Figma implementation, and the supplied PDF/PPTX source evidence.

The live validated Tjenester v4.1 CTA precedent was read directly and applied where relevant:
- primary CTA: horizontal blue gradient, 2 px Atlas-blue stroke, 4 px radius, Roboto SemiBold;
- secondary CTA: white fill, 2 px Atlas-blue stroke, 4 px radius;
- section/category label outline: 4 px radius and 1.5 px stroke.

The validated FAQ v4.1 editable-card precedent was also read directly and applied to the Kontakt form-field card reconstruction:
- white card fill;
- `#D8D4D4` border;
- 3 px stroke;
- 6 px radius;
- 12 px clipped blue gradient accent.

## Source findings

The five-slide source defines:
1. split-image contact hero with two calls to action;
2. four audience/contact categories with standalone pictographic icons;
3. a dense contact-form guidance section with six field cards, one compact submit CTA and one blue security guidance panel;
4. post-submission workflow guidance with a left-side photograph, a three-stage arrow graphic and success/error states; and
5. four FAQ items plus a privacy/security informational callout.

### Source export discrepancies

PDF inspection found two source-export canvas inconsistencies:
- PDF pages 1, 2 and 5: approximately `900 × 507.12 pt`;
- PDF page 3: `900 × 854.88 pt`;
- PDF page 4: `900 × 523.92 pt`;
- PPTX: all five slides are `10 × 5.625 in` / 16:9;
- canonical Atlas Figma contract: `1920 × 1080`.

The canonical 1920×1080 standard and PPTX geometry therefore govern the Figma handoff for slides 3 and 4. The taller PDF canvases are retained as source evidence and were not silently used to distort the Figma slide geometry.

## Issues observed before correction

1. Imported `Inter` typography instead of the controlled `Roboto Slab` / `Roboto` contract.
2. Imported text used `AUTO` line height rather than the controlled Atlas hierarchy.
3. Non-hero principal headings did not follow the approved 50 px / 118% rule.
4. Hero and form-submit CTAs remained raster image fills rather than editable Figma controls.
5. Six Slide-3 form-field card surfaces remained raster image fills.
6. Several imported box radii were mechanical PPTX/Gamma scaling artifacts rather than approved Atlas values, including:
   - Slide-2 label approximately `6.5448 px`;
   - Slide-3 label approximately `4.3960 px`;
   - Slide-3 security panel approximately `113.1039 px`;
   - Slide-4 label approximately `6.1290 px`;
   - Slide-5 label approximately `6.5448 px`;
   - four Slide-5 icon containers approximately `9.6856 px`;
   - Slide-5 privacy callout approximately `17.2145 px`.
7. Standalone line/pictographic icons on Slides 2 and 5 were imported with `CROP` rather than `FIT`.
8. Atlas source/status metadata was absent.

## Root cause

The PPTX-to-Figma import preserved source copy, broad geometry and source imagery, but also retained mechanical import typography, automatic line-height behavior, rasterized controls/card surfaces and scaled corner radii. These are import artifacts rather than approved Atlas design decisions.

## Corrective rules applied

- Preserve all five existing slide nodes and source order; do not delete or recreate slides.
- Use `Roboto Slab Regular` for principal/supporting/card headings and `Roboto` for body, labels and controls while preserving bold/italic emphasis.
- Preserve the 64 px / 104% hero treatment.
- Use 50 px / 118% for every non-hero principal heading.
- Preserve source-specific supporting/body sizes while assigning controlled line heights.
- Category/section label outlines use 4 px radius and 1.5 px stroke.
- Standard content cards/panels/callouts use 6 px radius.
- Rebuild raster CTAs as editable Figma frames and editable text.
- Rebuild raster form-field card surfaces as editable Figma cards using the validated FAQ card treatment.
- Use `FIT` for standalone line/pictographic icons; preserve source `CROP` for photography and the composite workflow arrow graphic.
- Preserve native unordered-list semantics on the security guidance list and do not add literal duplicate bullets.
- Keep design/content PASS separate from Wix/runtime/release approval.

## Actions completed

### Slide 1 — Kontakt hero
- Hero set to Roboto Slab Regular, 64 px / 104%.
- Body set to Roboto, 25.333 px / 133%.
- Removed one imported trailing blank line not present in the visible PDF source.
- Rebuilt two raster CTAs as editable controls:
  - `Send en henvendelse` — primary Atlas gradient;
  - `Se hvem vi hjelper` — secondary white/blue outline;
  - Roboto SemiBold 24 px / 30 px line height;
  - 2 px stroke and 4 px radius.
- Source hero photograph retained as CROP.

### Slide 2 — Hvem vi hjelper
- Section label set to Roboto 20 px / 96%.
- Principal heading set to Roboto Slab 50 px / 118%.
- Intro/body set to Roboto 25.333 px / 133%.
- Four category headings set to Roboto Slab 32 px / 104%.
- Four category body blocks set to Roboto 25.333 px / 133%.
- Section label radius/stroke corrected to 4 px / 1.5 px.
- Four standalone icons changed from CROP to FIT.

### Slide 3 — Kontaktskjema
- Section label set to Roboto 13.333 px / 96%.
- Principal heading set to Roboto Slab 50 px / 118%.
- Intro/body and field descriptions set to Roboto 17.333 px / 126%.
- Six field headings set to Roboto Slab 21.333 px / 104%.
- Existing bold category emphasis and blue required-field markers preserved.
- Six raster field-card surfaces rebuilt as editable cards:
  - white fill;
  - `#D8D4D4` border;
  - 3 px stroke;
  - 6 px radius;
  - 12 px clipped blue gradient accent.
- Blue `Viktig å huske` panel radius corrected from approximately 113.1 px to 6 px.
- Native unordered-list semantics preserved.
- Compact raster submit CTA rebuilt as editable `Send henvendelse` control using Atlas gradient, 2 px stroke, 4 px radius and Roboto SemiBold.
- No raster card or CTA image fills remain on this slide.

### Slide 4 — Etter innsending
- Section label set to Roboto 18.667 px / 96%.
- Principal heading set to Roboto Slab 50 px / 118%.
- Intro/body set to Roboto 24 px / 133%.
- Three workflow labels set to Roboto Slab 24 px / 104%.
- Success/error headings set to Roboto Slab 29.333 px / 104%.
- Success/error body text set to Roboto 24 px / 133%, preserving bold lead-ins.
- Section label radius/stroke corrected to 4 px / 1.5 px.
- Source photograph and composite arrow graphic retained as CROP.

### Slide 5 — Vanlige spørsmål
- Section label set to Roboto 20 px / 96%.
- Principal heading set to Roboto Slab 50 px / 118%.
- Intro/body set to Roboto 25.333 px / 133%.
- Four question headings set to Roboto Slab 32 px / 104%.
- FAQ body copy and informational callout text set to Roboto 25.333 px / 133%, preserving bold/italic emphasis.
- Section label radius/stroke corrected to 4 px / 1.5 px.
- Four icon-container radii corrected from approximately 9.686 px to 6 px.
- Privacy/security callout radius corrected from approximately 17.214 px to 6 px.
- Four FAQ icons and the callout icon changed from CROP to FIT.

## Validation result

**`PASS_DESIGN_AND_CONTENT_HANDOFF`**

A separate deterministic post-edit validator returned `pass: true` with zero errors and zero warnings.

| Control | Result |
|---|---:|
| Slide count/order | 5/5 PASS |
| Canvas | 5/5 at 1920×1080 PASS |
| Visible/editable text nodes | 56 |
| Exact controlled-copy multiset | FNV-1a `ef8253e6` PASS |
| Hero | 64 px / 104% PASS |
| Non-hero principal headings | 4/4 at 50 px / 118% PASS |
| Font-family violations | 0 PASS |
| Missing fonts | 0 PASS |
| Visible slide-bound violations | 0 PASS |
| Text-parent clipping warnings | 0 PASS |
| Unexplained radii above 6 px | 0 PASS |
| Editable CTAs | 3/3 PASS |
| Raster CTA controls remaining | 0 PASS |
| Editable form-field cards | 6/6 PASS |
| Raster form-card surfaces remaining | 0 PASS |
| Remaining source image-bearing nodes | 12/12 valid hashes PASS |
| Image modes | 3 CROP / 9 FIT PASS |
| Native security list semantics | UNORDERED PASS |
| Duplicate literal bullets | 0 PASS |
| Rendered page-by-page visual QA | 5/5 PASS |
| Atlas metadata readback | 5/5 PASS |

All five slides now carry:
- Gamma source `https://gamma.app/docs/ob03k9wee43in6c`;
- source PDF `Kontakt-v41.pdf`;
- source PPTX `Kontakt-v41.pptx`;
- `handoffStatus = PASS_DESIGN_AND_CONTENT_HANDOFF`;
- `deterministicValidation = PASS`;
- `renderedVisualQA = PASS_5_OF_5`;
- `validatedAt = 13:55, 11.08.2026 Europe/Oslo`;
- the recorded PDF/PPTX canvas discrepancy.

The slide row was renamed to `Kontakt v4.1`.

## Workflow/provider observation

A read-only attempt to inspect the Tjenester precedent via `page.findAll(...)` failed because the Slides runtime encountered an unsupported `CANVAS_GRID` object during broad page traversal. No design mutation occurred. The query was corrected to traverse `SLIDE_GRID → SLIDE_ROW → SLIDE` explicitly, after which the canonical Tjenester CTA and label controls were read successfully.

Corrective rule: in Figma Slides, avoid broad `PageNode.findAll` traversal when the runtime exposes grid/container node types that are not safely serialized by the plugin execution layer; traverse the slide-grid hierarchy explicitly.

## Provider / workflow limitation

The Figma connector cannot authoritatively enumerate every file in the supplied project folder. The PASS therefore applies specifically to file key `MoXhiyG67Lzft1Jo6Xyeej`.

The current execution surface does not provide an authoritative connector-created immutable version-history checkpoint for the existing Slides file. Recovery/reference evidence consists of the supplied PDF/PPTX, captured pre-edit inventory and non-slide-destructive mutation record.

## Release / implementation boundary

- Exact Figma design/content handoff: **PASS**.
- Gamma source: unchanged.
- Wix/runtime implementation: unchanged.
- Responsive/accessibility/runtime acceptance: separate.
- Production availability: unchanged.
- Public release remains **NO_GO** until controlling Atlas release gates pass.

## Classification

- Exact operator-directed design corrections, verified mechanical-import fixes, provider/export discrepancy evidence, validated QA and non-sensitive workflow improvements: **AUTO_APPROVED**.
- Figma project-folder completeness and immutable version-history capability: provider limitation / advisory only.
- Commercial, legal, provider-policy, safety-posture, production-availability and release decisions: unchanged; no new approval created by this Figma pass.
