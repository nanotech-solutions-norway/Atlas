# ATLAS PROJECT LOG UPDATE PACK — Tjenester v4.1 Figma reconciliation — 23:05, 04.08.2026

## Session/task

Review the supplied `Tjenester-v41.pdf` and `Tjenester-v41.pptx` exports from Gamma, correct the existing Tjenester v4.1 Figma Slides file in place against the controlled Atlas measurement and typography contract, validate the seven-slide handoff, and establish the workflow as the standard process for future Atlas Figma adjustments and website-draft preparation.

## Scope

- **Gamma source:** `https://gamma.app/docs/8xdk799x5l2hm0h`
- **Figma target:** `https://www.figma.com/deck/phWiIJ6v4Cl3AoXZ5ieeG0`
- **Supplied evidence:** `Tjenester-v41.pdf` and `Tjenester-v41.pptx`
- **Slides corrected:** seven existing slides, IDs `0:20`, `0:22`, `0:23`, `0:24`, `0:25`, `0:26`, `0:27`
- **Design scope only:** no Wix mutation, publication, checkout enablement, provider activation or Managed Secure activation.
- **Release state:** unchanged at `NO_GO`.

## Issues observed

1. The imported deck used `Inter` rather than the approved `Roboto Slab` / `Roboto` typography contract.
2. CTA controls were imported as raster image-filled frames and were not editable as native controls.
3. Source line breaks, paragraph spacing and label-box configuration were dependent on the imported PowerPoint layout rather than explicitly controlled in Figma.
4. Imported list paragraphs retained Figma bullet formatting. Adding literal bullet glyphs during reconstruction temporarily produced duplicate bullet marks on three lists.
5. The first final validator used incorrect slide-7 node IDs for the image and heading wrapper, creating a false-negative geometry result even though the live design was correct.

## Root cause

The deck was a mechanically imported PPTX representation. It preserved most source geometry and images but substituted fonts, rasterised controls and retained Office list-format metadata. The initial validation-ID mismatch was an expected-baseline construction error, not a design defect.

## Corrective rules

- Inspect PDF visuals and PPTX object geometry before editing.
- Capture a complete pre-edit Figma inventory and screenshots.
- Modify existing slides in place; do not delete or rebuild them without explicit instruction.
- Use `Roboto Slab` for display/card headings and `Roboto` for body text, labels and controls.
- Preserve source-approved copy, prices, labels, line breaks and claim boundaries.
- Convert raster buttons into editable frames and editable text labels.
- Inspect paragraph list formatting before adding literal bullet characters.
- Validate the expected-record schema and exact node IDs before classifying a Figma failure.
- Keep design, runtime implementation and release status separate.

## Evidence/source

- Current explicit user instruction.
- Supplied seven-page PDF and seven-slide PPTX exports.
- Live pre-edit Figma node inventory and rendered screenshots.
- Controlled Atlas geometry and typography rules.
- Live post-edit node readback and seven rendered slide screenshots.

## Action taken

- Corrected all seven existing slides in place; no slide was deleted or recreated.
- Renamed the slide row to `Tjenester v4.1`.
- Replaced all `Inter` segments with the controlled `Roboto Slab` / `Roboto` families.
- Preserved the seven source compositions:
  1. Tjenester hero and split image.
  2. Bedrift with price and included-scope blocks.
  3. Studenter with two circular images, price and eligibility list.
  4. Privatpersoner with three service cards.
  5. Managed Secure with delivery list, price/status card and qualification callout.
  6. Six-step common working method.
  7. Closing guidance, low-risk contact callout and two CTAs.
- Applied exact source geometry, margins, card dimensions, fills, strokes, dividers, radii and controlled line breaks.
- Converted eight CTA controls to editable Figma frames and editable labels:
  - `Se alle løp`
  - `Ta kontakt`
  - `Se bedrift`
  - `Se studenter`
  - `Se privatpersoner`
  - `Se Managed Secure`
  - `Start oppstart`
  - `Les mer om løpene`
- Removed the three duplicate-bullet conditions while retaining the imported paragraph-list formatting.
- Added namespaced source/status metadata to all seven slides.
- Created `ATLAS_FIGMA_ADJUSTMENT_AND_WEBSITE_DRAFT_PREPARATION_STANDARD.md` as the controlling repeatable process.

## Validation result

| Control | Result |
|---|---:|
| Slides accessible | 7/7 `PASS` |
| Slide dimensions | 7/7 at 1920 × 1080 `PASS` |
| Expected heading per slide | 7/7 `PASS` |
| Source/status metadata | 7/7 `PASS` |
| Text nodes reviewed | 63 |
| Font-family violations | 0 `PASS` |
| Missing fonts | 0 `PASS` |
| Visible nodes outside slide bounds | 0 `PASS` |
| Raster/image-filled CTA controls remaining | 0 `PASS` |
| Editable CTA controls | 8/8 `PASS` |
| Label-box configurations | 4/4 `PASS` |
| Key geometry records | 12/12 `PASS` |
| Controlled exact-copy/line-break samples | 5/5 `PASS` |
| Duplicate bullet conditions | 0 `PASS` |
| Rendered visual QA | 7/7 `PASS` |

### Key geometry readback

- Slide 1 image: `1200, 0, 720, 1080`.
- Slide 1 heading wrapper: `104.172, 366.813, 991.656, 81.375`.
- Slide 2 price card: `85.422, 564.844, 861.562, 245.109`.
- Slide 3 price card: `93.625, 853.844, 859.062, 102.922`.
- Slide 4 cards: three source-aligned cards at `553.187/553.203 px` widths.
- Slide 5 price/status card: `1062.766, 361.359, 772.797, 405.984`.
- Slide 5 qualification callout: `104.172, 796.641, 1711.656, 104.141`.
- Slide 7 image: `1200, 0, 720, 1080`.
- Slide 7 heading wrapper: `104.172, 140.578, 991.656, 162.750`.
- Slide 7 callout: `104.172, 692.687, 991.656, 145.812`.

## Final validation classification

`PASS_DESIGN_AND_CONTENT_HANDOFF`

This result applies only to the exact Tjenester v4.1 Figma file and seven-slide scope assessed. It does not constitute Wix implementation, responsive validation, accessibility acceptance or public-release approval.

## Limitations and unresolved items

1. The Figma connector cannot authoritatively enumerate all files in project folder v4.1. The specified target file was accessible and fully validated, but project-folder-wide membership/completeness is not certified.
2. Final Wix insertion, responsive behavior, accessibility, live links, SEO metadata and runtime acceptance remain separate workstreams.
3. Managed Secure remains qualification/architecture-review only.
4. Public release remains `NO_GO` until the controlling Atlas release gates pass.

## Classification

- Exact design corrections, validator correction, standard workflow and validation evidence: `AUTO_APPROVED`.
- Project-folder completeness: provider-capability limitation.
- Wix implementation and public release: unchanged; `NO_GO`.