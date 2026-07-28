# ATLAS PROJECT LOG UPDATE PACK — FAQ GAMMA DRAFTS — 11:42, 28.07.2026

## Timestamp

11:42, 28.07.2026 Europe/Oslo

## Session/task

Create two separate, current and implementation-aware Phase 1 FAQ webpage alternatives in Gamma, using the Atlas AI Phase 1 design system and the live Wix `AtlasFAQs` collection as the content baseline.

## Issue or mistake observed

1. FAQ had become the fifteenth approved Phase 1 public page role, and its Wix CMS foundation was prepared, but no dedicated FAQ webpage draft existed in Gamma or Figma and no current Wix Studio FAQ page had been validated.
2. The live CMS contained eight current Bokmål draft records and eight older English seed records with incomplete one-to-one language parity.
3. Earlier Atlas SEO/AEO/GEO planning referred to `FAQPage` structured data where eligible. Current Google Search documentation dated 15.06.2026 no longer lists FAQ as a supported Search rich-result feature. The page must therefore rely on visible, helpful, answer-first content and must not promise FAQ rich results, AI inclusion or ranking gains.

## Root cause

- FAQ was added to the canonical Phase 1 page tree after the earlier 14-page design coverage was prepared.
- CMS preparation advanced before a dedicated Gamma/Figma webpage contract was created.
- Legacy English seed content and current Bokmål content were created at different times and were not yet reconciled into reciprocal language parity.
- Provider search-display capabilities changed after the earlier consolidated discoverability blueprint.

## Corrective rule

1. Use exact paired naming: `FAQ v1.0` and `FAQ v1.1`.
2. Treat v1.0 as the completeness/control reference and v1.1 as the preferred public-facing base.
3. Use the Atlas AI 3.1 Icebreaker fluid-webpage system: white backgrounds, Atlas-blue surfaces, structured cards, restrained icons, generous whitespace, limited decorative imagery, clear actions and explicit warnings near sensitive-data boundaries.
4. Use current locale-matched Wix CMS records as the primary FAQ copy source. Legacy or unmatched entries are review inputs, not approved public facts.
5. Keep direct answers visible, concise and useful. Do not create schema-only questions or internal SEO questions for public users.
6. Do not claim provider partnerships, permanent model features, certifications, public availability, guaranteed rankings, rich results or generative-search inclusion.
7. Preserve `publicAllowed=false`, `purchaseAllowed=false`, `releaseApproved=false` and `NO_GO` until Figma, Wix Studio, claims, bilingual, accessibility and release evidence passes.

## Evidence/source

- Canonical decision `ATL-DEC-20260727-032` in `governance/registers/canonical/ATLAS_DECISIONS_REGISTER.md`.
- Live authenticated Wix collection readback: `AtlasFAQs`, 16 records, 8 Bokmål draft entries and 8 legacy English review-required entries; all `publicAllowed=false`.
- Google Drive: `Atlas AI Phase 1 FAQ CMS Update — 23:11, 27.07.2026`.
- Google Drive: `Atlas AI Website Phase Page Roadmap — 13:23, 23.07.2026`.
- Gamma Phase 1 source: `Resources v3`, theme `icebreaker`, webpage format, fluid dimensions.
- Prior approved drafting/ranking rules: claim/canonical alignment 45%, visual/source-structure quality 20%, readability 15%, sales/conversion/user value 20%; v1.1 preferred, v1.0 completeness/control reference.
- Current official Google Search guidance:
  - https://developers.google.com/search/docs/appearance/ai-features
  - https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
  - https://developers.google.com/search/docs/appearance
  - https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Current W3C accordion and keyboard guidance:
  - https://www.w3.org/WAI/ARIA/apg/patterns/accordion/
  - https://www.w3.org/WAI/WCAG22/Understanding/keyboard-accessible.html

## Action taken

Created and read back two separate Gamma webpages in the `Atlas AI - Contact` folder:

1. `FAQ v1.0`
   - https://gamma.app/docs/FAQ-v10-t8v4s3365l9qkjd
   - Completeness/control-oriented structure.
   - Seven content sections plus the generated version cover.
   - Covers the eight current Bokmål FAQ topics, audience/age boundary, platform/cost disclosure, data boundary, Managed Secure qualification boundary, student integrity and controlled next steps.

2. `FAQ v1.1`
   - https://gamma.app/docs/FAQ-v11-ptr7hc9q7c59dt1
   - Preferred public-facing candidate.
   - Search-first and audience-routing structure with quick answers, grouped detailed answers, trust boundaries and route-aware conversion.
   - Adds the approved consumer-safety boundary while preserving all current CMS answers and release controls.

Both drafts use:

- Norwegian Bokmål;
- Gamma `icebreaker` theme;
- webpage format;
- fluid dimensions;
- restrained Phase 1 visuals;
- answer-first copy;
- explicit no-sensitive-data warnings;
- no provider-specific feature promises or unsupported availability claims.

## Validation performed

| Check | Result |
|---|---|
| Exact paired naming | PASS — `FAQ v1.0` and `FAQ v1.1` |
| Target Gamma folder supplied | PASS — `Atlas AI - Contact` folder ID used for both generations |
| Theme/layout | PASS — `icebreaker`, webpage, fluid dimensions |
| Gamma readback | PASS — both pages accessible and complete |
| Live Wix CMS cross-check | PASS — 16 records read; eight current Bokmål questions reflected |
| Current age boundary | PASS — minimum age 16; 16–17 activation remains controlled |
| Public-form safety boundary | PASS — low-risk only; no sensitive uploads |
| Managed Secure claim boundary | PASS — qualification/architecture review only |
| Provider/price volatility | PASS — no fixed provider features or prices added |
| Search/ranking claims | PASS — no guarantee of rankings, rich results or AI inclusion |
| Secrets/customer-sensitive data | PASS — none included |
| Wix/Figma implementation | NOT PERFORMED |
| Public release | NO_GO; locks preserved |

## Unresolved items

1. Select or hybridise the final FAQ v2.0 candidate after comparative ranking.
2. Transfer the selected page into Figma and validate responsive geometry, keyboard/focus states and accordion interaction.
3. Create and bind the Wix Studio pages at `/resources/faq/` and `/en/resources/faq/`.
4. Filter the Wix dataset by locale, `phase=PHASE_1`, `pagePlacement=resources_faq`, approved review status and `publicAllowed=true`.
5. Reconcile Bokmål/English one-to-one parity and review all claims, privacy, security, provider, commercial and student wording.
6. Decide whether any structured data remains useful and supported at implementation time; maintain exact visible-content parity and do not promise a rich result.
7. Replace placeholder Gamma button links and the visual search prototype during Figma/Wix implementation.
8. Complete accessibility, responsive, metadata, canonical, hreflang, internal-link, performance and release acceptance testing.

## Classification

- Draft creation, live CMS cross-check, naming, design-system alignment, readback and preserved safety controls: `AUTO_APPROVED`.
- Final public copy, bilingual parity, structured-data choice, Figma/Wix implementation and release: `PENDING_REVIEW` / `NO_GO`.

## Release controls after task

- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
- Checkout, real payments, production entitlements and public Managed Secure availability remain disabled.
