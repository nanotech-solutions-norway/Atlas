# ATLAS PROJECT LOG UPDATE PACK

**Timestamp:** 23:10, 13.07.2026 Europe/Oslo  
**Session/task:** Correct the recreation prompt from a Business v1-specific instruction to a general one-or-multiple Gamma draft workflow.

## Issue or mistake observed

The recreation prompt delivered with Revision 2 was hardcoded to Business v1: eight slides, Business v1-specific section geometry, fixed source IDs and fixed copy/layout assumptions. The user corrected the scope and required a general prompt suitable for recreating any Gamma draft or an approved combination of multiple Gamma drafts in Figma Slides.

## Root cause

The prompt was derived too literally from the validated Business v1 implementation profile instead of separating:

1. the source-specific Business v1 measurement record; and
2. the reusable Gamma-to-Figma Slides operating procedure.

## Corrective rule

Reusable recreation prompts must not assume a fixed Gamma title, fixed slide count, fixed card order, fixed section names or one source draft. A general prompt must:

- accept one or more Gamma sources;
- inventory all source cards and visual locations;
- create a traceable source-to-slide map;
- detect duplicates, alternatives and contradictions;
- preserve or merge content only when sources agree;
- keep unresolved commercial, legal, provider-policy, security or public-availability conflicts as `PENDING_REVIEW`;
- extract applicable measurement/design tokens dynamically;
- create or update one durable Figma Slides file;
- validate source coverage, slide order, bounds, clipping, overlap, placeholders and source-specific exceptions;
- distinguish content fidelity, structural fidelity, visual fidelity and measurement compliance.

Business v1-specific geometry remains valid only as a source-specific validated profile and must not be presented as the universal Gamma recreation template.

## Evidence/source

- Exact user correction: “The prompt must be for general recreation of any gamma draft (or a combination of drafts) in figma slides.”
- Revision 2 prompt and report package.
- Validated Business v1 implementation profile retained separately.

## Action taken

- Replaced the Business v1-specific recreation prompt with `ATLAS_GENERAL_GAMMA_DRAFTS_TO_FIGMA_SLIDES_RECREATION_PROMPT_v1_2310_13072026.md`.
- Added support for one Gamma draft or multiple Gamma drafts.
- Added source inventory, duplicate detection, contradiction handling and source-to-slide mapping requirements.
- Removed fixed eight-slide, Business v1 copy and fixed Business v1 geometry assumptions from the reusable prompt.
- Retained general placeholder rules, including source-location tags for non-icon visuals and `icon` text only for icon placeholders.
- Updated the report text and prompt execution checklist.
- Created Revision 2.1 of the report package with updated DOCX, PDF, Markdown, text, manifest and checksums.

## Unresolved items

None for the prompt-scope correction. Individual future recreations may still contain source conflicts requiring `PENDING_REVIEW`.

## Classification

**AUTO_APPROVED** - exact user correction, non-sensitive workflow clarification, reusable quality-control rule and validated documentation correction.
