# ATLAS FIGMA DESIGN ASSET-TRANSFER AND DUPLICATE-PREVENTION STANDARD

**Approved:** 00:36, 06.08.2026 Europe/Oslo  
**Scope:** Atlas AI Figma Slides-to-Figma Design conversion and paste workflows  
**Classification:** `AUTO_APPROVED` — exact owner correction and non-sensitive quality-control rule  
**Precedence:** This standard supersedes any earlier Atlas instruction that permits replacing an available source image or icon with a placeholder during a Slides-to-Design transfer.

## 1. Source-asset transfer rule

When converting or pasting an Atlas AI Figma Slides presentation into a Figma Design file:

1. Transfer every source photograph, illustration, icon and other image-bearing asset that is available in the validated Figma Slides file, Gamma source, PDF export or PPTX export.
2. Prefer the exact embedded asset from the validated Figma Slides/PPTX source. Gamma and PDF are supporting visual evidence when needed.
3. Preserve the source asset's frame dimensions, position, crop intent, opacity and mask geometry.
4. Use `FILL`/approved crop behaviour for photographic regions and `FIT` for pictographic or line icons unless the approved source establishes a different treatment.
5. Placeholders are permitted only when:
   - the asset is genuinely unavailable from all supplied and connected sources;
   - the provider/runtime cannot transfer the asset after a documented recovery attempt; or
   - the owner explicitly requests placeholders for that task.
6. A transfer must not receive a pass classification while an available source asset remains represented by a placeholder.
7. Validation must inventory the expected source assets and prove:
   - exact asset count;
   - valid `IMAGE` fills and non-empty image hashes;
   - correct scale mode;
   - correct dimensions and placement;
   - no residual placeholder labels or frames;
   - no visible out-of-bounds asset nodes;
   - rendered page-by-page visual acceptance.

## 2. Duplicate-file prevention rule

Before creating a new Figma Design file:

1. Resolve and reuse the explicit target Design URL/file key supplied by the owner, or the latest recorded canonical Design file key for the page.
2. Search the Atlas project records for an existing file reference before calling `create_new_file`.
3. When the Figma connector cannot authoritatively enumerate a project folder and no explicit target file is available, ask the owner which existing file should be used rather than creating another same-name file.
4. Retries and corrections must remain in the same Design file. Do not create a replacement file merely because an earlier capture or transfer is incomplete.
5. Create a new Design file only when the owner explicitly requests a new file or when no existing target can be resolved after the required checks.
6. Record the canonical Design file key and any known redundant file keys in the project log.
7. The Figma connector currently does not expose a supported delete/archive action for project files. Redundant files must therefore be archived or deleted manually in Figma unless a supported action becomes available.

## 3. Privat v4.1 validated precedent

- Canonical Design file: `UEspHwA0ynegp8f8aizLAR`.
- Source Slides file: `w3sC60Cm6Y4SVbexEk76J8`.
- Source assets transferred and validated: `13/13`.
  - photographs: `2/2`, `FILL`;
  - feature icons: `6/6`, `FIT`;
  - privacy icons: `4/4`, `FIT`;
  - information icon: `1/1`, `FIT`.
- Residual source-asset placeholders: `0`.
- Asset bounds findings: `0`.
- Transfer classification: `PASS_DESIGN_TRANSFER_WITH_SOURCE_ASSETS`.

## 4. Release boundary

This standard controls design-file preparation only. It does not implement or publish Wix content, enable checkout or payment, activate providers, or change the Atlas public-release state. Public release remains `NO_GO` until the controlling runtime gates pass.
