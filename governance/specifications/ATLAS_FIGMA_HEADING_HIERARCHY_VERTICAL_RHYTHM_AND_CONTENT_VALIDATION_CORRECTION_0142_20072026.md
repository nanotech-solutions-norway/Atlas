# Atlas AI Figma Heading Hierarchy, Vertical Rhythm and Content Validation Correction — 01:42, 20.07.2026

## Status

**Classification: AUTO_APPROVED**

This correction records exact user corrections and validated non-sensitive layout fixes. It supersedes earlier Atlas Figma validation language wherever that language permits 72 px headings on ordinary content slides or validates spacing using parent-frame geometry rather than rendered text geometry.

## 1. Heading hierarchy

### Home section deck

- Hero H1: **72 px**.
- Closing CTA H1: **72 px**.
- Ordinary Home content-slide H1: **54 px**.
- Module, column and card headings: **maximum 30 px**, normally 27–30 px according to density.

### Other section decks

- Ordinary labelled-slide H1: **54 px**.
- Module, column and card headings: **maximum 30 px**.
- Headings remain Roboto Slab and left aligned.

The previous rule interpretation that allowed 72 px on every Home slide is invalid.

## 2. Vertical-rhythm contract

Spacing must be measured from the **rendered text bounding box**, not from an oversized imported parent frame.

- H1 rendered bottom → intro/subheading rendered top: **24 px**.
- Intro/subheading rendered bottom → first semantic content element top: **32 px**.
- Where no intro exists, H1 rendered bottom → first semantic content element top: **32 px**.
- Hero or closing body rendered bottom → CTA top: **32 px**.
- Content block → CTA: **24 px** unless the canonical hero/closing rule applies.

The first semantic content element is identified from the approved Gamma/source order. Decorative backgrounds, full-slide rectangles, labels and imported wrapper frames are excluded.

## 3. In-box typography

- Body text inside cards, rows, boxes, warnings, notices, process steps and comparable bounded elements: **exactly 150% line height**.
- CTA text: **24 px**, exact **30 px** line height, fixed **78 px** button height.
- Top label text: Roboto SemiBold **18 px**, exact **22 px** line height.

## 4. Content validation contract

Each slide must be compared against its corresponding current Gamma source for:

1. slide/card order;
2. H1 and intro wording;
3. module/card headings;
4. body copy;
5. warnings, restrictions and PENDING_REVIEW language;
6. CTAs and route wording;
7. safety and intake boundaries.

Content matching is case-aware for user-facing headings but may treat typographic line wrapping as non-semantic. Uppercase display treatment does not constitute missing content.

## 5. Required validation sequence

1. Read the latest approved GitHub and Drive specifications.
2. Read the current Gamma source.
3. Inspect rendered Figma text and element geometry.
4. Apply corrections.
5. Run deterministic checks for typography, spacing, bounds, clipping, images, metadata and content.
6. Review representative and affected-slide screenshots.
7. Set `atlas/referenceValidation = PASS` only after zero remaining issues.

## 6. Timestamp control

Before writing report titles or validation metadata, obtain the current user-local time. Do not infer or project a future timestamp. Intermediate future-dated validation metadata created during the correction session was replaced with the verified Oslo timestamp `2026-07-20T01:42:00+02:00`.

## 7. Safety and release boundary

This correction does not change Atlas safety posture or commercial/public-availability decisions. Managed Secure remains an architecture-review-only, non-public qualification route. Figma design validation does not establish Wix production readiness.
