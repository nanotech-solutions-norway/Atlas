# Atlas AI Figma Typography, Box and Grid Validation Addendum

**Timestamp:** 15:01, 18.07.2026 Europe/Oslo  
**Applies to:** Consumer v3, Prices v3, Platform lanes v3 and Resources v3, and future Atlas Gamma-to-Figma reconstructions.  
**Classification:** **AUTO_APPROVED** design and quality-control refinement. Commercial, pricing, provider, legal, privacy, accessibility, contractual and public-availability matters remain **PENDING_REVIEW**.

## Authority and relationship to existing instructions

This addendum supplements, and does not replace:

- `Atlas_AI_Canonical_Figma_Recreation_Specification_v3_0157_15072026.md`
- `MULTI_DECK_V3_HYBRID_RECONSTRUCTION_SPECIFICATION_1416_18072026.md`
- `Atlas_AI_Business_v1_Validated_Figma_Slides_Measurement_Profile_2116_13072026.md`
- The approved 24 px button-text override dated 17.07.2026.

Gamma continues to control wording, section order, component type, source colours and visual position. The approved Business reference and measurement profile control reusable geometry and styling.

## Exact operational typography

- Display H1: Roboto Slab Regular, 72 px, 118% line height.
- Content H1: Roboto Slab Regular, 54 px, 125% line height.
- Card/module title: Roboto Slab SemiBold, 27–30 px, 125% line height.
- Body and list text: Roboto Regular, normally 20–30 px, 125–135% line height.
- Label: Roboto SemiBold, 18 px, 22 px line height.
- Button: Roboto SemiBold, 24 px, 30 px line height, horizontally and vertically centred.

Do not substitute Roboto Bold for the button token, Roboto Medium for the label token, or Roboto Slab Bold for the normal card-title hierarchy.

## Boxes, padding and grid formula

- Standard content frame: x 104 to x 1816, width 1712 px.
- Standard grid gap: 32 px.
- Standard card/panel text inset: 32 px.
- Standard card border: 1 px `#CFD2D8`, radius 6 px.
- Highlight panel: source-defined `#476FD6`, with editable white text.
- Warning: `#FFFBF5`, 1 px `#B45309`, radius 6 px.
- Label: transparent, 2 px `#3257B8`, radius 4 px, 44 px height, width = rendered text + 28 px.
- Button: 78 px height, 2 px `#3257B8`, radius 4 px. Width remains source-specific or content-fit where required.
- Editable comparison tables may use 24 px cell insets when density requires it.

For equal three-column rows inside the 1712 px frame:

`card width = (1712 - 2 × 32) / 3 = 549.333 px`

Use x positions approximately 104, 685.333 and 1266.667 px. Do not retain a 64 px gap from imported layouts unless Gamma explicitly requires an asymmetric composition.

## Heading and content alignment

For labelled content slides:

- Label: x 104, y 58.
- H1: x 104, y 130, width 1712.
- Intro paragraph: 8 px below the rendered H1 block.
- Standard text alignment: left.

Hero and closing slides retain Gamma-defined alignment and image position. Do not force the generic centred hero geometry when Gamma explicitly uses a left-aligned behind-image hero or a left/right split.

## Implementation order for text and boxes

1. Assign final text width.
2. Load the final font and exact style.
3. Apply font size and line height.
4. Set automatic text height after width assignment.
5. Recalculate dependent body, card, warning, button and downstream positions from rendered text height.
6. Resize equal-row cards and then recalculate child text width while preserving intended left/right padding.
7. Validate text-to-text, text-to-box and foreground-shape obstruction.
8. Inspect screenshots for every source-specific image layout and representative card, table, process and closing layout.

## Acceptance gate

A deck passes only when:

- every slide is 1920 × 1080 with a white background;
- no object is outside the canvas;
- no text is clipped or overlapping;
- no unintended image fill remains;
- typography, label, button, border, padding and grid checks report zero violations;
- Gamma wording, hierarchy, component type and visual position are retained;
- all image replacements remain unique editable placeholders;
- all slide source and validation metadata is present;
- unsupported claims and release decisions remain explicitly qualified.

## Validated implementation evidence

The four v3 decks were adjusted and validated against this addendum on 18.07.2026:

- Consumer v3 — 6 slides.
- Prices v3 — 9 slides.
- Platform lanes v3 — 8 slides.
- Resources v3 — 8 slides.

Combined result: 31 slides, zero deterministic geometry, clipping, overlap, background, image-fill, typography, button, label, grid or metadata findings.