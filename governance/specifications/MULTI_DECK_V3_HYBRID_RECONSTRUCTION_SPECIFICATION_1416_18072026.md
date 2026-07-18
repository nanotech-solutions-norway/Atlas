# Atlas AI Multi-Deck v3 Hybrid Reconstruction Specification

**Timestamp:** 14:16, 18.07.2026 Europe/Oslo  
**Scope:** Consumer v3, Prices v3, Platform lanes v3 and Resources v3  
**Classification:** Verified design reconstruction rules and corrections are **AUTO_APPROVED**. Pricing, Family, provider, planned-resource, legal, privacy, accessibility, contractual, commercial and public-availability matters remain **PENDING_REVIEW**.

## Direct sources

### Figma Slides

- Consumer v3: https://www.figma.com/slides/gCPI4x84ehk6vzHLghlEMG
- Prices v3: https://www.figma.com/slides/UC9XULUw2g6qxqjMgKp2Ke
- Platform lanes v3: https://www.figma.com/slides/GbL4JMbnrLN8ZmBIaMOzlF
- Resources v3: https://www.figma.com/slides/RbyhdwQhANrHEqHTj5hs4a

### Gamma

- Consumer v3: https://gamma.app/docs/Consumer-v3-cw00glpuqcihzkm
- Prices v3: https://gamma.app/docs/Prices-v3-dgiw7zzgu6b6762
- Platform lanes v3: https://gamma.app/docs/Platform-lanes-v3-tzbulplvdgtijwq
- Resources v3: https://gamma.app/docs/Resources-v3-8qrcaja8btqk3zc

## Source authority applied

1. Current user instruction and supplied Figma file URLs.
2. Current approved Atlas operational tokens and later 24 px CTA correction.
3. Current Gamma v3 source wording, order, hierarchy and visual exceptions.
4. Supplied PPTX/PDF exports as visual evidence.
5. Approved Business v1 Figma reference.
6. Atlas AI Business v1 validated measurement profile v2.1.

The older 36 px CTA text value was superseded by the current approved 24 px operational token. No conflicting commercial, pricing, provider or public-availability information was silently merged.

## Governing reconstruction tokens

- Canvas: 1920 × 1080 px.
- Slide background: solid white `#FFFFFF`.
- Standard horizontal margin: 104 px.
- Standard content width: 1712 px.
- Standard grid gap: 32 px.
- Standard card/panel padding: 32 px.
- Hero H1: Roboto Slab Regular, 72 px.
- Content H1: Roboto Slab Regular, 54 px.
- Card headings: Roboto Slab Bold, approximately 27–30 px.
- Body: Roboto Regular, approximately 20–30 px with 130–155% line height according to density.
- Labels: transparent; 2 px `#3257B8`; radius 4; height 44; text width + 28 px.
- CTA controls: Roboto Bold 24 px; height 78; 2 px `#3257B8`; radius 4; centred vertically and horizontally.
- Standard cards: `#FFFFFF` or `#E9ECF2`; 1 px `#CFD2D8`; radius 6.
- Gamma source-highlight panels: `#476FD6`.
- Manual-validation panels: `#FFFBF5`; 1 px `#B45309`; radius 6.
- All text, tables, cards, panels, labels, buttons and placeholders remain editable.
- No Gamma image fill is retained.

## Slide maps

### Consumer v3 — 6 slides

1. Consumer hero with right-side image placeholder and two CTA controls.
2. Six everyday-task modules with editable icon placeholders.
3. Everyday Basic and Family plan panels with complete Family validation warning.
4. Five important-boundary cards.
5. Privacy principles blue panel, three supporting cards and full validation warning.
6. Editable plan-comparison table, qualification copy and two interest CTAs.

### Prices v3 — 9 slides

1. Pricing hero with behind-image placeholder and two CTAs.
2. Student Basic and Student Plus proposed-plan panels.
3. Everyday Basic and Family proposed-plan panels and Family warning.
4. Monthly AI-usage-frame language and mechanics warning.
5. Business-solution/provider-cost panels and commercial-pricing warning.
6. Five FAQ cards.
7. Early-access process with five editable icons and activation warning.
8. Editable six-column comparison table.
9. Closing route selector with left visual placeholder, cards, CTAs and qualification notice.

### Platform lanes v3 — 8 slides

1. Platform-lanes hero with behind-image placeholder and two CTAs.
2. Five-question decision guide.
3. Four delivery-lane cards and provider validation warning.
4. Microsoft lane with right image placeholder, four requirements and qualification warning.
5. Google lane with left image placeholder, four requirements and implementation notice.
6. Research / Multi-Engine controls.
7. Eight platform-selection criteria.
8. No-permanent-model-promise principle and CTA.

### Resources v3 — 8 slides

1. Resources hero with right image placeholder and two CTAs.
2. Four numbered need-definition cards and planned-resource warning.
3. Five business-resource cards and planned-resource warning.
4. Student-resource blue panel, guidance panel and validation warning.
5. Five private/household resource modules and warning.
6. Five responsible-AI-use modules.
7. Five platform-guide cards and publication warning.
8. Closing resource selector with left visual placeholder, audience cards, CTAs and publication-status warning.

## Placeholder inventory

### Consumer

- `[ASSET-GAMMA-CONSUMER-V3-C1-HERO-1]`

### Prices

- `[ASSET-GAMMA-PRICES-V3-C1-HERO-1]`
- `[ASSET-GAMMA-PRICES-V3-C9-CLOSING-1]`

### Platform lanes

- `[ASSET-GAMMA-PLATFORM-LANES-V3-C1-HERO-1]`
- `[ASSET-GAMMA-PLATFORM-LANES-V3-C4-MICROSOFT-1]`
- `[ASSET-GAMMA-PLATFORM-LANES-V3-C5-GOOGLE-1]`

### Resources

- `[ASSET-GAMMA-RESOURCES-V3-C1-HERO-1]`
- `[ASSET-GAMMA-RESOURCES-V3-C8-CLOSING-1]`

All eight placeholders are editable rectangles with neutral fill and 1 px border. Editable icon placeholders contain only `icon`.

## Implementation correction rule

Imported and generated text must be resized in this order:

1. Assign the target text width.
2. Load the final font.
3. Set `textAutoResize = HEIGHT` after width assignment.
4. Recalculate all dependent title/body, card, warning and downstream positions from rendered text height.
5. Run text-to-text and text-to-box visual checks; clipping checks alone are insufficient.

This rule prevents the fixed-height clipping and hidden shape-to-text overlap found during the first deterministic and screenshot passes.

## Governance boundary

The reconstruction preserves all proposed-price language, no-checkout limits, Family qualification, provider qualification, planned-resource qualification, no-unlimited-use language, no-sensitive-public-upload language and all manual-validation notices. It does not approve those matters for production or public publication.