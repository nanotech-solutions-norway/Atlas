# Atlas AI About v3 — Post-Validation Layout Corrections v1

**Timestamp:** 20:15, 16.07.2026 Europe/Oslo  
**Live Figma file:** https://www.figma.com/slides/YJrRudQSlemarUGuby5s4w  
**Gamma source:** https://gamma.app/docs/4r2wl5rog25safl  
**Approved recurring reference:** https://www.figma.com/slides/QjAYZsGDVS2qxrCzj8TZIA  
**Classification:** AUTO_APPROVED

## Purpose

Record the exact user-directed corrections applied after the Business v1 alignment validation. These corrections are page-specific overrides for `About v3` and supersede conflicting geometry or alignment statements in earlier About v3 validation records.

## Source-authority resolution

1. The user's explicit current instruction is the highest authority.
2. Gamma remains the authority for About v3 wording, section hierarchy and visual intent.
3. Business v1 and the measurement profile remain the recurring design-system authority for margins, grid, typography, borders, padding and CTA components.
4. The corrections below are **About v3-specific overrides**. They must not be generalized to unrelated Atlas slides without explicit approval.

## Slide 5 — `HVA ATLAS ER`

### User instructions

- Increase the sentence/list spacing inside the blue `Atlas eier` panel to 1.5.
- Resize the blue panel to fit the textual content.
- Adjust both height and width accordingly.
- Preserve borders, margins and measurement-report spacing.

### Final validated implementation

| Property | Final value |
|---|---:|
| Blue panel x | 104 px |
| Blue panel y | 350 px |
| Blue panel width | 432 px |
| Blue panel height | 392 px |
| Blue panel corner radius | 8 px |
| Blue panel border | 2 px accent stroke |
| Internal left padding | 32 px |
| Internal right padding | 32 px |
| Internal top padding | 32 px |
| Internal bottom padding | 32 px |
| Heading-to-list gap | 16 px |
| List font size | 22 px |
| List line height | 150% |
| List auto-resize | Height |
| Provider panel x | 568 px |
| Provider panel width | 1248 px |
| Column gap | 32 px |
| Left outer margin | 104 px |
| Right outer margin | 104 px |

### Width calculation rule

The longest rendered list line measured approximately 364 px. The content-fit width was calculated as:

`364 px rendered text + 32 px left padding + 32 px right padding = 428 px`

The result was rounded to the next 8 px measurement-grid increment: **432 px**.

The adjacent provider panel was expanded to consume the remaining 1712 px content frame while retaining the 32 px column gap and 104 px outer margins.

### Validation result

- 150% line height confirmed.
- Text fully contained.
- No clipping or overflow.
- 32 px internal padding maintained.
- 32 px column gap maintained.
- 104 px outer margins maintained.
- Panel and provider content remain inside the 1920 × 1080 slide.

## Slide 7 — Closing CTA

### User instruction

Align the Slide 7 heading and supporting paragraph to the left of the slide like the other slides, rather than centred.

### Final validated implementation

| Element | Final value |
|---|---|
| Heading x | 104 px |
| Heading y | 165 px |
| Heading width | 1712 px |
| Heading height | 110 px |
| Heading font size | 72 px |
| Heading alignment | Left |
| Supporting text x | 104 px |
| Supporting text y | 320 px |
| Supporting text width | 1712 px |
| Supporting text height | 96 px |
| Supporting text font size | 30 px |
| Supporting text alignment | Left |

The quote panel and CTA geometry were intentionally left unchanged.

### Supersession note

This explicit correction supersedes the earlier About v3 validation statement that Slide 7 should use the centred Business v1 closing composition. The current page-specific accepted state uses the Business v1 typography and spacing system while applying a left-aligned About v3 heading/body axis.

## Corrective rules for future Atlas recreation work

1. Content-fit panels must be sized from rendered content plus the approved internal padding, then rounded to the active measurement grid.
2. When one panel in a fixed content row changes width, redistribute the adjacent panel so the approved outer margins and inter-column gap remain exact.
3. Do not reduce text size to make a panel fit when content-fit resizing can preserve readability.
4. Page-specific user corrections override generic reference-deck composition rules.
5. Record every such override explicitly; do not silently treat it as a global template change.
6. Validate the final live Figma nodes after the last correction, not only the exported or earlier validated state.

## Evidence

- Live Figma node read after correction:
  - Slide 5 blue panel: x 104, y 350, w 432, h 392.
  - Slide 5 provider panel: x 568, w 1248.
  - Slide 5 list: 22 px, 150% line height, auto-height.
  - Slide 7 heading/body: x 104, w 1712, left aligned.
- Gamma source confirms the Slide 5 ownership/provider content and Slide 7 wording.
- No source copy was changed.

## Boundary

This record governs Figma recreation geometry and alignment only. It does not approve public launch, provider relationships, security claims, compliance claims, commercial terms or production availability.