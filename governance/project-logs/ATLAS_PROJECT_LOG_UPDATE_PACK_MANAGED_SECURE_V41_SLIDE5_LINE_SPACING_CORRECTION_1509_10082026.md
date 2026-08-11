# ATLAS PROJECT LOG UPDATE PACK — Managed Secure v4.1 Slide 5 line-spacing correction — 15:09, 10.08.2026

## Session/task

Correct the owner-reported line-spacing defect in the list text inside the Slide 5 qualification-area content blocks of the existing Managed Secure v4.1 Figma Slides deck, using the supplied Gamma PDF/PPTX exports as the source baseline.

## Scope

- Figma target: https://www.figma.com/slides/fORMCUk6KcaJolveyaC2zx/Managed-Secure-v41
- Slide: 5 (`0:25`)
- Affected list text nodes: `0:123` and `0:130`
- Source evidence: `Managed-Secure-v41.pptx`, slide 5; `Managed-Secure-v41.pdf`, page 5
- Gamma source: https://gamma.app/docs/hl2hwvvdeuldle7
- Design-only correction. No Gamma, Wix, pricing, activation, production or release-state mutation.

## Issue or mistake observed

The sentence/list-item spacing inside the two Slide 5 qualification-area text blocks was too tight. The previous Figma reconciliation had set the list body nodes to `118%` line height, which did not match the source presentation.

## Root cause

The global `118%` line-height setting approved for non-hero principal headings was incorrectly carried into Slide 5 body/list text during the earlier normalisation. The source PPTX uses a distinct paragraph line-spacing value of `1.33` for each list item in both qualification-area lists.

## Corrective rule

- The `118%` line-height standard applies to non-hero principal page/section headings only.
- Body text, list text and text inside boxes must retain or explicitly reproduce their validated source-specific line-height/paragraph-spacing values.
- For this Slide 5 source, both list bodies use `133%` line height with `0` paragraph spacing and `0` list spacing.
- Native Figma unordered-list formatting must be retained; do not add literal bullet glyphs.
- A design pass must compare line height as a separate typography field rather than inferring it from font size or heading standards.

## Evidence/source

- Programmatic inspection of `Managed-Secure-v41.pptx`, slide 5:
  - left list: Roboto 9.5 pt, line spacing `1.33`, no explicit space-before/space-after;
  - right list: Roboto 9.5 pt, line spacing `1.33`, no explicit space-before/space-after.
- Rendered `Managed-Secure-v41.pdf`, page 5, visually confirms the wider list-item spacing.
- Pre-correction live Figma readback showed both nodes at Roboto 25.3333 px with `118%` line height, paragraph spacing `0`, list spacing `0`.
- Pre- and post-correction Slide 5 screenshots were inspected at 1920 × 1080.

## Action taken

- Updated Figma text node `0:123` from `118%` to `133%` line height.
- Updated Figma text node `0:130` from `118%` to `133%` line height.
- Preserved Roboto Regular 25.3333 px body size.
- Preserved paragraph spacing `0` and list spacing `0`.
- Preserved native `UNORDERED` Figma list formatting with no literal bullet glyphs.
- Preserved all copy, text-frame dimensions, parent-frame dimensions, box geometry, 6 px box radius, heading content and heading typography.
- Updated Slide 5 Atlas validation metadata after deterministic and rendered validation.

## Validation

`PASS_DESIGN_AND_CONTENT_HANDOFF`

- Left list node `0:123`: `133%` line height — PASS
- Right list node `0:130`: `133%` line height — PASS
- Source copy match: 2/2 — PASS
- Roboto Regular 25.3333 px: 2/2 — PASS
- Paragraph spacing `0`: 2/2 — PASS
- List spacing `0`: 2/2 — PASS
- Native unordered-list formatting: 2/2 — PASS
- Literal duplicate bullets: 0 — PASS
- Missing fonts: 0 — PASS
- Blue panel geometry unchanged: 840 × 426.1094 px, 6 px radius — PASS
- Slide canvas unchanged: 1920 × 1080 — PASS
- Rendered Slide 5 visual QA after correction — PASS

## Unresolved items

- None for this exact Slide 5 line-spacing correction.
- The Figma connector's project-folder enumeration limitation remains unchanged and does not affect validation of the known Managed Secure v4.1 file.
- Wix/runtime/public release remain separate and `NO_GO` under the existing Atlas gates.

## Classification

- Owner-reported exact design defect and validated correction: `AUTO_APPROVED`.
- Corrective quality-control rule distinguishing heading line height from body/list source-specific spacing: `AUTO_APPROVED`.
- Commercial, legal, security-posture, provider-policy, production-availability and public-release decisions: unchanged.