# ATL-LRN-20260803-028 — Gamma-to-Figma validation must test component topology

**Timestamp/task:** 12:32, 03.08.2026 Europe/Oslo; detailed Kontakt and Juridisk v4 PPTX/Gamma/Figma review.  
**Classification:** `AUTO_APPROVED`.

## Issue observed

A deck can retain correct text, slide count, canvas size and in-bounds objects while still failing the source design because card/component structure has been collapsed.

## Root cause

Earlier validation treated text presence and geometric safety as sufficient proxies for Gamma fidelity. It did not require proof that forms, buttons, states, images, boxes, columns and badges existed as distinct visual components.

## Corrective rule

For every Gamma-to-Figma recreation or correction:

1. render the Figma or PPTX output and inspect every slide;
2. compare every Gamma card against the Figma slide for headings, subheadings, body copy, labels, buttons, images, boxes, shapes and states;
3. verify component topology separately from text parity;
4. verify all source paragraphs, including secondary/aside text that condensation may omit;
5. use approved public-language and terminology rules when Gamma contains internal implementation labels;
6. run independent post-write content-token, clipping and bounds validation;
7. inspect representative final renders at natural canvas size;
8. state image-parity limitations explicitly.

## Evidence/source

- User-supplied PPTX renders for Kontakt and Juridisk v4.
- Controlling Gamma IDs `wk2ngbae0pyn7c8` and `v5qbsp95v3tyrnd`.
- Corrected Figma keys `SjafXw83D5CISHOaKYncSn` and `LnGmSITkmM0pIad6mV9v55`.
- Validation `ATL-VAL-20260803-075`.

## Action taken

All 20 assessed slides were rebuilt in place and passed structural, content, clipping, bounds and visual validation.

## Unresolved item

Exact Gamma raster-image import remains unavailable in the current connector workflow; editable vector substitutions must not be described as pixel-identical.
