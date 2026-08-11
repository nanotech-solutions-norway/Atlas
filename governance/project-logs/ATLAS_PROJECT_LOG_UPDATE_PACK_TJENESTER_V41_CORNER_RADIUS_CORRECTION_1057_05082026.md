# ATLAS PROJECT LOG UPDATE PACK — Tjenester v4.1 corner-radius correction — 10:57, 05.08.2026

## Session/task

Review the approved Atlas Figma instructions, correct inaccurate corner radii in the controlled `Tjenester v4.1` Figma Slides file and validate the complete seven-slide presentation after mutation.

## Scope

- **Figma target:** `https://www.figma.com/deck/phWiIJ6v4Cl3AoXZ5ieeG0`
- **Slides:** 7
- **Design only:** no Gamma mutation, Wix mutation, publication, checkout activation, provider activation or release-state change.

## Issue observed

Several content cards and callouts retained mechanically imported or inconsistent radii:

- `40.517 px` on highlighted pricing/status panels;
- `31.694 px` on the three Privatpersoner cards;
- `18 px` on the closing information callout;
- `0 px` on the Studenter price panel and Managed Secure warning callout.

These values conflicted with the approved Atlas canonical Figma specification, which defines `6 px` for standard cards, boxes and neutral callouts and directs the operator to avoid decorative `18–34 px` radii unless explicitly required by the source visual.

## Root cause

Gamma/PPTX export geometry was retained without normalising the scaled corner values to the controlled Atlas component radius taxonomy. Earlier validation checked box dimensions and padding but did not classify and test every box-like node by component role.

## Corrective rule

- Standard cards, pricing/status panels and informational/warning callouts: `6 px`.
- Category labels and CTA controls: `4 px`.
- Full-slide backgrounds: `0 px`.
- Circular and intentionally shaped image masks retain their approved source geometry.
- Any other radius above `6 px` requires explicit evidence and documented approval.
- Validation must inspect all four individual corner values and render every affected slide.

## Action taken

Applied `6 px` to all four corners of:

- Bedrift price panel `0:51`;
- Studenter price panel `0:88`;
- Privatpersoner cards `0:114`, `0:121`, `0:128`;
- Managed Secure price/status panel `0:154`;
- Managed Secure warning callout `0:168`;
- Closing information callout `0:239`.

Preserved:

- label and CTA radius at `4 px`;
- full-slide backgrounds at `0 px`;
- all image fills, image masks and crop geometry;
- hero/non-hero heading sizes;
- text, dimensions, margins, padding, fills, strokes and slide positions.

## Validation result

| Control | Result |
|---|---:|
| Content cards/callouts at 6 px | 8/8 `PASS` |
| Label outlines at 4 px | 4/4 `PASS` |
| CTA controls at 4 px | 8/8 `PASS` |
| Full-slide backgrounds at 0 px | 7/7 `PASS` |
| Unexpected decorative radii above 6 px | 0 `PASS` |
| Hero heading | 64 px Roboto Slab `PASS` |
| Non-hero headings | 6/6 at 50 px Roboto Slab `PASS` |
| Image-bearing nodes | 12/12 `PASS` |
| Visible out-of-bounds nodes | 0 `PASS` |
| Rendered affected-slide QA | 5/5 `PASS` |

## Final classification

`PASS_DESIGN_AND_CONTENT_HANDOFF`

This classification applies to the corrected Figma presentation. It does not imply Wix implementation, responsive validation, accessibility acceptance or public release.

## Classification

- Exact owner correction, validated design fix and non-sensitive radius-control rule: `AUTO_APPROVED`.
- Wix implementation and public release: unchanged; `NO_GO`.
