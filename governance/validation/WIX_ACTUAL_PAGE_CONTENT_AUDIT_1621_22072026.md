# Atlas AI Wix Actual Page Content Audit — 16:21, 22.07.2026

**Site:** Atlas-AI  
**Wix site ID:** `1448ccad-68f0-43ea-8f0e-c9d8c0366082`  
**Wix state:** Draft  
**Publication performed:** No  
**Release decision:** Phase 1 public deployment remains **NO-GO**.

## 1. Scope and evidence method

This audit reads the actual Wix editor-authored translation-content entities for the Atlas-AI draft and maps each page-level parent entity to its rich-text and button children. A named entity is counted as content-bearing only when it has child editor components. A title without child content is treated as an empty shell.

The actual Wix text was cross-checked against:

- the approved Atlas Figma Home replacement deck;
- Business v1;
- Student v3;
- Consumer v3;
- Platform Lanes v3;
- the final 30-slide replacement-section validation;
- the 72-slide Phase 1 reference validation;
- the current GitHub governance and release-readiness records;
- the current Google Drive replacement map and validation reports.

### Limitation

Wix returned an editor preview URL, but the available browser environment could not open the authenticated Wix Studio preview. Therefore this is a definitive editor-content inventory and claim audit, but not a screenshot, responsive-layout, navigation, link-target or rendered-visual audit. The connector still does not expose a supported physical page-tree/menu mutation API.

## 2. Executive inventory

- **15 page entities contain actual child editor content.**
- **34 named page-like entities contain no child editor content.**
- The master page contains four global elements and is excluded from the page count.
- App, form and system entities are excluded from page counts.
- Every inspected page-content record is `UNPUBLISHED`.
- The current draft contains a mixture of June legacy pages, July Figma/Gamma imports, duplicate shells and obsolete provider/product pages.

The earlier 02:19 assessment identified eight existing concepts and seven pages to create. This is now superseded as a content inventory: the July import created or populated several previously missing page concepts, but did not complete route, menu, metadata, responsive or release validation.

## 3. Content-bearing pages

| Wix title / entity | Actual content | Alignment | Required disposition |
|---|---|---|---|
| **Hjem** (`fca96`) | Legacy commercial homepage with multi-engine, security, compliance, Norwegian storage, traceability, integration, support and speed claims | Low | **Full content replacement** with the validated seven-slide Home source |
| **Tjenester** (`apybc`) | Outcome-led Solutions hub, business areas, audience routes, platform criteria, packages and onboarding | High–medium | Keep hub; remove duplication, placeholders and unapproved commercial/provider detail |
| **Bedrift AI - Tjenester** (`d99p7`) | Business use cases, document workflows, integrations, packages and onboarding | Medium–low | Rewrite to Business source; remove upload, blanket GDPR/security and integration promises |
| **Student AI - Tjenester** (`w82qg`) | Legacy student services, writing, planning, source tools, quizzes and dashboards | Medium | Consolidate into the newer Student page and retire this duplicate |
| **Privatperson AI - Tjenester** (`zlu3k`) | Legacy consumer services, planning, contracts, budgeting, dashboards and rapid setup | Low | Consolidate into Consumer v3 page; remove legal, upload and speed claims |
| **Atlas Plattformen** (`d2eh6`) | Combined workspace/product presentation with controls, integrations, logging and Managed Secure | Low | Major rebuild or retire; split between Platform Lanes and Trust |
| **Plattform** (`aqstt`) | Near-faithful Platform Lanes v3 import | High | Canonicalize as Platform Lanes; remove visible placeholders/internal notes; validate providers |
| **Team Arbeidsområde** (`kqy5x`) | Shared workspace, roles, knowledge, QA, provider disclosure and support | Medium | Merge into Business AI/delivery model; remove operational, secure-channel and support commitments |
| **Managed Secure** (`svaub`) | Qualification logic plus operational security, storage, audit, backup, revocation, incident and SLA claims | Low/high risk | Keep hidden; retain architecture review only; remove/future-condition all operational claims |
| **Priser** (`zh53r`) | Delivery levels, numeric proposed prices, provider-cost separation and qualification | Medium–high structure, unapproved commercial content | Keep draft/non-indexed; suppress numeric/commercial claims until approval |
| **Ressurser** (`taa7b`) | Resource hub and planned guides for businesses, students and consumers | Medium–high structure, no actual assets | Render no resource cards until approved assets exist; remove placeholders/internal notes |
| **Juridisk** (`zczrr`) | Legal-center structure, privacy/terms/AUP/AI-limitations summaries and document-register fields | High as a placeholder structure; no approved legal documents | Keep hidden/non-indexed; publish only approved versioned legal texts and links |
| **Frame 1** (`ts3wz`) | Low-risk qualification/onboarding, audience and data-class routing, stop rules and collect/do-not-collect lists | High | Rename **Onboarding**, move under Contact, bind/test form and remove internal notes |
| **Frame 1** (`oa5lc`) | Near-faithful Student v3 import with proposed Basic/Plus plans, prices, provider functions and integrity controls | High structure, gated commercial content | Rename **Students**; consolidate legacy Student page; keep controlled until gates pass |
| **Privatperson - Pakker** (`owrex`) | Near-faithful Consumer v3 import with Everyday Basic/Family, prices, safety and privacy boundaries | High structure, gated commercial/Family content | Rename **Consumers**; consolidate legacy consumer page; keep controlled until gates pass |

## 4. Detailed corrections by populated page

### 4.1 Hjem — full replacement required

Actual Wix content includes:

- “Norges smarteste AI-assistent”;
- “presise svar – hver gang”;
- “ATLAS AI MULTI-ENGINE”;
- dedicated Norwegian customer success;
- ISO 27001, SOC 2 Type II, GDPR Article 28 and DPA statements;
- Norwegian data storage and EEA-only claims;
- full traceability and logging of all AI actions;
- integrations and sector-specific model framing;
- upload/report-in-seconds promises;
- student writing/plagiarism and personal dashboard claims;
- obsolete CTA “Utforsk pakker”.

**Correction:** replace the page body with the validated Home source: governed workflows, six outcome areas, qualified Team Workspace/Managed Secure distinction, trust-before-purchase, controlled delivery process and low-risk qualification. Remove all superlatives, blanket performance, security, compliance, data-residency, traceability, support, integration and speed claims. Change the CTA to “Utforsk løsninger”.

### 4.2 Tjenester — retain as canonical Solutions hub

The page contains genuine substantive copy and is the strongest current hub. It includes the solution-layer comparison, outcome-led areas, buyer routes, pricing logic, provider-selection criteria and conversion content.

**Correction:** keep the outcome-led architecture, but remove duplicate package and provider detail that belongs on Pricing and Platform Lanes. Use capability classes rather than permanent provider/model promises. Keep Managed Secure qualification-only. Remove all `[ASSET-...]`, `icon`, `[MANUELL VALIDERING KREVES]` and other internal production notes from visitor-facing content.

### 4.3 Bedrift AI - Tjenester — rewrite

The page includes useful business tasks and workflow framing but also invites document/contract/report uploads and implies ready integrations with Microsoft 365, Google Workspace, Slack, Teams, CRM, ERP and APIs. It uses blanket GDPR/security wording and legacy package selection.

**Correction:** use Business v1 as the content contract, retain outcome areas and human-control boundaries, prohibit public file uploads, qualify all integrations and exports, and route first contact to low-risk solution review. Numeric prices, support and provider inclusion remain PENDING_REVIEW.

### 4.4 Student AI - Tjenester — duplicate legacy page

This page contains study planning, explanations, note structure, academic writing, source checks, exam preparation, APA, source-library and dashboard claims.

**Correction:** consolidate into the newer Student v3 import (`oa5lc`) and retire or redirect this page. Remove unsupported APA/source-library/dashboard availability. Preserve academic-integrity, independent source verification, institutional-policy and age/provider/entitlement gates.

### 4.5 Privatperson AI - Tjenester — duplicate legacy page

This page contains planning, budgeting, contract interpretation, legal-rights examples, dashboards, reminders, file upload/paste instructions and an “under two minutes” setup claim.

**Correction:** consolidate into Consumer v3 (`owrex`). Remove legal interpretation/advice, financial-decision framing, public file-upload instructions, speed claims and unsupported dashboard/reminder functionality. Preserve no-emergency, no-companion and regulated-decision boundaries.

### 4.6 Atlas Plattformen — unsafe productisation

This page presents Atlas as a combined operational workspace with modules, knowledge, granular roles, logging, full traceability, Norwegian-requirement alignment, integrations, custom APIs and Managed Secure.

**Correction:** do not present an operational platform unless evidenced. Split provider-selection content into Platform Lanes and governance/control concepts into Trust. Remove or future-condition access, logging, storage, integration, audit and Managed Secure capability claims. Prefer retiring this page after canonical routes are ready.

### 4.7 Plattform — canonical Platform Lanes candidate

This is a close import of Platform Lanes v3: environment/data/licence/control assessment, conditional provider tracks, Microsoft/Google prerequisites, multi-engine source/budget/review/fallback and no permanent engine promise.

**Correction:** rename to Platform Lanes, place under Solutions, replace `[ASSET-...]` and `icon` placeholders, and move internal manual-validation notices out of the visible page. Validate current provider features, terms, processor roles, licences, costs and availability immediately before any public release.

### 4.8 Team Arbeidsområde — merge rather than publish standalone

This page contains shared configuration, knowledge base, roles, prompts/templates, QA, provider disclosure and cost separation. It also implies an available workspace, secure transfer/contact and recurring support/service expectations.

**Correction:** merge the useful concepts into Business AI and Pricing delivery levels. Remove secure-channel, SLA/support and operational workspace claims unless separately approved and evidenced.

### 4.9 Managed Secure — highest-risk page

The page combines valid architecture-review content with assertions that identity controls are verified, private storage is isolated, full activity logging is active, revocation timing is tested, backups are established, incident routines exist and Azure orchestration/protected artifacts are available.

**Correction:** keep hidden, non-indexed and architecture-review-only. Retain qualification criteria, lower-risk alternatives, evidence requirements and future acceptance gates. Remove or explicitly future-condition every operational security, storage, backup, logging, incident, availability, SLA and production claim until G20, G21 and explicit production approval pass.

### 4.10 Priser — real draft content, not approved offer content

The page contains Starter, Professional, Research/Multi-Engine, Business Workspace and Managed Secure delivery levels, with proposed prices from NOK 60,000, NOK 120,000, NOK 150,000 plus usage and NOK 300,000/year.

**Correction:** keep draft/non-indexed. Numeric prices, MVA treatment, provider cost separation, usage budgets, support and activation remain PENDING_REVIEW. Use the page structure only after commercial approval. Remove visitor-facing internal notes and asset placeholders.

### 4.11 Ressurser — content shell, not a resource library

The page includes sound source-grounded principles and proposed resources, but the resources are described as planned and no approved assets/working URLs are demonstrated. The CMS correctly records `assetExists=false` and `publicAllowed=false` for current resources.

**Correction:** keep the hub structure but render no resource cards until each item has an actual asset, owner, version/date, reviewed claims, attribution and working URL. Remove `icon`, `[ASSET-...]` and manual-validation text from the visitor layer.

### 4.12 Juridisk — structure only

The page correctly explains that summaries do not replace final legal text and contains document-register fields. It does not contain approved versioned legal documents or working public links and visibly contains dashes, PENDING_REVIEW and manual-validation notes.

**Correction:** keep hidden/non-indexed. Publish only after each document has approved wording, document name, version, effective date, owner, audience, approval status and public URL. Consolidate the many empty legal shells beneath this legal center rather than creating duplicate indexable pages.

### 4.13 Onboarding / qualification (`ts3wz`) — strong content, incomplete implementation

The page contains low-risk qualification, audience selection, high-level need/data classification, a stop rule for personal/sensitive/confidential information, collect/do-not-collect lists and control-sensitive routing.

**Correction:** rename from “Frame 1” to Onboarding, place under Contact, bind the revised Wix form, implement and test the stop rule, route outcomes and error states. Remove internal notes and proposed-plan wording from public content. Family/student age rules and any later controlled channel remain PENDING_REVIEW. Form consent, retention, notifications and backend routing remain unvalidated.

### 4.14 Students (`oa5lc`) — faithful design import, gated product

The page closely follows Student v3 and includes a responsible study journey, Student Basic/Plus, proposed NOK 119/169 pricing, planned ChatGPT/Claude functionality, academic-integrity controls, institutional rules and early-access qualification.

**Correction:** rename from “Frame 1” to Students and use this as the canonical student route. Remove or suppress proposed prices/provider names until approved. Remove placeholders and internal validation text. Keep non-indexed/non-public until age, institution, provider, entitlement, payment, usage and activation gates pass.

### 4.15 Consumers (`owrex`) — faithful design import, gated product

The page closely follows Consumer v3 and contains practical tasks, Everyday Basic/Family, proposed NOK 149/349 pricing, planned ChatGPT/Claude functionality, emergency/medical/legal/economic/companion boundaries and privacy principles.

**Correction:** rename to Consumers and use this as the canonical consumer route. Remove or suppress numeric prices/provider functions until approval. Family entitlement, age, guardian model, member administration, conversation separation, account-owner visibility, shared usage, consent, payment and privacy remain PENDING_REVIEW. Remove all placeholders/internal notes and keep controlled until gates pass.

## 5. Empty page-like shells — no editor child content

### 5.1 Canonical Phase 1 gaps

- **Om Oss** — About has no page body.
- **Kontakt** — Contact has no page body; the form and onboarding content do not make the Contact page complete.
- **Trust** — no populated Trust/Governance page exists in the current content-bearing inventory.
- **Process** — no populated Process page exists in the current content-bearing inventory.

These four canonical pages still require actual content implementation from the approved Figma/replacement sources.

### 5.2 Duplicate or obsolete commercial/audience shells

- Bedrift - Pakker
- Student - Pakker
- legacy duplicate Priser
- Privatperson - Inntak
- Studenter - Inntak
- Standard Kvalifikasjon
- Oppstart

These should be archived, deleted or redirected after canonical destinations are implemented and tested.

### 5.3 Empty provider/product shells

- ChatGPT
- Claude
- Copilot
- Gemini
- Perplexity
- Azure Sikkerhet

Do not create standalone indexable provider-product pages. Consolidate conditional provider information under Platform Lanes and Trust.

### 5.4 Empty legal/privacy/security shells

- Personvern
- Personvernerklæring
- Vilkår
- Informasjonskapsler
- DBA - Avtalevilkår
- Tredjepartsopplysninger
- Retningslinjer for bruk
- Tilgjengelighetserklæring
- AI Begrensninger
- Informasjonsbehandling
- Sikkerhet (two shells)
- Sikkerhetsstruktur
- Ansvarlig AI

Keep these non-public until the legal architecture and approved documents are finalized. Avoid duplicate indexable Trust/Legal content.

### 5.5 Empty content-program shells

- FAQ
- Casestudier
- Guider
- Demo-bibliotek
- Læringsplatform

Do not expose these in menus or search until real reviewed content and working destinations exist.

## 6. Contradictions and supersession

1. The 19 July audit correctly found eight page concepts at that time/API scope. The current editor-content inventory now shows 15 populated parent pages because July imports added substantial page bodies. The old “seven pages missing” statement is superseded for content existence, but not for route/menu/render readiness.
2. The 30/30 replacement-section Figma PASS and 72-slide reference PASS are design-handoff validations only. They do not prove Wix page implementation, correct routing, responsive rendering, form operation or release readiness.
3. Current CMS planning records describe a clean 15-page contract, while the actual Wix editor contains duplicate legacy pages, “Frame 1” titles, obsolete provider pages, empty shells and visible internal production notes. The CMS contract must not be treated as proof of actual page completion.
4. Contact, About, Trust and Process remain actual content gaps despite the broader July imports.

## 7. Priority correction sequence

1. Keep the entire site Draft; do not publish.
2. Freeze/export the current editor state and create a route/content replacement checklist.
3. Replace Home immediately; it has the broadest unsupported public claims.
4. Keep Managed Secure hidden and strip operational capability assertions.
5. Canonicalize the faithful July pages: Platform Lanes, Pricing, Resources, Legal, Onboarding, Students and Consumers.
6. Consolidate and retire duplicate legacy Student, Consumer, Atlas Platform and Team Workspace pages.
7. Create and bind About, Contact, Trust and Process.
8. Remove all visitor-visible `[ASSET-...]`, `icon`, `[MANUELL VALIDERING KREVES]`, `[PENDING_REVIEW]`, em-dash placeholders and internal QA instructions.
9. Delete/archive empty duplicate, provider, legal and content-program shells or keep them explicitly hidden until approved.
10. Implement actual menu nesting, routes, redirects, metadata, canonical URLs, hreflang, Open Graph and structured data.
11. Bind and test the low-risk form, consent, retention, notifications, routing, error states and no-upload boundary.
12. Run rendered QA at 1440, 1200, 1024, 768, 390 and 320 pixels, including accessibility, performance, links and CTAs.
13. Complete applicable G00–G22 evidence and record explicit release approval.

## 8. Classification

### AUTO_APPROVED

- exact editor-content inventory and page-content counts;
- identification of empty and duplicate shells;
- identification of visible placeholders/internal notes;
- verified correction of unsupported claims by removing or qualifying them;
- consolidation of duplicate provider/audience/legal page concepts;
- keeping unvalidated pages non-public and non-indexed;
- the correction workflow and validation sequence.

### PENDING_REVIEW

- pricing, MVA, provider functions/rights/costs and usage;
- subscriptions, entitlements, payment, activation and support/SLA commitments;
- legal/privacy document content and interpretation;
- student, consumer, Family, age and guardian rules;
- Managed Secure operational availability and security claims;
- routes, redirects, publication and production release.

## 9. Final decision

The Wix draft contains substantial real content, but **content existence is not completion**. Only Platform Lanes, Onboarding, Students and Consumers are close to their governing Figma text; all still contain placeholders or gated claims. Home, Atlas Plattformen and Managed Secure require the largest corrections. Contact, About, Trust and Process lack actual page bodies. Phase 1 remains **NO-GO** until the canonical page set is implemented, duplicates are resolved, claims are corrected, forms/routes are tested and launch-gate evidence is complete.
