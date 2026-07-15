# Atlas AI Approved Business Reference Comparison and 72-Slide Validation

**Timestamp:** 01:57, 15.07.2026 Europe/Oslo  
**Approved reference Figma:** https://www.figma.com/slides/QjAYZsGDVS2qxrCzj8TZIA  
**Reference Gamma:** Business v1 (`g_1fwdlwasdw96se3`)  
**Scope:** Students, Consumers, Pricing, Platform Lanes, Trust, Onboarding, Resources, About and Legal.

## Executive decision

**All 72 slides in the nine newly created Figma presentations pass the approved-reference structural and visual design-handoff gate.**

The live files were corrected directly. Each slide was checked programmatically and each complete eight-slide row was reviewed visually. Public implementation remains **NO-GO** until Wix, responsive, accessibility, SEO/AEO/GEO, legal, commercial, provider and security gates are completed.

## Reference hierarchy

1. Explicit user instructions and approved Atlas decisions.
2. Gamma for wording, section order, component type, source-specific colors and original visual location.
3. Approved Business Figma Slides file and measurement profile for reusable geometry and visual tokens.
4. Current Figma implementation evidence.
5. Earlier drafts and contextual reports.

Conflicts are recorded rather than silently merged.

## Approved global profile

| Property | Value |
|---|---|
| Canvas | 1920 × 1080 px |
| Side margin / content width | 104 px / 1712 px |
| Grid gap / card padding | 32 px / 32 px |
| Display / dense H1 | 72 px / 54 px |
| Body | 24–30 px |
| Card title / body | 27–30 px / 20–22 px |
| CTA height / text / gap | 78 px / 36 px / 16 px |
| Standard / accent stroke | 1 px / 2 px |
| Label | Transparent; text-hug; 14 px side padding; 2 px #3257B8 |

**Typography:** Roboto Slab Regular for primary headings, Roboto Slab SemiBold for card headings and Roboto for body/control text.  
**Colors:** `#15213F`, `#3257B8`, `#476FD6`, `#E9ECF2`, `#CFD2D8`, `#FFFFFF`.

## Deviations corrected

- Dark navy slide backgrounds replaced with white.
- Roboto Slab Bold headings replaced with the approved Regular hierarchy.
- Grey body copy `#4A5770` replaced with navy `#15213F`.
- Fixed-width filled labels rebuilt as transparent text-hug controls.
- Neutral card borders reduced to 1 px and radii to 6 px.
- Multi-card rows expanded to the 1712 px content width.
- Generic blue hero panels replaced with source-specific `behind` or `right` placeholders.
- CTA geometry standardised.
- Missing Students source maps added.
- `atlas/referenceValidation` added to all 72 slides.

## Hero layout resolution

The Business reference uses a behind-content visual. Gamma remains authoritative for original visual location:

- **Behind:** Students, Pricing, Platform Lanes, Trust, About.
- **Right:** Consumers, Onboarding, Resources, Legal.

Right-layout pages therefore reuse the Business typography, palette, borders, controls and spacing while retaining the source right-image position.

## Deck results

| Deck | Hero | Slides | Result | Figma |
|---|---|---:|---|---|
| Students | behind | 8 | PASS | https://www.figma.com/slides/tHWogSIF3M2EwAwVha1RAx |
| Consumers | right | 8 | PASS | https://www.figma.com/slides/7nNOkj1DEznfX8uEyuYYpA |
| Pricing | behind | 8 | PASS | https://www.figma.com/slides/mmgLii5WtDAWRGAvrWHZy1 |
| Platform Lanes | behind | 8 | PASS | https://www.figma.com/slides/y02fmtUiD5I4PRX5o9bsYD |
| Trust | behind | 8 | PASS | https://www.figma.com/slides/ChMMBp8Qpj7dnsunoySvOJ |
| Onboarding | right | 8 | PASS | https://www.figma.com/slides/o87PKhOWXYwqdbWh7SHUqI |
| Resources | right | 8 | PASS | https://www.figma.com/slides/AFkD8wwztw2rLTzkCj8o6S |
| About | behind | 8 | PASS | https://www.figma.com/slides/XG1k9njoNO6qzMuoHeFapE |
| Legal | right | 8 | PASS | https://www.figma.com/slides/Fzcnx2G7vIEbOF7RCJ1z2w |

## Validation evidence

- 72/72 slides are 1920 × 1080.
- 72/72 have zero visible out-of-bounds objects.
- 72/72 use white backgrounds and the approved palette.
- 54/54 applicable content slides use the approved labels.
- No visible body text uses `#4A5770`.
- No `#CFD2D8` neutral card retains a stroke above 1 px.
- 9/9 hero asset placeholders are present.
- 72/72 slides contain `atlas/sourceMap` and `atlas/referenceValidation`.
- 9/9 full-row contact-sheet reviews passed.

## Gamma review

The consolidated audit covers **160 Gamma cards/sections across 20 source files** and **72 source-to-slide mappings**. Students adds 32 audited source cards across Student v1, Student v2, Student Intake v2 and Responsible AI Study Guide v2.

Unsupported prices, quotas, checkout, entitlements, legal approvals, provider rights, runtime implementation, logging, automatic routing and public secure-production claims remain excluded or explicitly pending.

## Remaining gates

| Gate | Status |
|---|---|
| Figma approved-reference alignment | PASS |
| 72-slide structural/source validation | PASS |
| Full-row visual review | PASS |
| Gamma duplicate cleanup | MANUAL ACTION REQUIRED |
| Wix construction | OPEN |
| Responsive/accessibility/consent/SEO | OPEN |
| Pricing and commercial approval | PENDING_REVIEW |
| Legal approval | PENDING_REVIEW |
| Provider rights and delivery | PENDING_REVIEW |
| Managed Secure/Azure production evidence | PENDING_REVIEW |
| Public release | NO-GO |

## Classification

### AUTO_APPROVED

- Exact visual corrections against the approved reference.
- 72-slide geometry, typography, palette, label, border, card, CTA and placeholder validation.
- Students source-map correction.
- Reusable Figma recreation specification and validation-register updates.

### PENDING_REVIEW

- Prices, quotas, entitlements, tax, checkout and paid availability.
- Legal wording, effective dates, controller/processor details and ownership.
- Provider/model inclusion, delivery rights and current commercial terms.
- Managed Secure/Azure identity, logging, storage, residency and production status.
- Wix publication and public release.
