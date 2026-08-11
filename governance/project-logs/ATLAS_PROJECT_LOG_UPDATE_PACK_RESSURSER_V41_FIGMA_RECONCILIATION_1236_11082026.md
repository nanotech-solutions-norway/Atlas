# ATLAS PROJECT LOG UPDATE PACK — Ressurser v4.1 Figma reconciliation — 12:36, 11.08.2026

## Session / task
Review the supplied `Ressurser-v4.1.pdf` and `Ressurser-v4.1.pptx` exports from Gamma document `p9mdrhrx2a96uph`, reconcile the existing Ressurser v4.1 Figma Slides file against the owner-approved Atlas Home/Tjenester v4.1 configuration, modify the exact existing file in place, and validate the eight-slide design/content handoff.

## Scope
- Figma target: https://www.figma.com/slides/e5NXsscuo7IXzym00KKQZQ/Ressurser-v4.1
- Exact Figma file key: `e5NXsscuo7IXzym00KKQZQ`
- Figma project reference: https://www.figma.com/files/project/634220422
- Gamma source: https://gamma.app/docs/p9mdrhrx2a96uph
- Supplied evidence: `Ressurser-v4.1.pdf`; `Ressurser-v4.1.pptx`
- Slides assessed: 8 existing slides, IDs `0:20`, `0:22`, `0:23`, `0:24`, `0:25`, `0:26`, `0:27`, `0:28`.
- Design/content handoff only. No Gamma mutation, Wix mutation, checkout enablement, runtime activation, production availability or release-state change.

## Authority / baseline
Applied the current operator instruction, approved/canonical Atlas governance, the canonical `ATLAS Figma Adjustment and Website-Draft Preparation Standard`, live target-Figma evidence, supplied PDF/PPTX source evidence, and prior validated Home/Tjenester v4.1 handoffs. Conflicts were resolved in favour of the latest higher-authority approved source.

## Source findings
The source defines eight sections: a split hero; a recommended workflow-scoping guide; a five-theme resource taxonomy; a four-card workflow/effect section over a meeting image; paired data/privacy and platform/cost sections; responsible-use guidance with three pictograms and a right-side photograph; a five-pillar onboarding/implementation diagram; and a resource-structure table with closing CTAs.

## Issues observed
1. Imported typography used Inter rather than the approved Roboto Slab / Roboto families.
2. Non-hero principal headings were imported at 64 px or 60 px with automatic line height rather than the approved Roboto Slab Regular 50 px / 118% rule.
3. Seven CTA controls were raster image-filled frames rather than editable controls.
4. Imported box radii included mechanically scaled values above the approved 4 px / 6 px taxonomy, including approximately 6.54, 9.54, 9.69, 32.69, 72.20 and 103.24 px.
5. Standalone pictographic assets used CROP rather than FIT.
6. Atlas source/status/validation metadata was absent.
7. During native CTA reconstruction, the first batch positioned new direct slide children before reparenting. Figma Slides preserved page-absolute placement during append, producing local-coordinate offsets on several new CTAs. The deterministic validator detected the resulting bounds failures before completion.

## Root cause
The initial deck was a mechanical PPTX-to-Figma representation. It retained source copy, order, most geometry, photographs and composite graphics, but also retained import typography, rasterized controls, scaled radii and Office-derived image modes. The reconstruction-coordinate defect was caused by Figma Slides reparenting semantics: setting a new node's x/y before appending it to a slide can reinterpret those coordinates to preserve page-absolute position.

## Corrective rules
- Preserve the existing slide nodes and source order; do not delete or recreate slides unless explicitly instructed.
- Use Roboto Slab for principal/supporting headings and Roboto for body copy, labels and controls.
- Retain the source-approved hero size; use 50 px / 118% for non-hero principal headings.
- Normalize standard panels/cards/callouts to 6 px and labels/CTAs to 4 px unless an approved intentional image mask requires otherwise.
- Rebuild raster controls as native editable Figma frames and text.
- Use FIT for standalone pictographic icons; retain source CROP treatment for photographs and composite process graphics.
- Preserve native list formatting and do not add duplicate literal bullets.
- **Figma Slides direct-child creation rule:** append the new node to its target slide first, then set source-local x/y. Validate local and absolute bounds after reparenting.
- Validate the expected baseline before classifying any failure; a validator result is not itself evidence of a design defect.

## Actions completed
- Renamed the slide row to `Ressurser v4.1`.
- Converted all imported Inter text to Roboto Slab / Roboto while preserving source weight emphasis and paragraph/list semantics.
- Retained the hero H1 at source treatment: Roboto Slab Regular 64 px / 104%.
- Set all eight non-hero principal heading nodes (nine principal headings total because Slide 5 contains two) to Roboto Slab Regular 50 px / 118%.
- Preserved source body/list line-spacing treatment: 25.333 px body at 133% generally, 132% on Slide 6; 24 px Slide 8 body/table at 129%; source label and number treatments retained.
- Normalized labels/CTAs to 4 px and standard panels/cards/callouts to 6 px.
- Converted eight standalone pictographic image nodes from CROP to FIT.
- Rebuilt seven raster CTA controls as editable Figma controls: `Utforsk ressursene`, `Om metoden`, `Les guiden`, two `Se ressurser`, `Gå til ressursbiblioteket`, and `Kontakt oss`.
- Retained source native unordered-list formatting for the recommended-guide checklist without literal duplicate bullets.
- Corrected and revalidated the CTA reparenting-coordinate issue before final completion.
- Added namespaced `atlas.ai` source/status metadata to all eight slides and verified readback.

## Validation
Final classification: `PASS_DESIGN_AND_CONTENT_HANDOFF`.

- Slide count/order: 8/8 PASS.
- Canvas dimensions: 8/8 at 1920 × 1080 PASS.
- Visible/editable text nodes after reconstruction: 101.
- Font families: Roboto Slab / Roboto only.
- Missing fonts: 0 PASS.
- Font-family violations: 0 PASS.
- Principal headings: 9/9 exact source copy and approved typography PASS.
- Hero heading: 64 px / 104% PASS.
- Non-hero principal headings: 8/8 nodes at 50 px / 118% PASS.
- Visible slide-bound violations: 0 PASS.
- Unexplained radii above 6 px: 0 PASS.
- Editable CTA controls: 7/7 PASS.
- Raster/image-filled CTA controls remaining: 0 PASS.
- Remaining source image-bearing nodes: 16/16 with non-empty image hashes PASS.
- Source photographs/composite graphics retain CROP treatment; standalone pictograms use FIT PASS.
- Native unordered-list semantics retained; duplicate literal bullets: 0 PASS.
- Deterministic validator: PASS.
- Rendered page-by-page visual QA: 8/8 PASS.
- Metadata readback: 8/8 PASS (`status=PASS_DESIGN_AND_CONTENT_HANDOFF`, `deterministic=PASS`, `renderedQA=PASS_8_OF_8`, validated 12:36, 11.08.2026 Europe/Oslo).

## Provider / workflow limitation
The Figma connector cannot authoritatively enumerate every file in project folder `634220422`. This validation therefore applies only to exact file key `e5NXsscuo7IXzym00KKQZQ`; it must not be represented as project-folder-wide completeness certification.

## Release / implementation boundary
- Figma design/content handoff: PASS for the exact assessed eight-slide scope.
- Wix/runtime implementation: not changed by this workstream.
- Responsive/accessibility/runtime acceptance: separate workstreams.
- Public production release: unchanged; `NO_GO` remains in force until controlling Atlas release gates pass.

## Classification
- Exact operator-directed design corrections, verified bug fix, validation evidence and non-sensitive workflow correction: `AUTO_APPROVED`.
- Commercial, legal, provider-policy, safety-posture, production-availability and release decisions: unchanged.
