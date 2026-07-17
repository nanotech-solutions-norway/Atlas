# Student v3 Blue-Panel, Label and CTA Corrections

**Timestamp:** 12:01, 17.07.2026 Europe/Oslo  
**Figma:** https://www.figma.com/slides/I8mk7h7D2RtaRVoaZkPNRt  
**Gamma:** https://gamma.app/docs/8n0a8sr0yuuy672  
**Classification:** AUTO_APPROVED

## User instruction

- Correct the text treatment in the blue panels on Slides 3 and 7.
- Make every label border fit its rendered label text.
- Apply the approved button font, size and formatting.

## Source authority

1. Current user instruction.
2. Gamma Student v3 for exact wording and panel hierarchy.
3. Approved Atlas measurement profile and Student v3 reconstruction specification.
4. Approved content-fit and 150% blue-panel text rule established in the Atlas correction history.

## Slide 3 — Student Basic blue panel

The exact Gamma text was retained.

- Plan title: Roboto Slab SemiBold, 30 px, 125% line height, white.
- Price: Roboto SemiBold, 24 px, 125% line height, white.
- Description: Roboto Regular, 21 px, 150% line height, white.
- Five list items: Roboto Regular, 20 px, 150% line height, white.
- Text remains within the 840 × 520 px panel.

The Student Basic and Student Plus status labels were rebuilt as transparent, content-fit labels:

- height: 44 px;
- width: rendered text width + 28 px;
- horizontal padding: 14 px per side;
- border: 2 px;
- radius: 4 px;
- font: Roboto SemiBold, 18 px;
- Student Basic label: white text and white border on the blue panel;
- Student Plus label: blue text and blue border on the white panel.

Final status-label width: 264 px for 236 px rendered text.

## Slide 7 — institution-rules blue panel

The exact Gamma text was retained.

- Heading: Roboto Slab SemiBold, 30 px, 125% line height, white.
- Body: Roboto Regular, 22 px, 150% line height, white.
- Body is auto-height and remains fully contained with the approved internal margin.

## Global label-border rule

All visible section and status labels now use:

- transparent fill;
- 2 px border;
- 4 px radius;
- 44 px height;
- width = rendered text width + 28 px;
- Roboto SemiBold, 18 px.

Validated label widths:

- 283 px for `TIDLIG TILGANG — FORESLÅTT`;
- 250 px for `ET ANSVARLIG STUDIELØP`;
- 277 px for `VELG ETTER BRUKSMØNSTER`;
- 264 px for each `FORESLÅTT TIDLIG TILGANG` status label;
- 171 px for `BRUKSOMRÅDER`;
- 234 px for `AKADEMISK INTEGRITET`;
- 180 px for `TRYGGE GRENSER`;
- 313 px for `SKOLE- OG INSTITUSJONSREGLER`.

## CTA typography

All four Student v3 buttons use:

- Roboto SemiBold;
- 36 px font size;
- 44 px fixed line box;
- centered horizontal and vertical alignment;
- 78 px button height;
- 2 px border;
- 4 px radius;
- 16 px gap between paired buttons.

Source wording remains unchanged.

## Validation

**PASS**

- Exact Gamma blue-panel copy retained.
- Slide 3 description and all five list items use 150% line height.
- Slide 7 body uses 150% line height.
- Blue-panel text is fully contained.
- Every label is transparent and content-fit.
- Every label width equals text width + 28 px.
- All button typography and geometry match the approved tokens.
- Zero top-level out-of-bounds objects.
- Slides 1, 3, 7 and 8 were visually reviewed after correction.

## Boundary

This is a design and formatting correction only. It does not approve pricing, provider delivery, payment activation, age requirements, student eligibility or public availability.