# Atlas AI Kontakt and Juridisk v4 Detailed PPTX–Gamma–Figma Validation — 12:32, 03.08.2026

**Validation ID:** `ATL-VAL-20260803-075`  
**Scope:** `Kontakt v4` and `Juridisk v4` Figma Slides files, their user-supplied PPTX exports, and the controlling Gamma v4 drafts.  
**Classification:** Verified defect assessment and correction `AUTO_APPROVED`; public release remains `NO_GO`.

## Source identity

| Source | Identifier | Slides/cards | Integrity / role |
|---|---|---:|---|
| User-supplied Kontakt export | `Kontakt v4.pptx` | 9 | SHA-256 `fcf76b65840630563595cc7393fcd70c09d34ca7d9d7aa5cdef8989070f53bab`; pre-correction evidence |
| User-supplied Juridisk export | `Juridisk v4.pptx` | 11 | SHA-256 `43d16433aa0b9f96e2c256879b8457007a2e660336348d2dab6fb1db23727f9d`; pre-correction evidence |
| Kontakt Gamma | `wk2ngbae0pyn7c8` | 9 | Controlling copy/hierarchy/design evidence |
| Juridisk Gamma | `v5qbsp95v3tyrnd` | 11 | Controlling copy/hierarchy/design evidence |
| Kontakt Figma | `SjafXw83D5CISHOaKYncSn` | 9 | Corrected editable design artifact |
| Juridisk Figma | `LnGmSITkmM0pIad6mV9v55` | 11 | Corrected editable design artifact |

## Pre-correction finding

The PPTX render and live Figma readback showed the same systematic defect:

- Kontakt slide 1 contained 10 auto-shapes and no raster image; slides 2–9 each contained only three auto-shapes: one large rounded panel and two text shapes.
- Juridisk slide 1 contained 10 auto-shapes and no raster image; slides 2–11 each contained only three auto-shapes: one large rounded panel and two text shapes.
- No slide in either exported deck contained an image object.
- Nearly every content slide placed all copy into one compressed text block with a fixed 20 px text-node height while most of the panel remained empty.
- Gamma card topology was therefore not preserved: forms, buttons, warning/success/error states, numbered cards, metadata boxes, cookie controls, footer columns, status badges and image layouts were absent or collapsed.

This was a visual/component fidelity failure even though the principal text strings were mostly present.

## Authority and conflict handling

Gamma controlled the card order, section purpose and supplied public copy. Higher-authority approved Atlas rules controlled public labels and terminology. Therefore:

- Gamma internal label `Validation messages` was rendered as public Bokmål `Valideringsmeldinger`.
- Gamma internal label `Shared Status Labels` was rendered as `Statusmerker`.
- Gamma internal footer labels such as `Global Footer` were not exposed as public page headings; the public Atlas footer identity was used.
- Gamma was not modified.

## Kontakt v4 slide-by-slide result

| Slide | Gamma requirement | Pre-correction defect | Correction applied | Result |
|---:|---|---|---|---|
| 1 | Atlas header, navigation, `Oppstart`, `English`, hero image treatment | Text-only configuration slide; no image | Rebuilt header/navigation/buttons and added editable contact/form illustration matching the Gamma image intent | PASS |
| 2 | `Kontakt Atlas AI.` lead plus prominent sensitive-data warning | One empty panel and lead text only; warning absent | Added contained lead card and separate warning state | PASS |
| 3 | Complete contact form: labels, helper copy, category options, consent, warning and submit button | Entire form reduced to one text block; no fields, categories, warning card or button | Created editable form fields, category pills, consent panel, warning notice and `Send henvendelse` button | PASS |
| 4 | Five separate validation-message boxes with side-line treatment | Five messages collapsed into one text block | Created five numbered outlined cards with side lines; applied `Valideringsmeldinger` | PASS |
| 5 | Success state with confirmation aside | Plain text in generic panel | Created green success state, icon, heading and confirmation copy | PASS |
| 6 | Caution/error state | Plain text in generic panel | Created red/caution error state, icon and separated message hierarchy | PASS |
| 7 | Full footer with shortcuts, legal links, company and disclaimer | Only company summary retained | Restored three-column footer with all links and responsibility text | PASS |
| 8 | Cookie explanation, three action buttons, category boxes and save action | Only button labels shown as one sentence | Restored complete cookie-control layout and category cards | PASS |
| 9 | Explanatory status paragraph plus five solid status labels | Labels collapsed into one sentence | Restored paragraph and five distinct badges | PASS |

## Juridisk v4 slide-by-slide result

| Slide | Gamma requirement | Pre-correction defect | Correction applied | Result |
|---:|---|---|---|---|
| 1 | Atlas header, navigation, buttons and legal-document image-right layout | Text-only configuration slide; no image | Rebuilt header/navigation/buttons and added editable versioned-document illustration | PASS |
| 2 | Legal intro with document/version visual hierarchy | One generic panel and lead text | Added structured intro card, accent rule and versioned-document visual | PASS |
| 3 | Six numbered legal-document cards | Six titles collapsed into one text block | Created six numbered cards in a two-column grid | PASS |
| 4 | Nine metadata boxes plus change-summary aside | Metadata collapsed into one text block | Created 3×3 metadata grid and separate change-note panel | PASS |
| 5 | Two company/contracting-party paragraphs | Copy present but unstructured | Created two-column entity/contracting-party layout with full supplied copy | PASS |
| 6 | Three complete privacy paragraphs | Third paragraph was missing; first two collapsed | Restored all three paragraphs and added privacy/shield visual | PASS |
| 7 | Two-column necessary/optional cookie layout with complete copy | Three sentences collapsed into one block | Rebuilt blue necessary panel and light optional panel with headings and complete copy | PASS |
| 8 | Two terms/status paragraphs | Copy collapsed into one block | Restored paragraph hierarchy and source-derived status tags | PASS |
| 9 | Full footer, legal links, company and warning disclaimer | Only company summary retained | Restored complete footer columns and disclaimer | PASS |
| 10 | Cookie explanation, three actions, four boxes and save button | Only action labels retained | Restored complete cookie UI including necessary note and save control | PASS |
| 11 | Status explanation plus five labels | Labels collapsed into one sentence | Restored paragraph and five distinct badges | PASS |

## Visual and structural validation

Post-write Figma readback covered all 20 slides.

- Slide counts remained 9 and 11; no slide was deleted or recreated.
- Existing slide IDs and deck order were preserved.
- All required Gamma-derived content tokens were found after correction.
- All 20 slides passed out-of-bounds validation.
- All 20 slides passed text-within-parent clipping validation.
- Representative renders were inspected at natural 1920×1080:
  - Kontakt: header, form, footer and cookie controls.
  - Juridisk: header, metadata grid, cookie overview and cookie controls.
- Typography is consistently Roboto Slab Bold for headings and Roboto for body/UI copy.
- Atlas blue/ink/light-panel design roles and consistent borders/radii were applied.

## Image boundary

The controlling Gamma hero cards reference generated raster images. The available connector workflow did not provide a reliable direct import of those exact raster bytes into the existing Figma Slides files. The corrected hero slides therefore use editable Atlas-styled vector illustrations representing the same contact-form and controlled-legal-document concepts. They are intentionally not represented as pixel-identical copies of the Gamma raster images.

## Final status

- `Kontakt v4`: `PASS_CONTENT / PASS_COMPONENT_TOPOLOGY / PASS_LAYOUT / PASS_VISUAL_REVIEW`.
- `Juridisk v4`: `PASS_CONTENT / PASS_COMPONENT_TOPOLOGY / PASS_LAYOUT / PASS_VISUAL_REVIEW`.
- Exact Gamma raster-image parity: `PARTIAL / EDITABLE_VECTOR_SUBSTITUTION`.
- Gamma artifacts: unchanged.
- Wix implementation and production release: not affected.

`NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.
