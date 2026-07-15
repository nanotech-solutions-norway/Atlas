# Atlas AI Canonical Figma Recreation Specification v3

**Timestamp:** 01:57, 15.07.2026 Europe/Oslo  
**Approved reference:** https://www.figma.com/slides/QjAYZsGDVS2qxrCzj8TZIA  
**Reference Gamma:** Business v1 (`g_1fwdlwasdw96se3`)  
**Measurement authority:** `Atlas_AI_Business_v1_Validated_Figma_Slides_Measurement_Profile_2116_13072026.md`

## Source hierarchy

1. Explicit user instructions and approved Atlas decisions.
2. Gamma for wording, section order, component type, source colors and visual position.
3. Approved Business Figma Slides file and measurement report for reusable geometry, typography, palette and component styling.
4. Current Figma implementation evidence.
5. Earlier drafts and contextual reports.

A conflict must be recorded. Do not silently merge it.

## Global slide profile

| Property | Canonical value |
|---|---|
| Canvas | 1920 × 1080 px |
| Aspect ratio | 16:9 |
| Side margins | 104 px |
| Content width | 1712 px |
| Grid gap | 32 px |
| Card padding | 32 px |
| Background/card fill | #FFFFFF |
| Navy text | #15213F |
| Heading/accent | #3257B8 |
| Highlighted Gamma panel | #476FD6 |
| Neutral panel | #E9ECF2 |
| Border | #CFD2D8 |
| Standard border | 1 px |
| Accent/label border | 2 px |

## Typography

- Display H1: Roboto Slab Regular, 72 px, 118% line height, #3257B8.
- Dense/content H1: Roboto Slab Regular, 54 px, 125% line height, #3257B8.
- Body: Roboto Regular, 24–30 px, 125–135% line height, #15213F.
- Card title: Roboto Slab SemiBold, 27–30 px, 125% line height.
- Card body: Roboto Regular, 20–22 px, 125–135% line height.
- Labels: Roboto SemiBold, 18 px, #3257B8.
- CTA: Roboto SemiBold, 36 px, vertically and horizontally centred.

Do not use the former grey body color `#4A5770`. Do not use Roboto Slab Bold for the normal page hierarchy.

## Labels

- Position: x 104, y 58.
- Height: 44 px.
- Width: rendered text width + 28 px.
- Internal padding: 14 px per side.
- Fill: transparent.
- Stroke: 2 px #3257B8.
- Radius: 4 px.
- Text baseline position: approximately x 118, y 69.

## Cards, boxes and panels

- Default card fill: #FFFFFF.
- Default card border: 1 px #CFD2D8.
- Default radius: 6 px.
- Grid gap and text inset: 32 px.
- Source-defined highlighted panels may use #476FD6 with white text.
- Neutral callouts use #E9ECF2 and 6 px radius.
- Side-line cards use an editable 8–10 px accent line; text begins 32 px after the line.
- Avoid decorative 18–34 px radii unless Gamma explicitly requires them.
- Keep cards, text, tables, diagrams and placeholders editable.

## Bullets, lists and paragraphs

- Body/list font: Roboto Regular 20–22 px.
- Headings inside cards: Roboto Slab SemiBold 27–30 px.
- Line height: 125–135%.
- Paragraph and list spacing: 6 px.
- Left inset after bullets or side line: 32 px.
- Use native bullets and editable characters.
- Do not convert list or table content to images.

## Buttons

- Height: 78 px.
- Primary width: 480 px.
- Secondary width: 320 px.
- Gap: 16 px.
- Primary: #3257B8 fill/border, white text.
- Secondary: white fill, 2 px #3257B8 border, blue text.
- Radius: 4 px.
- Text: Roboto SemiBold 36 px, centred.
- Links are excluded from design acceptance unless explicitly required.

## Hero variants

### Gamma `image-layout="behind"`

- Placeholder: x 48, y 48, w 1824, h 984.
- Placeholder remains behind content and editable.
- Title: x 260, y 180, w 1400, 72 px, centred.
- Body: x 360, y 410, w 1200, 30 px, centred.
- Primary CTA: x 552, y 650, w 480, h 78.
- Secondary CTA: x 1048, y 650, w 320, h 78.
- Keep a source-specific asset tag until the original visual is inserted.

### Gamma `image-layout="right"`

- Left title: x 104, y 180, w 1100, 72 px.
- Left body: x 104, y 410, w 1080, 30 px.
- Right placeholder: x 1260, y 120, w 556, h 840.
- Primary CTA: x 104, y 690, w 480, h 78.
- Secondary CTA: x 600, y 690, w 320, h 78.
- Do not replace the source right-image structure with a generic blue feature panel.

## Content slides

- Label: x 104, y 58.
- H1: x 104, y 130, w 1712, 54 px.
- Intro starts 8 px after the rendered H1 block.
- Preserve Gamma component type: card grid, comparison, process, pricing, table, callout, infographic or trust block.
- Scale multi-card rows proportionally into 1712 px.
- Use 32 px gaps, except process arrows may require a 54 px corridor.
- Tables remain editable.
- Pricing stays vertically structured where the approved source requires it.

## Closing slide

- Label hidden.
- H1: x 260, y 140, w 1400; 72 px, or 54 px only to prevent overlap.
- Body: x 360, y 340, w 1200, 30 px, centred.
- Notice: x 360, y 490, w 1200, h 210, 1 px #CFD2D8, radius 6.
- Primary CTA: x 552, y 760, w 480, h 78.
- Secondary CTA: x 1048, y 760, w 320, h 78.

## Traceability

Every slide must contain:

- `atlas/sourceMap`: Gamma IDs, section IDs, semantic name and disposition.
- `atlas/referenceValidation`: approved reference file, profile, slide number and adjustment status.

Every slide row must contain:

- `atlas/referenceDeck = QjAYZsGDVS2qxrCzj8TZIA`
- `atlas/referenceProfile = Atlas_AI_Business_v1_Validated_Figma_Slides_Measurement_Profile_2116_13072026.md`

## Validation gate

A slide passes only when:

- it is 1920 × 1080 with no out-of-bounds object;
- no clipping or overlap is visible in the full-row screenshot review;
- typography, palette, label, border, card and CTA measurements match this profile;
- Gamma hierarchy and source visual location are preserved;
- source metadata is present;
- text and shapes remain editable;
- unsupported commercial, legal, provider, runtime and production claims are excluded or explicitly pending.
