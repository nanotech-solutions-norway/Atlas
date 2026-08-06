# ATLAS PROJECT LOG UPDATE PACK — Privat v4.1 source-parity correction — 01:49, 07.08.2026

**Classification:** AUTO_APPROVED  
**Release effect:** None. `NO_GO`, `publicAllowed=false`, `purchaseAllowed=false`, and `releaseApproved=false` remain unchanged.

## Session/task

Correct the canonical Figma Design `UEspHwA0ynegp8f8aizLAR` against the validated Figma Slides source `VRfwAuekUaxqm4YqvSLvCt` after the strict comparison merged in PR #55 established that the files were not identical.

## Issue observed

The pre-correction Design was a valid editable handoff but differed materially from the Slides source in geometry, typography, text wrapping/list representation, CTA and label properties, Pages 4–5 vertical layout, source image crop modes and several image assets.

## Root cause

The Design had been reconstructed as an editable Atlas-standard handoff rather than cloned from the Slides source. Several values were normalized to the Atlas design baseline instead of preserving the current Slides-source values. In addition, two previously blank-render icons had been regenerated, and the Design contains non-source photograph assets because the current Figma connector/runtime does not provide a supported direct binary bridge for source-only image hashes between the Slides and Design files.

## Corrective rule

- When the operator requests correction to the validated Slides source, source geometry, copy, typography, list representation, fills, strokes, radii, image placement and crop mode take precedence over the normalized handoff baseline.
- Preserve editability while matching the visible Slides source.
- Do not claim strict identity when source image bytes/hashes cannot be transferred or when the Design editor quantizes imported sub-pixel/property values differently from Slides.
- Report handoff validity, visual parity and strict identity separately.

## Evidence/source

- Canonical Design: `https://www.figma.com/design/UEspHwA0ynegp8f8aizLAR`
- Validated Slides source: `https://www.figma.com/slides/VRfwAuekUaxqm4YqvSLvCt`
- Gamma source: `https://gamma.app/docs/u7krag2wz6gcus7`
- Merged PR #55 and merge commit `d0502c3fb1e9e47cfec1a57945aad87f3a5cd7b6`
- Source PPTX/PDF evidence: `Privat-v41.pptx` and `Privat-v41.pdf`
- Fresh source-property readback from all five Slides pages and fresh rendered screenshots of all five corrected Design frames.

## Action taken

### Pages 1–3

- Repositioned and resized all visible text and controls to the current Slides-source measurements.
- Restored source text-frame behavior and source line-break representation.
- Restored Page 2 item headings to `32 px` and body/intro copy to `25.333333969 px`.
- Restored source CTA geometry and the secondary CTA `1.5 px` stroke.
- Changed both photographs from `FILL` to source `CROP` mode with the source identity transform.
- Restored the six Page 2 icons to source positions/dimensions and `FIT` mode.

### Page 4

- Rebuilt the layout to the source vertical positions rather than the previous normalized Design positions.
- Restored the Everyday Basic and Family card/label geometry, colors, radii and stroke weights.
- Restored source typography and precise source positions for headings, prices and suffixes.
- Replaced literal bullet glyph implementation with Figma unordered-list formatting matching the Slides source.

### Page 5

- Rebuilt the privacy layout to source geometry.
- Replaced four rectangular icon-circle approximations with actual editable Figma ellipse nodes.
- Restored source card/callout geometry, source colors, typography and icon placement.
- Restored the information icon to the source dimensions and `FIT` treatment.

### Precision pass

A second pass applied the full-precision Slides measurements and source color values available through the Plugin API. The Design editor stores some of those values with slightly different quantization than the Slides editor; for example a source `367.6405029296875` position is read back from Design as `367.640625`. This is a provider/editor representation difference, not an unresolved layout decision.

## Validation result

Deterministic Design validation after correction: **PASS** for the corrected editable Design scope.

- Frames: `5/5`, each `1920 × 1080`.
- Group: `1920 × 5880`, Figma `GROUP`.
- Frame positions: `0`, `1200`, `2400`, `3600`, `4800`.
- Missing fonts: `0`.
- Text truncation findings: `0`.
- Visible text out-of-bounds findings: `0`.
- Page 4 Basic and Family lists: source-style `UNORDERED` formatting confirmed.
- Image-bearing nodes: `13`.
- Exact source image hashes: `8/13`.
- Regenerated but visually source-equivalent icons: `3/13` — Notes, Health and information icon.
- Non-source photographs remaining: `2/13` — hero photograph `3:3` and consultation photograph `3:39`.
- Source crop treatment for both photographs: `CROP` restored.
- Final rendered visual comparison:
  - Page 2: visual parity PASS.
  - Page 4: visual parity PASS.
  - Page 5: visual parity PASS.
  - Page 1: copy/layout/control parity PASS; exact photograph parity FAIL.
  - Page 3: copy/layout parity PASS; exact photograph parity FAIL.

## Rendered identity

Strict PNG byte identity remains `0/5`. The corrected Design render hashes are:

- Page 1: `2b190c80`
- Page 2: `f57826c0`
- Page 3: `8b8912d6`
- Page 4: `ecf7d682`
- Page 5: `9cc0058f`

Validated Slides hashes remain:

- Page 1: `0ba81933`
- Page 2: `518ba7df`
- Page 3: `94676ebd`
- Page 4: `f1c3564a`
- Page 5: `27ea1e92`

Page 4 is visually indistinguishable in rendered review but still differs at byte level because the Design editor quantizes certain source values differently from the Slides editor and the files have different editable node structures.

## Figma metadata

All five canonical Design frames now record:

- `status=DESIGN_SOURCE_PARITY_CORRECTED`
- `validation=PASS_LAYOUT_CONTENT_CONTROL_VISUAL_PARITY_WITH_ASSET_LIMITATION`
- `identityValidation=FAIL_NOT_IDENTICAL`
- `assetParity=8_OF_13_SOURCE_HASH_MATCH__3_REGENERATED_ICON_EQUIVALENTS__2_SOURCE_PHOTOGRAPHS_NOT_EXACT`
- `visualParity=PAGES_2_4_5_PASS__PAGES_1_3_SOURCE_PHOTO_MISMATCH`

## Unresolved items

- Exact source photograph bytes for Page 1 and Page 3 are not currently transferable into the Design through the available Figma connector/runtime. The source images are present in the Slides/Gamma evidence, but source-only image hashes are not resolvable from the Design file and the runtime does not support direct `createImageAsync` or a cross-file image-hash bridge.
- The regenerated Notes, Health and information icons remain visually equivalent but have different image hashes from the Slides source.
- Strict layer/property/render identity is therefore not achieved and must remain `FAIL_NOT_IDENTICAL`.
- The redundant Design `LSIuAlOSCIRPPfeK5pLA7L` remains a manual archive/delete task.
- Wix implementation, responsive/runtime validation, accessibility acceptance, checkout/production availability and public release remain outside this task.

## State boundary

- Corrected editable Figma Design: **PASS** for layout/content/control parity with the stated asset limitation.
- Strict Slides-to-Design identity: **FAIL_NOT_IDENTICAL**.
- Public release: **NO_GO**.
