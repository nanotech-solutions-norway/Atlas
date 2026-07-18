# Atlas AI Multi-Deck v3 Typography, Box and Gamma Similarity Validation

**Timestamp:** 15:01, 18.07.2026 Europe/Oslo  
**Scope:** Consumer v3, Prices v3, Platform lanes v3 and Resources v3.  
**Figma slide count:** 31.  
**Classification:** Verified design corrections and QA results are **AUTO_APPROVED**. Commercial, pricing, provider, legal, privacy, accessibility, contractual and public-production matters remain **PENDING_REVIEW**.

## Sources reviewed

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

### Measurement and instruction authority

- `Atlas_AI_Canonical_Figma_Recreation_Specification_v3_0157_15072026.md`
- `MULTI_DECK_V3_HYBRID_RECONSTRUCTION_SPECIFICATION_1416_18072026.md`
- `Atlas_AI_Business_v1_Validated_Figma_Slides_Measurement_Profile_2116_13072026.md`
- `ATLAS_FIGMA_TYPOGRAPHY_BOX_GRID_VALIDATION_ADDENDUM_1501_18072026.md`
- Approved Business v1 Figma reference: https://www.figma.com/slides/QjAYZsGDVS2qxrCzj8TZIA
- Uploaded Gamma PPTX/PDF exports for all four decks.

## Corrections applied

### Typography

- Display H1 retained at Roboto Slab Regular 72 px and corrected to 118% line height.
- Content H1 retained at Roboto Slab Regular 54 px and corrected to 125% line height.
- Card/module headings changed from Roboto Slab Bold to Roboto Slab SemiBold, 27–30 px, 125% line height.
- Label text changed from Roboto Medium to Roboto SemiBold, 18 px, 22 px line height.
- Button text changed from Roboto Bold to Roboto SemiBold, 24 px, 30 px line height.
- Body/list line heights outside the approved range were normalized to 125–135%.

### Alignment and spacing

- Labelled content-slide labels aligned to x 104, y 58.
- Labelled content-slide H1 blocks aligned to x 104, y 130, width 1712.
- Intro copy aligned 8 px below the rendered H1 block.
- Standard left alignment retained for content-slide hierarchy.
- Gamma-defined hero and closing alignment retained rather than forced into a generic centred template.

### Boxes, margins, padding and borders

- Slide size confirmed at 1920 × 1080.
- All slide backgrounds confirmed as solid white `#FFFFFF`.
- Standard horizontal content frame confirmed at 104 px margins and 1712 px width.
- Standard card/panel text inset retained at 32 px.
- Standard card/panel border normalized to 1 px `#CFD2D8`, radius 6 px.
- Warning panels normalized to `#FFFBF5`, 1 px `#B45309`, radius 6 px.
- Labels confirmed transparent with 2 px `#3257B8`, radius 4 px, height 44 px and dynamic content-fit width.
- Buttons confirmed at 78 px height, 2 px `#3257B8`, radius 4 px and centred text.
- Equal three-column card rows changed from 528 px cards with 64 px gaps to 549.333 px cards with 32 px gaps.
- Editable dense tables retain 24 px cell insets as a documented density exception.

## Deterministic validation

| Check | Consumer | Prices | Platform lanes | Resources | Combined |
|---|---:|---:|---:|---:|---:|
| Slides | 6 | 9 | 8 | 8 | 31 |
| Out-of-bounds objects | 0 | 0 | 0 | 0 | 0 |
| Clipped text | 0 | 0 | 0 | 0 | 0 |
| Text overlaps | 0 | 0 | 0 | 0 | 0 |
| Image fills | 0 | 0 | 0 | 0 | 0 |
| Typography/style violations | 0 | 0 | 0 | 0 | 0 |
| Three-column grid violations | 0 | 0 | 0 | 0 | 0 |
| Missing source metadata | 0 | 0 | 0 | 0 | 0 |
| Non-white slide backgrounds | 0 | 0 | 0 | 0 | 0 |

## Gamma content cross-check

A final source-critical text audit was run after all design corrections. No copy was intentionally rewritten during this refinement.

| Deck | Source-critical strings checked | Missing |
|---|---:|---:|
| Consumer v3 | 20 | 0 |
| Prices v3 | 21 | 0 |
| Platform lanes v3 | 22 | 0 |
| Resources v3 | 27 | 0 |
| **Total** | **90** | **0** |

The audited strings include headings, proposed prices, qualification language, manual-validation notices, provider boundaries, no-checkout language, no-unlimited-use language, publication status, sensitive-upload restrictions and CTA wording.

## Visual QA

Eighteen post-adjustment screenshots were inspected:

- Consumer: hero, five-boundary-card layout and comparison/CTA slide.
- Prices: behind-image hero, FAQ card grid, comparison table and closing split layout.
- Platform lanes: behind-image hero, delivery-lane cards, Microsoft image exception, selection-criteria grid and closing principle slide.
- Resources: right-image hero, business-resource grid, student two-panel layout, responsible-use card grid, platform-guide layout and closing split layout.

The screenshots confirm:

- correct white backgrounds;
- no visible clipping or overlap;
- consistent heading and body hierarchy;
- readable content density;
- stable internal padding and card alignment;
- corrected 32 px three-column gaps;
- correct button typography and centring;
- preserved Gamma image-position exceptions;
- editable placeholders located where the source images appeared.

## Detailed Gamma-to-Figma similarity assessment

The scores below are qualitative design-review scores, not automated pixel-similarity measurements. Gamma is a fluid webpage source, while Figma is a fixed 1920 × 1080 slide system with intentionally editable image placeholders.

### Consumer v3

**Content fidelity: 10.0/10**  
All audited source-critical copy is present. The six-section order, price and Family qualification, safety boundaries, privacy warning and comparison table are retained.

**Structural fidelity: 9.8/10**  
The right-image hero, six everyday-task modules, two-plan comparison, 3+2 boundary-card rhythm, two-column privacy composition and editable comparison table match the Gamma component types.

**Visual fidelity: 9.3/10**  
The source composition and blue/white hierarchy are retained. The principal intentional difference is replacement of the generated hero image with an editable source-tagged placeholder and application of the approved Atlas type/spacing tokens.

**Technical quality: 10.0/10**  
Zero deterministic findings after correction.

### Prices v3

**Content fidelity: 10.0/10**  
All audited prices, MVA wording, proposed-status language, usage limits, provider qualifications, FAQ content, no-active-checkout statement and closing qualification are retained.

**Structural fidelity: 9.8/10**  
The behind-image hero, paired pricing panels, four-card usage section, paired business/provider section, 3+2 FAQ layout, five-step process, six-column table and left-image closing composition match the Gamma source.

**Visual fidelity: 9.2/10**  
The fixed-slide implementation preserves hierarchy, card rhythm, highlighting and image locations. Source images are placeholders and the 32 px Atlas grid is more regular than Gamma's fluid spacing.

**Technical quality: 10.0/10**  
Zero deterministic findings after correction.

### Platform lanes v3

**Content fidelity: 10.0/10**  
All audited provider-lane qualifications, Microsoft and Google prerequisites, research controls, selection criteria and no-permanent-model promise are retained.

**Structural fidelity: 9.9/10**  
The behind-image hero, vertical five-question guide, four delivery-lane blocks, Microsoft right-image exception, Google left-image exception, four research controls, eight selection criteria and closing principle are preserved.

**Visual fidelity: 9.4/10**  
Provider imagery is intentionally replaced with editable placeholders, but visual position, two-column balance, warnings, card shapes and closing CTA hierarchy remain source-faithful.

**Technical quality: 10.0/10**  
Zero deterministic findings after correction.

### Resources v3

**Content fidelity: 10.0/10**  
All audited planned-resource qualifications, student age/guardian language, private-use boundaries, responsible-use principles, platform-guide warnings and publication-status notice are retained.

**Structural fidelity: 9.8/10**  
The right-image hero, numbered need cards, 3+2 business-resource grid, two-panel student section, 3+2 private and responsible-use grids, five platform-guide cards and left-image closing section match Gamma.

**Visual fidelity: 9.3/10**  
The source blue-panel emphasis and audience hierarchy are retained. Generated imagery is replaced by placeholders and equal three-column rows use the canonical Atlas 32 px grid.

**Technical quality: 10.0/10**  
Zero deterministic findings after correction.

## Overall assessment

| Dimension | Assessment |
|---|---:|
| Content fidelity | 10.0/10 |
| Section-order and component-type fidelity | 9.8/10 |
| Visual/layout fidelity | 9.3/10 |
| Typography and spacing consistency | 10.0/10 |
| Editability and implementation quality | 10.0/10 |
| Overall hybrid reconstruction quality | 9.7/10 |

The result is **hybrid faithful rather than pixel-identical**. It deliberately combines Gamma's wording, hierarchy, component types, source colours and image positions with the approved Atlas Business-reference geometry, typography, margins, padding, borders and CTA system.

## Remaining gates

The following remain **PENDING_REVIEW** and are not approved by this validation:

- proposed prices and MVA/tax treatment;
- Family entitlement, minimum age, guardian model, membership, privacy and billing mechanics;
- provider identities, delivery form, rights, license/API basis, processor roles, availability and costs;
- usage measurement, warning, limitation, reset, upgrade and billing behaviour;
- business pricing/package publication;
- planned-resource publication, live links, ownership and claims status;
- legal, privacy, accessibility, contractual, commercial and public-production approval.

## Final status

**PASS — AUTO_APPROVED** for Figma geometry, slide height, backgrounds, typography, line spacing, text alignment, margins, padding, borders, box width, grid spacing, content fit, editability, source traceability and Gamma comparison quality.