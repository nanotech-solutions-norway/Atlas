# ATLAS PROJECT LOG UPDATE PACK — Om oss v4.1 Figma reconciliation — 13:28, 11.08.2026

## Session / task

Review the supplied `Om-oss-v41.pdf` and `Om-oss-v41.pptx` exports from Gamma document `6lifuxnndbjmk4m`, reconcile the existing `Om oss v4.1` Figma Slides file against the owner-approved Atlas Home/Tjenester v4.1 configuration, modify the exact existing file in place, and validate the seven-slide design/content handoff.

## Scope

- **Figma target:** `https://www.figma.com/slides/f5pGt04qtRgNkjtG407ywN/Om-oss-v41`
- **Exact Figma file key:** `f5pGt04qtRgNkjtG407ywN`
- **Figma project reference:** `https://www.figma.com/files/project/634220422`
- **Gamma source:** `https://gamma.app/docs/6lifuxnndbjmk4m`
- **Supplied exports:** `Om-oss-v41.pdf`; `Om-oss-v41.pptx`
- **Slides:** 7 existing slides — `0:20`, `0:22`, `0:23`, `0:24`, `0:25`, `0:26`, `0:27`.
- **Scope type:** Figma design/content handoff only.
- **Excluded:** Gamma mutation, Wix/runtime mutation, checkout/activation, production availability and public release.

The Figma connector cannot authoritatively enumerate every file in project folder `634220422`. This validation therefore applies only to the exact supplied file key and is not a folder-wide completeness certification.

## Authority / baseline

Execution followed the current operator instruction, canonical Atlas source-authority hierarchy, the CANONICAL `ATLAS Figma Adjustment and Website-Draft Preparation Standard`, current live Figma implementation evidence, and the supplied Gamma/PDF/PPTX source evidence. Lower-authority evidence was not allowed to silently override an approved Atlas design rule.

## Source findings

The source defines:

1. split-image hero with two calls to action;
2. company/ownership explanation with a blue ownership panel and native bullet list;
3. six Atlas principles presented as stacked numbered cards;
4. a four-stage method from mapping through scaling using a composite process graphic;
5. platform-independent evaluation with a two-column clarification layout and native bullet list;
6. governance-as-delivery guidance with three pictographic icons; and
7. a closing section with three blue value cards and two calls to action.

### Source export discrepancy

PDF inspection found one source-export canvas inconsistency:

- PDF pages 1, 2, 4, 5, 6 and 7: approximately `900 × 507.12 pt`;
- PDF page 3: approximately `900 × 663.12 pt`;
- PPTX: all seven slides are 16:9 (`10 × 5.625 in`);
- canonical Atlas Figma contract: `1920 × 1080`.

The canonical 1920×1080 contract and PPTX geometry therefore govern Slide 3. The taller PDF page is retained as evidence and was not used to distort the Figma canvas.

## Issues observed before correction

1. Imported `Inter` typography instead of `Roboto Slab` / `Roboto`.
2. Imported text used automatic line-height rather than controlled source-specific values.
3. Non-hero principal headings were imported at 64 px, with Slide 3 at approximately 46.667 px, rather than the approved 50 px / 118% rule.
4. Slide 1 and Slide 7 CTA controls were raster image-filled frames rather than editable controls.
5. Slide 2 ownership panel used a mechanically scaled radius of approximately 73.62 px.
6. Slide 3 contained six rasterized principle-card surfaces rather than editable card structures.
7. Slide 6 pictographic icons used `CROP` rather than `FIT`.
8. Slide 7 closing cards used mechanically scaled radii of approximately 38.58 px.
9. Atlas source/status metadata was absent.

## Root cause

The PPTX-to-Figma import preserved source copy, hierarchy, most geometry and embedded source imagery, but also carried over Office/import typography, automatic line-height behavior, mechanically scaled corner radii and rasterized controls/card surfaces. These are mechanical transfer artifacts rather than approved Atlas design decisions.

## Corrective rules applied

- Preserve all seven existing slide nodes and source order; do not delete/recreate slides.
- Use `Roboto Slab` for principal/supporting/card headings and `Roboto` for body, labels and controls while preserving source emphasis.
- Retain the approved 64 px / 104% hero treatment.
- Use 50 px / 118% for every non-hero principal heading.
- Preserve source-specific body/supporting spacing independently from the principal-heading rule.
- Preserve native list semantics and avoid duplicate literal bullet glyphs.
- Standard panels/cards/callouts use 6 px radius; CTA controls use 4 px.
- Rebuild raster controls and content-card surfaces as editable Figma structures where required.
- Use `FIT` for standalone pictographic icons; preserve source `CROP` for photography and the composite process graphic.
- Keep design/content handoff status separate from Wix/runtime/release status.

## Actions completed

### Slide 1 — hero

- Hero principal heading retained at `Roboto Slab Regular`, 64 px / 104%.
- Body set to Roboto, 25.333 px / 133%.
- Rebuilt `Ta kontakt` and `Les mer om Atlas` as editable CTA frames/text.
- CTA radii set to 4 px.
- CTA label scale corrected against the supplied source to Roboto Bold 26.667 px / 104% and re-centred.
- Source office photograph retained with valid source hash and `CROP`.

### Slide 2 — Selskapet bak Atlas

- Principal heading corrected to 50 px / 118%.
- Main body converted to Roboto 25.333 px / 133% while preserving bold company-name emphasis.
- Source paragraph separation preserved at 22.667 px after the first paragraph.
- `Tydelig eierskap` set to Roboto Slab 32 px / 104%; supporting copy uses Roboto 25.333 px / 133%.
- Native unordered list retained with zero list spacing.
- Ownership panel radius corrected from approximately 73.62 px to 6 px.

### Slide 3 — Prinsippene bak Atlas

- Principal heading corrected from approximately 46.667 px to 50 px / 118%.
- Intro retained at source 18.667 px / 116%.
- Number labels use Roboto Slab 28 px / 100%.
- Principle headings use Roboto Slab 22.667 px / 104%.
- Principle bodies use Roboto 18.667 px / 116%.
- Rebuilt all six raster principle-card surfaces as editable Figma cards with:
  - white body fill;
  - source blue `#476FD6` 2 px border;
  - 6 px radius;
  - 79 px editable blue number band;
  - no residual image-filled card surface.
- The canonical/PPTX 16:9 geometry was retained rather than the anomalous taller PDF page canvas.

### Slide 4 — Fra behov til avgrenset løsning

- Principal heading corrected to 50 px / 118%.
- Intro and closing body set to Roboto 25.333 px / 133%.
- Stage labels use source 30.667 px / 104%.
- Source four-stage composite process graphic retained with original hash and `CROP`.

### Slide 5 — Plattformuavhengig vurdering

- Principal heading corrected to 50 px / 118%.
- Supporting headings use Roboto Slab 32 px / 104%.
- Body/list text uses Roboto 25.333 px / 133%.
- Source paragraph separation in the left narrative preserved at 22.667 px.
- Native unordered-list semantics retained on the clarification list with zero list spacing and no literal duplicate bullets.

### Slide 6 — Styring som en del av leveransen

- Principal heading corrected to 50 px / 118%.
- Intro/body set to Roboto 25.333 px / 133%.
- Three supporting headings use Roboto Slab 32 px / 104%.
- Three standalone pictographic icons changed from `CROP` to `FIT`; source image hashes preserved.

### Slide 7 — Kom i gang med Atlas

- Principal heading corrected to 50 px / 118%.
- Intro/body set to Roboto 25.333 px / 133%.
- Three supporting headings use Roboto Slab 32 px / 104%.
- Three closing-card radii corrected from approximately 38.58 px to 6 px.
- Rebuilt `Ta kontakt` and `Last ned prinsippdokument` as editable controls with 4 px radius.
- CTA labels use source-faithful Roboto Bold 26.667 px / 104%.

## Validation result

**`PASS_DESIGN_AND_CONTENT_HANDOFF`**

A separate corrected deterministic post-edit validator returned `pass: true`, with zero errors and zero warnings.

| Control | Result |
|---|---:|
| Slide count/order | 7/7 PASS |
| Canvas | 7/7 at 1920×1080 PASS |
| Visible/editable text nodes | 61 |
| Controlled-copy FNV-1a hash | `effa19f7` PASS |
| Hero | 64 px / 104% PASS |
| Non-hero principal headings | 6/6 at 50 px / 118% PASS |
| Source-specific supporting/body line heights | PASS |
| Source paragraph spacing | PASS |
| Native list semantics | 2/2 PASS |
| Literal duplicate bullets | 0 PASS |
| Font-family violations | 0 PASS |
| Missing fonts | 0 PASS |
| Visible slide-bound violations | 0 PASS |
| Text truncation findings | 0 PASS |
| Unexplained radii above 6 px | 0 PASS |
| Editable CTAs | 4/4 PASS |
| Raster CTA controls remaining | 0 PASS |
| Editable principle cards | 6/6 PASS |
| Raster principle-card surfaces remaining | 0 PASS |
| Remaining source image-bearing nodes | 5/5 with valid image hashes PASS |
| Image modes | 2 CROP / 3 FIT PASS |
| Rendered page-by-page visual QA | 7/7 PASS |
| Atlas metadata readback | 7/7 PASS |

Remaining validated image nodes:

- Slide 1 hero photograph: `CROP`;
- Slide 4 four-stage composite process graphic: `CROP`;
- Slide 6 three standalone pictograms: `FIT`.

All seven slides now carry:

- Gamma source `https://gamma.app/docs/6lifuxnndbjmk4m`;
- source PDF `Om-oss-v41.pdf`;
- source PPTX `Om-oss-v41.pptx`;
- `handoffStatus = PASS_DESIGN_AND_CONTENT_HANDOFF`;
- `deterministicValidation = PASS`;
- `renderedVisualQA = PASS_7_OF_7`;
- `validatedAt = 13:28, 11.08.2026 Europe/Oslo`;
- source-export discrepancy note for the taller PDF page 3.

## Workflow/provider findings

Two non-design execution issues occurred and were corrected without corrupting the Figma file:

1. A CTA-label resize attempt failed atomically because `Roboto Bold` had not been loaded in that plugin execution. Corrective rule: load the exact active font/style before every text-property mutation, including newly created text nodes.
2. The first read-only full validator used `TextEncoder`, which is not exposed in the current Figma plugin runtime. No design mutation occurred. The validator was rewritten using a supported UTF-16 code-unit FNV-1a implementation and then passed with zero errors/warnings.

These are workflow/provider evidence, not design defects.

## Provider limitation

The Figma connector cannot authoritatively enumerate every file in the supplied project folder. The PASS therefore applies specifically to file key `f5pGt04qtRgNkjtG407ywN`.

The connector also does not expose an authoritative recoverable version/duplicate workflow for this existing Slides file in the current task. The supplied PDF/PPTX and the captured pre-edit inventory remain recovery/reference evidence.

## Release / implementation boundary

- Exact Figma design/content handoff: **PASS**.
- Gamma source: unchanged.
- Wix/runtime implementation: unchanged.
- Responsive/accessibility/runtime acceptance: separate.
- Production availability: unchanged.
- Public release remains **NO_GO** until controlling Atlas release gates pass.

## Classification

- Exact operator-directed design corrections, validated mechanical-import fixes, workflow/provider findings and non-sensitive validation evidence: **AUTO_APPROVED**.
- Commercial, legal, provider-policy, safety-posture, production-availability and release decisions: unchanged; no new approval created by this Figma pass.
