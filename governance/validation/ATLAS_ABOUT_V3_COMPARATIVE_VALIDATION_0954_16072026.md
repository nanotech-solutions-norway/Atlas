# Atlas AI About v3 Comparative Validation — 09:54, 16.07.2026

## Scope

Comparative validation of:

1. Gamma source: `https://gamma.app/docs/4r2wl5rog25safl`
2. Recreated Figma Slides file: `https://www.figma.com/slides/YJrRudQSlemarUGuby5s4w`
3. Imported Figma Slides file: `https://www.figma.com/slides/NQl63nHaqsaRFaPoBvkoOP`
4. Exported files: `About v3.deck.zip`, `About v3.pptx`, `About v3 (1).pptx`
5. Measurement source: `Atlas_AI_Technical_Drawing_and_Measurement_Report_COMPLETE_PACKAGE_v2_1_2330_13072026(4).zip`

## Source authority

- Gamma controls wording, card order, component hierarchy, source-specific colours, visual locations and warning language.
- The measurement package controls applicable fixed-slide geometry, recurring typography, spacing, borders and CTA tokens.
- Business v1 slide-specific geometry is an approved exemplar, not a universal layout for every Atlas draft.
- Contradictions are reported rather than silently merged.

## Method

Weighted scoring:

- Content fidelity to Gamma: 35%
- Visual and hierarchy fidelity to Gamma: 30%
- Alignment with applicable measurement tokens: 20%
- Editability and production quality: 15%

## Executive result

| File | Overall | Decision |
|---|---:|---|
| Recreated About v3 | 8.7 / 10 | Stronger production baseline; requires source-fidelity corrections and original visual insertion |
| Imported presentation | 8.4 / 10 | Stronger visual reference on six slides; not acceptance-ready because Slide 5 overflows and several elements are rasterized |

The recreated file should remain the technical baseline. The imported file should be treated as the preferred visual and asset reference, not as the final production file.

## Exported file comparison

`About v3.pptx` and `About v3 (1).pptx` render as the same seven-slide design. They are not separate design alternatives.

- Both are 16:9 and contain the same visible copy, positions and placeholder design.
- `About v3 (1).pptx` contains 19 additional small raster support images used for lines and accents.
- These extra images do not produce a material visual difference.
- `About v3.deck.zip` identifies the file as `About v3`, exported at `2026-07-16T07:40:09.692Z`.

## Recreated About v3 findings

### Strengths

- Seven native 1920 × 1080 slides.
- Complete Gamma source copy is present.
- 104 px safe margins and 1712 px content width are used consistently on the principal content slides.
- Slide 2 uses 840 px columns with a 32 px gap and a consistent three-row grid.
- Roboto Slab and Roboto are used as required by the Atlas measurement system.
- Highlight panel `#476FD6`, primary blue `#3257B8`, navy `#15213F`, border `#CFD2D8` and warning surfaces are correctly applied.
- Native editable text, cards, buttons and placeholders are retained.
- No detected top-level bounds failure or text clipping.

### Material deviations

1. **Slide names are currently numeric** (`1`–`7`). This contradicts the prior validation log stating that descriptive slide names were corrected.
2. **Slide 3 hierarchy diverges from Gamma.** Gamma uses a vertical five-stage steps-with-icons sequence; the reconstruction converts it into five horizontal cards.
3. **Slide 7 hierarchy diverges from Gamma.** Gamma uses a left-aligned closing composition; the reconstruction applies a centred Business v1-style closing layout.
4. **Unapproved source additions are present:**
   - Slide 3: `En dokumentert kjede fra forståelse til forvaltning.`
   - Slide 4: `Dokumentert leveransespor`
   - Slide 7: `Atlas AI — konkrete arbeidsflyter, tydelige grenser og sporbart ansvar.`
5. **Visual parity remains incomplete.** Original Gamma hero, offer images, provider diagram and icons are represented by placeholders.
6. **Measurement deviations:**
   - Slide 1 H1 is 62 px instead of the 72 px display token.
   - CTA text is 28 px instead of 36 px.
   - Slide 7 CTA gap is 20 px instead of 16 px.
   - Plain section labels use white fill and blue borders, although Gamma uses plain text labels and the measurement profile calls for transparent labels.
7. Cards and labels are more angular than the Gamma source, reducing source-specific visual similarity.

## Imported Figma presentation findings

### Strengths

- Seven native 1920 × 1080 slides.
- Gamma wording, order, source images and icons are substantially preserved.
- Slides 1, 2, 3, 4, 6 and 7 are visually closer to Gamma than the recreated file.
- Slide 3 preserves the vertical process sequence.
- Slide 4 preserves all three offer images and source card hierarchy.
- Slide 6 preserves the source icons and rounded card treatment.
- Plain section labels and left-aligned closing composition are source-faithful.

### Critical defects

1. **Slide 5 fails bounds validation.** The blue panel extends below the 1080 px canvas and the closing quote/accent are positioned at approximately y 1110–1118, entirely outside the slide.
2. **Slide 5 typography is severely undersized.** Principal body and list text is approximately 10.7–17.3 px, materially below the 20–30 px Atlas range and not presentation-safe.
3. **Typography is Inter Regular throughout**, not the required Roboto Slab / Roboto Atlas pairing.
4. **CTA controls on Slides 1 and 7 are raster/image elements rather than native editable text controls.** The visible primary CTA also appears cropped, showing `Se hvordan Atlas arbeide` rather than the full `Se hvordan Atlas arbeider`.
5. Several cards, icons, lines and controls are image-fill frames, reducing editability and semantic structure.
6. Slide names are numeric (`1`–`7`).
7. Heading sizes and spacing vary substantially from the approved recurring token system.

## Slide-by-slide scores

| Slide | Recreated | Imported | Preferred basis |
|---|---:|---:|---|
| 1 — Hero | 8.8 | 8.5 | Recreated geometry; imported original visual |
| 2 — Utgangspunktet | 9.5 | 9.2 | Recreated geometry; imported label/card styling |
| 3 — Atlas-modellen | 8.1 | 9.1 | Imported hierarchy and icons, rebuilt natively |
| 4 — Tilbud | 8.3 | 9.2 | Imported visual hierarchy and images; remove added status text |
| 5 — Hva Atlas er | 9.1 | 5.2 | Recreated structure; imported provider image only |
| 6 — Prinsipper | 9.1 | 9.2 | Imported rounded styling/icons, rebuilt with Atlas fonts/tokens |
| 7 — Closing CTA | 8.0 | 8.4 | Imported left alignment; recreated native CTA controls |

## Recommended controlled correction

Use a hybrid correction of the existing recreated Figma file:

- retain its native editable geometry and Slide 5 implementation;
- insert the imported file's original Gamma assets;
- restore Gamma's vertical Slide 3 hierarchy;
- restore Gamma's left-aligned Slide 7 hierarchy;
- remove the three unapproved added text items;
- correct Slide 1 H1, CTA text sizes and Slide 7 CTA gap;
- restore plain/transparent source-appropriate labels;
- use native editable CTA text and controls;
- apply descriptive slide names;
- rerun deterministic bounds, clipping, overlap, typography, content and visual QA.

This remediation recommendation is **PENDING_REVIEW** until explicitly approved for implementation.

## Validation classification

- Observed defects, content differences and geometry findings: **AUTO_APPROVED**
- Recommended hybrid design implementation: **PENDING_REVIEW**

## Boundary

This review validates design reconstruction only. It does not approve public launch, production availability, commercial policy, provider relationships, legal/compliance claims, security posture or Managed Secure production status.