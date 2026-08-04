# ATLAS FIGMA ADJUSTMENT AND WEBSITE-DRAFT PREPARATION STANDARD

**Approved:** 23:05, 04.08.2026 Europe/Oslo  
**Scope:** Atlas AI website drafts and Gamma/PDF/PPTX-to-Figma adjustments  
**Classification:** `AUTO_APPROVED`  
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
7. Use a 1920 × 1080 slide canvas. Apply the controlled 104 px principal side margin and 1,712 px principal content width where the section uses the standard full-width contract. Preserve documented source-specific offsets for intentional split layouts, image bleeds and specialist cards.
8. Reconstruct rasterised controls as editable Figma frames and editable text labels.
9. Preserve source images and crop intent in Figma Slides. For a Figma Design transfer, use embedded images or explicit user-approved editable placeholders; report which scope is active.
10. Preserve exact box configuration, including dimensions, padding, alignment, fill, stroke, stroke weight, corner radius, dividers and callout treatment.
11. Keep public-price copy separate from purchase, activation and release status. Managed Secure remains qualification/architecture-review only unless separately approved.
12. Do not mutate Wix, publish, enable checkout or change release status as part of a Figma design correction.

## 5. Typography and list-format control

1. Load every current and target font before changing text.
2. Validate font-family replacement across styled text segments, not only the top-level text property.
3. Inspect imported paragraph-list formatting before adding literal bullet glyphs. Use either Figma list formatting or literal bullets, never both.
4. Validate text frames for clipping and visible overflow after font replacement.
5. Preserve paragraph spacing and intentional blank-line separation where the source uses distinct paragraphs.

## 6. Required validation suite

After mutation, perform a separate readback and rendered QA. At minimum validate:

- exact slide count and order;
- 1920 × 1080 dimensions for every slide;
- expected heading on every slide;
- exact controlled line-break samples;
- required source-copy samples;
- principal margins and content widths;
- key frame, card, image and callout geometry;
- label-box fills, strokes, stroke weights and corner radii;
- CTA count, labels, dimensions, fills, borders and editability;
- absence of raster/image-filled CTA controls;
- image-fill or approved-placeholder scope;
- font-family violations and missing fonts;
- visible nodes outside the slide bounds;
- text clipping or range-fit warnings;
- duplicate bullet glyphs;
- Atlas source and status metadata;
- page-by-page rendered visual inspection.

A validator must prove its expected baseline before classifying a design failure. When a check fails, inspect the node ID, coordinate system and expected-record construction before mutating the design.

## 7. Figma Design handoff

When slides are copied to a Figma Design file:

1. create one 1920 × 1080 frame per slide;
2. preserve source order;
3. align frames on one horizontal axis;
4. use a uniform 120 px vertical gap unless another approved spacing is specified;
5. group the complete sequence and name the page/group consistently;
6. preserve editable text, controls, cards and placeholders where required;
7. validate group-relative positions by subtracting the group origin because children of a Figma `GROUP` retain page-relative coordinates;
8. export and revalidate the resulting `.fig` package when portability is required.

## 8. Evidence and write-back

At completion:

1. prepare an Atlas project-log update pack with timestamp, issue, root cause, corrective rule, evidence, action, validation and unresolved items;
2. commit the standard and task-specific log to canonical GitHub through a reviewable branch/PR;
3. mirror the standard and task log to the controlled Atlas Google Drive folder and verify the destination parent and document readback;
4. classify exact user corrections, validated design fixes and non-sensitive quality-control rules as `AUTO_APPROVED`;
5. keep commercial, legal, provider-policy, safety-posture and release changes as `PENDING_REVIEW` unless separately approved.

## 9. Completion vocabulary

Use separate states:

- `DRAFTED` — design/copy artifact exists;
- `MEASUREMENT_CORRECTED` — controlled geometry and typography applied;
- `PASS_DESIGN_AND_CONTENT_HANDOFF` — exact assessed Figma scope passed the required validation suite;
- `IMPLEMENTED` — built in Wix or another runtime;
- `VALIDATED_RUNTIME` — responsive, accessible and functional implementation passed tests;
- `APPROVED/RELEASED` — explicit release approval issued.

A Figma pass never implies Wix implementation or public release.