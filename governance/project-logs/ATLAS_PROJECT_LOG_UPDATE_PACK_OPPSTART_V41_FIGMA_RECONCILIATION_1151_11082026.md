# ATLAS PROJECT LOG UPDATE PACK — Oppstart v4.1 Figma reconciliation — 11:51, 11.08.2026

## Session / task
Review the supplied `Oppstart-v41.pdf` and `Oppstart-v41.pptx` exports from Gamma document `89xg2k4rorukyth`, reconcile the existing `Oppstart v4.1` Figma Slides file against the owner-approved Atlas Home/Tjenester v4.1 Figma standard, modify the exact file in place, and validate the complete seven-slide design/content handoff.

## Scope
- Figma target: `https://www.figma.com/slides/iKwtwwGOkibOUjwUpyfH9S/Oppstart-v41`
- Exact Figma file key: `iKwtwwGOkibOUjwUpyfH9S`
- Figma project reference supplied by operator: `https://www.figma.com/files/project/634220422`
- Gamma source: `https://gamma.app/docs/89xg2k4rorukyth`
- Supplied exports: `Oppstart-v41.pdf`, `Oppstart-v41.pptx`
- Slides: 7
- Scope type: design/content handoff only.
- Excluded: Gamma mutation, Wix mutation, live form implementation, responsive/runtime acceptance, production availability and public release.

The Figma connector cannot authoritatively enumerate all files in a project folder. This validation therefore applies to the exact supplied Figma file key only and does not claim folder-wide completeness.

## Authority / baseline
Applied controlling sources in order: current operator instruction; approved/canonical Atlas governance and design rules; live Figma implementation evidence; supplied Gamma/PDF/PPTX evidence; controlled Drive standards and prior validated Home/Tjenester handoffs; labelled inference only where unavoidable.

The canonical `ATLAS Figma Adjustment and Website-Draft Preparation Standard — 23:05, 04.08.2026` was applied. Relevant controls include 1920×1080 canvases, 104 px principal side margins, Roboto Slab/Roboto typography, source-specific layout exceptions, 50 px/118% non-hero principal headings, 6 px cards/panels/callouts, 4 px labels/CTAs, editable controls, source asset preservation and separate deterministic/rendered validation.

## Source evidence
The seven-page PDF was rendered and inspected page by page. The PPTX was inspected programmatically for canvas dimensions, exact copy and paragraph structure, geometry, typography, fills, strokes, radii and embedded image placement. The source defines: a split hero; four-step process; six possible-outcome cards plus callout; prohibited-data warning plus allowed/not-allowed cards; low-risk intake fields; classification/constraints timeline; and final submission checklist/confirmation/CTA.

The public form copy explicitly prohibits sending confidential, sensitive or security-classified information. Slide 6 includes high-level data-category choices such as `Konfidensiell` and `Særskilt beskyttet`; these were preserved as category labels only and do not override the explicit low-risk submission boundary.

## Issues observed before correction
1. All live Figma text used Inter rather than the approved Roboto Slab / Roboto pairing.
2. Non-hero principal headings used inconsistent imported sizes rather than the approved 50 px / 118% rule.
3. Slide 1 and Slide 7 CTA controls were raster image-filled frames rather than editable controls.
4. Slide 4 and Slide 7 used raster image-backed content-card surfaces rather than editable Atlas cards.
5. Mechanically scaled rounded corners exceeded the approved radius taxonomy on outcome cards, callouts, form panel and closing cards.
6. Pictographic warning/info assets used CROP where FIT is the controlled treatment.
7. Mixed field-label emphasis and final confirmation italics required preservation during the font conversion.
8. Atlas source/status/validation metadata were absent.

## Root cause
The deck was mechanically transferred from the Gamma/PPTX source into Figma Slides. Copy, order, imagery and principal geometry were substantially retained, but import typography, rasterized controls/card surfaces, mechanically scaled radii and image scale modes were not normalized to the approved Atlas Figma contract.

## Corrective rules applied
- Hero retained its explicit source treatment: Roboto Slab Regular at 73.3333 px / 104%, with the deliberate two-line source break.
- Slides 2–7 principal headings use Roboto Slab Regular at 50 px / 118%.
- Supporting/card headings use Roboto Slab; body, labels, fields and controls use Roboto.
- Source-specific body/list spacing and list semantics were preserved.
- Standard cards/panels/callouts use 6 px radius; section labels and CTA controls use 4 px.
- Raster CTA controls and raster card surfaces were reconstructed as editable Figma structures.
- Composite process ribbons remain source CROP assets; standalone pictographic warning/info assets use FIT.
- Approved copy, claim boundaries and low-risk data restrictions were preserved exactly.

## Corrections completed
- Slide 1: typography normalized; source two-line hero retained; both CTAs rebuilt as editable controls (`Beskriv behovet`, `Les mer`); source photograph retained.
- Slide 2: label and principal heading normalized; process headings/body converted to Roboto Slab/Roboto; four composite process ribbons retained with source geometry.
- Slide 3: label and principal heading normalized; all six outcome cards corrected to 6 px; supporting typography normalized; information callout corrected to 6 px; icon set to FIT.
- Slide 4: principal/body typography normalized; warning callout corrected to 6 px; warning icon set to FIT; both `Tillatt` / `Ikke tillatt` raster card surfaces rebuilt as editable Atlas cards with white surface, neutral border and blue accent strip.
- Slide 5: label and principal heading normalized; large blue contact panel corrected to 6 px; mixed bold/regular field hierarchy preserved; content typography normalized.
- Slide 6: principal heading normalized to 50 px / 118%; four-column timeline layout retained; list formatting retained as native unordered lists; category wording preserved.
- Slide 7: principal/supporting typography normalized; both raster checklist/confirmation cards rebuilt as editable Atlas cards; quote italics preserved; warning callout corrected to 6 px; warning icon set to FIT; `Send til vurdering` CTA rebuilt as editable control.

## Validation result
**PASS_DESIGN_AND_CONTENT_HANDOFF**

Deterministic validation:
- Slide count/order: 7/7 PASS.
- Canvas: 7/7 at 1920×1080 PASS.
- Visible text nodes after editable reconstruction: 63.
- Font families: Roboto Slab / Roboto only.
- Missing fonts: 0 PASS.
- Font-family violations: 0 PASS.
- Visible out-of-bounds nodes: 0 PASS.
- Hero: source 73.3333 px / 104% with deliberate source two-line break PASS.
- Non-hero principal headings: 6/6 at 50 px / 118% PASS.
- Controlled radii: labels/CTAs 4 px; cards/panels/callouts 6 px PASS.
- Raster CTA controls remaining: 0 PASS.
- Raster content-card surfaces remaining: 0 PASS.
- Image-bearing nodes after editability reconstruction: 8/8 PASS.
- Image hashes: non-empty PASS.
- Image treatment: source photo/process composites CROP; standalone pictograms FIT PASS.
- Native unordered lists preserved on Slide 6 classification/track choices and Slide 7 pre-submit checklist.
- Rendered page-by-page visual QA: 7/7 PASS.

All seven slides carry shared Atlas metadata (`atlas.ai`) recording Gamma/PDF/PPTX sources, `PASS_DESIGN_AND_CONTENT_HANDOFF`, deterministic `PASS`, rendered `PASS_7_OF_7`, validation timestamp and the controlling standard.

## Provider / workflow errors observed
1. During metadata write-back, Figma rejected private `setPluginData` in the host runtime and instructed use of shared plugin data. The failed call was atomic and made no mutation. The operation was corrected using the stable `atlas.ai` shared-data namespace and read back successfully.
2. One redundant GitHub branch-create call returned `Reference already exists` after the branch had already been created successfully. No repository content was lost or overwritten.

## Unresolved items
- The Figma connector cannot prove project-folder-wide completeness; exact-file validation only.
- Wix/live form implementation, responsive/runtime validation and public release remain separate workstreams.
- No content/design discrepancy remains within the exact seven-slide assessed scope.

## Release boundary
This pass does not imply live form implementation, Wix implementation, responsive/runtime acceptance, production availability or public release. Existing Atlas release locks remain unchanged and public release remains `NO_GO` until the controlling runtime/release gates pass.

## Classification
- Operator-directed Figma correction, validated typography/geometry/radius/editability/image-treatment fixes and non-sensitive QA evidence: **AUTO_APPROVED**.
- Provider/runtime error records above: **AUTO_APPROVED** workflow evidence.
- Commercial, legal, provider-policy, safety-posture, production-availability and public-release decisions: unchanged.
