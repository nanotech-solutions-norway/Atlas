# ATLAS PROJECT LOG UPDATE PACK — Tjenester v4.1 slide 3 margin and typography correction — 01:23, 05.08.2026

## Session/task

Correct slide 3 of the controlled `Tjenester v4.1` Figma Slides file after owner feedback that the box margins, box-text margins and heading typography were still inaccurate.

## Scope

- **Figma target:** `https://www.figma.com/deck/phWiIJ6v4Cl3AoXZ5ieeG0`
- **Gamma source:** `https://gamma.app/docs/8xdk799x5l2hm0h`
- **Slide:** `0:23`, `Lær mer, forstå dypere`
- **Design only:** no Gamma mutation, Wix mutation, publication, checkout activation, provider activation or release-state change.

## Issue observed

1. The prior correction retained the compact slide-3 export typography (`36 / 17.3333 / 13.3333 px`) rather than the established Tjenester page hierarchy used on slides 2, 4 and 5.
2. The price card remained offset from the left content column and used approximately `14.641 px` horizontal text inset rather than the established Tjenester card inset.
3. The first follow-up pass aligned the card horizontally but used an `18 px` top inset and a smaller inter-text gap. This still did not match the established card configuration.
4. A validation comparison initially used supporting-text node `0:141` as a heading peer instead of the actual Managed Secure heading node `0:144`, producing a false heading-consistency failure.

## Root cause

The first slide-3 adaptation treated the mechanically exported compact layout as the controlling typography scale. It also preserved source-specific price-card offsets instead of applying the established cross-slide card alignment and `26.031 px` inset pattern.

## Corrective rule

For Tjenester page-level slides:

- category labels use `Roboto 20 px` unless an explicitly approved specialist layout applies;
- page headings use `Roboto Slab 64 px` where peer page headings use that level;
- supporting/card headings use `Roboto Slab 32 px`;
- body, list and price text use `Roboto 25.3333 px`;
- CTA labels use `Roboto SemiBold 20 px`;
- content cards align to the controlled column boundary;
- card heading/text use the established `26.031 px` left, right and top inset and `26.031 px` heading-to-body spacing;
- validator peer IDs must be verified by text content before a mismatch is classified as a design failure.

## Action taken

- Preserved the approved 30% image reduction and `IMAGE/CROP` fills.
- Restored the main heading to `Roboto Slab Regular 64 px`, matching slides 2, 4 and 5.
- Set category label to `Roboto Regular 20 px` and centred it within a `136 × 40 px` outline box.
- Set both supporting headings to `Roboto Slab Regular 32 px`.
- Set supporting body copy, price and eligibility list to `Roboto Regular 25.3333 px`.
- Set CTA label to `Roboto SemiBold 20 px` and normalised the CTA to `165.875 × 71.625 px`.
- Aligned the price card to the left column at `x=104.172 px`, width `850.672 px`.
- Applied `26.031 px` left/right/top card insets and `26.031 px` heading-to-body spacing.
- Applied the same horizontal and vertical inset pattern to the right `Passer for` content block.
- Increased the price-card height to `150 px` and preserved a `20 px` outer gap from the body block.

## Validation result

| Control | Result |
|---|---:|
| Main heading peer consistency | `64 px Roboto Slab` across slides 2, 3, 4 and 5 — `PASS` |
| Slide-3 typography nodes | 11/11 `PASS` |
| Missing fonts | 0 `PASS` |
| Price-card column alignment | `x=104.172`, `w=850.672` — `PASS` |
| Price-card outer vertical gap | `20 px` — `PASS` |
| Price-card left/right/top text inset | `26.031 px` — `PASS` |
| Price-card heading-to-body spacing | `26.031 px` — `PASS` |
| Right block left/right/top inset | `26.031 px` — `PASS` |
| Right block heading-to-body spacing | `26.031 px` — `PASS` |
| Label box | `136 × 40`, `1.5 px` stroke, `4 px` radius — `PASS` |
| CTA box | `165.875 × 71.625`, `2 px` stroke, `4 px` radius — `PASS` |
| Images | exact 70% dimensions, centred, `IMAGE/CROP` — `PASS` |
| Visible out-of-bounds nodes | 0 `PASS` |
| Rendered visual QA | `PASS` |

## Final classification

`PASS_DESIGN_AND_CONTENT_HANDOFF`

This result applies only to slide 3 after the owner-requested typography and margin correction. It does not imply Wix implementation, responsive validation, accessibility acceptance or public release.

## Classification

- Owner correction, validated layout correction and validator correction: `AUTO_APPROVED`.
- Runtime implementation and public release: unchanged; `NO_GO`.
