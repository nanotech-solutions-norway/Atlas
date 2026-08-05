# ATLAS PROJECT LOG UPDATE PACK — Privat asset transfer and duplicate-file correction — 00:36, 06.08.2026

## Session/task

Correct the Privat v4.1 Figma Slides-to-Design transfer so that available photographs and icons are included rather than replaced by placeholders, determine why two identical Design files appeared in the Figma project, and establish the corrected process for future Atlas transfers.

## Owner correction

“Include icons and images (if available) when converting / pasting into the figma design file from figma presentation file. There's 2 identical design files located in the figma project folder, why?”

## Issue observed

1. The initial Privat v4.1 Design transfer used placeholders for available source photographs and icons.
2. The transfer was incorrectly classified as passed under a placeholder scope despite the source assets being accessible from the validated Slides/PPTX evidence.
3. A second same-name Design file was created because the workflow called `create_new_file` without first resolving and reusing an existing canonical Design target. The Figma connector cannot authoritatively enumerate the complete contents of a project folder, so it did not detect the same-name file before creation.

## Root cause

- The previous operational rule allowed user-approved placeholders as an alternative to embedded source assets. The owner has now explicitly corrected this: available assets must be transferred.
- The file-creation workflow treated a transfer retry as a new-file workflow instead of a correction within the existing target file.
- Project-folder enumeration is unavailable through the current Figma connector, and the workflow did not compensate by requiring an explicit target URL or recorded canonical file key.

## Corrective rule

- Transfer all available source photographs, illustrations and icons from the validated Slides/PPTX/Gamma evidence.
- Preserve source dimensions, placement, crop intent and mask geometry.
- Use `FILL` for photographic regions and `FIT` for line/pictographic icons unless the approved source shows otherwise.
- Use placeholders only when the asset is unavailable, a documented provider limitation prevents transfer, or the owner explicitly requests placeholders for that task.
- Do not pass a transfer while an available source asset remains a placeholder.
- Resolve and reuse the explicit or recorded canonical Design file before calling `create_new_file`.
- If project enumeration is unavailable and no target can be resolved, ask the owner rather than creating another same-name file.
- Retries must remain in the same Design file.

## Evidence/source

- Source Figma Slides file: `w3sC60Cm6Y4SVbexEk76J8`.
- Canonical Figma Design file: `UEspHwA0ynegp8f8aizLAR`.
- Gamma source: `u7krag2wz6gcus7`.
- Supplied `Privat-v41.pptx` and `Privat-v41.pdf` exports.
- Live source-asset inventory: 13 image-bearing nodes.
- Live post-transfer readback and rendered full-group screenshot.

## Action taken

- Replaced every available source-asset placeholder in the canonical Privat v4.1 Design file.
- Transferred two source photographs using `FILL`:
  - hero photograph;
  - consultation/qualified-professional photograph.
- Transferred six feature icons using `FIT`.
- Transferred four privacy icons using `FIT`.
- Transferred the information icon using `FIT`.
- Removed all source-asset placeholder labels.
- Preserved the five 1920 × 1080 design frames, source order, 120 px vertical gaps and 1920 × 5880 group geometry.
- Added the separate Atlas Figma asset-transfer and duplicate-prevention standard.

## Validation result

| Control | Result |
|---|---:|
| Design frames | 5/5 PASS |
| Source assets transferred | 13/13 PASS |
| Photographs | 2/2 FILL PASS |
| Feature icons | 6/6 FIT PASS |
| Privacy icons | 4/4 FIT PASS |
| Information icons | 1/1 FIT PASS |
| Residual source-asset placeholders | 0 PASS |
| Image-fill/hash findings | 0 PASS |
| Asset bounds findings | 0 PASS |
| Frame spacing | 4/4 at 120 px PASS |
| Group dimensions | 1920 × 5880 PASS |
| Rendered visual QA | PASS |

**Final classification:** `PASS_DESIGN_TRANSFER_WITH_SOURCE_ASSETS`.

## Duplicate-file finding

The duplicate was created by the transfer workflow, not automatically by Figma. A new Design file was created without first resolving the already existing target. The current connector does not expose an authoritative project listing or supported delete/archive action, so the redundant file cannot be safely identified and removed through this execution surface without its exact URL/file key. The canonical file for continued work is `UEspHwA0ynegp8f8aizLAR`.

## Unresolved item

The redundant Design file must be archived or deleted manually in Figma, or its exact URL must be supplied for a read-only comparison before the owner removes it.

## Classification

- Exact owner correction and validated asset-transfer fix: `AUTO_APPROVED`.
- Duplicate-prevention workflow improvement: `AUTO_APPROVED`.
- Public release/Wix implementation: unchanged; `NO_GO`.
