# ATLAS DECISIONS REGISTER

**Project:** Atlas Website / Atlas AI  
**Created:** 02:29, 25.07.2026 Europe/Oslo  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Repository path:** `governance/registers/canonical/`  
**Drive mirror:** https://drive.google.com/drive/folders/1cXjuJQONMu9lEDYqk6uc62SKJqnTWKiz

> **Authority rule:** The file is a canonical container. Each entry has its own classification. Only entries marked `CANONICAL`, `APPROVED`, or `AUTO_APPROVED` may be applied as governing instructions. `PENDING_REVIEW` entries are advisory and must not be represented as approved decisions.

## Decision schema

| Field | Requirement |
|---|---|
| Decision ID | Stable `ATL-DEC-YYYYMMDD-NNN` identifier |
| Decision | Exact governing choice |
| Scope | Systems, phases, routes or artifacts affected |
| Rationale | Why the decision exists |
| Evidence | Approved or verified source |
| Owner | Responsible decision owner |
| Review trigger | Event that requires re-evaluation |
| Status | `CANONICAL`, `APPROVED`, `AUTO_APPROVED`, `PENDING_REVIEW`, `SUPERSEDED` or `REJECTED` |

## Active decisions

| ID | Date | Decision | Scope | Rationale / evidence | Owner | Review trigger | Status |
|---|---|---|---|---|---|---|---|
| ATL-DEC-20260725-001 | 25.07.2026 | The active execution plan is the 11.07.2026 consolidated phase guide, supplemented by the 23.07.2026 website page roadmap. Separate June Phase 0–6 files are historical evidence. | All phases | Prevent phase-numbering conflicts and silent merges. | Project owner | Explicit replacement plan approved | `AUTO_APPROVED` |
| ATL-DEC-20260725-002 | 25.07.2026 | Source authority order is: explicit current user approval; approved/canonical decision register; approved governance records; current implementation evidence; official external sources; project reports; prior chat; labelled inference. | All systems and reports | Matches the Atlas learning protocol. | Project owner | User approves a revised hierarchy | `CANONICAL` |
| ATL-DEC-20260725-003 | 25.07.2026 | GitHub Markdown is the canonical register source. Drive mirrors the controlled files. Gamma, Wix and Figma may contain non-public reference/index artifacts but do not become competing canonical sources. | Governance registers | Prevent cross-platform drift. | Governance owner | Repository or operating model changes | `AUTO_APPROVED` |
| ATL-DEC-20260725-004 | 23.07.2026 | Phase 1 uses 14 canonical public page roles. The current Wix Studio tree contains 13 visible pages because a separate `Kontakt` page is absent. | Phase 1, Wix | Verified editor evidence and page roadmap. | Website owner | Current Wix editor tree changes | `AUTO_APPROVED` |
| ATL-DEC-20260725-005 | 25.07.2026 | Bokmål is the root-language experience and English is a reciprocal `/en/` localized mirror, not an independent tree. | Phase 1+, Wix, SEO | Approved website model. | Website owner | Explicit multilingual architecture change | `APPROVED` |
| ATL-DEC-20260725-006 | 25.07.2026 | Managed Secure remains qualification/architecture-review only until identity, private storage, logging, revocation, backup/restore, incident and acceptance evidence is approved. | Phase 1 and Phase 4 | Preserve the secure-delivery claim boundary. | Security owner | Phase 4/6 evidence pack approved | `CANONICAL` |
| ATL-DEC-20260725-007 | 25.07.2026 | Ordinary public Wix forms may collect low-risk qualification data only and must not request confidential or restricted files. | Phase 1, 2, 4, 6 | Atlas safety and privacy lock. | Privacy/security owner | Approved controlled secure-intake implementation | `CANONICAL` |
| ATL-DEC-20260725-008 | 25.07.2026 | No real-money betting, auto-betting, bookmaker execution, public write endpoint, frontend provider token or unapproved production availability is permitted. | Entire Atlas program | Preserved Atlas safety locks. | Project owner | Only explicit user-approved safety-posture change | `CANONICAL` |
| ATL-DEC-20260725-009 | 25.07.2026 | Content/design status must be reported separately from implementation, validation and release approval. | All audits and registers | Prevent false completion claims. | Validation owner | None; permanent quality-control rule | `AUTO_APPROVED` |
| ATL-DEC-20260725-011 | 25.07.2026 | Adopt the 13:01 pricing report as the approved commercial baseline: B2C 129/169/159/399 and the business/managed price book recorded in `governance/pricing/`. | Phase 0.5–5 | Explicit current user instruction. | Project owner | New explicit pricing approval or material provider/economic trigger | `APPROVED` |
| ATL-DEC-20260725-012 | 25.07.2026 | Public B2C delivery uses Atlas-managed APIs with hard caps; retail-seat resale/pass-through is prohibited. Copilot and Workspace Gemini are customer-owned licence lanes. | Phase 0.5–3 | Provider terms and current commercial evidence. | Product/legal owner | Provider terms change | `APPROVED` |
| ATL-DEC-20260725-013 | 25.07.2026 | Commercial price approval is separate from `publicAllowed`, `purchaseAllowed` and production activation. All remain false until evidence gates pass. | Phase 0.5–6 | Prevent approval-state conflation. | Release owner | Passed activation gate and written release approval | `CANONICAL` |
| ATL-DEC-20260725-014 | 25.07.2026 | Wix is the public/CMS/plan/order/member surface; provider routing, usage ledger, caps, reconciliation and secure controls remain external. | Phase 0–6 | Current Wix capability boundary. | Architecture owner | Approved architecture change | `APPROVED` |
| ATL-DEC-20260725-015 | 25.07.2026 | Use 25% as the controlled domestic Norwegian MVA planning baseline, but do not represent it as final treatment for every transaction. | Pricing, invoicing, checkout and accounting | Official Skatteetaten category guidance supports the rate; customer, jurisdiction, bundle and event treatment remains transaction-specific. | Tax/accounting owner | Signed offer/jurisdiction tax position or law change | `APPROVED_CONTROL` |
| ATL-DEC-20260725-016 | 25.07.2026 | Final MVA treatment requires completion of the offer/jurisdiction matrix, OSS decision, reverse-charge procedure, invoice/credit-note mapping, Wix tax tests and professional sign-off. | Phase 0.5, 3, 5 and 6 | Prevent a general rate assumption from being treated as complete tax implementation. | Tax/accounting owner | All applicable MVA-001–MVA-020 controls pass | `CANONICAL` |
| ATL-DEC-20260725-017 | 25.07.2026 | Adopt the consumer-law deep research prompt as the mandatory research scope for Norwegian consumer terms, withdrawal, cancellation, refunds, digital-service commencement and checkout. | Legal, pricing, Wix and release | Ensures complete primary-source and implementation analysis before drafting final terms. | Legal owner | Research pack completed and reviewed | `AUTO_APPROVED` |
| ATL-DEC-20260725-018 | 25.07.2026 | No Norwegian consumer checkout, paid immediate commencement or Wix Pricing Plan creation is permitted until the consumer-law pack, MVA treatment, Wix implementation and acceptance evidence are approved. | Phase 0.5–6 | Angrerettloven payment-obligation, commencement, withdrawal and durable-medium requirements are implementation gates. | Release/legal owner | LEG-001–LEG-020 and applicable MVA gates pass with written release approval | `CANONICAL` |
| ATL-DEC-20260726-019 | 26.07.2026 | Research completion may update only the private research/draft status. It must not change legal approval, professional-signoff, checkout, purchase, publication, activation or release states. | GitHub, Drive and Wix readiness metadata | Validated separation of research, implementation and release states. | Governance/release owner | Explicit approved state-model change | `AUTO_APPROVED` |
| ATL-DEC-20260726-020 | 26.07.2026 | Treat the four consumer subscriptions as continuing digital services and use the early-start/proportional-payment model drafted in the research pack. | Consumer terms and checkout | Primary-law research supports the model, but no Norwegian legal opinion exists. | Legal owner | Norwegian counsel approval or contrary authority | `PENDING_REVIEW` |
| ATL-DEC-20260726-021 | 26.07.2026 | Restrict initial self-service consumer checkout to Norway and keep all foreign consumer checkout disabled until destination-VAT and OSS/local-registration controls are approved. | Tax, checkout and launch countries | Reduces unresolved cross-border tax exposure; not yet explicitly approved as launch scope. | Project owner + tax adviser | Explicit scope approval and signed tax position | `PENDING_REVIEW` |
| ATL-DEC-20260726-022 | 26.07.2026 | Structure paid top-ups and boosts as fixed non-transferable Atlas service entitlements rather than generic stored-value credit. | Product, tax and refunds | Reduces ambiguity but still requires legal and tax classification. | Product/legal/tax owners | Signed top-up classification | `PENDING_REVIEW` |
| ATL-DEC-20260726-023 | 26.07.2026 | Future-proof checkout for the enacted electronic withdrawal function, but do not represent it as a current in-force requirement until commencement is verified. | Consumer portal and legal monitoring | 2026 amendment enacted; commencement not effective at research date. | Legal/product owner | Official commencement date | `PENDING_REVIEW` |

## Pending governance correction

`ATL-DEC-20260725-015` uses `APPROVED_CONTROL`, which is not one of the statuses defined by this register. The explicit current user instruction independently preserves the 25% working baseline for this session. Normalising the stored entry to `APPROVED` or another allowed status is `PENDING_REVIEW`; no silent change has been made.

## Superseded decisions

| ID | Superseded decision | Replacement | Status |
|---|---|---|---|
| ATL-DEC-20260725-010 | Public prices, MVA treatment, provider-delivery rights, plan allowances, Family conditions, legal interpretation, production routing and Managed Secure activation were collectively unresolved. | Prices and commercial controls are approved by ATL-DEC-20260725-011–014. MVA is governed by ATL-DEC-20260725-015–016. Consumer-law research and checkout locks are governed by ATL-DEC-20260725-017–018. Legal conclusions, provider contracts, Family/minor implementation, publication, checkout, routing and Managed Secure activation remain pending. | `SUPERSEDED` |