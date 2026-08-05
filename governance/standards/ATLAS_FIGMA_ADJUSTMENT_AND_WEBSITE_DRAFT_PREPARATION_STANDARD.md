# ATLAS FIGMA ADJUSTMENT AND WEBSITE-DRAFT PREPARATION STANDARD

**Approved:** 23:05, 04.08.2026 Europe/Oslo  
**Updated:** 11:54, 05.08.2026 Europe/Oslo  
**Scope:** Atlas AI website drafts and Gamma/PDF/PPTX-to-Figma adjustments  
**Classification:** `CANONICAL`  
**Release effect:** None; Wix implementation and public release remain separate and `NO_GO` until their controlling gates pass.

## 1. Purpose

This standard governs future Atlas AI Figma adjustments and website-draft preparation. It converts the validated Home v4.1 and Tjenester v4.1 workflows into one repeatable, evidence-based process for correcting Figma Slides and preparing subsequent Figma Design handoffs.

## 2. Source and authority order

Apply the Atlas source-authority hierarchy. For design work, use the following operational sequence:

1. explicit current user instruction or correction;
2. approved/canonical Atlas governance and design rules;
3. current live Figma implementation evidence;
4. supplied Gamma source plus its PDF and PPTX exports;
5. controlled Drive reports and prior validated handoffs;
6. inference, clearly labelled.

Do not silently merge conflicting geometry, copy, pricing, claim boundaries or status wording. Record the contradiction and prefer the latest higher-authority approved source.

## 3. Mandatory pre-edit preparation

Before any substantive mutation:

1. Activate Atlas project memory and read the approved/canonical learning, decision, error, validation, source-authority and session-close records.
2. Resolve the exact target Figma file key and all known slide IDs.
3. Record the Gamma source URL and the supplied PDF/PPTX filenames.
4. Inspect the PDF visually, page by page, including images, box relationships, spacing and intended line breaks.
5. Inspect the PPTX programmatically for:
   - canvas dimensions;
   - shape positions and dimensions;
   - text strings and paragraph breaks;
   - fonts, sizes and colors;
   - fills, strokes, corner radii and image crops.
6. Capture a complete live Figma pre-edit inventory containing slide IDs, child counts, text digests, geometry, fills, strokes, fonts and source/status metadata.
7. Render representative or all slides before editing.
8. Create a recoverable version or duplicate when the provider supports it. If unavailable, disclose the limitation and preserve the exports plus pre-edit inventory as recovery evidence.

The Figma connector cannot authoritatively enumerate all files in a project folder. Project-folder completeness must not be claimed solely from connector access to a known file key.

## 4. Controlled mutation rules

1. Modify existing slides in place. Do not delete or recreate slides unless explicitly instructed.
2. Work in incremental batches and validate each batch before continuing.
3. Return and retain every created or mutated node ID.
4. Preserve approved copy, terminology, labels, prices, claim boundaries and source order exactly.
5. Preserve deliberate source line breaks. Do not rely on incidental automatic wrapping where the source establishes a controlled break.
6. Use the approved Atlas typography contract:
   - `Roboto Slab` for display and card headings;
   - `Roboto` for body copy, labels, controls and supporting text;
   - verified italic or semibold variants only where required.
7. Use a 1920 × 1080 slide canvas. Apply the controlled 104 px principal side margin and 1,712 px principal content width where the section uses the standard full-width contract. Use a 32 px grid/card rhythm and 32 px card padding as the global default; preserve only documented source-specific exceptions for intentional split layouts, image bleeds and specialist cards.
8. Reconstruct rasterised controls as editable Figma frames and editable text labels.
9. Preserve source images and crop intent in Figma Slides. For a Figma Design transfer, use embedded images or explicit user-approved editable placeholders; report which scope is active.
10. Preserve exact box configuration, including dimensions, padding, alignment, fill, stroke, stroke weight, corner radius, dividers and callout treatment.
11. Keep public-price copy separate from purchase, activation and release status. Managed Secure remains qualification/architecture-review only unless separately approved.
12. Do not mutate Wix, publish, enable checkout or change release status as part of a Figma design correction.

## 5. Typography and list-format control

1. Load every current and target font before changing text.
2. Validate font-family replacement across styled text segments, not only the top-level text property.
3. **Default page-heading rule:** retain the explicitly approved hero heading size for the hero section; set every non-hero page heading to `Roboto Slab Regular, 50 px`, with `118%` line height, unless a later explicit user instruction overrides it. This rule applies to the principal page/section heading only, not card headings, supporting headings, labels or CTA text.
4. Inspect imported paragraph-list formatting before adding literal bullet glyphs. Use either Figma list formatting or literal bullets, never both.
5. Validate text frames for clipping and visible overflow after font replacement.
6. Preserve paragraph spacing and intentional blank-line separation where the source uses distinct paragraphs.

## 6. Corner-radius taxonomy

Use these values unless a later explicit owner instruction or an approved source visual establishes a documented exception:

- standard content cards and boxes: `6 px` on all corners;
- highlighted pricing/status panels: `6 px` on all corners;
- neutral, warning and informational callouts: `6 px` on all corners;
- category/section label outlines: `4 px` on all corners;
- primary and secondary CTA buttons: `4 px` on all corners;
- full-slide backgrounds and edge-to-edge image frames: `0 px`;
- circular or intentionally shaped image masks: preserve the approved crop geometry.

Do not retain decorative `18–34 px` radii or mechanically scaled values such as approximately `31.694 px` or `40.517 px` merely because they originated from a Gamma/PPTX export. Any radius above `6 px` requires explicit evidence and documented approval.

## 7. Required validation suite

After mutation, perform a separate readback and rendered QA. At minimum validate:

- exact slide count and order;
- 1920 × 1080 dimensions for every slide;
- expected heading on every slide;
- hero heading retains its approved size and every non-hero principal page heading is exactly 50 px unless explicitly overridden;
- exact controlled line-break samples;
- required source-copy samples;
- principal margins and content widths;
- key frame, card, image and callout geometry;
- box dimensions and internal text margins/padding against the approved baseline;
- all four individual corner values for every box-like node;
- cards/callouts/highlighted panels at 6 px, labels/CTAs at 4 px and backgrounds at 0 px;
- CTA count, labels, dimensions, fills, borders and editability;
- absence of raster/image-filled CTA controls;
- image-fill or approved-placeholder scope;
- every image-bearing node on every slide, including valid `IMAGE` fill, non-empty image hash, visible opacity, approved scale/crop mode, clipping, finite transform, positive dimensions, slide-bound containment and rendered focal-subject/crop inspection;
- font-family violations and missing fonts;
- visible nodes outside the slide bounds;
- text clipping or range-fit warnings;
- duplicate bullet glyphs;
- Atlas source and status metadata;
- page-by-page rendered visual inspection.

A validator must prove its expected baseline before classifying a design failure. When a check fails, inspect the node ID, coordinate system and expected-record construction before mutating the design.

## 8. Figma Design handoff

When slides are copied to a Figma Design file:

1. create one 1920 × 1080 frame per slide;
2. preserve source order;
3. align frames on one horizontal axis;
4. use a uniform 120 px vertical gap unless another approved spacing is specified;
5. group the complete sequence and name the page/group consistently;
6. preserve editable text, controls, cards and placeholders where required;
7. validate group-relative positions by subtracting the group origin because children of a Figma `GROUP` retain page-relative coordinates;
8. export and revalidate the resulting `.fig` package when portability is required.

## 9. Evidence and write-back

At completion:

1. prepare an Atlas project-log update pack with timestamp, issue, root cause, corrective rule, evidence, action, validation and unresolved items;
2. commit the standard and task-specific log to canonical GitHub through a reviewable branch/PR;
3. mirror the standard and task log to the controlled Atlas Google Drive folder and verify the destination parent and document readback;
4. classify exact user corrections, validated design fixes and non-sensitive quality-control rules as `AUTO_APPROVED`;
5. classify the consolidated rules as `CANONICAL` only when explicitly approved by the owner, as occurred at 11:54, 05.08.2026;
6. keep commercial, legal, provider-policy, safety-posture and release changes as `PENDING_REVIEW` unless separately approved.

## 10. Completion vocabulary

Use separate states:

- `DRAFTED` — design/copy artifact exists;
- `MEASUREMENT_CORRECTED` — controlled geometry and typography applied;
- `PASS_DESIGN_AND_CONTENT_HANDOFF` — exact assessed Figma scope passed the required validation suite;
- `IMPLEMENTED` — built in Wix or another runtime;
- `VALIDATED_RUNTIME` — responsive, accessible and functional implementation passed tests;
- `APPROVED/RELEASED` — explicit release approval issued.

A Figma pass never implies Wix implementation or public release.

## 11. Canonical saved configuration — 11:54, 05.08.2026

The owner explicitly approved this standard for future Atlas AI Figma configuration and adjustment work.

The following configuration is therefore canonical until superseded by a later explicit instruction:

- hero principal heading: retain the explicitly approved hero size;
- non-hero principal headings: `Roboto Slab Regular, 50 px, 118%` line height;
- standard cards, pricing/status panels and callouts: `6 px` radius;
- labels and CTA controls: `4 px` radius;
- backgrounds: `0 px` radius;
- intentional image masks: preserve source geometry;
- global layout baseline: 1920 × 1080, 104 px side margins, 1,712 px content width, 32 px grid/card rhythm and 32 px card padding, subject to documented approved section-specific exceptions;
- every image-bearing node must be validated on every slide;
- box dimensions, outer margins, internal text margins/padding, line breaks, typography, fills, strokes and bounds must be validated before a pass is issued;
- all corrections remain design-only and do not alter Wix implementation or the `NO_GO` release state.
