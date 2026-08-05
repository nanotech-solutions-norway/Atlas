# ATLAS PROJECT LOG UPDATE PACK — Tjenester v4.1 50 px headings and image validation — 09:56, 05.08.2026

## Session/task

Apply the owner-approved default that all principal page headings outside the hero section use 50 px, preserve the approved hero heading, and validate every image-bearing node across all seven `Tjenester v4.1` Figma slides.

## Scope

- **Figma target:** `https://www.figma.com/deck/phWiIJ6v4Cl3AoXZ5ieeG0`
- **Gamma source:** `https://gamma.app/docs/8xdk799x5l2hm0h`
- **Slides:** 7
- **Design scope only:** no Gamma mutation, Wix mutation, publication, checkout activation, provider activation or release-state change.

## Owner correction

- Keep the hero-section heading at its approved size.
- Set all non-hero principal page headings to 50 px.
- Use this as the default Atlas Figma instruction.
- Validate images across every slide.

## Corrective rule

1. Hero headings retain the approved hero-specific size unless explicitly changed.
2. Every non-hero principal page heading defaults to `Roboto Slab Regular, 50 px`, with `118%` line height.
3. This rule applies only to the principal page/section heading; card headings, supporting headings, labels and CTA text retain their separately controlled hierarchy.
4. Every image-bearing node on every slide must be validated for:
   - `IMAGE` fill;
   - non-empty image hash;
   - visibility and opacity;
   - approved crop/scale mode;
   - clipping;
   - finite image transform;
   - positive geometry;
   - containment inside the slide;
   - rendered crop and focal-subject quality.

## Action taken

- Preserved slide 1 hero heading `Velg riktig AI-løp for behovet.` at `Roboto Slab Regular, 64 px`.
- Set the following non-hero headings to `Roboto Slab Regular, 50 px`, `118%` line height:
  - slide 2: `AI tilpasset din virksomhet`;
  - slide 3: `Lær mer, forstå dypere`;
  - slide 4: `AI til hverdagen – enkelt og trygt`;
  - slide 5: `Managed Secure`;
  - slide 6: `En felles arbeidsmåte.`;
  - slide 7: `Usikker på hvilket løp som\npasser?`.
- Resized heading frames to the controlled line-height footprint while preserving x/y positions, widths, copy and deliberate line breaks.
- Preserved the approved slide-3 30% image reduction.
- Added slide metadata identifying the 50 px non-hero heading standard.
- Updated the canonical Atlas Figma adjustment standard with the new default and full-slide image-validation requirement.

## Image validation result

| Slide | Image-bearing nodes | Result |
|---|---:|---:|
| 1 | 1 hero image | `PASS` |
| 2 | 0 | `N/A` |
| 3 | 2 circular student images | `PASS` |
| 4 | 0 | `N/A` |
| 5 | 1 callout icon image | `PASS` |
| 6 | 6 process icon images | `PASS` |
| 7 | 1 split hero image + 1 callout icon | `PASS` |

Total image-bearing nodes validated: **12/12 `PASS`**.

All 12 nodes have a visible `IMAGE` fill, non-empty image hash, opacity 1, `CROP` scale mode, clipping enabled, finite identity transform, positive dimensions and complete slide-bound containment.

## Heading validation result

| Control | Result |
|---|---:|
| Hero heading | 64 px, unchanged `PASS` |
| Non-hero headings | 6/6 at 50 px `PASS` |
| Typeface | Roboto Slab Regular 7/7 `PASS` |
| Missing fonts | 0 `PASS` |
| Controlled slide-7 line break | Preserved `PASS` |
| Visible out-of-bounds nodes | 0 `PASS` |
| Rendered visual QA | 7/7 `PASS` |

## Final classification

`PASS_DESIGN_AND_CONTENT_HANDOFF`

This result covers the specified seven-slide Figma design/content handoff. It does not imply Wix implementation, responsive validation, accessibility acceptance or public release.

## Classification

- Exact owner correction, standard update, validated Figma mutation and image QA: `AUTO_APPROVED`.
- Runtime implementation and public release: unchanged; `NO_GO`.