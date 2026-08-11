# ATLAS PROJECT LOG UPDATE PACK — FAQ v4.1 Figma reconciliation — 13:05, 11.08.2026

## Session / task

Review the supplied `FAQ-v41.pdf` and `FAQ-v41.pptx` exports from Gamma document `8nh3stzfnbmgfi4`, reconcile the existing `FAQ v4.1` Figma Slides file against the owner-approved Atlas Home/Tjenester v4.1 Figma configuration, modify the exact existing file in place, and validate the seven-slide design/content handoff.

## Scope

- **Figma target:** `https://www.figma.com/slides/53mrsK8eCHzlLBLPu123DK/FAQ-v41`
- **Exact Figma file key:** `53mrsK8eCHzlLBLPu123DK`
- **Figma project reference:** `https://www.figma.com/files/project/634220422`
- **Gamma source:** `https://gamma.app/docs/8nh3stzfnbmgfi4`
- **Supplied exports:** `FAQ-v41.pdf`; `FAQ-v41.pptx`
- **Slides:** 7 existing slides — `0:20`, `0:22`, `0:23`, `0:24`, `0:25`, `0:26`, `0:27`.
- **Scope type:** Figma design/content handoff only.
- **Excluded:** Gamma mutation, Wix/runtime mutation, checkout/activation, production availability and public release.

The Figma connector cannot authoritatively enumerate every file in project folder `634220422`. This validation therefore applies only to the exact supplied file key and is not a folder-wide completeness certification.

## Authority / baseline

Execution followed the current operator instruction, canonical Atlas source-authority hierarchy, the CANONICAL `ATLAS Figma Adjustment and Website-Draft Preparation Standard`, current Figma implementation evidence, and the supplied Gamma/PDF/PPTX source evidence. No lower-authority source was allowed to silently override a higher approved design rule.

## Source findings

The source defines:

1. split-image FAQ hero with seven topic labels;
2. three service/ownership/partner-status questions;
3. four consumer price-plan cards;
4. consumption and examination-use guidance;
5. data/trust guidance with three pictograms and an informational callout;
6. four platform/provider visual marks; and
7. age, answer-quality and Managed Secure guidance with two closing CTAs.

### Source export discrepancy

PDF inspection found one source-export canvas inconsistency:

- PDF pages 1–4 and 6–7: `900 × 507.12 pt`;
- PDF page 5: `900 × 571.92 pt`;
- PPTX: all seven slides are `10 × 5.625 in` / 16:9;
- canonical Atlas Figma contract: `1920 × 1080`.

The canonical 1920×1080 standard and PPTX geometry therefore govern the Figma handoff for page/slide 5. The taller PDF page is retained as source evidence and was not silently used to distort the Figma canvas.

## Issues observed before correction

1. Imported `Inter` typography instead of `Roboto Slab` / `Roboto`.
2. All imported text line heights were `AUTO` instead of the controlled source-specific values.
3. Non-hero principal headings were imported at 52 px, and Slide 5 at 45.333 px, instead of the approved 50 px / 118% rule.
4. Seven Slide-1 category labels had mechanically scaled `6.5448 px` radii instead of 4 px.
5. Slide-4 blue academic-use panel had a mechanically scaled `71.3011 px` radius instead of 6 px.
6. Slide-5 informational callout had a `14.2055 px` radius instead of 6 px.
7. Slide-5 pictographic icons used `CROP` instead of `FIT`.
8. Four Slide-3 price-card surfaces remained raster image fills rather than editable card structures.
9. Two Slide-7 CTAs remained raster image fills rather than editable controls.
10. Atlas source/status metadata was absent.

## Root cause

The PPTX-to-Figma import preserved source copy, general geometry and source imagery, but also retained import typography, automatic line-height behavior, mechanically scaled corner radii and rasterized controls/content-card surfaces. These are mechanical import artifacts rather than intentional Atlas design decisions.

## Corrective rules applied

- Preserve all seven existing slide nodes and source order; do not delete or recreate slides.
- Use `Roboto Slab Regular` for principal/supporting/card headings and `Roboto` for body, labels and controls while preserving bold/italic source emphasis.
- Preserve the 64 px / 104% hero treatment.
- Use 50 px / 118% for every non-hero principal heading.
- Preserve source-specific supporting/body spacing independently: 32/28 px headings at 104%; 25.333 px body at 133%; Slide-5 22.667 px body at 126%; Slide-1 labels at 20 px / 96%.
- Preserve Slide-4 paragraph spacing equivalent to the source 8.5 pt gap: 22.667 px.
- Standard content cards/panels/callouts use 6 px radius; labels/CTAs use 4 px.
- Rebuild raster controls as editable Figma structures.
- Rebuild the four FAQ price-card background surfaces as editable cards with the source white body, `#D8D4D4` border, 6 px radius and 12 px vertical blue gradient accent.
- Use `FIT` for Slide-5 standalone pictograms; preserve source `CROP` for photography, the Slide-2 numbered composite badges and the Slide-6 source provider marks.
- Preserve native list semantics on Managed Secure requirements; do not add literal duplicate bullets.
- Keep design/content PASS separate from Wix/runtime/release approval.

## Actions completed

### Slide 1 — hero

- Hero kept at `Roboto Slab Regular`, 64 px / 104%.
- Body set to Roboto, 25.333 px / 133%.
- Seven topic labels set to Roboto, 20 px / 96%.
- Seven label radii corrected to 4 px.
- Source hero photography retained as CROP.

### Slide 2 — Om tjenesten

- Principal heading set to 50 px / 118%.
- Supporting question headings set to Roboto Slab, 32 px / 104%.
- Body copy set to Roboto, 25.333 px / 133%, preserving bold and italic emphasis.
- Three source numbered composite badge assets retained as CROP.

### Slide 3 — Priser og planer

- Principal heading set to 50 px / 118%.
- Four plan headings retained at Roboto Slab 32 px / 104%.
- Price/status copy retained at Roboto 25.333 px / 133%, preserving bold/italic emphasis.
- Four raster price-card surfaces removed and rebuilt as editable Figma card structures:
  - white fill;
  - `#D8D4D4` inside border;
  - 3 px border weight;
  - 6 px radius;
  - 12 px source-faithful vertical blue gradient accent.

### Slide 4 — Bruk og forbruk

- Principal heading set to 50 px / 118%.
- Intro/body text set to source 25.333 px / 133%.
- Question headings set to Roboto Slab 32 px / 104%.
- Source paragraph gap preserved at 22.667 px.
- Blue academic-use panel radius corrected from approximately 71.3 px to 6 px.

### Slide 5 — Data og tillit

- Principal heading set to 50 px / 118% under the canonical non-hero rule.
- Source body copy retained at 22.667 px / 126%.
- Supporting card headings retained at Roboto Slab 28 px / 104%.
- Three category pictograms plus the callout pictogram changed from CROP to FIT.
- Informational callout radius corrected from approximately 14.2 px to 6 px.
- Source security photograph retained as CROP.
- PPTX 16:9 geometry retained over the anomalous taller PDF-page canvas.

### Slide 6 — Plattformer og leverandører

- Principal heading set to 50 px / 118%.
- Intro/body copy set to 25.333 px / 133%.
- Provider headings retained at Roboto Slab 32 px / 104%.
- Four source provider-mark images retained as CROP because the PDF/PPTX explicitly establish their clipped source presentation.

### Slide 7 — Oppstart, aldersgrenser og Managed Secure

- Principal heading set to 50 px / 118%.
- Supporting question headings set to Roboto Slab 32 px / 104%.
- Body/list text set to Roboto 25.333 px / 133%, preserving bold and italic emphasis.
- Managed Secure list semantics retained without duplicate literal bullets.
- Two raster CTAs rebuilt as editable controls:
  - `Kontakt oss` — primary blue;
  - `Les mer om Managed Secure` — secondary white/blue outline;
  - Roboto Bold 29.333 px / 104%;
  - 4 px radius.

## Validation result

**`PASS_DESIGN_AND_CONTENT_HANDOFF`**

A separate deterministic post-edit validator returned `pass: true` with zero errors and zero warnings.

| Control | Result |
|---|---:|
| Slide count/order | 7/7 PASS |
| Canvas | 7/7 at 1920×1080 PASS |
| Visible/editable text nodes | 59 |
| Exact controlled-copy multiset | FNV-1a `beff7092` PASS |
| Hero | 64 px / 104% PASS |
| Non-hero principal headings | 6/6 at 50 px / 118% PASS |
| Source-specific supporting/body line heights | PASS |
| Slide-4 paragraph spacing | PASS |
| Font-family violations | 0 PASS |
| Missing fonts | 0 PASS |
| Visible slide-bound violations | 0 PASS |
| Unexplained radii above 6 px | 0 PASS |
| Editable price cards | 4/4 PASS |
| Raster FAQ price-card surfaces remaining | 0 PASS |
| Editable CTAs | 2/2 PASS |
| Raster CTA controls remaining | 0 PASS |
| Remaining source image-bearing nodes | 13/13 valid image hashes PASS |
| Image modes | 9 CROP / 4 FIT PASS |
| Duplicate literal bullets | 0 PASS |
| Rendered page-by-page visual QA | 7/7 PASS |
| Atlas metadata readback | 7/7 PASS |

All seven slides now carry:

- Gamma source `https://gamma.app/docs/8nh3stzfnbmgfi4`;
- source PDF `FAQ-v41.pdf`;
- source PPTX `FAQ-v41.pptx`;
- `handoffStatus = PASS_DESIGN_AND_CONTENT_HANDOFF`;
- `deterministicValidation = PASS`;
- `renderedVisualQA = PASS_7_OF_7`;
- `validatedAt = 13:05, 11.08.2026 Europe/Oslo`.

## Provider / workflow limitation

The Figma connector cannot authoritatively enumerate every file in the supplied project folder. The PASS therefore applies specifically to file key `53mrsK8eCHzlLBLPu123DK`.

The Figma connector also does not expose an authoritative recoverable version/duplicate workflow for the existing Slides file in this task. The supplied PDF/PPTX and the captured pre-edit inventory are retained as recovery/reference evidence.

## Release / implementation boundary

- Exact Figma design/content handoff: **PASS**.
- Gamma source: unchanged.
- Wix/runtime implementation: unchanged.
- Responsive/accessibility/runtime acceptance: separate.
- Production availability: unchanged.
- Public release remains **NO_GO** until controlling Atlas release gates pass.

## Classification

- Exact operator-directed design corrections, verified mechanical-import fixes, provider/export discrepancy evidence and non-sensitive validation improvements: **AUTO_APPROVED**.
- Commercial, legal, provider-policy, safety-posture, production-availability and release decisions: unchanged; no new approval created by this Figma pass.
