# Atlas AI Legal v3 — Box and Content Recheck Validation

**Timestamp:** 01:21, 18.07.2026 Europe/Oslo  
**Figma:** https://www.figma.com/slides/WAVCUxiETXqzHFhriKVNKf  
**Gamma:** https://gamma.app/docs/Legal-v3-8zysfcnlqw6he4r

## Executive result

The Legal v3 deck was rechecked against the complete Gamma source and corrected in place. The recheck identified excessive blank area caused by fixed-height text frames and static box dimensions. The content remained exact, but several boxes did not satisfy the content-fit requirement. Those boxes and the associated content flow have been corrected.

## Corrections completed

- Corrected the Slide 1 hero H1-to-body spacing to 32 px and reduced the legal-summary notice to content-fit height.
- Rebuilt Slide 2 supporting privacy geometry as two paired rows plus a full-width fifth card; reduced the blue panel and warning to content-fit dimensions.
- Corrected Slides 3–6 H1/body flow and reduced topic, disclaimer, provider and caution boxes to rendered-content dimensions.
- Corrected Slide 7 H1 frame, all five content modules and the validation warning.
- Retained Slide 8 table geometry because the longest public-link warnings govern the required row height.

## Validation matrix

| Check | Result |
|---|---|
| Slide count | PASS — 8 |
| Canvas size | PASS — all 1920 × 1080 |
| Exact Gamma visible text | PASS — 0 missing, 0 unexpected |
| Gamma order and hierarchy | PASS |
| Source metadata | PASS — all 8 slides |
| Out-of-bounds nodes | PASS — 0 |
| Clipped text | PASS — 0 |
| Text-to-text overlaps | PASS — 0 |
| Image fills | PASS — 0 |
| Unique non-icon placeholders | PASS — 3 of 3 |
| Label transparency | PASS — 8 of 8 |
| Label dynamic-width formula | PASS — rendered text width + 28 px |
| Label height / border / radius | PASS — 44 px / 2 px / 4 px |
| CTA font and line height | PASS — Roboto SemiBold 24 px / 30 px |
| CTA frame token | PASS — 78 px / 2 px border / 4 px radius |
| Editable legal register | PASS — 8 header cells and 48 body cells |
| Screenshot QA | PASS — all 8 corrected slides inspected |

## Corrected visual QA

1. **Legal Centre hero:** Correct H1/body/CTA/notice flow. Placeholder remains behind the editable content.
2. **Privacy:** Blue panel no longer contains excessive blank space. Five privacy cards are balanced; the fifth card spans the complete supporting column.
3. **Terms and use:** Topic cards and `PENDING_REVIEW` warning now fit rendered content without unnecessary height.
4. **Acceptable use:** Five topics and the Family/account-sharing caution use consistent content-fit geometry.
5. **AI providers:** Atlas panel, provider boundary and full validation warning are compact, readable and traceable.
6. **AI disclaimer:** Four disclaimer cards and the primary-source statement are content-fit and aligned.
7. **Cookies, accessibility and contact:** Five modules and the complete validation notice are content-fit; WCAG language remains qualified.
8. **Legal document register:** Full table remains readable and editable; no content or status was changed.

## Final deterministic evidence

- 0 out-of-bounds nodes.
- 0 clipped text frames.
- 0 text-to-text overlaps.
- 0 image fills.
- 3 unique non-icon placeholders.
- 8 compliant labels.
- 2 compliant 24 px CTA controls.
- 8 screenshots inspected after correction.

## Remaining manual-validation gates

No change was made to unresolved legal, privacy, provider, accessibility, contractual, compliance or public-availability matters. These remain **PENDING_REVIEW**, including privacy practice and legal bases, provider disclosure and authorization, subscription and Family terms, cookie/analytics implementation, accessibility testing, document-register ownership/status data and public links.

## Final result

**PASS — AUTO_APPROVED** for verified box, spacing, layout and content-fidelity corrections.

This validation does not establish legal approval, privacy compliance, WCAG compliance, provider authorization, contractual readiness or public availability.