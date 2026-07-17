# Atlas AI v3 Button Text Token Validation

**Timestamp:** 12:32, 17.07.2026 Europe/Oslo  
**Result:** PASS  
**Classification:** AUTO_APPROVED

## Files validated

- About v3: https://www.figma.com/slides/YJrRudQSlemarUGuby5s4w
- Trust v3: https://www.figma.com/slides/7QKfZugfK821aN8pKb9TZU
- Student v3: https://www.figma.com/slides/I8mk7h7D2RtaRVoaZkPNRt

## Deterministic result

| Deck | Controls | 24 px | 30 px line height | Roboto SemiBold | H/V centred | Frame retained |
|---|---:|---|---|---|---|---|
| About v3 | 4 | PASS | PASS | PASS | PASS | PASS |
| Trust v3 | 3 | PASS | PASS | PASS | PASS | PASS |
| Student v3 | 4 | PASS | PASS | PASS | PASS | PASS |
| **Total** | **11** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

All button text nodes use:

- font family: Roboto;
- style: SemiBold;
- font size: 24 px;
- line height: 30 px;
- horizontal alignment: center;
- vertical alignment: center;
- text container x/y: 0/0 within the button frame;
- text container width/height equal to the button frame.

## Preserved component geometry

- Button height remains 78 px.
- Border remains 2 px.
- Radius remains 4 px.
- Paired-button gap remains 16 px.
- Existing source-specific/content-fit widths remain unchanged.
- Gamma CTA wording remains unchanged.

## Control inventory

### About v3

- Slide 1: `Se hvordan Atlas arbeider`, 480 × 78 px.
- Slide 1: `Les Trust`, 320 × 78 px.
- Slide 7: `Se hvordan Atlas arbeider`, 480 × 78 px.
- Slide 7: `Les Trust`, 320 × 78 px.

### Trust v3

- Slide 1: `Se kontrollpunktene`, 480 × 78 px.
- Slide 1: `Les datagrensene`, 320 × 78 px.
- Slide 8: `Be om kvalifisering`, 480 × 78 px.

### Student v3

- Slide 1: `Finn riktig studentplan`, 480 × 78 px.
- Slide 1: `Se hvordan det fungerer`, 420 × 78 px.
- Slide 8: `Registrer interesse — Student Basic`, 600 × 78 px.
- Slide 8: `Registrer interesse — Student Plus`, 600 × 78 px.

## Visual QA

Screenshots were reviewed for:

- About v3 Slides 1 and 7;
- Trust v3 Slides 1 and 8;
- Student v3 Slides 1 and 8.

Visual result:

- no wrapping;
- no clipping;
- no baseline drift;
- no overlap;
- balanced visual weight inside existing frames;
- primary and secondary hierarchy preserved.

## Supersession

This validation supersedes prior deck-specific validation statements that identify 36 px as the active CTA text size. Those records remain historical evidence only.

## Boundary

The validation concerns button typography and layout only. CTA links, destinations, public availability, commercial activation and provider rights remain outside this approval.