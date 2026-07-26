# PROJECT LEARNING LOG

**Project:** Atlas Website / Atlas AI  
**Created:** 02:29, 25.07.2026 Europe/Oslo  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Repository path:** `governance/registers/canonical/`  
**Drive mirror:** https://drive.google.com/drive/folders/1cXjuJQONMu9lEDYqk6uc62SKJqnTWKiz

> Only `CANONICAL`, `APPROVED` and `AUTO_APPROVED` entries govern execution. Do not store secrets or customer-sensitive material.

## Learning entries

### ATL-LRN-20260725-001 — Canonical register layer must exist as files
The six prescribed filenames must exist in GitHub and be mirrored to Drive. Setup instructions or historical branches are not substitutes. `AUTO_APPROVED`.

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
- **Unresolved items:** Execute research, obtain legal sign-off, implement and test.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260726-010 — Generated research is not controlled evidence until ingested

- **Timestamp/task:** 02:08, 26.07.2026 Europe/Oslo; consumer-law report review.
- **Issue observed:** A generated report was referenced in the project thread but absent from canonical GitHub and the controlled Drive folder.
- **Root cause:** The research output was not ingested after generation, while report generation and controlled completion were treated as one event.
- **Corrective rule:** Store the complete artifact with stable filename, version and checksum before recording `RESEARCH_COMPLETED`; then perform source review, legal approval, implementation and release approval as separate states.
- **Evidence/source:** GitHub and Drive searches; primary-source checkpoint review.
- **Action taken:** Created a controlled partial review, added an ingestion gate and preserved all release locks.
- **Validation performed:** Report absence verified; statutory checkpoints re-verified independently.
- **Unresolved items:** Ingest and review the report, obtain counsel approval, implement and test.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260726-011 — Concurrent canonical updates require reconciliation, not overwrite

- **Timestamp/task:** 02:50, 26.07.2026 Europe/Oslo; research-pack ingestion.
- **Issue observed:** Two newer commits modified the same legal and canonical records while the research branch was being prepared.
- **Root cause:** Parallel workstreams used a shared baseline.
- **Corrective rule:** Re-read current `main`, preserve the newer canonical entries, carry forward only non-conflicting artifacts and explicitly reconcile affected matrices.
- **Evidence/source:** Commit comparison and the closed, unmerged synchronization PR #9.
- **Action taken:** Created a fresh branch from current `main`, transferred exact new artifact blobs and excluded stale canonical-file versions.
- **Validation performed:** New branch is based on current main; conflicted sync PR was closed without merge.
- **Unresolved items:** Draft PR review and merge decision.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260726-012 — Native platform capability is not complete compliance evidence

- **Timestamp/task:** 02:50, 26.07.2026 Europe/Oslo; Wix/Velo/backend mapping.
- **Issue observed:** Native plan, order and cancellation features could be treated as a complete legal/tax solution.
- **Root cause:** Platform functions were conflated with Atlas consent, version, entitlement, location, refund and accounting evidence.
- **Corrective rule:** Allocate every requirement to native Wix, Wix+Velo, external backend or manual administration and validate the complete journey.
- **Evidence/source:** Official Wix capability review, current site readback and implementation matrix.
- **Action taken:** Created the requirement-level architecture and acceptance suite.
- **Validation performed:** Pricing Plans remained zero and all four consumer release locks remained active.
- **Unresolved items:** Implementation and test evidence.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260726-013 — Status write-back must be limited to exact evidence

- **Timestamp/task:** 02:50, 26.07.2026 Europe/Oslo; Wix readiness metadata.
- **Issue observed:** Completing research could accidentally relax legal, checkout or release gates.
- **Root cause:** Multiple readiness dimensions coexist in the same offer records.
- **Corrective rule:** Patch only fields directly supported by completed evidence and read back every safety/release field after the write.
- **Evidence/source:** Four successful Wix CMS patches and filtered readback.
- **Action taken:** Updated research and draft-terms status only.
- **Validation performed:** `NO_GO`, professional sign-off true, purchase/public false and Family block all preserved.
- **Unresolved items:** None for this status write; all substantive gates remain open.
- **Classification:** `AUTO_APPROVED`.

### ATL-LRN-20260726-014 — Refund completion requires payment, entitlement and accounting agreement

- **Timestamp/task:** 02:50, 26.07.2026 Europe/Oslo; cancellation/refund and MVA operations.
- **Issue observed:** Internal approval could be mistaken for completed reimbursement and tax correction.
- **Root cause:** Legal decision, provider transaction, entitlement adjustment, credit note and accounting posting are separate events.
- **Corrective rule:** Keep a refund case open until provider completion, entitlement/usage adjustment, accounting correction and reconciliation agree.
- **Evidence/source:** Consumer refund SOP and MVA reconciliation design.
- **Action taken:** Created reason codes, approval controls and end-to-end test cases.
- **Unresolved items:** System implementation and professional approval.
- **Classification:** `AUTO_APPROVED`.