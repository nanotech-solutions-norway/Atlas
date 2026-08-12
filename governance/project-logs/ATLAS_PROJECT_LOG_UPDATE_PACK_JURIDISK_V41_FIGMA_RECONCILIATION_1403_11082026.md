# ATLAS PROJECT LOG UPDATE PACK — Juridisk v4.1 Figma reconciliation — 14:03, 11.08.2026

## Session / task

Review the supplied `Juridisk-v41.pdf` and `Juridisk-v41.pptx` exports from Gamma document `q3pfbgyqejakgyr`, reconcile the existing `Juridisk v4.1` Figma Slides file against the owner-approved Atlas Home/Tjenester v4.1 configuration, modify the exact existing file in place, and validate the ten-slide design/content handoff.

## Scope

- **Figma target:** `https://www.figma.com/slides/EgdS2GMkqDH5bQOOgod3xw/Juridisk-v41`
- **Exact Figma file key:** `EgdS2GMkqDH5bQOOgod3xw`
- **Figma project reference:** `https://www.figma.com/files/project/634220422`
- **Gamma source:** `https://gamma.app/docs/q3pfbgyqejakgyr`
- **Supplied exports:** `Juridisk-v41.pdf`; `Juridisk-v41.pptx`
- **Slides:** ten existing slides — `0:20`, `0:22`, `0:23`, `0:24`, `0:25`, `0:26`, `0:27`, `0:28`, `0:29`, `0:30`.
- **Scope type:** Figma design/content handoff only.
- **Excluded:** Gamma mutation, Wix/runtime mutation, legal approval, production availability and public release.

The Figma connector cannot authoritatively enumerate every file in project folder `634220422`. This validation therefore applies only to the exact supplied file key and is not a folder-wide completeness certification.

## Authority / baseline

Execution followed the current operator instruction, the canonical Atlas source-authority hierarchy, the CANONICAL `ATLAS Figma Adjustment and Website-Draft Preparation Standard`, the validated Home v4.1 and Tjenester v4.1 precedents, the current live Figma implementation, and the supplied PDF/PPTX source evidence.

The controlling design rules applied were:

- 1920×1080 fixed slide canvas;
- 104 px principal side margin and 1,712 px principal content width where the full-width contract applies;
- Roboto Slab for display/card headings;
- Roboto for body, labels and controls;
- hero heading retains its approved 64 px / 104% treatment;
- non-hero principal headings use Roboto Slab Regular 50 px / 118%;
- standard cards/callouts use 6 px radius;
- CTA/label outlines use 4 px radius;
- raster controls/cards are reconstructed as editable Figma structures;
- source imagery and crop intent are preserved;
- design/content PASS remains separate from Wix implementation, legal approval and public release.

## Source findings

The ten-slide source defines:

1. a split-image legal-information hero with two calls to action;
2. six legal-document navigation cards;
3. a legal-document metadata table;
4. contracting-company / contractual-party information with a split photograph and blue callout;
5. a three-column privacy overview;
6. a data-subject-rights vertical timeline;
7. cookie-information columns plus an informational callout;
8. a three-stage terms/order-flow graphic;
9. three delivery-type/special-terms cards; and
10. three contact/legal-feedback cards plus a document-version status label.

### Source export discrepancy

The PPTX uses `10 × 5.625 in` / 16:9 for all ten slides. The PDF is not geometrically uniform:

- most PDF pages are approximately `900 × 507.12 pt`;
- PDF page 2 is approximately `900 × 654.96 pt`;
- PDF page 8 is approximately `900 × 532.08 pt`.

The canonical Atlas 1920×1080 contract and PPTX 16:9 geometry therefore govern the Figma handoff. The variable PDF canvases remain source evidence and were not silently used to distort the fixed Figma slide geometry.

## Issues observed before correction

1. Imported `Inter` typography was used across the deck instead of the controlled `Roboto Slab` / `Roboto` contract.
2. Imported text used `AUTO` line height instead of the controlled Atlas hierarchy.
3. Non-hero principal headings varied from approximately 38.667 px to 52 px rather than the canonical 50 px / 118%.
4. Hero CTAs remained raster image fills rather than editable controls.
5. All six legal-document navigation card surfaces on Slide 2 remained raster image fills.
6. Two imported full-width wrappers were approximately 1,807.656 px wide rather than the 1,711.656 px controlled principal content width:
   - Slide 2 intro wrapper `0:47`;
   - Slide 3 intro wrapper `0:103`.
7. Several box radii were mechanical Gamma/PPTX scaling artifacts rather than approved Atlas values:
   - Slide 3 metadata-table outer boundary approximately 122.461 px;
   - Slide 4 company/contact callout approximately 74.186 px;
   - Slide 5 icon containers approximately 9.686 px;
   - Slide 6 icon containers approximately 9.383 px;
   - Slide 7 informational callout approximately 17.214 px;
   - Slide 9 delivery cards approximately 59.247 px;
   - Slide 10 contact cards approximately 53.351 px;
   - Slide 10 status-label outline approximately 6.545 px.
8. Standalone pictographic icons were imported with `CROP` instead of `FIT`.
9. Atlas source/status metadata was absent.

## Root cause

The PPTX-to-Figma import preserved source copy, broad geometry and source imagery, but also retained mechanical font substitution, automatic line-height behavior, rasterized controls/card surfaces, oversized imported wrappers and mechanically scaled corner radii. These are import artifacts rather than approved Atlas design decisions.

## Corrective rules applied

- Preserve all ten existing slide nodes and source order; do not delete or recreate slides.
- Preserve supplied Norwegian copy, terminology, legal wording and claim boundaries exactly.
- Use Roboto Slab Regular for principal/supporting/card headings and Roboto for body, labels and controls while preserving bold/italic emphasis.
- Keep the hero at 64 px / 104%.
- Use 50 px / 118% for every non-hero principal heading.
- Preserve source-specific supporting/body sizes while assigning controlled line heights.
- Restore the full-width contract to approximately 1,712 px where applicable.
- Rebuild raster CTAs as editable Figma frames and editable text.
- Rebuild raster legal-document card surfaces as editable Figma cards.
- Use 6 px radius for cards/callouts and 4 px for CTA/label outlines.
- Use `FIT` for standalone pictographic icons; preserve `CROP` for photographs and the composite terms/order-flow graphic.
- Keep legal/document content as source evidence; this design correction does not constitute legal approval.
- Keep design/content PASS separate from Wix/runtime/release approval.

## Actions completed

### Slide 1 — Juridisk informasjon og ansvarlig bruk

- Hero changed to Roboto Slab Regular, 64 px / 104%.
- Body changed to Roboto, 25.333 px / 133%.
- Rebuilt `Les personvernerklæringen` as an editable primary Atlas-gradient CTA.
- Rebuilt `Se alle dokumenter` as an editable secondary white/blue-outline CTA.
- Both CTA labels use Roboto SemiBold, 24 px / 30 px; controls use 2 px stroke and 4 px radius.
- Source photograph retained as CROP.

### Slide 2 — Juridiske dokumenter

- Principal heading changed to Roboto Slab Regular, 50 px / 118%.
- Intro changed to Roboto with controlled line height.
- Six document headings changed to Roboto Slab; six descriptions changed to Roboto.
- Rebuilt all six raster legal-document card surfaces as editable cards with white fill, Atlas-blue outline, 6 px radius and editable blue left panel.
- Six standalone pictographic icons changed from CROP to FIT.
- Intro wrapper reduced from approximately 1,807.656 px to 1,711.656 px while preserving the left margin and content.

### Slide 3 — Dokumentmetadata

- Principal heading changed to Roboto Slab Regular, 50 px / 118%.
- Intro changed to Roboto, 25.333 px / 133%.
- Table content changed to Roboto while preserving bold header/field emphasis.
- Metadata-table outer radius corrected from approximately 122.461 px to 6 px.
- Intro wrapper reduced from approximately 1,807.656 px to 1,711.656 px.

### Slide 4 — Selskap og avtalepart

- Principal heading changed to Roboto Slab Regular, 50 px / 118%.
- Body changed to Roboto while preserving bold emphasis on `Atlas AI` and `NanoTech Solutions Norway AS`.
- `Kontakt og organisasjon` changed to Roboto Slab.
- Blue callout radius corrected from approximately 74.186 px to 6 px.
- Source photograph retained as CROP.

### Slide 5 — Personvern – kort oversikt

- Principal heading changed to 50 px / 118%.
- Three supporting headings changed to Roboto Slab; body copy to Roboto.
- Three icon-container radii corrected to 6 px.
- Three standalone icons changed from CROP to FIT.

### Slide 6 — Dine rettigheter som registrert

- Principal heading changed to 50 px / 118%.
- Five right headings changed to Roboto Slab; body copy to Roboto.
- Five icon-container radii corrected to 6 px.
- Five standalone icons changed from CROP to FIT.
- Existing timeline geometry preserved.

### Slide 7 — Informasjonskapsler

- Principal heading changed to 50 px / 118%.
- Column headings changed to Roboto Slab; body copy to Roboto.
- Existing bold emphasis around the cookie-choice link preserved.
- Informational callout radius corrected to 6 px.
- Callout icon changed from CROP to FIT.

### Slide 8 — Tjenestevilkår og bestillingsflyt

- Principal heading corrected from 44 px to Roboto Slab Regular 50 px / 118%.
- Supporting stage headings changed to Roboto Slab; stage/body copy to Roboto.
- Composite workflow graphic preserved as CROP because it is a source-designed diagram rather than a standalone icon.

### Slide 9 — Leveransetyper og spesielle vilkår

- Principal heading changed to 50 px / 118%.
- Three card headings changed to Roboto Slab; card body copy to Roboto.
- Three blue card radii corrected from approximately 59.247 px to 6 px.
- Managed Secure qualification boundary and Family availability wording preserved exactly.

### Slide 10 — Spørsmål eller tilbakemeldinger?

- Principal heading changed to 50 px / 118%.
- Three card headings changed to Roboto Slab; card body copy to Roboto.
- Three neutral card radii corrected from approximately 53.351 px to 6 px.
- Bottom status-label outline corrected to 4 px radius / 1.5 px stroke.
- Status label text changed to Roboto with controlled label line height.

## Validation result

**`PASS_DESIGN_AND_CONTENT_HANDOFF`**

A separate deterministic post-edit validator returned `pass: true` with zero errors and zero warnings.

| Control | Result |
|---|---:|
| Slide count/order | 10/10 PASS |
| Canvas | 10/10 at 1920×1080 PASS |
| Visible/editable text nodes | 96 |
| Exact controlled-copy multiset | FNV-1a `88c417fd` PASS |
| Hero | 64 px / 104% PASS |
| Non-hero principal headings | 9/9 at 50 px / 118% PASS |
| Font-family violations | 0 PASS |
| Missing fonts | 0 PASS |
| Visible slide-bound violations | 0 PASS |
| Text-parent clipping warnings | 0 PASS |
| Full-width wrapper violations | 0 PASS |
| Unexplained radii above 6 px | 0 PASS |
| Editable CTAs | 2/2 PASS |
| Raster CTA controls remaining | 0 PASS |
| Editable legal-document cards | 6/6 PASS |
| Raster legal-card surfaces remaining | 0 PASS |
| Remaining source image-bearing nodes | 18/18 valid hashes PASS |
| Image modes | 3 CROP / 15 FIT PASS |
| Rendered page-by-page visual QA | 10/10 PASS |
| Atlas metadata readback | 10/10 PASS |

Rendered QA confirmed all ten corrected slides visually without clipping, missing source images or visible geometry failures.

All ten slides now carry:

- Gamma source `https://gamma.app/docs/q3pfbgyqejakgyr`;
- source PDF `Juridisk-v41.pdf`;
- source PPTX `Juridisk-v41.pptx`;
- `handoffStatus = PASS_DESIGN_AND_CONTENT_HANDOFF`;
- `deterministicValidation = PASS`;
- `renderedVisualQA = PASS_10_OF_10`;
- `validatedAt = 14:20, 11.08.2026 Europe/Oslo`;
- the recorded PDF/PPTX canvas discrepancy.

The slide row was renamed to `Juridisk v4.1`.

## Provider / workflow limitations

The Figma connector cannot authoritatively enumerate every file in the supplied project folder. The PASS therefore applies specifically to file key `EgdS2GMkqDH5bQOOgod3xw`.

The current execution surface does not provide an authoritative connector-created immutable version-history checkpoint for the existing Slides file. Recovery/reference evidence consists of the supplied PDF/PPTX, the captured pre-edit inventory and the non-slide-destructive mutation record.

## Release / legal boundary

- Exact Figma design/content handoff: **PASS**.
- Gamma source: unchanged.
- Source legal wording: preserved as supplied; no new legal approval or interpretation was created.
- Wix/runtime implementation: unchanged.
- Responsive/accessibility/runtime acceptance: separate.
- Production availability: unchanged.
- Public release remains **NO_GO** until controlling Atlas release gates pass.

## Classification

- Exact operator-directed design corrections, verified mechanical-import fixes, source-export discrepancy evidence, validated QA and non-sensitive workflow improvements: **AUTO_APPROVED**.
- Legal conclusions, provider-policy changes, production-availability changes and release decisions: unchanged; this Figma pass creates no new approval.
- Figma project-folder completeness and immutable version-history capability: provider limitation / advisory only.
