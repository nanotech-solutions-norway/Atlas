# Atlas AI About v3 — Wix Color, Placeholder and Typography Corrections v1

**Original timestamp:** 23:38, 16.07.2026 Europe/Oslo  
**Button-token revision:** 12:32, 17.07.2026 Europe/Oslo  
**Live Figma:** https://www.figma.com/slides/YJrRudQSlemarUGuby5s4w  
**Gamma source:** https://gamma.app/docs/4r2wl5rog25safl  
**Classification:** AUTO_APPROVED

## Purpose

Record the user-directed corrections applied to `About v3`: correct subheading colors, Wix-aligned caution boxes, transparent labels, unique non-icon image placeholders, approved button typography, measured text spacing and content-fit internal box heights.

## Current supersession

The 17.07.2026 explicit correction supersedes the former 36 px button-text value in this record. Current About v3 buttons use Roboto SemiBold 24 px with 30 px line height, vertically and horizontally centred. Button frames, source wording, widths, height, border and gap remain unchanged.

## Source authority

1. Current explicit user instruction.
2. Approved Atlas Wix/website visual guidance.
3. `Atlas_AI_Canonical_Figma_Recreation_Specification_v3_0157_15072026.md`.
4. Gamma About v3 for wording, hierarchy, image locations and icon retention.
5. Existing live Figma evidence.

## Wix evidence note

The Wix connector confirmed the controlled Atlas-AI Wix Studio site and provided its editor/preview references. The Studio canvas styles were not visually retrievable through the available API connection. The caution-box correction therefore uses the latest approved Atlas Wix build-plan palette rather than an unsupported visual guess:

- surface: `#FFFBF5`;
- dark amber border/icon: `#B45309`;
- copy: `#15213F`.

This supersedes the prior `#FFF1AB` fill and neutral border on the two About v3 warning boxes.

## Final rules

### Subheadings

Subheadings on white or light surfaces use Roboto Slab SemiBold, 28 px, 125% line height and `#3257B8`. The provider heading remains 30 px. The `Atlas eier` heading remains white on `#476FD6`.

### Labels

Every visible label uses a transparent fill, 2 px `#3257B8` stroke, 4 px radius, 44 px height, 14 px horizontal padding and Roboto SemiBold 18 px blue text. The former solid Slide 1 label is superseded.

### Non-icon image placeholders

All non-icon images were removed and replaced at their original locations by these editable unique tags:

1. `[ASSET-GAMMA-ABOUT-V3-C1-HERO-1]`
2. `[ASSET-GAMMA-ABOUT-V3-C4-BUSINESS-1]`
3. `[ASSET-GAMMA-ABOUT-V3-C4-STUDENT-2]`
4. `[ASSET-GAMMA-ABOUT-V3-C4-FAMILY-3]`
5. `[ASSET-GAMMA-ABOUT-V3-C5-PROVIDER-1]`

Placeholder styling is `#E9ECF2` fill, 1 px `#CFD2D8` border, 6 px radius and centered Roboto SemiBold 18 px blue tag text. Full Gamma source detail is retained in layer names and Atlas metadata. Gamma icons remain intact.

### Buttons

Slides 1 and 7 use 480/320 px button widths, 78 px height, 16 px gap, 4 px radius, 2 px blue border and centred Roboto SemiBold **24 px** text with **30 px** line height. Text remains `Se hvordan Atlas arbeider` and `Les Trust`.

### Spacing

- Content H1 to intro: 8 px.
- Card heading to body: 8 px.
- Body line height: 130%.
- Card-heading line height: 125%.
- Offer body to status: 16 px.
- Slide 1 and Slide 7 H1 to body: 32 px.

### Height interpretation

Figma Slides canvases remain fixed at 1920 × 1080. Content-fit height was applied to internal panels instead of resizing the slide canvas. The Slide 4 warning is 96 px high and the Slide 6 warning is 104 px high; both end at y=1000.

## Validation

- Seven 1920 × 1080 slides.
- Zero remaining image fills.
- Five unique placeholders.
- Zero label background fills.
- Zero out-of-bounds nodes.
- CTA gaps: 16 px.
- Button typography: PASS — Roboto SemiBold 24 px / 30 px line height.
- Required subheading color: `#3257B8`.
- Warning palette: `#FFFBF5`, `#B45309`, `#15213F`.
- Visual review of all seven slides: PASS.

## Boundary

This record governs design reconstruction only and does not approve public launch or other gated Atlas decisions.