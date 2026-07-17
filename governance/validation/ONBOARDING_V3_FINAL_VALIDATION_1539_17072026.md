# Atlas AI Onboarding v3 - Final Validation

**Timestamp:** 15:39, 17.07.2026 Europe/Oslo  
**Figma:** https://www.figma.com/slides/yxQvAPJDTZLos5LAx3JLCu  
**Gamma:** https://gamma.app/docs/Onboarding-v3-m6pyyxk2g2r1i2m

## Validation matrix

| Check | Result |
|---|---|
| Slide count | PASS - 8 slides |
| Canvas size | PASS - all slides 1920 x 1080 |
| Gamma order and wording | PASS |
| Out-of-bounds top-level nodes | PASS - 0 |
| Remaining image fills | PASS - 0 |
| Unique non-icon placeholders | PASS - 1 of 1 |
| Label transparency | PASS |
| Label width formula | PASS - text width plus 28 px |
| Label border / radius / height | PASS - 2 px / 4 px / 44 px |
| CTA font | PASS - Roboto SemiBold 24 px |
| CTA line height | PASS - 30 px |
| CTA height / border / radius | PASS - 78 px / 2 px / 4 px |
| CTA alignment | PASS - centred horizontally and vertically |
| Source metadata | PASS on all slides |
| Hero title wrapping | PASS after width correction |
| Screenshot review | PASS for Slides 1, 3, 5 and 8 |

## Live-node evidence

- Slide 1 title: x 104, y 180, w 900, h 210, 72 px.
- Slide 1 buttons: 420 x 78 and 360 x 78, Roboto SemiBold 24 px, 30 px line height.
- Slide labels use exact content-fit widths, including 96 px, 140 px, 274 px, 270 px and 194 px variants.
- All eight slides contain Gamma section metadata.
- No Figma image fills remain.
- One unique editable hero placeholder is present:
  - `[ASSET-GAMMA-ONBOARDING-V3-C1-HERO-1]`

## Visual assessment

- Slide 1 retains the Gamma right-image hero and now wraps the title cleanly without crossing the visual column.
- Slide 3 preserves the source blue needs panel, four data-class cards and red stop-condition notice.
- Slide 5 preserves the source blue/white intake comparison with readable list rhythm.
- Slide 8 preserves five status cards, the manual-validation warning and the submission boundary.

## Manual validation gates

The following source statements remain PENDING_REVIEW and must not be treated as operational guarantees:

- minimum age and guardian model;
- student and institution requirements;
- Family roles and public qualification rules;
- staffing and processing workflow;
- response times and status notifications;
- controlled-channel availability;
- public intake and production availability.

## Result

**PASS** for design reconstruction, content fidelity, hierarchy, typography, spacing, labels, CTA tokens, bounds and visual QA.

**PENDING_REVIEW** remains for operational, age, provider, process and public-availability claims.