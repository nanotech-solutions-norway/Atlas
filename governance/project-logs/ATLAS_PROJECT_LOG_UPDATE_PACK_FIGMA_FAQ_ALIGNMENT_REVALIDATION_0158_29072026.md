# ATLAS PROJECT LOG UPDATE PACK — FIGMA FAQ ALIGNMENT REVALIDATION

**Timestamp:** 01:58, 29.07.2026 Europe/Oslo  
**Project:** Atlas Website / Atlas AI  
**Task:** Correct FAQ slide 4 and slide 7 box alignment, then revalidate both Figma presentations  
**Classification:** `AUTO_APPROVED`  
**Release effect:** None — `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`

## Issue observed

The owner identified that the three boxes on FAQ slide 4 and the blue Managed Secure box on FAQ slide 7 did not conform precisely to the approved margin, gutter and border-alignment instructions.

## Root cause

1. FAQ slide 4 used three 549 px columns, producing a one-pixel cumulative shortfall against the 1712 px content width and leaving the right edge at x=1815 instead of x=1816.
2. FAQ slide 7 used asymmetric 820 px and 860 px columns. Although the outer edges and 32 px gutter were technically inside the content area, the configuration did not follow the equal-column presentation rule.
3. The first post-change audit counted two deliberately oversized hero diagonals as out-of-slide. Their parent panel was clipped correctly; the audit required clipped-ancestor awareness rather than a design change.

## Corrective rule

- Use x=104 and x=1816 as the exact Phase 1 presentation content boundaries.
- Use a 32 px standard gutter.
- For three equal columns across 1712 px: use 549.333333 px per column with x positions 104, 685.333333 and 1266.666667.
- For two equal columns: use 840 px widths at x=104 and x=976.
- Resize child text widths with their parent boxes while retaining 32 px internal horizontal padding.
- Validation scripts must exclude overflow that is intentionally contained by a clipped ancestor.

## Action taken

### FAQ slide 4

- Recalculated all three route boxes to equal widths of 549.333333 px.
- Set exact x positions to 104, 685.333333 and 1266.666667.
- Confirmed 32 px gutters and exact right edge x=1816.
- Resized title and body text widths to preserve 32 px internal padding.

### FAQ slide 7

- Set the left public-intake panel to x=104, width=840.
- Set the blue Managed Secure panel to x=976, width=840.
- Confirmed a 32 px gutter and exact right edge x=1816.
- Resized child text widths to 776 px and matched the left accent line to the panel height.

## Evidence

- FAQ Figma Slides: https://www.figma.com/slides/By3uvqtSoHpP7ioqasm4OO
- Generell kontakt Figma Slides: https://www.figma.com/slides/6UODS1tY13e5kO2UnpyGKr
- Targeted 1920×1080 screenshots of corrected FAQ slides 4 and 7 were visually reviewed after modification.
- Figma Plugin API readback was used for all geometry and QA checks.

## Validation result

### FAQ

- Slides: 11/11
- Canvas: 1920×1080
- Background: approved `#FBFCFE`
- Fonts: Roboto and Roboto Slab only
- Minimum text size: 18 px
- Label border profile: x=104, y=58, height=44, 2 px `#3257B8`, radius 4
- Out-of-slide defects: 0 after correct clipped-ancestor handling
- Parent/text overflow: 0
- Slide 4 equal-column geometry: PASS
- Slide 7 equal-column geometry: PASS
- Overall: `PASS`

### Generell kontakt

- Slides: 6/6
- Canvas: 1920×1080
- Background, margins, typography, labels, clipping and overflow: PASS
- Overall: `PASS`

## Unresolved items

This is a Figma presentation-design validation only. Wix implementation, responsive behavior, accessibility acceptance, link binding, legal/privacy approval and public release remain separate pending gates. No deployment, purchase, publication or production capability was enabled.
