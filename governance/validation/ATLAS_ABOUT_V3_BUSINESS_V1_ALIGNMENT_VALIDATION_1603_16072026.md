# Atlas AI About v3 — Business v1 Alignment and Final Validation

**Timestamp:** 16:03, 16.07.2026 Europe/Oslo  
**Live About v3:** https://www.figma.com/slides/YJrRudQSlemarUGuby5s4w  
**Approved Business v1 reference:** https://www.figma.com/slides/QjAYZsGDVS2qxrCzj8TZIA  
**Measurement source:** Atlas AI Technical Drawing and Measurement Report Complete Package v2.1  
**Reviewed exports:** `About v3.deck`, `About v3.pptx`

## Supersession

This record supersedes `ATLAS_ABOUT_V3_HYBRID_RECONSTRUCTION_VALIDATION_1502_16072026.md` as the current final design-validation baseline.

The earlier record correctly validated content and bounds but treated Gamma-plain labels, heavier heading weights, source-style card radii and a left-aligned closing slide as final. The user's latest explicit instruction identified the live Business v1 project as the correctly created reference. Under the Atlas source-authority hierarchy, that explicit instruction overrides the earlier style decision for recurring Figma Slides components.

## Export review

The attached `.deck` and `.pptx` represent the same seven-slide pre-adjustment design.

- `About v3.deck` identifies file name `About v3` and export timestamp `2026-07-16T13:46:06.102Z`.
- It contains the five expected image hashes: one hero, three offer visuals and one provider visual.
- `About v3.pptx` is 16:9 with seven slides and no detected slide-boundary violations.
- The export content matches the live pre-adjustment Figma file and is now superseded by the corrected live deck.

## Pre-adjustment differences from Business v1

1. Section labels were plain and borderless instead of transparent, text-sized, 2 px `#3257B8` outlined labels.
2. Headings and card titles used Bold weights rather than the Business v1 Regular/SemiBold hierarchy.
3. Slide 2 used y positions 340/560/780 and 188 px card heights rather than the validated 350/572/794 and 190 px grid.
4. Several standard cards used square or 28 px radii rather than the Business v1 4/6/8 px radius system.
5. Highlighted and provider panels lacked the validated border/radius treatment.
6. CTA controls lacked the Business v1 4 px corner radius and SemiBold text treatment.
7. The closing slide used a left-aligned source layout rather than the validated Business v1 centred closing composition.
8. The hero retained source-specific split imagery, but its typography did not use the Business v1 72 px Regular display treatment.

## Corrections applied

### Global recurring system

- Retained 1920 × 1080 px canvas and 104 px safe margins.
- Applied Roboto Slab Regular to display and dense H1 headings.
- Applied Roboto Slab SemiBold to card and module titles.
- Applied Roboto Regular to body copy and Roboto SemiBold to labels, warnings and CTA text.
- Retained primary colours `#15213F`, `#3257B8`, `#476FD6`, `#E9ECF2`, `#CFD2D8` and white.

### Labels

Slides 2–6 now use:

- x 104 px;
- y 58 px;
- 44 px height;
- transparent fill;
- 2 px `#3257B8` stroke;
- 4 px corner radius;
- 14 px horizontal text padding;
- 18 px Roboto SemiBold.

The solid hero label remains a source-specific About exception.

### Slide 1 — Hero

- Preserved the source-specific split hero and original Gamma visual.
- Changed H1 to Roboto Slab Regular, 72 px.
- Changed body copy to Roboto Regular, 30 px.
- Applied 78 px CTA height, 36 px SemiBold text, 4 px radius and 2 px borders.
- Preserved clean separation between heading, body and CTA controls.

### Slide 2 — Utgangspunktet

- Applied exact Business v1 grid geometry:
  - columns x 104 / 976;
  - width 840 px;
  - rows y 350 / 572 / 794;
  - height 190 px;
  - 32 px gaps.
- Applied 6 px card radius, 1 px `#CFD2D8` border, 28 px SemiBold titles and 21 px body text.

### Slide 3 — Atlas-modellen

- Preserved the source-specific vertical five-step component hierarchy.
- Applied the Business label and H1 system.
- Changed step titles to 28 px Roboto Slab SemiBold and bodies to 21 px Roboto Regular.
- Retained native editable icons and source-specific progression.

### Slide 4 — Tilbud

- Applied the Business label and H1 system.
- Applied 6 px card radius, 1 px border, 28 px SemiBold titles and 21 px body text.
- Retained original Gamma visuals, qualification wording and source-specific yellow warning.
- Applied validated warning border and radius treatment.

### Slide 5 — Hva Atlas er

- Applied the Business label and H1 hierarchy.
- Added 8 px radius and 2 px accent stroke to the `#476FD6` Atlas-owned panel.
- Added 8 px radius and 1 px border to the provider panel.
- Applied 30 px SemiBold panel headings and 22 px body/list text.
- Retained the original provider visual and complete ownership quotation.

### Slide 6 — Prinsipper

- Applied the Business label and H1 hierarchy.
- Reduced standard card radii to 6 px and added 1 px `#CFD2D8` borders.
- Applied 28 px SemiBold card titles and 21 px body text.
- Retained source-specific icons, neutral fill and the complete Managed Secure manual-validation warning.

### Slide 7 — Closing CTA

Applied the validated Business v1 closing geometry:

- title x 220, y 165, w 1480, h 110; 72 px centred;
- body x 260, y 320, w 1400, h 96; 30 px centred;
- quote/notice x 360, y 490, w 1200, h 170; 6 px radius and 1 px border;
- primary CTA x 552, y 750, w 480, h 78;
- secondary CTA x 1048, y 750, w 320, h 78;
- CTA text 36 px SemiBold; 16 px gap.

The About quotation remains source content; no unsupported copy was added.

## Final deterministic validation

**PASS**

- Seven native 1920 × 1080 slides.
- No top-level out-of-bounds objects.
- No zero-size text containers.
- No missing required source content.
- Unsupported additions remain absent.
- Slides 2–6 labels pass all recurring Business token checks.
- Slide 2 card grid passes exact coordinate and size checks.
- Slide 1 and Slide 7 CTAs pass height, typography, stroke and radius checks.
- Slide 7 passes exact Business closing geometry checks.
- Fonts are limited to approved Roboto / Roboto Slab families and intended Regular, SemiBold, Italic or icon-warning Bold uses.
- Five source images remain present.

## Visual QA

Screenshots of all seven slides were reviewed after correction.

- Slide 1 has no title/body overlap or CTA wrapping.
- Slide 2 aligns visually with the Business v1 card system.
- Slide 3 preserves the About-specific vertical process without introducing Business-specific layout assumptions.
- Slides 4–6 use consistent label, type, border and radius treatment.
- Slide 7 now matches the Business v1 closing composition and remains fully editable.

## Final assessment

| Category | Pre-adjustment | Final |
|---|---:|---:|
| Content/source fidelity | 10.0 | 10.0 |
| Business v1 visual-system alignment | 7.8 | 9.8 |
| Measurement-profile alignment | 8.2 | 9.8 |
| Editability and production quality | 9.4 | 9.8 |
| **Weighted overall** | **8.8** | **9.8** |

## Acceptance decision

**ACCEPTED as the current About v3 Figma Slides production-design baseline.**

The attached exported files are now historical pre-adjustment evidence and should not be treated as the current final design. A fresh export from the live Figma file is required for an updated offline `.deck` or `.pptx` copy.

## Known provider limitation

Native Figma Slide-node names continue to reload as numeric names `1`–`7`. Visible titles and slide order are correct. This does not affect presentation output.

## Classification

**AUTO_APPROVED** — exact user-directed alignment to the approved Business v1 reference, validated geometry corrections, repeatable typography/card/CTA corrections and verified visual QA.

## Boundary

This validation concerns design reconstruction only. It does not approve public launch, production availability, commercial policy, provider agreements, legal/compliance claims, security posture or Managed Secure production status.