# ATLAS PROJECT LOG UPDATE PACK — Business v4.1 Figma reconciliation — 12:10, 05.08.2026

## Session/task

Review the supplied `Business-v41.pdf` and `Business-v41.pptx` exports from Gamma document `5uondkr0kwxcest`, reconcile the existing Business v4.1 Figma Slides file against the canonical Atlas Home/Tjenester adjustment standard, modify the file in place and validate the complete six-slide handoff.

## Scope

- **Figma target:** `https://www.figma.com/slides/irLsoGqsIKr22nbKe1kWMq/Business-v41`
- **Gamma source:** `https://gamma.app/docs/5uondkr0kwxcest`
- **Supplied evidence:** `Business-v41.pdf`, `Business-v41.pptx`
- **Slides:** 6
- **Design scope only:** no Wix mutation, publication, checkout activation, provider activation or release-state change.

## Issue observed

1. The imported file used Inter instead of the canonical Roboto Slab / Roboto typography contract.
2. Principal non-hero headings varied between approximately 42.67 px, 53.33 px and 64 px rather than the canonical 50 px.
3. Deliberate line breaks from the Gamma/PDF source were not consistently preserved, including the slide-2 heading.
4. CTA controls on slides 1 and 6 were raster image fills rather than editable Figma frames and labels.
5. Multiple content cards and callouts retained mechanically scaled decorative radii between approximately 9 px and 43.75 px instead of the canonical 6 px card/callout radius.
6. Pricing-card geometry used non-canonical outer margins and approximately 26 px padding rather than the controlled 104 px page margin, 32 px grid and 32 px card-padding baseline.
7. The slide-3 and slide-5 information icons required aspect-preserving FIT treatment after callout normalization.
8. The Figma section name and Atlas source/status metadata were absent.

## Root cause

The Gamma/PPTX export had been imported by mechanical scaling into a 1920 × 1080 Slides canvas. This retained source imagery and broad structure but also retained substituted fonts, raster controls, scaled corner values, inconsistent heading hierarchy and non-canonical card geometry.

## Corrective rule applied

- Hero principal heading retains its explicitly approved 64 px size.
- Non-hero principal/major headings use Roboto Slab Regular at 50 px with 118% line height.
- Roboto Slab is used for card headings; Roboto is used for body copy and controls.
- Standard cards, pricing/status panels and callouts use 6 px corner radius.
- CTA controls use 4 px corner radius and 2 px border.
- Standard full-width content uses 104 px side margins, 1,712 px width, 32 px grid spacing and 32 px card padding.
- Source images and crop intent are preserved; small information icons use FIT.
- Raster CTA controls are rebuilt as editable Figma frames and labels.
- Deliberate source line breaks and approved Norwegian copy are preserved.

## Action taken

- Corrected all six existing slides in place; no slide was deleted or recreated.
- Renamed the slide row to `Business v4.1`.
- Replaced all Inter typography with Roboto Slab / Roboto.
- Preserved the approved hero heading at 64 px.
- Set all non-hero principal/major headings to 50 px with 118% line height.
- Rebuilt four CTA controls as editable frames with editable labels:
  - Start oppstart
  - Se priser
  - Start oppstart
  - Kontakt oss
- Reworked slide 2 into four 131 px cards with 32 px horizontal/top text padding, 20 px row gaps and 6 px radii while retaining the timeline treatment.
- Preserved all six working-area images on slide 3 and corrected the bottom callout to 6 px radius and controlled internal geometry.
- Rebuilt slides 4 and 5 on the 104 / 1,712 / 32 geometry contract with 840 px cards, 32 px gaps, 32 px internal padding and 6 px radii.
- Corrected slide 5’s public-price reference callout and hid one empty imported artifact rectangle.
- Reflowed slide 6 after reducing both major headings to 50 px and rebuilt its CTA controls.
- Added Atlas Gamma-source and `MEASUREMENT_CORRECTED` metadata to every slide.

## Validation result

| Control | Result |
|---|---:|
| Slides accessible and ordered | 6/6 `PASS` |
| Canvas size | 6/6 at 1920 × 1080 `PASS` |
| Canonical heading checks | 7/7 `PASS` |
| Font-family violations | 0 `PASS` |
| Missing fonts | 0 `PASS` |
| Visible nodes outside slide bounds | 0 `PASS` |
| Text-fit / clipping findings | 0 `PASS` |
| Card/callout/CTA/background radius findings | 0 `PASS` |
| Image-bearing nodes | 10/10 `PASS` |
| Raster/image-filled CTA controls remaining | 0 `PASS` |
| Editable CTA controls | 4/4 `PASS` |
| Card-padding checks | 11/11 `PASS` |
| Principal margin/width checks | 6/6 `PASS` |
| Required exact-copy samples | 3/3 `PASS` |
| Atlas source/status metadata | 6/6 `PASS` |
| Rendered visual QA | 6/6 `PASS` |

## Final classification

`PASS_DESIGN_AND_CONTENT_HANDOFF`

This classification applies to the exact six-slide Business v4.1 Figma Slides file assessed. It does not imply Wix implementation, responsive validation, accessibility acceptance or public release.

## Unresolved items / limitations

1. The Figma connector cannot authoritatively enumerate every file in project folder `634220422`; folder-wide membership or completeness is not certified.
2. The Gamma source was used as evidence through the supplied PDF/PPTX exports; the Gamma document itself was not mutated.
3. Wix implementation and public release remain separate workstreams and remain `NO_GO` until their controlling gates pass.

## Classification

- Exact design corrections, validated geometry/typography fixes and quality-control evidence: `AUTO_APPROVED`.
- Project-folder completeness limitation: provider capability limitation.
- Wix implementation/public release: unchanged; `NO_GO`.
