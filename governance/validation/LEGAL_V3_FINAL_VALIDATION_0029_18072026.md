# Atlas AI Legal v3 — Final Validation

**Timestamp:** 00:29, 18.07.2026 Europe/Oslo  
**Figma:** https://www.figma.com/slides/WAVCUxiETXqzHFhriKVNKf  
**Gamma:** https://gamma.app/docs/Legal-v3-8zysfcnlqw6he4r

## Validation matrix

| Check | Result |
|---|---|
| Slide count | PASS — 8 slides |
| Canvas size | PASS — all slides 1920 × 1080 |
| Gamma order and exact wording | PASS |
| Gamma source metadata | PASS — all 8 slides |
| Top-level and descendant bounds | PASS — 0 out-of-bounds nodes |
| Text clipping | PASS — 0 after correction |
| Text-to-text overlaps | PASS — 0 |
| Remaining image fills | PASS — 0 |
| Unique non-icon placeholders | PASS — 3 of 3, all unique |
| Editable icon placeholders | PASS — 10 |
| Label transparency | PASS — all 8 labels |
| Label width formula | PASS — rendered text width + 28 px |
| Label height / border / radius | PASS — 44 px / 2 px / 4 px |
| CTA font | PASS — Roboto SemiBold 24 px |
| CTA effective line height | PASS — 30 px |
| CTA height / border / radius | PASS — 78 px / 2 px / 4 px |
| CTA alignment | PASS — centred horizontally and vertically |
| Editable legal register | PASS — 8 header cells and 48 body cells |
| Exact manual-validation and pending-review qualification | PASS |
| Full-deck screenshot review | PASS — all 8 slides inspected |

## Label evidence

| Slide | Final label width | Formula result |
|---|---:|---|
| 1 | 268 px | PASS |
| 2 | 144 px | PASS |
| 3 | 170 px | PASS |
| 4 | 189 px | PASS |
| 5 | 187 px | PASS |
| 6 | 258 px | PASS |
| 7 | 379 px | PASS |
| 8 | 208 px | PASS |

## CTA evidence

- Primary CTA: 420 × 78 px; 2 px border; 4 px radius; Roboto SemiBold 24 px; 30 px effective line height; centred.
- Secondary CTA: 350 × 78 px; 2 px border; 4 px radius; Roboto SemiBold 24 px; 30 px effective line height; centred.
- Source wording preserved: `Se dokumentoversikten` and `Les bruksgrensene`.

## Corrective action during QA

The first deterministic pass found one clipped text frame on Slide 5 in the provider-boundary card:

- Text: `Atlas lover ikke en permanent modellversjon eller et komplett leverandørabonnement uten formell avtale.`
- Initial frame height: 70 px.
- Required height: 78 px.
- Corrected frame height: 84 px.

The second deterministic pass returned zero clipped text, zero overlaps and zero boundary failures.

## Visual QA by slide

1. **Legal Centre hero** — source-position placeholder, label, 72 px hero heading, supporting copy, both 24 px CTA controls and legal-summary notice are balanced and readable.
2. **Privacy** — blue primary panel and five supporting cards preserve the Gamma hierarchy. The full manual-validation notice remains visible without abbreviation.
3. **Terms and use** — four topic cards and complete `PENDING_REVIEW` notice remain readable over the source-position placeholder.
4. **Acceptable use** — all five prohibited-use topics and the Family/account-sharing limitation are present and traceable.
5. **AI providers** — left visual placeholder, Atlas blue panel, third-party explanation, provider boundary and complete manual-validation notice are retained.
6. **AI disclaimer** — all four disclaimers and the primary-source/qualified-advice statement are preserved without guarantee language.
7. **Cookies, accessibility and contact** — five modules, icons, qualified WCAG wording and complete manual-validation notice are present.
8. **Legal document register** — all eight headings, six rows, em dashes, `MANUELL VALIDERING KREVES`, `PENDING_REVIEW` and final navigation notice are readable on one slide.

## Placeholder inventory

- `[ASSET-GAMMA-LEGAL-V3-C1-HERO-1]`
- `[ASSET-GAMMA-LEGAL-V3-C3-TERMS-1]`
- `[ASSET-GAMMA-LEGAL-V3-C5-PROVIDER-1]`

## Manual validation gates

The deck does not establish or approve:

- legal approval or contractual readiness;
- privacy compliance or verified processing practice;
- WCAG compliance;
- provider authorization or approved provider disclosure;
- published legal document versions, dates, owners, audiences, statuses or public links;
- subscription, cancellation, refund, withdrawal, Family or sanctions terms;
- public or production availability.

## Result

**PASS** for design reconstruction, content fidelity, editability, geometry, typography, spacing, labels, CTA tokens, warnings, placeholders, table structure, deterministic checks and full-deck visual QA.

**PENDING_REVIEW** remains for all unresolved legal, privacy, provider, accessibility, compliance, contractual and public-availability matters.
