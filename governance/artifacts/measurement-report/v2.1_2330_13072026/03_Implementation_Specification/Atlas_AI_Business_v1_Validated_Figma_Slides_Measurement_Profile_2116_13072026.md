# Atlas AI Business v1 - Validated Figma Slides Measurement Profile

**Revision:** 2  
**Timestamp:** 21:16, 13.07.2026 Europe/Oslo  
**Gamma source:** Business v1 (`g_1fwdlwasdw96se3`)  
**Figma Slides:** https://www.figma.com/slides/QjAYZsGDVS2qxrCzj8TZIA

## Source authority

1. Gamma controls content order, wording, component hierarchy, source-specific colors and original visual locations.
2. The Atlas measurement report controls the fixed Figma Slides implementation profile.
3. Explicit user instructions override general rules: white cards unless Gamma defines a highlighted panel; icon placeholders contain only `icon`; CTA links are excluded.
4. Contradictions must be flagged; do not silently merge.

## Global slide profile

| Token | Final value |
|---|---:|
| Canvas | 1920 x 1080 px |
| Aspect ratio | 16:9 |
| Standard side margin | 104 px |
| Content width | 1712 px |
| Grid gap | 32 px |
| Card padding | 32 px |
| Display H1 | 72 px |
| Dense-slide H1 | 54 px |
| Body | 24-30 px |
| Card title | 27-30 px |
| Card body | 20-22 px |
| CTA height | 78 px |
| CTA text | 36 px |
| CTA gap | 16 px |
| Standard stroke | 1 px |
| Accent stroke | 2 px |
| Label padding | 14 px per side |
| Label fill | Transparent |
| Label border | 2 px #3257B8 |

## Color profile

- Primary navy: `#15213F`
- Heading/accent blue: `#3257B8`
- Gamma highlighted panel: `#476FD6`
- Neutral panel: `#E9ECF2`
- Border: `#CFD2D8`
- Canvas/card: `#FFFFFF`

## Slide geometry

### Slide 1 - Hero
- Behind-content placeholder: x 48, y 48, w 1824, h 984.
- Title: x 260, y 180, w 1400, h 180; Roboto Slab 72 px; centred.
- Body: x 360, y 410, w 1200, h 130; Roboto 30 px; centred.
- Primary CTA: x 552, y 650, w 480, h 78.
- Secondary CTA: x 1048, y 650, w 320, h 78.
- CTA gap: 16 px.

### Slide 2 - Work areas
- Cards: x 104 / 976; w 840; h 190.
- Rows: y 350 / 572 / 794.
- Gap: 32 px.
- Padding: 32 px.
- Icon placeholders: 110 x 70; text only `icon`.

### Slide 3 - Delivery
- Diagram placeholder: x 104, y 360, w 1712, h 400.
- Five editable stage labels distributed evenly below the placeholder.

### Slide 4 - Transparent prismodell
- H1: 72 px.
- Left column: x 104, w 924.
- Column gap: 32 px.
- Right panel: x 1060, y 300, w 756, h 520.
- Panel fill: `#476FD6`; text white; six native bullets; 2 px accent border.

### Slide 5 - Pricing
- Five stacked cards: x 104, w 1712, h 128.
- First card y 330; vertical gap 12 px.
- Internal hierarchy: package name, price, description.
- Pale left accent strip: 80 px.

### Slide 6 - Platform selection
- Two columns: x 104 and x 976; each 840 px; 32 px gap.
- Infographic placeholder: x 104, w 1712.

### Slide 7 - Boundaries
- H1: 72 px.
- Cards: x 104 / 976; w 840; h 240.
- Rows y 370 / 642; 32 px gaps.
- Blue 10 px side line; text begins 32 px after the side line.

### Slide 8 - Closing CTA
- H1: 72 px; body 30 px.
- Notice: x 360, y 490, w 1200, h 170.
- Notice icon placeholder: x 400, y 540, 64 x 64; text only `icon`.
- CTA controls use the same 78 / 36 / 16 px profile as Slide 1.

## Acceptance criteria

- Exactly eight slides in Gamma order.
- All Gamma copy and pricing preserved.
- No out-of-bounds objects, clipping or text overlap.
- Slides 2-7 use 104 px margins.
- Labels are transparent, text-sized and use 2 px blue borders.
- Slide 5 remains vertically structured; no table conversion.
- Slide 4 uses `#476FD6`.
- Original visuals are inserted manually into placeholders.
- CTA links are not required.