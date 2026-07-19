# Atlas AI Figma Full-Section Reanalysis, Heading/Spacing Correction and Content Revalidation — 01:42, 20.07.2026

## 1. Executive result

All seven Atlas AI replacement-section Figma files were reanalysed from source after the user identified two valid defects:

1. the heading hierarchy in the Home section deck was incorrect; and
2. the vertical spacing below headings in the Managed Secure section deck was incorrect.

The reanalysis did not stop at those two files. It covered all **30 slides** across Home, Solutions, Packages, Governance, Process, Managed Secure and Contact, with content cross-checking against the current Gamma sources and layout checks against the latest approved GitHub/Google Drive specifications.

**Final Figma design-handoff result: PASS — 30/30 slides.**

**Final deterministic issue count after correction: 0.**

**Wix Phase 1 public deployment result: NO-GO.** Figma compliance does not establish Wix binding, responsive behaviour, forms, accessibility, SEO, bilingual parity, legal/privacy readiness, provider eligibility, production availability or release approval.

This report supersedes `ATLAS_FIGMA_SECTION_CANONICAL_CROSSCHECK_ADJUSTMENT_AND_RANKING_0004_20072026.md` wherever the two reports conflict.

## 2. Source authority applied

1. Latest approved GitHub and Google Drive corrections.
2. `ATLAS_FIGMA_HEADING_HIERARCHY_VERTICAL_RHYTHM_AND_CONTENT_VALIDATION_CORRECTION_0142_20072026.md`.
3. Atlas AI Canonical Figma Recreation Specification v3.
4. Current Gamma sources in `Atlas AI - sections` for wording, order and section-specific hierarchy.
5. Atlas AI 3.0 and Business v1 as visual comparators.
6. Technical Drawing and Measurement Report v2.1 as historical measurement evidence.

The current approved CTA token remains 24 px text / 30 px line height / 78 px height. The historical 36 px CTA value is superseded.

## 3. Confirmed root causes

### 3.1 Home heading hierarchy

The prior validation treated the 72 px display token as suitable for every Home slide. That was incorrect.

Correct hierarchy:

- Home hero H1: 72 px.
- Home closing CTA H1: 72 px.
- Home ordinary content-slide H1: 54 px.
- Module, column and card headings: maximum 30 px.

### 3.2 Managed Secure heading spacing

The prior spacing checks relied partly on imported parent-frame geometry and generic nearest-node detection. Imported frames had excess height, so a visually incorrect gap could pass a structural check.

Correct measurement method:

- measure from rendered H1 text bottom;
- identify the approved semantic intro and first content element from Gamma/source order;
- exclude labels, full-slide backgrounds and wrapper frames;
- enforce 24 px H1→intro and 32 px intro→content, or 32 px H1→content where no intro exists.

### 3.3 Wider cross-deck findings

The full reanalysis identified the same pattern in several other files:

- ordinary module headings remained at 36 px in Solutions, Packages, Governance and Contact;
- some process, warning and bounded body text remained at 130% rather than the approved exact 150%;
- several decks had visually inconsistent H1→intro or intro→content spacing despite earlier PASS metadata.

All were corrected.

## 4. Canonical typography and spacing contract applied

| Element | Final rule |
|---|---|
| Canvas | 1920 × 1080 |
| Primary left margin | 104 px |
| Label border | x=104, y=58, h=44, transparent, 2 px blue stroke |
| Label text | x=118, y=69, Roboto SemiBold 18 px, exact 22 px line height |
| Content H1 | Roboto Slab Regular 54 px, left aligned |
| Home hero/closing H1 | Roboto Slab Regular 72 px, left aligned |
| Module/card heading | Roboto Slab, maximum 30 px |
| H1→intro | 24 px from rendered text bounds |
| Intro→first content | 32 px from rendered text bounds |
| H1→first content without intro | 32 px |
| Hero/closing body→CTA | 32 px |
| General content→CTA | 24 px |
| Bounded body line height | exactly 150% |
| CTA | 24 px text, 30 px line height, 78 px height |

## 5. File-level corrections and final results

### 5.1 Home — 7/7 PASS

Figma: https://www.figma.com/slides/pYqjywOP26KcONlLFpfSSQ

- Retained 72 px only on hero and closing CTA slides.
- Corrected slides 2–6 to 54 px H1.
- Reduced oversized module/column headings to 30 px.
- Rebuilt the slide-level vertical rhythm using rendered text bounds.
- Enforced exact 150% bounded body text.
- Preserved all Gamma-derived content, warnings and CTA wording.

### 5.2 Solutions — 2/2 PASS

Figma: https://www.figma.com/slides/AwXFzwDMiWMsygRJpV3Ej6

- Reduced the remaining 36 px module heading to 30 px.
- Converted all remaining 130% bounded/process text to 150%.
- Corrected H1→intro to 24 px and intro→content to 32 px on both slides.
- Preserved all pricing, provider-cost and manual-validation PENDING_REVIEW boundaries.

### 5.3 Packages — 4/4 PASS

Figma: https://www.figma.com/deck/iUlIgUQhmSPv2Tti4JWA25

- Reduced six remaining 36 px module headings to 30 px.
- Converted remaining 130% bounded text to 150%.
- Corrected intro and no-intro spacing on all four slides.
- Preserved delivery-level, student/consumer and Managed Secure qualification wording.

### 5.4 Governance — 6/6 PASS

Figma: https://www.figma.com/deck/GHRYg5KepItU2DNCSWbwTZ

- Reduced twelve remaining 36 px module headings to 30 px.
- Corrected the remaining release-gate body line height to 150%.
- Corrected vertical rhythm on all six slides, including the previously undersized release-gate intro.
- Preserved claims, legal-readiness, FAQ and bilingual-parity restrictions.

### 5.5 Process — 2/2 PASS

Figma: https://www.figma.com/slides/YqapmYRPdgngWFtT8UP8JA

- Converted seven remaining roadmap body fields from 130% to 150%.
- Corrected the customer-process H1→intro→content sequence.
- Moved the no-intro Phase 0–6 timeline to 32 px below the rendered H1.
- Preserved Phase 1 NO-GO wording and evidence-first status logic.

### 5.6 Managed Secure — 5/5 PASS

Figma: https://www.figma.com/slides/Iq2cGzkBoN4Xbwhvu0mZ7t

- Corrected every slide's H1, intro, warning, columns, diagram and CTA flow.
- Applied 24 px H1→intro and 32 px intro→content or H1→content spacing as applicable.
- Content-fitted warning/callout frames rather than relying on imported dimensions.
- Left-aligned editable decision-diagram headings.
- Retained Managed Secure as architecture-review-only and non-public.

### 5.7 Contact — 4/4 PASS

Figma: https://www.figma.com/slides/xHQOe7uKx2bmiPpgIxQAvA

- Reduced four remaining 36 px route headings to 30 px.
- Converted ten remaining process/warning fields from 130% to 150%.
- Corrected vertical rhythm on all four slides.
- Confirmed that uppercase `DETTE KAN SENDES INN` and `DETTE SKAL IKKE SENDES INN` were present; the earlier apparent mismatch was a case-sensitive audit artefact, not missing content.
- Preserved the low-risk-only/no-confidential-upload intake boundary.

## 6. Content validation against Gamma

| Deck | Gamma cards / Figma slides checked | Content result |
|---|---:|---|
| Home | 7/7 | PASS |
| Solutions | 2/2 | PASS |
| Packages | 4/4 | PASS |
| Governance | 6/6 | PASS |
| Process | 2/2 | PASS |
| Managed Secure | 5/5 | PASS |
| Contact | 4/4 | PASS |
| **Total** | **30/30** | **PASS** |

Validated content dimensions:

- H1 and intro wording;
- slide/card order;
- module and card headings;
- body copy and process steps;
- warnings and PENDING_REVIEW notices;
- CTA and route wording;
- low-risk intake and no-sensitive-upload restrictions;
- Managed Secure non-public qualification boundary;
- release and production NO-GO language.

No Gamma source needed modification. The Figma files were adjusted to the approved current Gamma content and Atlas governance boundaries.

## 7. Final deterministic validation matrix

| Check | Result |
|---|---:|
| Slides validated | 30/30 |
| Current Gamma content matched | 30/30 |
| Correct Home 72/54 heading hierarchy | PASS |
| Content H1 54 px | PASS |
| Module/card heading ≤30 px | PASS |
| H1→intro 24 px | PASS |
| Intro→content 32 px | PASS |
| No-intro H1→content 32 px | PASS |
| Exact 150% bounded body line height | PASS |
| CTA 24/30/78 token | PASS |
| Canonical label geometry | PASS |
| Headings left aligned | PASS |
| Remaining image-fill UI elements | 0 |
| Out-of-bounds visible elements | 0 |
| Text clipping defects | 0 |
| `atlas/sourceMap` present | 30/30 |
| `atlas/referenceValidation = PASS` | 30/30 |

Representative screenshots were reviewed after the final vertical-rhythm changes for Home, Solutions, Packages, Governance, Process, Managed Secure and Contact.

## 8. Updated section ranking

Method:

- canonical and claims alignment: 45%;
- visual execution: 20%;
- readability and hierarchy: 15%;
- sales/CTA effectiveness: 20%.

| Rank | Section | Canonical / claims | Visual | Readability | Sales / CTA | Weighted score |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Home | 9.9 | 9.7 | 9.7 | 9.8 | **9.81** |
| 2 | Managed Secure | 9.9 | 9.6 | 9.5 | 9.4 | **9.68** |
| 3 | Contact | 9.8 | 9.5 | 9.5 | 9.4 | **9.62** |
| 4 | Solutions | 9.7 | 9.4 | 9.4 | 9.2 | **9.50** |
| 5 | Packages | 9.7 | 9.4 | 9.4 | 9.1 | **9.48** |
| 6 | Process | 9.8 | 9.3 | 9.3 | 8.7 | **9.41** |
| 7 | Governance | 9.9 | 9.2 | 9.1 | 8.4 | **9.34** |

Governance remains last only under the commercial weighted rubric. It is the strongest control/evidence section but is deliberately dense and not conversion-led.

## 9. Slide/card-level updated ratings

### Home

1. Styrte KI-arbeidsflyter for reelt arbeid — 9.8
2. Fra enkeltbruk til styrt arbeidsflyt — 9.7
3. Resultatbaserte løsningsområder — 9.8
4. Team Workspace eller Managed Secure? — 9.7
5. Tillit før kjøp — 9.7
6. Slik starter en bedriftsleveranse — 9.6
7. Start med oppgaven — ikke modellnavnet — 9.8

### Solutions

1. Prismodell og leverandørkostnader — 9.5
2. Plattformvalg etter dokumentert kontekst — 9.5

### Packages

1. Seks resultatbaserte bedriftsområder — 9.5
2. Omfanget bestemmes etter behovsavklaring — 9.5
3. Kontrollerte student- og forbrukerspor — 9.4
4. Kvalifiseringskort — Arkitekturgjennomgang — 9.5

### Governance

1. Oppdatert styringskart — 9.4
2. Release-gate oversikt — 9.4
3. Hver offentlig påstand må kunne spores — 9.5
4. Juridisk og publiseringsmessig beredskap — 9.3
5. FAQ og answer-engine prinsipp — 9.3
6. Bilingual parity — 9.2

### Process

1. Kundens leveranseprosess — 9.5
2. Phase 0–6 med evidens før status — 9.4

### Managed Secure

1. Arkitekturgjennomgang for kontrollsensitive behov — 9.7
2. Når et kontrollert arkitekturspor kan vurderes — 9.6
3. Velg laveste tilstrekkelige kontrollnivå — 9.7
4. Hva som må dokumenteres før operativ beskrivelse — 9.6
5. Start med kontrollkravet — uten vedlegg — 9.7

### Contact

1. Lavrisiko kontaktkontrakt — 9.7
2. Riktig rute etter overordnet behov — 9.6
3. Når behovet kan kreve høyere kontroll — 9.7
4. Etter innsending — 9.5

## 10. Validation-process correction

During this session, intermediate Figma validation metadata was initially written with assumed future timestamps. The current Oslo time was then explicitly retrieved, and every affected slide was corrected to the verified timestamp:

`2026-07-20T01:42:00+02:00`

Future Atlas validation work must resolve the current user-local time before writing report titles or validation metadata.

## 11. Classification

### AUTO_APPROVED

- Exact user correction to Home heading hierarchy.
- Exact user correction to Managed Secure heading spacing.
- Rendered-text-bound spacing methodology.
- 54 px content H1 / 72 px Home hero and closing H1 rule.
- Maximum 30 px module/card heading rule.
- 24/32 px vertical-rhythm rule.
- Exact 150% bounded-body rule.
- Corrected case-aware content-validation logic.
- Verified timestamp-control rule.
- Validated Figma corrections and zero-issue reanalysis.

### PENDING_REVIEW

- Pricing and entitlement.
- Provider eligibility and subscription inclusion.
- Age, family and account model.
- Legal, privacy and security claims.
- Public availability, production status and release decisions.

## 12. Remaining Wix release blockers

- Wix Studio section insertion and page/CMS binding.
- Desktop, tablet and mobile breakpoint validation.
- Working CTA routes and audience routes.
- Tested low-risk contact/intake form, routing, spam and error handling.
- Accessibility, SEO and bilingual parity evidence.
- Approved legal, privacy, security and provider-disclosure text.
- Sanitised release evidence, rollback and explicit publication approval.
