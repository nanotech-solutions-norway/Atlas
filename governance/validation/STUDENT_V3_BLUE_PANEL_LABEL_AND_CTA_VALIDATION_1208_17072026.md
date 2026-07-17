# Atlas AI Student v3 — Blue Panel, Label and CTA Validation

**Timestamp:** 12:08, 17.07.2026 Europe/Oslo  
**Figma:** https://www.figma.com/slides/I8mk7h7D2RtaRVoaZkPNRt  
**Gamma:** https://gamma.app/docs/8n0a8sr0yuuy672

## Result

**PASS**

## Deterministic checks

| Check | Result |
|---|---|
| Slide count | PASS — 8 |
| Canvas size | PASS — 1920 × 1080 |
| Top-level out-of-bounds objects | PASS — 0 |
| Slide 3 Student Basic Gamma copy | PASS — exact source text retained |
| Slide 3 card height | PASS — 500 px |
| Slide 3 body/list line height | PASS — 150% |
| Slide 3 internal text rhythm | PASS — approved 8/16 px pattern |
| Slide 3 paired card alignment | PASS — both cards 500 px |
| Slide 7 Gamma heading/body copy | PASS — exact source text retained |
| Slide 7 blue panel height | PASS — 296 px content-fit |
| Slide 7 body line height | PASS — 150% |
| Slide 7 heading-to-body gap | PASS — 16 px |
| Slide 7 bottom padding | PASS — 35 px |
| Dynamic label widths | PASS — 9 of 9 |
| Label transparency | PASS — 9 of 9 |
| Label padding | PASS — 14 px per side |
| Label border/radius/height | PASS — 2 px / 4 px / 44 px |
| CTA font | PASS — Roboto SemiBold |
| CTA size | PASS — 36 px |
| CTA line height | PASS — 44 px |
| CTA height | PASS — 78 px |
| CTA border/radius | PASS — 2 px / 4 px |
| CTA wrapping | PASS — none |

## Label width evidence

Every label width equals its rendered text width plus 28 px. Verified examples:

- `BRUKSOMRÅDER`: 143 + 28 = 171 px.
- `AKADEMISK INTEGRITET`: 206 + 28 = 234 px.
- `SKOLE- OG INSTITUSJONSREGLER`: 285 + 28 = 313 px.
- `FORESLÅTT TIDLIG TILGANG`: 236 + 28 = 264 px.

## CTA evidence

- Slide 1 primary: 480 × 78 px.
- Slide 1 secondary: 420 × 78 px.
- Slide 8 primary: 600 × 78 px.
- Slide 8 secondary: 600 × 78 px.
- All four use Roboto SemiBold 36 px with 44 px line height.

## Visual review

- Slide 3: PASS — both plan cards align; blue-panel text has consistent rhythm; labels fit their text; warnings remain inside the slide.
- Slide 7: PASS — the blue rules panel now fits its text and no longer carries excessive unused height; table and warning remain unchanged and aligned.

## Pending review boundary

Commercial pricing, provider rights, payment/access mechanics, age, guardian model, student eligibility and public availability remain PENDING_REVIEW.

## Classification

- Design correction and validation: **AUTO_APPROVED**
- Unresolved commercial/legal/provider gates: **PENDING_REVIEW**