# ATLAS PROJECT LOG UPDATE PACK — Home v4.1 Figma reconciliation — 15:56, 03.08.2026

## Session/task

Review the Atlas AI Home v4.1 Gamma exports and the existing Figma Slides file, correct the Figma file in place against the approved Atlas measurement and typography contract, and validate the complete seven-slide design handoff.

## Scope

- **Figma target:** `https://www.figma.com/slides/i5H1gVE9PEiH7cTcS7wGBe/Home-v41`
- **Gamma source:** `https://gamma.app/docs/91svnxefumo4k2p`
- **Supplied exports reviewed:** `Home-v41.pdf` and `Home-v41.pptx`
- **Design state only:** no Wix mutation, publication, purchase enablement, provider activation, production entitlement or Managed Secure activation.
- **Release state:** `NO_GO`; this work does not alter release locks.

## Issue or mistake observed

1. The imported Figma deck used **Inter** instead of the controlled **Roboto Slab / Roboto** typography contract.
2. Slide 3 inherited the tall Gamma-page geometry directly: the second audience row extended beyond the 1920×1080 slide, with objects positioned below y=1,800. The intro wrapper was also 1,807.656 px wide rather than the required 1,712 px content width.
3. Source CTA controls were imported as raster image fills rather than editable button frames and labels.
4. The Gamma PDF contains variable-height webpage sections, while the Figma handoff uses fixed 1920×1080 slides. Blind coordinate scaling therefore produced clipping and unusable image crops in tall sections.
5. The available Figma runtime does not support `saveVersionHistoryAsync`, so an immutable connector-created version-history checkpoint could not be created.

## Root cause

The PowerPoint export was scaled mechanically into a fixed 16:9 Figma Slides canvas without normalising variable-height webpage sections to the Atlas slide contract. The import also preserved rasterised controls and substituted fonts.

## Corrective rule

For Gamma-to-Figma Atlas website-section handoffs:

- keep every slide at **1920×1080**;
- use **104 px side margins** and a **1,712 px principal content width**;
- use **Roboto Slab** for display and card headings and **Roboto** for body copy and controls;
- preserve approved copy, source order, labels and claim boundaries exactly;
- reconstruct CTA controls as editable frames and text rather than retaining raster button images;
- when a Gamma webpage section is taller than 16:9, adapt its internal layout to the fixed canvas without omitting content, shrinking text below the controlled hierarchy or leaving nodes outside the slide;
- capture a full pre-edit inventory and perform complete post-edit readback; when Figma version-history creation is unavailable, disclose the limitation and retain source exports as recovery evidence.

## Evidence/source

- Current user instruction and supplied `Home-v41.pdf` / `Home-v41.pptx` exports.
- Live Figma pre-edit inventory of all seven slides and all existing layers.
- Approved Atlas Figma geometry and typography records: 1920×1080, 104 px margins, 1,712 px content width, Roboto Slab / Roboto.
- Final live Figma node readback and seven rendered slide screenshots.

## Action taken

- Corrected all seven existing slides in place; no slide was deleted or recreated.
- Renamed the slide row to `Home v4.1` and wrote namespaced Atlas source/status metadata to every slide.
- Replaced Inter across the deck with Roboto Slab / Roboto, including italic and semibold styles where required.
- Preserved the supplied Norwegian copy and explicit line breaks, including the Home AI/KI explanation and Managed Secure qualification boundary.
- Converted all CTA image fills to editable Figma button frames with editable labels.
- Rebuilt slide 3 as a complete 2×2 horizontal audience-card layout so all four audiences, images, descriptions and CTAs fit inside 1920×1080 without subject-distorting panoramic crops.
- Retained the source image assets while resetting imported crop transforms where necessary.
- Rebuilt the slide 5 security cards as editable bordered cards with Atlas accent stripes and retained the fixed split-image composition.
- Preserved public pricing and the phrase `Separat aktivering`; no purchase or activation state was changed.

## Validation result

| Check | Result |
|---|---:|
| Slides accessible | 7/7 `PASS` |
| Canvas size | 7/7 at 1920×1080 `PASS` |
| Expected heading per slide | 7/7 `PASS` |
| Font-family violations | 0 `PASS` |
| Missing fonts | 0 `PASS` |
| Visible node bounds outside slide | 0 `PASS` |
| Raster/image-filled CTA frames remaining | 0 `PASS` |
| Editable CTA labels present | 15/15 `PASS` |
| Required exact-copy sample set | 11/11 `PASS` |
| Slide source/status metadata | 7/7 `PASS` |
| Rendered visual QA | 7/7 `PASS` |

**Validation classification:** `PASS_DESIGN_AND_CONTENT_HANDOFF` for the exact Figma file and seven-slide scope assessed. This is not Wix implementation or release approval.

## Unresolved items / limitations

1. The Figma connector does not provide an authoritative project-folder inventory, so membership/completeness of every file in project folder v4.1 cannot be certified through this execution surface. The supplied target file was accessible and fully validated.
2. `saveVersionHistoryAsync` is unsupported in the current Figma runtime. Recovery evidence consists of the supplied PDF/PPTX, the full pre-edit node inventory and the non-slide-destructive mutation record.
3. Wix Studio insertion, responsive behaviour, accessibility, link destinations, SEO metadata, performance and runtime acceptance remain separate workstreams.
4. Public release remains `NO_GO` until the controlling Atlas release gates pass.

## Classification

- **Validated design corrections, copy preservation, geometry correction, editable-control reconstruction and QA results:** `AUTO_APPROVED`.
- **Figma project-folder completeness and immutable version-history availability:** `PENDING_REVIEW` / provider-capability limitation.
- **Wix implementation and public release:** unchanged; `NO_GO`.
