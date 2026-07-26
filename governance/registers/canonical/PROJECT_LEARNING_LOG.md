# PROJECT LEARNING LOG

**Project:** Atlas Website / Atlas AI  
**Created:** 02:29, 25.07.2026 Europe/Oslo  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Repository path:** `governance/registers/canonical/`  
**Drive mirror:** https://drive.google.com/drive/folders/1cXjuJQONMu9lEDYqk6uc62SKJqnTWKiz

> Only `CANONICAL`, `APPROVED` and `AUTO_APPROVED` entries govern execution. Do not store secrets or customer-sensitive material.

## Learning entries

### ATL-LRN-20260725-001 — Canonical register layer must exist as files
The prescribed filenames must exist in GitHub and be mirrored to Drive. Setup instructions or historical branches are not substitutes. `AUTO_APPROVED`.

### ATL-LRN-20260725-002 — Current Wix page existence requires current editor evidence
Use authenticated Wix Studio page-tree evidence for current page existence. CMS, translation, Gamma and Figma records are supporting evidence. `AUTO_APPROVED`.

### ATL-LRN-20260725-003 — July phase definitions supersede June numbering
Use the 11.07 consolidated guide and 23.07 page roadmap as the active phase model. `AUTO_APPROVED`.

### ATL-LRN-20260725-004 — Draft coverage is not implementation readiness
Report `PLANNED`, `DRAFTED`, `IMPLEMENTED`, `VALIDATED` and `APPROVED/RELEASED` separately. `AUTO_APPROVED`.

### ATL-LRN-20260725-005 — Canonical governance must not be duplicated across design tools
GitHub is canonical; Drive is the controlled mirror; Wix/Gamma/Figma references cannot become competing canonical sources. `AUTO_APPROVED`.

### ATL-LRN-20260725-006 — Public release remains locked
No paid activation, production availability or Managed Secure claim without explicit approval and passed gates. `CANONICAL`.

### ATL-LRN-20260725-007 — Commercial approval must be versioned separately from activation

- **Timestamp/task:** 19:02, 25.07.2026 Europe/Oslo; pricing and Wix reconciliation.
- **Issue observed:** Three conflicting price states existed across Phase 0.5, an unmerged pricing PR and Drive.
- **Root cause:** Research recommendations and implementation state were not bound to one commercial version.
- **Corrective rule:** Use one approved price-book version and separate `commercialStatus`, `publicAllowed`, `purchaseAllowed` and `activationStatus`.
- **Evidence/source:** Current user approval; 13:01 pricing report; live GitHub/Drive/Wix readback.
- **Action taken:** Created v0.5.1 and preserved activation locks.
- **Validation performed:** Cross-file offer IDs/prices checked; Wix plan count refreshed.
- **Unresolved items:** Legal, provider, identity, entitlement and release evidence.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260725-008 — A tax rate is not a complete tax treatment

- **Timestamp/task:** 20:33, 25.07.2026 Europe/Oslo; MVA finalisation workstream.
- **Issue observed:** The standard 25% rate could be mistaken for final treatment across domestic, export, OSS, top-up, refund and provider-purchase cases.
- **Root cause:** Rate, place-of-supply, supply classification, tax point and accounting implementation were discussed as one issue.
- **Corrective rule:** Separate the domestic working rate from offer classification, customer/jurisdiction treatment, billing/refund events and professional sign-off.
- **Evidence/source:** Official Skatteetaten guidance and the Atlas MVA finalisation register.
- **Action taken:** Created MVA-001–MVA-020 and an offer/jurisdiction matrix.
- **Validation performed:** Domestic category support checked; final treatment explicitly remains pending.
- **Unresolved items:** Accountant/tax-adviser opinion, OSS, reverse charge, invoices, credit notes, Wix tax and reconciliation.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260725-009 — Legal research, legal approval and checkout implementation are separate states

- **Timestamp/task:** 20:33, 25.07.2026 Europe/Oslo; consumer terms and checkout readiness.
- **Issue observed:** A complete research prompt or draft terms could be misreported as legal compliance.
- **Root cause:** Research scope, legal interpretation, copy drafting, Wix implementation and acceptance testing were not separated.
- **Corrective rule:** Record `RESEARCH_MANDATE_CREATED`, `RESEARCH_COMPLETED`, `LEGAL_APPROVED`, `IMPLEMENTED`, `TESTED` and `RELEASE_APPROVED` separately.
- **Evidence/source:** Angrerettloven payment-obligation, commencement, withdrawal and durable-medium requirements; LEG-001–LEG-020.
- **Action taken:** Created the deep research mandate and legal readiness matrix; preserved checkout lock.
- **Validation performed:** Prompt coverage checked against the complete consumer contract lifecycle and Wix implementation surfaces.
- **Unresolved items:** Research, sign-off, implementation and testing.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260726-010 — Service and digital-content withdrawal models must not be silently combined

- **Timestamp/task:** 02:06, 26.07.2026 Europe/Oslo; consumer-law deep research.
- **Issue observed:** A continuing subscription could be treated as losing withdrawal rights at activation by importing a digital-content waiver model.
- **Root cause:** The legal exceptions apply to different supply types and performance states.
- **Corrective rule:** Classify every offer/component first; use a separate early-start request and do not infer full loss of withdrawal for continuing access.
- **Evidence/source:** Current Angrerettloven, Digitalytelsesloven and preparatory works.
- **Action taken:** Created offer/component matrix, consent design and proportional-payment model.
- **Validation performed:** Draft pack coverage mapped to LEG-001–LEG-020.
- **Unresolved items:** Norwegian legal opinion.
- **Classification:** `AUTO_APPROVED` as a research/quality-control method; substantive classification remains pending legal review.

### ATL-LRN-20260726-011 — Native platform capability is not compliance evidence

- **Timestamp/task:** 02:06, 26.07.2026 Europe/Oslo; Wix implementation mapping.
- **Issue observed:** Native plan, order and cancellation features could be treated as a complete legal checkout solution.
- **Root cause:** Platform capability and Atlas evidence obligations were conflated.
- **Corrective rule:** Allocate each requirement to `NATIVE_WIX`, `WIX_PLUS_VELO`, `EXTERNAL_BACKEND` or `MANUAL_ADMIN_PROCESS`, then test the complete journey.
- **Evidence/source:** Official Wix Pricing Plans/CMS documentation and live site readback.
- **Action taken:** Created the implementation and acceptance-test matrix.
- **Validation performed:** Pricing Plans count 0 and four consumer lock records read back.
- **Unresolved items:** Implementation, provider validation and tests.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260726-012 — Status write-back must be limited to exact evidence

- **Timestamp/task:** 02:06, 26.07.2026 Europe/Oslo; Wix readiness metadata.
- **Issue observed:** Completing research could accidentally relax checkout or publication gates.
- **Root cause:** Multiple readiness dimensions coexist in the same records.
- **Corrective rule:** Patch only fields directly supported by completed evidence and read back every lock after the write.
- **Evidence/source:** Four successful Wix CMS patches/readbacks.
- **Action taken:** Updated research and terms-draft fields only.
- **Validation performed:** `NO_GO`, purchase/public false and professional sign-off true all preserved.
- **Unresolved items:** None for this status update.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260726-013 — A refund is complete only after payment, entitlement and accounting agree

- **Timestamp/task:** 02:06, 26.07.2026 Europe/Oslo; cancellation/refund and MVA operations.
- **Issue observed:** Internal approval could be mistaken for completed reimbursement and tax correction.
- **Root cause:** Legal decision, provider transaction, credit note and ledger posting are separate events.
- **Corrective rule:** Keep the case open until provider completion, entitlement adjustment, credit note/accounting and reconciliation agree.
- **Evidence/source:** Consumer refund SOP and MVA reconciliation design.
- **Action taken:** Created immutable reason codes and end-to-end test scenarios.
- **Unresolved items:** System implementation.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260726-014 — Cross-border tax must fail closed

- **Timestamp/task:** 02:06, 26.07.2026 Europe/Oslo; MVA implementation pack.
- **Issue observed:** A Norwegian 25% working rate could be applied to foreign consumers or unsupported business evidence.
- **Root cause:** Domestic rate, customer status and destination VAT are separate decisions.
- **Corrective rule:** Block unsupported countries and conflicting evidence; enable a jurisdiction only after signed tax logic and reconciliation exist.
- **Evidence/source:** Skatteetaten and EU VAT/OSS research.
- **Action taken:** Created launch-country, evidence-conflict and Wix tax decision tables.
- **Unresolved items:** Project-owner launch scope and tax-adviser approval.
- **Classification:** `AUTO_APPROVED` as a fail-closed control rule.