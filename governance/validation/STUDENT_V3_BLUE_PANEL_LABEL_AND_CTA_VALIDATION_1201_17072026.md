# Student v3 Blue-Panel, Label and CTA Validation

**Timestamp:** 12:01, 17.07.2026 Europe/Oslo  
**Figma:** https://www.figma.com/slides/I8mk7h7D2RtaRVoaZkPNRt

## Result

**PASS**

| Check | Result |
|---|---|
| Slide count | PASS — 8 |
| Slide 3 exact Gamma copy | PASS |
| Slide 3 description line height | PASS — 150% |
| Slide 3 list-item line height | PASS — 150% on all five items |
| Slide 3 text containment | PASS |
| Slide 7 exact Gamma copy | PASS |
| Slide 7 body line height | PASS — 150% |
| Slide 7 text containment | PASS |
| Transparent label fills | PASS — all labels |
| Label width formula | PASS — text width + 28 px |
| Label height | PASS — 44 px |
| Label stroke and radius | PASS — 2 px / 4 px |
| CTA font | PASS — Roboto SemiBold |
| CTA font size | PASS — 36 px |
| CTA line box | PASS — 44 px |
| CTA button height | PASS — 78 px |
| CTA stroke and radius | PASS — 2 px / 4 px |
| CTA alignment | PASS — centered horizontally and vertically |
| Top-level out-of-bounds objects | PASS — 0 |
| Visual review | PASS — Slides 1, 3, 7 and 8 |

## Label evidence

Validated content-fit widths:

- 283 px / 255 px text;
- 250 px / 222 px text;
- 277 px / 249 px text;
- 264 px / 236 px text for both plan-status labels;
- 171 px / 143 px text;
- 234 px / 206 px text;
- 180 px / 152 px text;
- 313 px / 285 px text.

Each difference is exactly 28 px, providing 14 px padding on each side.

## CTA evidence

- `Finn riktig studentplan`: Roboto SemiBold 36 px, 44 px line box.
- `Se hvordan det fungerer`: Roboto SemiBold 36 px, 44 px line box.
- `Registrer interesse — Student Basic`: Roboto SemiBold 36 px, 44 px line box.
- `Registrer interesse — Student Plus`: Roboto SemiBold 36 px, 44 px line box.

## Classification

**AUTO_APPROVED** — explicit user correction and verified design-system alignment.