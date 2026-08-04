# ATLAS PROJECT LOG UPDATE PACK — Tjenester v4.1 slide 3 image reduction — 01:08, 05.08.2026

## Session/task

Reduce both images on slide 3 of the controlled `Tjenester v4.1` Figma Slides file by 30%, preserve the approved source content and column structure, re-apply the approved Atlas typography sizes, and validate the affected box margins and configurations.

## Scope

- **Gamma source:** `https://gamma.app/docs/8xdk799x5l2hm0h`
- **Figma target:** `https://www.figma.com/deck/phWiIJ6v4Cl3AoXZ5ieeG0`
- **Slide:** slide 3, node `0:23`, heading `Lær mer, forstå dypere`
- **Image nodes:** `0:74` and `0:81`
- **Design scope only:** no Gamma content mutation, Wix mutation, publication, checkout activation, provider activation or release-state change.

## Issue or adjustment observed

The owner requested that both circular images on slide 3 be reduced by 30% while retaining the established layout and ensuring that typography, box margins and box configuration remained compliant with the approved Atlas Figma process.

## Root cause

This was an explicit visual-balance correction, not a defect in the prior source reconciliation. The existing images matched the Gamma/PDF/PPTX export dimensions, but the approved current instruction supersedes those image dimensions for this exact slide.

## Corrective rule

When an approved image-size correction is issued after source reconciliation:

1. apply the percentage change to both width and height;
2. preserve the image centre unless the owner specifies another anchor;
3. preserve crop mode, image fill, clipping and column alignment;
4. re-apply and validate the complete affected-slide typography contract;
5. validate principal margins, column geometry, label boxes, price/status cards, internal box padding and CTA configuration;
6. render and inspect the complete slide after mutation;
7. treat the explicit current user correction as higher authority than the earlier exported geometry for the corrected property only.

## Evidence/source

- Explicit current user instruction at 01:08, 05.08.2026.
- Live Gamma readback of the seven-section `Tjenester - v4.1` source, including the slide-3 student smart-layout and exact public copy.
- Existing approved Atlas Figma adjustment standard.
- Live pre-edit Figma node inventory for slide `0:23`.
- Live post-edit Figma node readback and rendered screenshot.

## Action taken

- Reduced image `0:74` from `612.468689 × 612.468689 px` to `428.728088 × 428.728088 px`.
- Reduced image `0:81` from `612.484436 × 612.484436 px` to `428.739105 × 428.739105 px`.
- Preserved both original centres:
  - left image centre: `529.500061, 463.578171`;
  - right image centre: `1390.476593, 463.586044`.
- Preserved `IMAGE` fills, `CROP` scale mode and frame clipping.
- Re-applied the approved slide-3 typography:
  - label: Roboto Regular, `10.6667 px`;
  - main heading: Roboto Slab Regular, `36 px`;
  - section and box headings: Roboto Slab Regular, `17.3333 px`;
  - body, price, list and CTA text: Roboto Regular/SemiBold, `13.3333 px`.
- Preserved all source copy, pricing, labels, list content, CTA text and claim boundaries.

## Validation result

| Control | Result |
|---|---:|
| Slide canvas | `1920 × 1080` `PASS` |
| Left image reduction | Exact 70% dimensions and centre preserved `PASS` |
| Right image reduction | Exact 70% dimensions and centre preserved `PASS` |
| Image fill/crop/clipping | 2/2 `PASS` |
| Typography nodes tested | 11/11 `PASS` |
| Missing fonts | 0 `PASS` |
| Principal side margins | `104.172 px` left/right `PASS` |
| Label box | Position, size, 1.5 px stroke, 4 px radius, no fill `PASS` |
| Price box | Position, size, Atlas blue fill and square configuration `PASS` |
| Price-box inner margins | `14.641 px` left/right and `8.234 px` top `PASS` |
| Column geometry | Widths and `10.297 px` inter-column gap `PASS` |
| CTA box | Position, size, 2 px stroke, 4 px radius, editable gradient fill `PASS` |
| Visible out-of-bounds nodes | 0 `PASS` |
| Rendered visual QA | `PASS` |

## Final validation classification

`PASS_DESIGN_AND_CONTENT_HANDOFF`

This result applies only to slide 3 in the specified Figma file after the explicit 30% image reduction. It does not constitute Wix implementation, responsive validation, accessibility acceptance or public-release approval.

## Unresolved items

- Gamma remains unchanged because the Gamma connector exposes read/export/generation actions but no in-place edit action for the existing regular Gamma.
- Wix implementation and runtime validation remain separate workstreams.
- Public release remains `NO_GO` under the controlling Atlas gates.

## Classification

- Exact owner correction, validated Figma mutation and quality-control evidence: `AUTO_APPROVED`.
- Runtime implementation and public release: unchanged; `NO_GO`.