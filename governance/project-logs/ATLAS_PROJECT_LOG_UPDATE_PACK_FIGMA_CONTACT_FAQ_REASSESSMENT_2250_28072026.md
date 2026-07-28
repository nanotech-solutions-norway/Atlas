# ATLAS PROJECT LOG UPDATE PACK — Figma Contact and FAQ Reassessment

**Timestamp:** 22:50, 28.07.2026 Europe/Oslo  
**Project:** Atlas Website / Atlas AI  
**Task:** Reassess and correct every slide in the persistent Figma Slides files for `Generell kontakt v1.1` and `FAQ v1.1` in Figma project `Atlas AI v3` (project ID `626439448`).  
**Classification:** `AUTO_APPROVED` for exact source-supported copy restoration, verified non-sensitive design corrections, typography normalization and validation rules. Public implementation, accessibility acceptance, legal/privacy approval and release remain `PENDING_REVIEW`.  
**Release state:** `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.

## Files validated

- Generell kontakt: https://www.figma.com/slides/6UODS1tY13e5kO2UnpyGKr
- FAQ: https://www.figma.com/slides/By3uvqtSoHpP7ioqasm4OO
- Contact Gamma source: `g_a0mswzsmjo8r7hz`
- FAQ Gamma source: `g_rody04q71isib3q`

## Issues observed

1. Several auxiliary number/step labels used 16 px text, below the current Atlas presentation readability floor.
2. Some label layers used generic names even though their rendered geometry matched the approved label component.
3. FAQ hero and split-panel H1 text boxes extended beneath decorative/right-side panels, although the rendered text did not visibly collide.
4. FAQ slides 3–9 contained abbreviated copy despite sufficient box capacity; relevant Gamma v1.1 details had not been carried into Figma.
5. FAQ slide 6 used generic `Avklaring` headings not present in the Gamma source and omitted provider, cost and usage qualifiers.
6. FAQ slide 9 omitted half of the source-supported allowed/prohibited use lists.
7. Decorative hero shapes extended outside their side-panel parents because the motif frames did not clip content.
8. Two FAQ slide-9 accent lines retained the old 500 px height after the parent cards were shortened to 450 px.

## Root cause

The initial reconstruction prioritized safe fixed-canvas fit and concise content, causing unnecessary source-copy reduction. Some generated layer helpers also applied internal defaults for badge sizes, label naming and decorative overflow that were not fully normalized during the first pass.

## Corrective rule

1. Reconcile every Figma text node against the latest approved Gamma source before final validation.
2. Do not abbreviate source-supported copy merely to simplify a slide when approved box capacity permits readable inclusion.
3. Preserve approved claim/safety corrections where Gamma wording is contradictory or unsupported.
4. Use Roboto and Roboto Slab only; minimum auxiliary presentation text is 18 px unless a separately approved exception exists.
5. Apply the Atlas component profile: 1920×1080, 104 px side margins, 1712 px content width, label 44 px high / 2 px `#3257B8` / 4 px radius, standard cards 1 px `#CFD2D8` / 6 px radius, warnings `#FFFBF5` with 1 px `#B45309`, CTA 78 px high with 24/30 text.
6. Decorative bleed must be clipped by its intended panel when programmatic parent-overflow validation is required.
7. Re-run full property validation and representative/all-modified-slide screenshots after correction.

## Action taken

### Generell kontakt

- Raised all number badges from 16/20 to 18/22.
- Standardized every top label as `Label border` / `Label text`.
- Clipped the hero motif to its side panel.
- Preserved the corrected distinction between required name/e-mail and prohibited sensitive, confidential, restricted or security-critical data.
- Preserved runtime, routing and receipt statements as implementation requirements rather than completed facts.

### FAQ

- Corrected hero H1 line height to 85 px and constrained its text box to the left content region.
- Constrained the slide-5 H1 to the left column.
- Restored omitted Gamma-supported copy on slides 3–9, including platform/provider qualifiers, low-risk intake restrictions, Managed Secure limitations, privacy/provider dependencies, human-review requirements, student controls and consumer-use boundaries.
- Removed non-source generic `Avklaring` headings from slide 6 and used the available space for the actual qualification text.
- Restored both allowed and prohibited use lists on slide 9.
- Raised step labels and final status text from 16 px to 18 px.
- Rebalanced affected card heights and positions without changing the 1920×1080 canvas or 104 px margins.
- Standardized all label layer names.
- Clipped the hero motif and matched accent-line heights to revised card heights.

## Validation performed

### Generell kontakt

- Slides: 6/6
- Canvas: 1920×1080
- Font families: Roboto / Roboto Slab only
- Text below 18 px: 0
- Out-of-bounds objects: 0
- Unclipped parent overflow: 0
- Label token failures: 0
- Card/warning token failures: 0
- Final programmatic result: `PASS`

### FAQ

- Slides: 11/11
- Canvas: 1920×1080
- Font families: Roboto / Roboto Slab only
- Text below 18 px: 0
- Out-of-bounds objects: 0
- Unclipped parent overflow: 0
- Label-pair/token failures: 0
- Card/warning token failures: 0
- Final programmatic result: `PASS`

All slides were visually reviewed before correction; every modified FAQ slide was rendered and reviewed again after correction. No clipping, overlap, illegible text, broken label, incorrect background or unresolved box defect remained.

## Unresolved items

- Native Figma Slides captions continue to read back as numeric labels even when custom slide names are assigned; section and Gamma source metadata remain stored.
- CTA links, Wix binding, responsive implementation, accessibility/assistive-technology testing, legal/privacy approval and public release validation remain open.
- No public page, checkout, account, Managed Secure production service or release state was activated.
