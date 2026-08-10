# ATLAS PROJECT LOG UPDATE PACK — Priser v4.1 Figma reconciliation — 16:03, 10.08.2026

## Session / task

Reconcile and validate the existing `Priser v4.1` Figma Slides deck against the supplied Gamma-derived PDF/PPTX exports and the owner-approved Atlas Home/Tjenester v4.1 Figma configuration, including the later Managed Secure body/list line-spacing correction.

## Scope

- **Figma target:** `https://www.figma.com/slides/zUbaSTh5qBaZJYihxcK0p5/Priser-v41`
- **Exact Figma file key:** `zUbaSTh5qBaZJYihxcK0p5`
- **Figma project reference:** `https://www.figma.com/files/project/634220422`
- **Gamma source:** `https://gamma.app/docs/rgllqe3mgbkcrgv`
- **Supplied exports:** `Priser-v41.pdf`, `Priser-v41.pptx`
- **Slides:** 7
- **Scope type:** design/content handoff only.
- **Excluded:** Gamma mutation, Wix mutation, responsive/runtime acceptance, checkout/payment activation, production availability and public release.

The Figma connector cannot authoritatively enumerate every file in the project folder. This validation therefore applies only to the exact supplied file key above and does not claim project-folder completeness.

## Authority / repository state

Before write-back, canonical GitHub main was re-read at:

- `7d44a17d854d4d6ab680d6c733ddef02d8ec0ddb`

Current relevant PR state was also rechecked. PRs `#49`, `#50`, `#51`, `#52` and `#61` remain OPEN / UNMERGED and were reported mergeable at the current read. This differs from the earlier transfer-pack snapshot that reported several of them non-mergeable.

The owner-approved Figma standard content on PR `#49` was **not** silently treated as merged main. The controlled Drive copy of `ATLAS Figma Adjustment and Website-Draft Preparation Standard` is classified `CANONICAL`, and the current explicit transfer-pack instruction also restates the same approved rules. The work therefore applied the approved standard without overwriting or consolidating the open historical branches.

## Source inspection

### PDF

The seven-page PDF was rendered and visually inspected page by page before mutation.

### PPTX

The PPTX was inspected programmatically for:

- canvas dimensions;
- copy and deliberate line breaks;
- font families and sizes;
- line height;
- paragraph spacing;
- geometry and margins;
- card/table/callout dimensions;
- fills and strokes;
- imported image-backed controls/cards;
- image treatment.

Source-specific text spacing established by the PPTX was preserved independently from the principal-heading rule.

## Corrective rules applied

1. Hero principal heading remains `Roboto Slab Regular`, 64 px.
2. Non-hero principal headings use `Roboto Slab Regular`, 50 px, 118% line height.
3. `118%` applies only to principal non-hero headings.
4. Body, list and box text follows source-specific line height and paragraph/list spacing.
5. `Roboto Slab` is used for display/card headings; `Roboto` is used for body, labels and controls.
6. Standard card/panel/callout radius = 6 px; category/section labels and CTAs = 4 px; full-slide/edge-to-edge image geometry = 0 px.
7. Raster CTA controls and raster content-container cards must be rebuilt as editable Figma structures.
8. Line/pictographic icons use `FIT`; photography retains `CROP` where applicable.
9. Explicit source-specific specialist-card/split-layout geometry is preserved as an exception to normalized default spacing where the source proves that geometry.

## Figma corrections completed

### Slide 1 — hero

- Replaced Inter with `Roboto Slab` / `Roboto`.
- Hero heading retained at 64 px with source 104% line height.
- Hero body set to source 133% line height.
- Rebuilt both raster CTA controls as editable Figma frames + text:
  - `Se alle planer`
  - `Kontakt oss`
- Both CTA controls use 4 px radius.
- Right-side hero photography retained as `CROP`.

### Slide 2 — public price explanation

- Replaced Inter with `Roboto Slab` / `Roboto`.
- Both explanatory headings use source 32 px / 104%.
- Both body blocks use source 25.3333 px / 133%.
- Blue panel radius corrected from mechanically scaled value to 6 px.
- Intentional source split-panel geometry preserved.

### Slide 3 — consumer plans

- Principal heading corrected to 50 px / 118%.
- Label, card headings, body and status text corrected to source-specific spacing.
- Rebuilt all four raster plan-card backgrounds as editable Figma card structures.
- Preserved the source visual treatment with:
  - editable white card fill;
  - `#D8D4D4` border;
  - 6 px card radius;
  - 12 px blue vertical accent strip with source-faithful vertical blue gradient.
- Section/status label outlines corrected to 4 px.
- Source price/body paragraph spacing preserved; the PPTX 5.5 pt paragraph gap was applied as 14.6667 px.
- Status copy now renders without unintended wrapping.

### Slide 4 — business services

- Principal heading corrected to 50 px / 118%.
- Table/intro text uses source 133% line height.
- Section label corrected to 4 px.
- Imported table outer radius corrected from approximately 88 px to 6 px.
- Exact service names and public-price copy preserved.

### Slide 5 — managed services

- Principal heading corrected to 50 px / 118%.
- Managed intro and pricing/body copy use source 133% line height.
- Card headings use source 32 px / 104%.
- Source paragraph spacing after the first two pricing paragraphs was applied at 14.6667 px.
- Three managed-pricing card radii corrected from approximately 57.5 px to 6 px.
- Section label corrected to 4 px.
- Managed Secure price copy was preserved exactly; no new pricing decision was created.

### Slide 6 — additional costs

- Principal heading corrected to 50 px / 118%.
- Intro/body uses source 22.6667 px / 126% line height.
- Item headings use `Roboto Slab`, 28 px / 104%.
- Section label corrected to 4 px.
- All eight source arrow icons changed from `CROP` to `FIT` so the complete pictogram remains visible.

### Slide 7 — VAT and billing

- Principal heading corrected to 50 px / 118%.
- Intro/card/callout body text uses source 133% line height.
- Card headings use `Roboto Slab`, 32 px / 104%.
- Section label corrected to 4 px.
- Rebuilt all three raster card-background images as editable Figma card structures with:
  - white body fill;
  - `#D8D4D4` border;
  - source `#F2EEEE` top band;
  - 6 px card radius.
- Three card icons and the bottom callout icon use `FIT`.
- Bottom information callout radius corrected to 6 px.
- The source-specific 1807.65625 px intro width was preserved as explicit source geometry.

## Source-specific layout exceptions recorded

The canonical 32 px card padding remains the Atlas default. The following specialist layouts retain explicit PPTX-established geometry and are recorded as source-specific exceptions rather than silently normalized:

- Slide 2 split blue/white explanatory layout.
- Slide 3 accent-strip plan cards.
- Slide 5 managed-pricing cards.
- Slide 7 header-band VAT/billing cards.

These exceptions preserve the supplied source geometry while maintaining canonical typography, radius, editability and image-treatment controls.

## Validation result

A separate expected-baseline validator was executed after all design mutations.

| Control | Result |
|---|---:|
| Slide count/order | 7/7 `PASS` |
| Canvas | 7/7 at 1920×1080 `PASS` |
| Controlled copy | Exact multiset comparison on all visible text `PASS` |
| Hero heading | 64 px / 104% `PASS` |
| Non-hero principal headings | Slides 3–7 at 50 px / 118% `PASS` |
| Slide 2 source two-heading layout | Preserved `PASS` |
| Source-specific body/list/box line height | `PASS` |
| Per-paragraph pricing spacing | Applied; readback reports mixed paragraph spacing as expected `PASS` |
| List spacing | 0 on controlled price blocks `PASS` |
| Font-family violations | 0 `PASS` |
| Missing fonts | 0 `PASS` |
| Unexplained radius > 6 px | 0 `PASS` |
| Raster CTA controls remaining | 0 `PASS` |
| Raster content-card backgrounds remaining | 0 `PASS` |
| Image-bearing nodes | 13/13 `PASS` |
| Image hashes | 13/13 non-empty `PASS` |
| Expected image modes | 1 photography `CROP`; 12 icons `FIT` `PASS` |
| Image clipping/opacity/finite transform/positive geometry | 13/13 `PASS` |
| Visible out-of-bounds nodes | 0 `PASS` |
| Text truncation findings | 0 `PASS` |
| Literal duplicate-bullet text | 0 `PASS` |
| Source metadata | 7/7 `PASS` |
| Rendered visual QA | 7/7 `PASS` |

### Validator/provider limitation observed

Two read-only diagnostic probes failed before the final validator:

1. `TextNode.getRangeBoundingBox` is not exposed by the current Figma Plugin API runtime used by the connector.
2. A subsequent diagnostic probe accidentally included a rectangle node ID while requesting text-only properties.

Both probes were read-only and caused no design mutation. The validator was corrected to use supported text properties, deterministic geometry/font/copy checks and page-by-page rendered QA. The final corrected validator returned `pass: true` with zero errors and zero warnings.

This provider/runtime behavior should be treated as workflow evidence, not as a design defect.

## Final Figma metadata

All seven slides now carry:

- Gamma source: `https://gamma.app/docs/rgllqe3mgbkcrgv`
- Source PDF: `Priser-v41.pdf`
- Source PPTX: `Priser-v41.pptx`
- Status: `PASS_DESIGN_AND_CONTENT_HANDOFF`
- Deterministic validation: `PASS`
- Rendered visual QA: `PASS_7_OF_7`
- Validated at: `16:03, 10.08.2026 Europe/Oslo`

## Final classification

`PASS_DESIGN_AND_CONTENT_HANDOFF`

This classification applies only to the exact seven-slide Figma design/content handoff assessed above.

It does **not** imply:

- Wix implementation;
- responsive/runtime validation;
- payment or checkout activation;
- Managed Secure production availability;
- production readiness;
- public release.

Public release remains `NO_GO` until the controlling release/runtime gates pass.

## Classification of this update

- Exact operator-directed Figma correction, validated bug fixes, source-specific spacing control, editability fixes, image treatment and non-sensitive validation improvements: `AUTO_APPROVED`.
- Commercial/pricing policy changes: none created.
- Production availability and public release: unchanged / `NO_GO`.
