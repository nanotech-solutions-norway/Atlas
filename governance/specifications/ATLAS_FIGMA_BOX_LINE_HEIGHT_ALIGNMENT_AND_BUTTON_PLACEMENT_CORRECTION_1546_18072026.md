# Atlas AI Figma Box Line Height, Heading Alignment and Button Placement Correction

**Timestamp:** 15:46, 18.07.2026 Europe/Oslo  
**Classification:** **AUTO_APPROVED** exact user correction and validated design rule.  
**Applies to:** Consumer v3, Prices v3, Platform lanes v3, Resources v3 and future Atlas Gamma-to-Figma reconstructions.

## Supersession notice

This correction supersedes the earlier 125–135% box-body line-height rule and the prior 15:01 validation where that range was incorrectly accepted as compliant. It also supersedes any earlier instruction that permits centred slide headings or places CTAs according to a generic template instead of the actual Gamma content flow.

The following remain unchanged:

- Gamma controls wording, section order, component type, visual position and CTA sequence.
- The approved Business v1 reference and measurement profile control reusable Atlas geometry and styling.
- All commercial, pricing, provider, legal, privacy, accessibility, contractual and public-availability matters remain **PENDING_REVIEW**.

## 1. Box text line spacing

- Body, paragraph, list and callout text inside cards, boxes, panels, warnings and notices must use **exactly 150% line height**.
- Card/module headings retain their approved heading token and are not changed to 150% solely because they are inside a box.
- Button text retains 24 px font size and 30 px line height.
- Labels retain 18 px font size and 22 px line height.
- Dense editable tables may retain their table-specific compact line spacing where 150% would prevent the table from fitting on a readable 1920 × 1080 slide.

## 2. Content-fit boxes

Every box must be recalculated after final font, width and 150% line height are applied.

Required order:

1. Assign final text width.
2. Load and apply the final font and style.
3. Apply exact line height.
4. Set text to automatic height.
5. Reflow headings, paragraphs and lists.
6. Resize the box to the rendered content.
7. Equalise boxes only within the same visual row.
8. Move subsequent rows, warnings, notices and CTAs to preserve the required vertical gap.

Default box insets remain 32 px where the source layout allows. Compact process rows may use a validated density exception of 16 px top padding, 8 px title-to-body spacing and at least 24 px bottom padding.

A box fails if text is clipped, if rendered text extends beyond its boundary, or if less than 20 px bottom clearance remains after rendering.

## 3. Heading alignment

- **All slide headings and subheadings are left aligned.**
- This includes hero headings, content H1 headings, closing-slide headings, in-slide H2 headings and card headings.
- Centred Gamma headings are adapted to the explicit user correction and therefore left aligned in Figma.
- Heading widths must remain sufficient to avoid unnecessary line breaks or clipping.

## 4. Vertical rhythm below slide headings

For labelled content slides:

- Label: x 104, y 58.
- Main H1: x 104, y 130, width 1712.
- H1 to introductory paragraph: 24 px.
- Introductory paragraph to first card, panel, diagram, process, warning or table: 32 px.
- Where no introductory paragraph exists, H1 to first content element: 32 px.

For source-specific image heroes and closing layouts:

- Preserve Gamma's left/right or behind-image structure.
- Maintain the same content sequence as Gamma.
- Use 32 px between hero body text and CTA group.

## 5. Button placement

- Buttons follow the preceding Gamma content block, rather than a generic absolute slide coordinate.
- Standard content-to-button gap: 24 px.
- Hero body-to-button gap: 32 px.
- Inter-button gap: 16 px.
- Buttons remain in the same left/right sequence as Gamma.
- Button x alignment follows the source content column.
- Primary and secondary widths remain source-specific or content-fit when the wording requires more space.
- Button token: Roboto SemiBold 24 px, 30 px line height, 78 px height, 2 px #3257B8 border, 4 px radius.

## 6. Validation gate

A slide passes only when all of the following are zero:

- out-of-bounds objects;
- clipped text;
- unintended text overlaps;
- unintended image fills;
- non-white slide backgrounds;
- non-left-aligned headings;
- box-body text not using 150% line height;
- box text overflow or insufficient bottom clearance;
- incorrect CTA vertical gap;
- missing Atlas source or validation metadata.

Every slide must also be inspected visually after adjustment. Programmatic validation alone is insufficient.

## 7. Validated implementation

The correction was applied to all 31 current slides:

- Consumer v3 — 6 slides.
- Prices v3 — 9 slides.
- Platform lanes v3 — 8 slides.
- Resources v3 — 8 slides.

Final deterministic findings: zero across all listed acceptance checks.