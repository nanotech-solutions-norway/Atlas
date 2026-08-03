# ATL-ERR-20260803-030 — Figma component-topology collapse in Kontakt and Juridisk v4

**Observed:** 03.08.2026  
**Status:** Corrected for the two assessed decks  
**Classification:** `AUTO_APPROVED`

## Observed defect

The user-supplied `Kontakt v4` and `Juridisk v4` PPTX exports and the corresponding live Figma Slides files preserved many principal text strings but collapsed nearly every Gamma content card into one oversized generic panel and one compressed text block. No image objects were present. Forms, buttons, warnings, success/error states, numbered cards, metadata boxes, cookie controls, footer columns and status badges were absent or collapsed.

## Root cause

The initial recreation normalized Gamma cards into generic editable panels. Validation focused on slide count, text presence, 1920×1080 dimensions and object bounds, which did not prove component topology or visual equivalence.

## Impact

The decks could be misclassified as validated even though their visible structure, hierarchy and interaction representation did not match the controlling Gamma drafts.

## Corrective action

- Rebuilt all 9 Kontakt and 11 Juridisk slides in place.
- Preserved slide IDs, counts and order.
- Restored all required source copy and component structures.
- Restored the omitted Juridisk privacy paragraph.
- Ran content-token, bounds, clipping and visual-render validation.

## Corrective rule

Future Gamma-to-Figma validation must include rendered exported-output inspection and component-topology checks for cards, images, fields, buttons, states, columns and badges. Text/count/bounds validation alone is insufficient.

## Evidence

- Detailed validation: `governance/validation/ATLAS_KONTAKT_JURIDISK_V4_DETAILED_PPTX_GAMMA_FIGMA_VALIDATION_1232_03082026.md`
- Kontakt Figma key: `SjafXw83D5CISHOaKYncSn`
- Juridisk Figma key: `LnGmSITkmM0pIad6mV9v55`

## Remaining boundary

Exact Gamma raster-image parity remains partial; editable vector illustrations were substituted for the two hero concepts. Public release remains `NO_GO`.
