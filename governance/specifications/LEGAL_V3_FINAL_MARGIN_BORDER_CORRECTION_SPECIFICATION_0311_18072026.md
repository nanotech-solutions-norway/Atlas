# Atlas AI Legal v3 — Final Margin and Border Correction Specification

**Timestamp:** 03:11, 18.07.2026 Europe/Oslo  
**Figma:** https://www.figma.com/slides/WAVCUxiETXqzHFhriKVNKf  
**Gamma:** https://gamma.app/docs/Legal-v3-8zysfcnlqw6he4r  
**Classification:** Verified design and geometry corrections **AUTO_APPROVED**. Legal, privacy, provider, accessibility, contractual, compliance and public-availability matters remain **PENDING_REVIEW**.

## Purpose

This specification supersedes the margin and border conclusions in the earlier Legal v3 box-content validation where compliance was overstated. It records the final measured correction of outer margins, inter-box gaps, box-content padding, content-fit heights and border tokens in the existing native Figma Slides file.

## Governing instructions

- Canvas: 1920 × 1080.
- Side margins: 104 px.
- Content width: 1712 px.
- Standard grid gap: 32 px.
- Standard card and panel padding: 32 px.
- Content-fit rounding: 8 px grid where required.
- Standard cards: 1 px `#CFD2D8` border, 6 px radius.
- Blue panels: `#476FD6`, white text and 32 px padding.
- Manual-validation warnings: `#FFFBF5` fill, 2 px `#B45309` border, `#15213F` text.
- Higher-risk caution: `#FFF1F2` fill, 2 px `#B91C1C` border, `#15213F` text.
- Labels: transparent fill, 2 px `#3257B8` border, 4 px radius and 44 px height.
- Buttons: 78 px height, 2 px border, 4 px radius and Roboto SemiBold 24 px.

## Corrections applied

### Slide 2 — Privacy

- Expanded the supporting-card column to the correct 104 px right margin.
- Corrected the two supporting-card column widths and retained a 32 px inter-column gap.
- Corrected all five privacy cards to 32 px left and right content padding.
- Recalculated each privacy-card height from rendered title/body height plus 32 px top and bottom padding, rounded to the 8 px grid.
- Corrected the full manual-validation warning to 32 px horizontal content padding.

### Slide 3 — Terms and use

- Corrected the `PENDING_REVIEW` warning from 24 px to 32 px horizontal content padding.
- Retained 32 px separation from the topic-card row.

### Slide 4 — Acceptable use

- Corrected all icon positions from 28 px to 32 px from the card border.
- Recalculated all five topic-card heights using rendered content height plus 32 px top and bottom padding.
- Corrected the Family/account-sharing caution to 32 px horizontal content padding.

### Slide 5 — AI providers

- Recalculated the provider-boundary box from rendered title/body height and 32 px padding.
- Corrected the provider warning to 32 px horizontal padding and content-fit height.
- Retained the 32 px horizontal and vertical panel gaps.

### Slide 6 — AI disclaimer

- Recalculated the primary-source statement to content height plus 32 px padding.
- Final measured padding is 32 px horizontally and 33 px vertically due to 8 px-grid rounding.

### Slide 7 — Cookies, accessibility and contact

- Rebuilt the top module row to 104 px left and right margins.
- Corrected both top-row inter-module gaps from 64 px to 32 px.
- Corrected all five module content margins to 32 px.
- Recalculated each module to rendered content height plus 32 px top and bottom padding.
- Corrected the full manual-validation warning to 32 px on all four sides.

### Slides 1 and 8

- Slide 1 already complied with the label, CTA, notice, border and main content-margin requirements.
- Slide 8 retained its source-specific compact table-cell padding because the complete editable legal register and longest validation strings must remain readable on one slide. Table borders, content bounds and status wording were revalidated.

## Border treatment

Programmatic border inspection covered 110 relevant labels, buttons, cards, panels, warnings, icon placeholders, notices and table cells. No invalid border width, colour or radius was found after correction.

## Content fidelity

The complete live Gamma source was reread after adjustment. An exact visible-string comparison returned zero missing and zero unexpected source strings on all eight Figma slides. No `MANUELL VALIDERING KREVES` or `PENDING_REVIEW` wording was changed.

## Governance boundary

These corrections approve measured design geometry only. They do not establish legal approval, privacy compliance, WCAG compliance, provider authorization, contractual readiness, subscription readiness or public availability.