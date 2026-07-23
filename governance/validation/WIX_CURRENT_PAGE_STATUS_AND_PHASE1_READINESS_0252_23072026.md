# Atlas AI Wix Current Page Status and Phase 1 Readiness — 02:52, 23.07.2026

**Site:** Atlas-AI  
**Wix site ID:** `1448ccad-68f0-43ea-8f0e-c9d8c0366082`  
**Primary locale:** Norwegian  
**URL rule:** English slugs; English display names in the English locale  
**Site state:** Draft  
**Publication performed:** No  
**Release decision:** **NO-GO**

## 1. Scope

This reassessment reads the current Wix Translation Content page titles and editor children after the latest page cleanup and naming changes. It cross-checks the current Wix bodies against the approved Atlas GitHub governance record, the current Google Drive presentation-ranking evidence, and the canonical Figma Slides sources for About v3, Trust v3, Onboarding v3 and Platform Lanes v3.

The user confirmed that no website sections have yet been replaced. Therefore the earlier body-level defects remain applicable except where new About and Trust content has been imported or obsolete shells have been removed.

## 2. Current inventory

- 25 named Wix page entities, excluding the master page.
- 16 pages contain editor child content.
- 9 pages are empty shells.
- All inspected translation-content records are unpublished.
- The prior 34-page empty-shell inventory has been materially reduced.

### Verified empty pages

- Casestudier
- DBA - Avtalevilkår
- Demo-bibliotek
- FAQ
- Informasjonskapsler
- Personvernerklæring
- Retningslinjer for bruk
- Tilgjengelighetserklæring
- Vilkår

## 3. Critical current contradiction

The Wix entity titled **Kontakt** (`z08w5`) contains the complete **About v3 / Om Atlas AI** body. Its content includes `OM ATLAS AI`, the Atlas model, offers, provider boundary, principles and About CTAs. It is not Contact content.

This means:

1. About content now exists but is attached to the wrong page identity.
2. A valid Contact page is still missing.
3. Title, route, body source, CTAs and metadata are not aligned.

**Corrective rule:** A page is not canonical merely because its title or body exists. Readiness requires title, route, locale name, source body, CTA targets and metadata to identify the same page role.

## 4. Current populated-page ranking

Method: 0–10, weighted 45% claim/canonical alignment, 20% visual/source-structure proxy, 15% readability, 20% sales/conversion. Rendered Wix visual and responsive quality remains unverified, so visual scores are provisional source-structure proxies.

| Rank | Current Wix page | Score | Current status | Primary blocker |
|---:|---|---:|---|---|
| 1 | Oppstart | 8.90 | Strong controlled draft | Form routing, consent, retention, notifications and error states unvalidated; placeholders remain |
| 2 | Plattform | 8.79 | Strong canonical candidate | Rename to Plattformspor; remove placeholders; current provider validation required |
| 3 | Tillit | 8.72 | Strong canonical draft | Visible manual-validation notes and asset placeholders; CTAs and claims require release validation |
| 4 | Tjenester | 8.23 | Strong hub with targeted edits | Duplicate package/provider detail and internal production notes |
| 5 | Student AI - Tjenester | 8.19 | Strong gated Student v3 body | Canonical name, proposed prices, providers, age, entitlement and activation gates |
| 6 | Privatperson - Pakker | 8.09 | Strong gated Consumer v3 body | Canonical name, Family/provider/entitlement/payment/privacy gates |
| 7 | Ressurser | 7.90 | Good structure, incomplete library | No verified public assets or working resource destinations; placeholders remain |
| 8 | Kontakt — About body | 7.66 | High-quality About content under wrong identity | P0 title/route/body mismatch; actual Contact page absent |
| 9 | Priser | 7.59 | Good structure, commercial draft only | Numeric pricing, VAT, usage, providers, support and activation unapproved |
| 10 | Juridisk | 7.50 | Good legal navigation structure | No approved versioned legal documents or working public links |
| 11 | Bedrift AI - Tjenester | 6.75 | Useful legacy body; rewrite required | Upload invitations, integration implications and blanket GDPR/security wording |
| 12 | Team Arbeidsområde | 6.68 | Useful concepts; merge required | Operational workspace, secure-channel, support and service implications |
| 13 | Privatperson AI - Tjenester | 6.23 | Obsolete legacy duplicate | Legal/financial framing, uploads, speed and unsupported functionality |
| 14 | Atlas Plattformen | 6.08 | Obsolete productisation | Operational platform, integration, logging, traceability and security implications |
| 15 | Hjem | 5.84 | Full replacement required | Superlatives and unsupported performance, compliance, storage, traceability, integration and support claims |
| 16 | Managed Secure | 5.22 | Highest-risk page; hidden only | Operational identity, storage, logging, backup, incident, revocation, availability and SLA claims |

**Mean populated-page content score:** 7.40/10. This is not a release-readiness score.

## 5. Phase 1 page requirements

### Definitely required

1. **Kontakt** — create or repurpose a genuine low-risk Contact page with the correct Contact body, form entry point, privacy notice, consent, success/error states and route to Oppstart.
2. **Om Atlas AI** — no new copy is required, but the About v3 body currently under Kontakt must be renamed/reassigned to the canonical About identity and `/about/` route.

### Required under the currently approved route map unless formally consolidated

3. **Prosess / Slik arbeider Atlas** — no current page entity exists. Process content is present inside About and Onboarding, so a standalone page may be omitted only through an explicit approved consolidation decision with route/CTA updates. Until then, it remains a Phase 1 page gap.

### Existing pages requiring content, not additional page creation

- Personvernerklæring
- Vilkår
- Informasjonskapsler
- Retningslinjer for bruk
- Tilgjengelighetserklæring
- DBA - Avtalevilkår, if retained

These can be standalone approved pages or approved versioned documents linked from Juridisk. Additional duplicate legal shells should not be created.

### Not required for Phase 1

- provider-specific public pages for ChatGPT, Claude, Copilot, Gemini, Perplexity or Azure;
- Casestudier;
- Demo-bibliotek;
- FAQ as a standalone page;
- additional package/intake duplicates.

## 6. Overall assessment

- **Content quality across populated pages:** 7.40/10.
- **Information architecture:** 6.4/10 due mainly to the Contact/About identity defect, unresolved canonical names and remaining legacy duplicates.
- **Phase 1 release readiness:** 3.8/10 because no replacement rollout has started, all records remain unpublished, legal/commercial/form gates are incomplete, and rendered desktop/tablet/mobile QA has not been completed.

## 7. Priority sequence

1. Correct the Kontakt/About page identity before further route work.
2. Implement the approved Home replacement.
3. Keep Managed Secure hidden and replace operational claims with qualification-only wording.
4. Canonicalize Plattformspor, Studenter, Privatpersoner and Om Atlas AI names/routes.
5. Complete the remaining planned section replacements.
6. Create the genuine Contact body and bind/test the low-risk form.
7. Decide whether Prosess remains standalone or is formally consolidated.
8. Remove all visible `ASSET`, `icon`, `MANUELL VALIDERING`, `PENDING_REVIEW` and internal QA text.
9. Approve and connect legal documents; resolve pricing/provider/Family/entitlement gates.
10. Complete menu, route, redirect, metadata, multilingual, accessibility, responsive and link/CTA validation.
11. Complete G00–G22 and obtain explicit release approval.

## 8. Validation limitation

The Wix connector exposes editor-authored translation content but not a supported rendered Wix Studio visual audit or physical page-tree/menu mutation flow. Current visual scores are therefore source-structure proxies. Desktop, tablet and mobile layout quality, link targets, navigation and accessibility remain unverified until rendered QA is completed.

## Classification

- **AUTO_APPROVED:** verified page inventory, empty-page reduction, Contact/About identity defect, current content findings, ranking method and correction sequence.
- **PENDING_REVIEW:** standalone Process consolidation, commercial/pricing decisions, providers, Family/entitlements, legal text, public routes and production publication.