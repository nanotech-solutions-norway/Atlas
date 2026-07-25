# PROJECT LEARNING LOG

**Project:** Atlas Website / Atlas AI  
**Created:** 02:29, 25.07.2026 Europe/Oslo  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Repository path:** `governance/registers/canonical/`  
**Controlled branch:** `agent/canonical-governance-registers-20260725`  
**Drive mirror:** https://drive.google.com/drive/folders/1cXjuJQONMu9lEDYqk6uc62SKJqnTWKiz  

> **Authority rule:** The file is a canonical container. Each entry has its own classification. Only entries marked `CANONICAL`, `APPROVED`, or `AUTO_APPROVED` may be applied as governing instructions. `PENDING_REVIEW` entries are advisory and must not be represented as approved decisions.

## Purpose

Capture reusable Atlas lessons from verified corrections, mistakes, implementation findings, provider limitations, source conflicts and validated workflow improvements.

## Entry requirements

Every entry must include:

- timestamp and task;
- issue or observation;
- root cause;
- corrective rule;
- evidence/source;
- action taken;
- validation performed;
- unresolved items;
- classification.

Do not store secrets, API keys, credentials, customer-sensitive data, bank/accounting records or private commercial information.

## Learning entries

### ATL-LRN-20260725-001 — Canonical register layer must exist as files

- **Timestamp/task:** 02:29, 25.07.2026 Europe/Oslo; Phase 0–6 completeness audit and governance bootstrap.
- **Issue observed:** The July governance baseline prescribed six exact canonical files, but they were not present on the active `main` branch or in the controlled Drive source folder under their prescribed names.
- **Root cause:** Setup instructions, historical branches, general validation spreadsheets and project-log packs were treated as substitutes for operational canonical registers.
- **Corrective rule:** The six prescribed filenames must exist in GitHub and be mirrored to the controlled Drive source folder. References to setup instructions or superseded branches are not sufficient.
- **Evidence/source:** `08_Atlas_AI_Governance_Source_Authority_Claims_and_Learning_Baseline_1135_11072026`; Atlas Phase 0–6 audit dated 25.07.2026.
- **Action taken:** Created the six canonical containers and a final-tree compliance matrix.
- **Validation performed:** Exact filename readback required in GitHub and Drive after write-back.
- **Unresolved items:** Merge approval for the controlled GitHub branch.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260725-002 — Current Wix page existence requires current editor evidence

- **Timestamp/task:** 23–25.07.2026; Wix current-state correction.
- **Issue observed:** Retained Wix Translation Content records were previously interpreted as proof that deleted or renamed pages still existed.
- **Root cause:** Content records and active Wix Studio page instances were not separated.
- **Corrective rule:** For current page existence, use the authenticated Wix Studio page tree or another authoritative active-page result. Translation content, CMS records, Gamma, Figma, GitHub and Drive are supporting evidence only.
- **Evidence/source:** `Atlas AI Wix Page-Tree Correction — 14:31, 23.07.2026`; user-provided authenticated Wix Studio screenshot.
- **Action taken:** Current visible tree fixed at 13 pages; a separate `Kontakt` page remains missing.
- **Validation performed:** Screenshot inventory reconciled against the 14-role Phase 1 roadmap.
- **Unresolved items:** Routes, menus, hidden pages, SEO metadata, CTA targets and responsive behavior still require direct validation.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260725-003 — July phase definitions supersede June numbering

- **Timestamp/task:** 02:29, 25.07.2026 Europe/Oslo; phase completeness audit.
- **Issue observed:** June files used Phase 3 for the Azure Secure Control Plane, while the July consolidated plan defines Phase 3 as entitlement, usage, routing and reconciliation.
- **Root cause:** Historical phase plans remained accessible without an explicit active-plan boundary.
- **Corrective rule:** Use the 11.07.2026 consolidated implementation guide and the 23.07.2026 page roadmap as the active phase model. June Phase 0–6 documents remain historical evidence.
- **Evidence/source:** `02_Atlas_AI_Phase_by_Phase_Implementation_Guide_1135_11072026`.
- **Action taken:** Reclassified phase findings to the July sequence.
- **Validation performed:** Phase requirements compared line by line against current implementation evidence.
- **Unresolved items:** Historical files should be visibly marked `SUPERSEDED` in future source-register maintenance.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260725-004 — Draft coverage is not implementation readiness

- **Timestamp/task:** 02:29, 25.07.2026 Europe/Oslo; Gamma/Figma/Wix completeness audit.
- **Issue observed:** Strong Gamma and Figma coverage could be read as proof that pages, portals or secure workflows were implemented.
- **Root cause:** Content, design, CMS planning objects, physical Wix pages and operational runtime controls were not consistently reported as separate states.
- **Corrective rule:** Report at least five distinct states: `PLANNED`, `DRAFTED`, `IMPLEMENTED`, `VALIDATED`, and `APPROVED/RELEASED`.
- **Evidence/source:** July implementation guide; current Gamma inventory; Wix CMS and page-tree evidence; Figma validation records.
- **Action taken:** Final-tree matrix uses separate artifact and implementation statuses.
- **Validation performed:** Phase 1–6 evidence was reclassified without inferring operational completion.
- **Unresolved items:** Release-gate owners and sign-off workflow remain incomplete.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260725-005 — Canonical governance must not be duplicated across design tools

- **Timestamp/task:** 02:29, 25.07.2026 Europe/Oslo; cross-platform register creation.
- **Issue observed:** The same content is required in GitHub, Drive, Gamma, Wix and Figma, creating a risk of competing “canonical” copies.
- **Root cause:** Each platform serves a different operational role.
- **Corrective rule:** GitHub Markdown is the canonical machine-readable source. Drive is the controlled mirror and human-access archive. Gamma, Wix and Figma hold non-public reference/index copies only and must point back to GitHub/Drive.
- **Evidence/source:** Atlas source-authority protocol and current platform-role decisions.
- **Action taken:** Created a canonical GitHub set, Drive mirror, and non-public reference artifacts elsewhere.
- **Validation performed:** Cross-platform references must use the same filenames, version date and release lock.
- **Unresolved items:** Automated drift checks are Phase 5 work.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260725-006 — Public release remains locked

- **Timestamp/task:** 02:29, 25.07.2026 Europe/Oslo; governance bootstrap.
- **Issue observed:** Planning, content and design maturity are materially ahead of operational validation.
- **Root cause:** Phase 0.5 runtime, Phase 1 release evidence, Phase 2 identity, Phase 3 entitlement, and Phase 4–6 operational controls are incomplete.
- **Corrective rule:** No public production availability, paid activation or Managed Secure availability claim may be made without explicit written approval and passed release gates.
- **Evidence/source:** July launch gates, Wix release locks and Phase 0–6 audit.
- **Action taken:** Every new cross-platform register reference is marked non-public.
- **Validation performed:** No public page, checkout plan or production route was created by this workstream.
- **Unresolved items:** All outstanding P0/P1 release blockers.
- **Classification:** `CANONICAL`.
