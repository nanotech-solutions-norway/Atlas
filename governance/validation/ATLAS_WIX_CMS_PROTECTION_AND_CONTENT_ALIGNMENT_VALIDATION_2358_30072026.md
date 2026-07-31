# Atlas Wix CMS Protection and Content Alignment Validation — 23:58, 30.07.2026

## 1. Control metadata

- **Project:** Atlas Website / Atlas AI
- **Wix site:** `Atlas-AI`
- **Wix site ID:** `1448ccad-68f0-43ea-8f0e-c9d8c0366082`
- **Wix state:** Draft
- **Engineering repository:** `nanotech-solutions-norway/atlas_wix`
- **Canonical governance repository:** `nanotech-solutions-norway/Atlas`
- **Primary locale assessed:** Norwegian Bokmål (`no`)
- **Release state:** `NO_GO`
- **Preserved controls:** `publicAllowed=false`, `purchaseAllowed=false`, `releaseApproved=false`

## 2. Scope

1. Protect internal Wix CMS authoring, evidence, validation and implementation records.
2. Resolve the stale Process page-plan record against current authenticated Wix and repository evidence.
3. Retrieve and assess current unpublished Wix Studio page text.
4. Compare page text with the latest approved/canonical Atlas records, the 29.07.2026 website-strategy report, the 27.07.2026 Trust copy pack, current Gamma Contact/FAQ sources and corrected Figma Contact/FAQ sources.
5. Produce a page-by-page remediation ranking without publishing or applying public copy.

## 3. CMS protection implementation

Authenticated post-change readback confirms the following collections now use `CMS_EDITOR` for read, insert, update and remove:

- `AtlasClaimsRegistry`
- `AtlasLegalDocs`
- `AtlasTrustTopics`
- `AtlasReleaseGates`
- `AtlasValidationGates`
- `AtlasPagePlan`
- `AtlasLocaleStrings`

The existing FAQ split remains intact:

- `AtlasFAQs`: `CMS_EDITOR` read/write — private authoring collection.
- `AtlasFAQsPublic`: `ANYONE` read and `CMS_EDITOR` write — controlled public rendering collection.

**Result:** `PASS_LEAST_PRIVILEGE_READBACK`

No public collection, page, form, pricing plan, checkout, payment, publication or runtime state was changed.

## 4. Process-page resolution

Current authenticated evidence establishes:

- no separate Process page exists in the Wix Studio translation/editor content index;
- no Process page-code entity exists in the current `atlas_wix` page inventory;
- ordinary occurrences of the word “prosess” remain only as explanatory prose;
- FAQ exists as a current Wix page and repository entity under the Resources role;
- the existing `AtlasPagePlan` Process record was stale.

The stale record was re-categorized in place to preserve audit history:

- **Title:** `FAQ`
- **Navigation group:** `Resources`
- **Slug:** `resources/faq`
- **State:** `EXISTING_REBUILD_CMS_BINDING_REQUIRED`
- **Control:** bind only `AtlasFAQsPublic`; preserve `AtlasFAQs` as private authoring.

Authenticated readback confirms the update.

**Result:** `PASS_STALE_PROCESS_ROLE_SUPERSEDED`

## 5. Current page-role inventory

Fifteen public-role candidates are represented in current Wix engineering evidence:

1. Home
2. Services / Solutions
3. Business
4. Students
5. Individuals
6. Platforms
7. Managed Secure
8. Pricing
9. Trust
10. Legal
11. Resources
12. FAQ
13. About
14. Contact
15. Getting Started

The Wix Members Area account-settings page is a system page and is excluded from the public-role count.

## 6. Evaluation method

The alignment score is a controlled readiness indicator, not a release score. It considers:

- role alignment with the current 15-page strategy;
- consistency with approved Atlas positioning;
- public-claim safety and evidence status;
- removal of internal QA instructions and placeholders;
- conversion clarity and audience priority;
- Norwegian language quality;
- CMS/source-of-truth readiness;
- distinction between proposed and operational capabilities.

## 7. Page-by-page content ranking

| Remediation rank | Page | Alignment | Primary finding | Recommended adjustment |
|---:|---|---:|---|---|
| 1 | Home | 15/100 | Contains unsupported operational and certification claims, including full GDPR compliance, Norway-only storage, ISO/SOC presentation, instant document processing and conflicting 73%/87% metrics. Positioning is generic “smart assistant” rather than the governed solution layer. | Complete rewrite. Lead with Norway-first governed AI adoption for real work; make Business primary; show controlled secondary lanes; remove every unapproved metric, certification, residency and runtime claim; use a qualification CTA. |
| 2 | Managed Secure | 22/100 | Describes identity, private storage, logging, revocation, backup and incident handling as tested or operational, contradicting the controlled Trust copy pack. Contains English terms and a typo (`MANAGE SECURE`). | Replace with the approved qualification-only copy: controlled architecture review for confidential workflows. State that production availability is not approved until exact controls are implemented and tested. CTA: request architecture review. |
| 3 | Business | 32/100 | Correct primary audience, but copy implies operational uploads, module activation, document processing, integrations and GDPR-safe delivery. | Reframe around business outcomes, three or four controlled work patterns, human review and a solution assessment. Remove live upload/activation language until runtime evidence exists. |
| 4 | Services / Solutions | 38/100 | Strong need-first principle, but mixes service architecture, personas, pricing, plans and internal terminology. Uses `vendor`, `runtime`, `pass-through`, `capped` and `scope`. | Convert to a short solution-navigation page organized by work need and control level. Move pricing detail to Pricing and persona detail to audience pages. Use Norwegian terms and one primary qualification CTA. |
| 5 | Pricing | 42/100 | Correctly labels plans as proposed, but publishes unresolved entitlement mechanics, two student plans, Family concepts, provider functionality, internal validation markers and monthly-usage mechanics. | Present pricing logic only: business pricing after qualification; student/private concepts not purchasable; no automatic paid overage. Remove unresolved plan cards, Family entitlement text and all internal QA markers. |
| 6 | Contact | 52/100 | Uses the newer Contact source and correct low-risk principle, but contains version labels, implementation requirements, duplicated category sets, routing-state specifications and validation notes as visitor text. | Replace the implementation brief with a concise user page. Use the corrected Figma wording: necessary name/email allowed; prohibit sensitive, confidential, security-critical and unnecessary personal data. Keep no-file-upload and separate secure routes. |
| 7 | Legal | 55/100 | Governance intent is sound, but the public draft contains `PENDING_REVIEW`, `MANUELL VALIDERING KREVES`, implementation instructions and empty-document-table specifications. | Show only approved, effective documents from a sanitized public index. Hide unavailable documents and retain draft/review metadata in the private `AtlasLegalDocs` collection. |
| 8 | Students | 58/100 | Responsible-use controls are strong, but Student Basic/Plus conflicts with the later merge decision. Minimum age 16 is not clearly foregrounded. Internal launch controls and a literal Gamma asset placeholder remain. | Use one controlled student lane, age 16+, focused on planning, explanation, repetition, note structure and source verification. Remove two-plan entitlement language, placeholder assets and activation mechanics. |
| 9 | Individuals | 60/100 | Safety boundaries are useful, but Family appears as an unresolved consumer entitlement despite later reclassification. Internal manual-validation markers remain. | Keep a limited individual-use lane. Remove Family as a public consumer product until separately approved; remove entitlement/payment mechanics; use explicit boundaries for health, legal, financial and emotional-dependency use. |
| 10 | FAQ | 68/100 | Current copy is mostly aligned with the latest Gamma/Figma source and correctly states Managed Secure, sensitive-data and no-purchase boundaries. It is static, duplicated in places and CMS binding is not proven. | Bind the page exclusively to `AtlasFAQsPublic`, promote only approved records from `AtlasFAQs`, remove duplicate static blocks and validate schema eligibility, locale parity, links and rendering. |
| 11 | Trust | 70/100 | Core message is aligned and avoids broad promises, but internal manual-validation notes and technical drafting instructions remain visible. It does not fully use the newer Trust copy-pack structure. | Adopt the current H1 and lead from the controlled Trust copy pack; add provider/location/retention disclosures; remove internal QA text; link only approved evidence and public legal records. |
| 12 | Resources | 72/100 | Appropriate support role, but literal Gamma asset placeholders remain and the page risks becoming a generic document archive. | Remove placeholders. Curate a small set of task-based guides, checklists and FAQs that support the business qualification funnel. Use owner, review date and public-status metadata. |
| 13 | About | 76/100 | General solution-layer framing is directionally correct, but company identity, ownership and boundaries can be clearer. A trailing-space page-name defect exists in generated engineering evidence. | Explain Atlas AI as an NTSN-operated governed solution layer, distinguish it from model providers, and describe human responsibility. Correct the page name in Wix Studio—not by renaming generated code files. |
| 14 | Platforms | 80/100 | Correctly places platform selection after need, data and control assessment. Some vendor-centric and English terminology remains. | Retain structure; simplify to environment, work need, data class and governance fit. Explain that provider selection depends on validated configuration and agreement. |
| 15 | Getting Started | 84/100 | Best-aligned funnel page: low-risk qualification, minimal disclosure and controlled next step. | Keep distinct from Contact. Remove any residual implementation language, validate actual form fields/routing, and state clearly that submission is not an order or delivery commitment. |

## 8. Cross-site corrections

### Remove from public page layers

- bracketed asset placeholders;
- `PENDING_REVIEW` and `MANUELL VALIDERING KREVES` markers;
- implementation specifications and runtime-state descriptions;
- version labels such as `v1.1` unless intentionally shown as document metadata;
- unresolved commercial, entitlement and plan mechanics;
- unsubstantiated certification, residency, compliance, security, availability and performance claims.

### Preserve as private evidence

- claim review status;
- source references;
- evidence requirements;
- implementation actions;
- owners and approvers;
- release and validation gates;
- unpublished legal and security notes.

## 9. Norwegian language normalization

Use `Atlas AI` as the brand, but prefer `KI`, `KI-løsning`, `KI-verktøy` and `KI-bruk` in Norwegian body copy. Recommended replacements include:

| Current wording | Recommended Bokmål |
|---|---|
| AI-løsning | KI-løsning |
| compliance | etterlevelse / etterlevelse av regelverk |
| solution review | løsningsgjennomgang |
| scope | omfang |
| vendorlisenser | leverandørlisenser |
| runtime / runtimekostnader | drift / driftskostnader |
| pass-through | viderefakturert etter avtale |
| capped | med avtalt kostnadstak |
| support | brukerstøtte |
| incident-håndtering | håndtering av sikkerhetshendelser |
| backup | sikkerhetskopi |
| revocation | tilbakekalling av tilgang |
| sign-off | faglig godkjenning |
| reseller | videreselger |
| data residency | hvor data behandles og lagres / datalokasjon |
| ghostwriting | skrivearbeid på vegne av studenten |

Use active verbs, short sentences, direct address and explanations for unavoidable technical terms.

## 10. Validation results

| Check | Result |
|---|---|
| Seven recommended internal collections protected | PASS |
| Private/public FAQ split preserved | PASS |
| Process page exists | NO |
| Stale Process page-plan record corrected | PASS |
| Fifteen public page roles represented | PASS_ENTITY_COVERAGE |
| Current Wix design-time copy retrieved | PASS_UNPUBLISHED_EDITOR_CONTENT |
| Current Gamma Contact/FAQ source reviewed | PASS |
| Corrected Figma Contact/FAQ source reviewed | PASS |
| Latest Drive strategy and Trust copy reviewed | PASS |
| Literal asset placeholders absent | FAIL |
| Internal QA text absent from public page drafts | FAIL |
| Claims aligned with approved evidence | FAIL_HOME_MANAGED_SECURE_BUSINESS |
| Student structure aligned with latest decision | FAIL_TWO_PLAN_LEGACY |
| Family public entitlement aligned | FAIL_LEGACY_CONCEPT |
| Norwegian terminology normalized | PARTIAL |
| Responsive/rendered validation | NOT_PERFORMED_REQUIRES_STUDIO_PREVIEW |
| Publication or release | NOT_PERFORMED / NO_GO |

## 11. Required controlled sequence

1. Approve the page-content remediation order and final public claims.
2. Produce page-specific Bokmål copy manifests from approved sources.
3. Remove internal QA text and placeholder assets from Wix page layers.
4. Bind FAQ and other governed public content only to sanitized public collections.
5. Apply text changes in Wix Studio/Local Editor or through approved CMS/Velo bindings.
6. Validate desktop, tablet and mobile rendering; accessibility; links; forms; locales; SEO metadata and structured-data parity.
7. Re-read the exact Studio text and compare against approved manifests.
8. Keep publication blocked until all acceptance gates pass.

## 12. Classification

### AUTO_APPROVED

- exact CMS permission hardening and successful readback;
- stale Process-to-FAQ page-plan correction;
- verified current page/entity inventory;
- identification of placeholders, internal QA leakage, stale plans and unsupported claims;
- Norwegian terminology and workflow quality improvements;
- no-release-effect validation.

### PENDING_REVIEW

- final public page wording and commercial positioning;
- removal or selection of public claims;
- final plan/pricing presentation;
- public legal and security statements;
- final page/menu labels and routes;
- any publication, purchase, payment or production decision.

## 13. Preserved safety locks

- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
- No Wix publication.
- No payment, checkout or plan activation.
- No public write endpoint.
- No frontend provider token.
- Release remains `NO_GO`.
