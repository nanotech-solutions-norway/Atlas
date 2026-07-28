# ATLAS PROJECT LOG UPDATE PACK — Figma Contact and FAQ in Atlas AI v3

**Timestamp:** 22:29, 28.07.2026 Europe/Oslo  
**Project:** Atlas Website / Atlas AI  
**Session/task:** Recreate the current `Generell kontakt v1.1` and `FAQ v1.1` Gamma drafts as persistent, editable Figma Slides files inside the established `Atlas AI v3` Figma project.

## Issue or mistake observed

1. Earlier attempts produced transient previews, files in the wrong Figma plan, empty files, or completion statements without durable file/folder evidence.
2. The exact Figma project target was not initially resolved. The approved project is `Atlas AI v3`, project ID `626439448`.
3. Starter/View plans exposed read and generation quotas that blocked reliable recreation and validation.
4. A first geometry audit identified text nodes that required explicit auto-height normalization after width assignment.
5. Figma Slides normalizes visible slide captions to numeric labels in connector readback even after custom-name mutations.

## Root cause

- Team-plan names were similar and were previously selected without binding the exact Pro plan key and project ID.
- Preview generation and persistent file creation were conflated.
- Earlier validation relied too heavily on successful tool execution rather than persistent URL, complete slide inventory, geometry checks and visual inspection.
- Figma text sizing order requires width assignment followed by `textAutoResize='HEIGHT'` to avoid false clipping risk.

## Corrective rule

1. Resolve and record the exact Figma `planKey` and `projectId` before creating Atlas Slides files.
2. Use the Full/Pro plan and create files directly in the approved project.
3. Treat a deck as completed only after a persistent Figma URL, expected slide count, source traceability and final readback exist.
4. Use append-first node construction in Figma Slides and normalize text auto-height after width assignment.
5. Validate slide count, order, 1920×1080 geometry, out-of-bounds nodes, parent overflow, duplicates and representative screenshots before reporting PASS.
6. Preserve Figma/Gamma as design evidence only; GitHub remains canonical and Drive the controlled mirror.

## Evidence/source

- Figma project: `Atlas AI v3`, project ID `626439448`.
- Pro plan: `Ruben A. Meyer's team`, key `team::1466418306299765062`.
- Gamma source — Generell kontakt v1.1: `g_a0mswzsmjo8r7hz`, `https://gamma.app/docs/Generell-kontakt-v11-u79q5mc86i1kudh`.
- Gamma source — FAQ v1.1: `g_rody04q71isib3q`, `https://gamma.app/docs/FAQ-v11-ptr7hc9q7c59dt1`.
- Figma — Generell kontakt: `https://www.figma.com/slides/6UODS1tY13e5kO2UnpyGKr`.
- Figma — FAQ: `https://www.figma.com/slides/By3uvqtSoHpP7ioqasm4OO`.
- Approved Atlas measurement profile: 1920×1080, 104 px side margins, 1712 px content width, Roboto/Roboto Slab hierarchy, 32 px gaps/padding, 78 px CTAs, approved borders/radii and warning treatment.

## Action taken

### Generell kontakt

- Created a persistent Figma Slides file directly in `Atlas AI v3`.
- Recreated six Gamma sections as six editable slides.
- Corrected the contradiction between required name/email fields and a blanket ban on personal information.
- Limited prohibited data to sensitive, confidential, restricted, security-critical and unnecessary personal information.
- Removed unsupported absolute deletion/confidentiality wording.
- Presented receipt, routing and status behaviour as implementation requirements rather than verified runtime facts.
- Added Gamma source traceability to every slide.

### FAQ

- Created a persistent Figma Slides file directly in `Atlas AI v3`.
- Recreated eleven Gamma sections as eleven editable slides.
- Preserved current Atlas claims, low-risk form boundary, Managed Secure qualification-only status, student age controls, responsible-use limits and release qualifications.
- Corrected the remaining slide-6 warning-panel overflow before final validation.
- Added Gamma source traceability to every slide.

## Validation performed

### Generell kontakt

- Slide count: **6** — PASS.
- Native canvas: **1920×1080** — PASS.
- Out-of-bounds objects: **0**.
- Parent/text overflow: **0**.
- Accidental duplicate slides: **0**.
- Editable text, shapes, panels, labels and cards retained.
- Representative title/content/final slides visually inspected.

### FAQ

- Slide count: **11** — PASS.
- Native canvas: **1920×1080** — PASS.
- Out-of-bounds objects: **0**.
- Parent/text overflow after correction: **0**.
- Accidental duplicate slides: **0**.
- Editable text, shapes, panels, labels and cards retained.
- Representative data/Managed Secure and closing/content slides visually inspected.

## Unresolved items

1. Figma’s connector readback continues to show numeric native slide captions even after custom naming; section labels and per-slide Gamma source metadata remain intact.
2. CTA hyperlinks, Wix Studio binding, responsive web implementation, accessibility testing, legal/privacy review and public release validation remain separate workstreams.
3. No public availability, checkout, production or Managed Secure activation is approved.

## Classification

- **AUTO_APPROVED:** Exact non-sensitive design corrections, persistent project placement, source traceability, geometry fixes, validation method and verified PASS results.
- **PENDING_REVIEW:** Public copy approval, Wix implementation, accessibility, legal/privacy/provider validation and release approval.

## Release state

- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
- **NO_GO**
