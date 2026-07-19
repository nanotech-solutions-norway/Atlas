# ATLAS PROJECT LOG UPDATE PACK — 00:04, 20.07.2026

## Session / task

Full canonical cross-check, visual comparison, correction and ranking of the seven Atlas AI Figma replacement-section files against GitHub, Google Drive, Gamma, the attached Technical Drawing and Measurement Report v2.1, Atlas AI 3.0 Figma files and Business v1.

## Issue or mistake observed

1. The earlier 23:03 Figma validation declared PASS before all later approved 17–18.07.2026 rules were applied consistently.
2. Numerous card, warning and notice body texts still used 125–130% line height instead of the approved exact 150% value.
3. Several imported top labels had visually similar but non-canonical geometry; some border shapes were too short, displaced or detached from their text.
4. The first label-normalisation pass selected only conventional 35–60 px border candidates and missed low-height imported border shapes.
5. A generic in-box typography pass temporarily treated some top labels as ordinary box text, changing them to 150% line height and causing overlaps on Managed Secure slides 1 and 5.
6. The Managed Secure decision-diagram frame extended beyond the slide canvas even though its actual content ended substantially earlier.
7. Historical measurement evidence retained 36 px CTA text, conflicting with the later approved 24 px token.
8. Atlas AI 3.0 comparator files contained mixed historical behaviours, including centred headings, older CTA variants, mixed line heights and incomplete validation metadata.

## Root cause

- Source precedence was not applied deeply enough during the earlier pass.
- Imported PPTX/Figma structures used inconsistent frame and rectangle geometries.
- Broad visual heuristics were insufficient for exact canonical label detection.
- Historic measurement values were initially treated as current without fully applying the approved override chain.
- Visual QA was required in addition to deterministic checks to detect semantic misclassification and overlap.

## Corrective rules

1. Latest approved GitHub/Drive corrections override older measurement values and older Atlas AI 3.0 inconsistencies.
2. Apply exactly 150% line height to body copy inside cards, boxes, panels, warnings and notices.
3. Top labels must use exact geometry:
   - border x=104, y=58, h=44;
   - text x=118, y=69, h=22;
   - Roboto SemiBold 18 px, exact 22 px line height.
4. Label detection must identify semantic top labels and not rely only on imported border height.
5. All headings, including editable diagram headings, must be left aligned.
6. Current CTA token is 24 px text / 30 px line height / 78 px height.
7. Imported diagrams and cards must be reduced to content-fit geometry before bounds validation.
8. Deterministic validation must be followed by representative and full-deck screenshot review.
9. A slide receives PASS metadata only after zero remaining structural issues.
10. Figma design-handoff PASS must not be represented as Wix release readiness.

## Evidence / sources

- Attached Technical Drawing and Measurement Report v2.1.
- Drive: `Atlas AI Canonical Figma Recreation Specification v3 — 01:57, 15.07.2026`.
- Drive: `Atlas AI v3 Button Text Token Update — 12:32, 17.07.2026`.
- Drive: `Atlas AI Multi-Deck Box Line Height, Alignment and Button Revalidation — 15:46, 18.07.2026`.
- GitHub: `governance/specifications/Atlas_AI_Canonical_Figma_Recreation_Specification_v3_0157_15072026.md`.
- GitHub: `governance/specifications/ATLAS_FIGMA_BOX_LINE_HEIGHT_ALIGNMENT_AND_BUTTON_PLACEMENT_CORRECTION_1546_18072026.md`.
- Gamma folder: `Atlas AI - sections`.
- Atlas AI 3.0 Figma comparator files and Business v1.
- Final validation report: `governance/validation/ATLAS_FIGMA_SECTION_CANONICAL_CROSSCHECK_ADJUSTMENT_AND_RANKING_0004_20072026.md`.

## Action taken

- Audited 30 slides across Home, Solutions, Packages, Governance, Process, Managed Secure and Contact.
- Profiled nine Atlas AI 3.0 files and Business v1 for visual comparison.
- Resolved the historical 36 px CTA conflict in favour of the approved 24 px token.
- Applied exact 150% in-box line height and content-fit body sizing.
- Left-aligned all headings and decision-diagram headings.
- Normalised every top label to exact canonical geometry.
- Repositioned labelled H1s and the Home hero structure.
- Repaired Managed Secure label overlaps on slides 1 and 5.
- Reduced the Managed Secure decision-diagram frame to eliminate the out-of-bounds defect.
- Confirmed zero remaining image-fill UI elements, out-of-bounds elements and clipping defects.
- Added final `atlas/referenceValidation = PASS` metadata to all 30 slides.
- Ranked all seven files and all 30 slide sections using the approved weighted methodology.

## Validation result

- Figma design handoff: **PASS**.
- Slides validated: **30/30**.
- Canonical labels: **PASS**.
- Exact 150% in-box text: **PASS**.
- CTA 24 px / 30 px / 78 px: **PASS**.
- Heading alignment: **PASS**.
- Remaining image-fill UI elements: **0**.
- Out-of-bounds visible elements: **0**.
- Text clipping defects: **0**.
- `atlas/sourceMap`: **30/30**.
- `atlas/referenceValidation = PASS`: **30/30**.
- Wix Phase 1 public deployment: **NO-GO**.

## Unresolved items

- Wix Studio insertion and CMS/page binding.
- Responsive breakpoint validation.
- CTA route and low-risk intake-form implementation.
- Accessibility, SEO and bilingual parity evidence.
- Legal, privacy, security and provider eligibility approval.
- Sanitised release evidence, rollback and explicit publication approval.

## Classification

### AUTO_APPROVED

- Exact user-approved layout corrections.
- 150% in-box line-height correction.
- 24 px CTA token enforcement.
- Left-alignment and canonical-label corrections.
- Content-fit diagram and bounds corrections.
- Deterministic plus visual QA workflow.
- Ranking methodology application.

### PENDING_REVIEW

- Pricing and commercial entitlement.
- Provider eligibility and subscription inclusion.
- Age, family and account model.
- Legal, privacy and security claims.
- Public availability, production status and release decisions.
