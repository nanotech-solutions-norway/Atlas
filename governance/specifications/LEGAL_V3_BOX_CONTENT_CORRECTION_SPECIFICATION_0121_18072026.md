# Atlas AI Legal v3 — Box and Content Correction Specification

**Timestamp:** 01:21, 18.07.2026 Europe/Oslo  
**Figma:** https://www.figma.com/slides/WAVCUxiETXqzHFhriKVNKf  
**Gamma:** https://gamma.app/docs/Legal-v3-8zysfcnlqw6he4r  
**Classification:** Verified design corrections **AUTO_APPROVED**. Legal, privacy, provider, accessibility, contractual, compliance and public-availability matters remain **PENDING_REVIEW**.

## Scope

This specification records the second-pass correction of the existing Legal v3 Figma Slides file. The review focused on box dimensions, fixed-height text frames, H1-to-body spacing, card padding, panel hierarchy, warning geometry and exact Gamma content retention.

## Source authority

1. Current user instruction.
2. Current approved Atlas operational design tokens.
3. Gamma Legal v3 wording, order and component hierarchy.
4. Existing Legal v3 Figma file and screenshot evidence.
5. Approved Business v1 geometry and typography reference.

No legal or commercial source conflict was merged. The current 24 px button token remains governing.

## Issues found

- Several H1 and body text frames retained oversized fixed heights, producing gaps substantially larger than the approved 8 px content-H1 gap or 32 px hero gap.
- Multiple cards and warnings were dimensioned around fixed text-frame heights rather than rendered content height.
- Slide 2 used a half-width fifth privacy card, leaving an unintended empty grid cell and weakening the Gamma hierarchy.
- Slide 2 blue panel, Slides 3 and 6 cards, Slide 5 provider panel and warning, and Slide 7 modules contained unnecessary blank internal area.
- Geometry-only validation had passed because the content was not clipped; it did not identify excessive internal whitespace.

## Corrective rules applied

- Convert text inside cards, panels, notices and warnings to rendered content-height sizing before resizing the surrounding box.
- Apply 32 px standard internal card/panel padding and 8 px title-to-body spacing, except source-specific warnings using 24 px horizontal padding and centred vertical placement.
- Apply 32 px hero H1-to-body spacing and 8 px content H1-to-introductory-body spacing.
- Round content-fit geometry to the 8 px grid where practical.
- Preserve exact Gamma wording and all qualification language.
- Do not reduce the approved 24 px CTA text size or legal-detail text merely to retain an oversized or unsuitable box.

## Slide corrections

### Slide 1 — Legal Centre hero

- Corrected the hero H1-to-body gap to 32 px.
- Moved CTA controls and the legal-summary notice upward with the corrected content flow.
- Reduced the notice to content-fit height while retaining source wording and editable geometry.

### Slide 2 — Privacy

- Reduced the blue primary panel to content-fit height.
- Rebalanced the five supporting cards into two paired rows plus one full-width final card.
- Expanded `Offentlige skjemaer` across the full supporting-card column.
- Applied content-fit row heights and reduced the validation warning to content-fit geometry.

### Slide 3 — Terms and use

- Corrected the H1-to-intro spacing to 8 px.
- Reduced all four topic cards and the `PENDING_REVIEW` warning to rendered-content dimensions.
- Preserved the behind-image placeholder and complete wording.

### Slide 4 — Acceptable use

- Corrected heading/body flow.
- Standardised topic cards to content-fit heights.
- Reduced the Family/account-sharing caution to content-fit height without changing its higher-risk legal treatment.

### Slide 5 — AI providers

- Corrected H1-to-intro spacing.
- Reduced the Atlas blue panel to content-fit geometry.
- Reduced the provider-boundary and manual-validation boxes while preserving the complete provider warning.

### Slide 6 — AI disclaimer

- Corrected heading/body flow.
- Reduced all four disclaimer cards to content-fit heights.
- Reduced and centred the primary-source/qualified-advice statement box.

### Slide 7 — Cookies, accessibility and contact

- Removed the oversized H1 text frame.
- Reduced the five content modules and validation warning to rendered-content dimensions.
- Preserved all five editable icon placeholders and the qualified WCAG wording.

### Slide 8 — Legal document register

- Revalidated the complete editable register.
- No box correction was required; row heights remain governed by the longest manual-validation text in the public-link column.

## Content result

A programmatic exact-string comparison against Gamma returned zero missing and zero unexpected source strings on all eight slides. No `MANUELL VALIDERING KREVES` or `PENDING_REVIEW` content was rewritten or abbreviated.

## Governance boundary

This correction is a design and content-fidelity action only. It does not approve legal readiness, privacy compliance, WCAG compliance, provider authorization, contractual readiness, subscription terms or public availability.