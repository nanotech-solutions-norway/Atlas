# Atlas AI Current PENDING_REVIEW Index

**Timestamp:** 02:13, 12.08.2026 Europe/Oslo  
**Purpose:** Consolidate current, non-superseded Atlas items that still require owner/professional/procurement/implementation review.  
**Interpretation:** Historical pending notes that have been superseded by later approved/canonical records are excluded. Source-level `PENDING_REVIEW` classifications are consolidated under the decision/task they support rather than double-counted.

## A. Legal / consumer-service interpretation

### ATL-DEC-20260726-020 — Consumer digital-service classification
**Source:** `governance/registers/canonical/ATLAS_DECISIONS_REGISTER.md`  
**Pending question:** Confirm the working view that Atlas consumer subscriptions are continuing digital services, that activation does not automatically extinguish withdrawal rights, and separately classify top-ups/components.  
**What must be done:** Obtain a focused Norwegian legal review/counsel confirmation or authoritative contradictory interpretation for the exact Atlas scope.  
**How to close:** Review the current consumer terms/checkout model against Angrerettloven and digitalytelsesloven; record a signed/owner-approved conclusion; update terms, checkout states and the decision register; mark this decision `APPROVED`, `REJECTED` or `SUPERSEDED`.

## B. Workspace and full-deployment architecture

### ATL-DEC-20260805-034 — Atlas-owned Workspace architecture
**Source:** `governance/registers/canonical/ATLAS_WORKSPACE_UPDATE_REGISTER_1854_05082026.md`  
**Pending question:** Approve/reject an authenticated Atlas-owned Workspace for Atlas-managed API-metered plans, preferably separately deployed, while Wix remains the public/commercial/account-entry surface and protected runtime controls remain server-side.  
**What must be done:** Owner architecture decision.  
**How to close:** Approve or reject the architecture proposal; if approved, produce the Workspace PRD/UX, CIAM design, threat model, DPIA screening, entitlement/metering contract, upload-security design and test plan; then move through D1–D3 validation.

### ATL-DEC-20260806-036 — Server-side production control baseline
**Source:** `governance/registers/canonical/ATLAS_FULL_DEPLOYMENT_UPDATE_REGISTER_1545_06082026.md`  
**Pending question:** Formally adopt the requirement for authoritative identity/session validation, tenant/object authorization, entitlement resolution, atomic usage reservation, immutable ledger/settlement, hard caps, provider routing, audit, observability and a minimum operator Control Center before paid/production AI execution.  
**What must be done:** Owner architecture/security approval and implementation design.  
**How to close:** Convert the requirement into approved ADRs and acceptance criteria; implement in D2–D5; validate negative paths, reconciliation and tenant isolation; then reclassify based on evidence.

### ATL-DEC-20260806-037 — Separate Workspace and Control Center deployment boundary
**Source:** `governance/registers/canonical/ATLAS_FULL_DEPLOYMENT_UPDATE_REGISTER_1545_06082026.md`  
**Pending question:** Approve the preferred model of separately deployed protected Workspace and Control Center on Atlas-controlled application subdomains while Wix stays public/commercial/account-entry.  
**What must be done:** Owner architecture decision including hosting/domain boundary.  
**How to close:** Compare deployment options, select the trust boundary and hosting model, issue an approved ADR, define DNS/subdomain strategy without exposing secrets, then implement and validate before any public availability.

### ATL-DEC-20260806-038 — Platform/technology stack selection
**Source:** `governance/registers/canonical/ATLAS_FULL_DEPLOYMENT_UPDATE_REGISTER_1545_06082026.md`  
**Pending question:** Select or reject the preferred shortlist: Microsoft Azure, Next.js/React, Entra External ID subject to Auth0 comparison, PostgreSQL, object storage, managed queues/jobs, vault-backed secrets and OpenTelemetry observability.  
**What must be done:** Procurement/architecture comparison.  
**How to close:** Run current cost/licensing, region/data-location, CIAM, security, operational burden, performance/load and contractual comparisons; document the decision matrix; owner approves selected stack; record ADR/procurement evidence.

### ATL-DEC-20260806-039 — Connector and action-safety sequence
**Source:** `governance/registers/canonical/ATLAS_FULL_DEPLOYMENT_UPDATE_REGISTER_1545_06082026.md`  
**Pending question:** Approve initial connector scope as manual upload/export plus controlled read-only integrations, with consequential writes requiring preview, explicit approval, idempotency, receipts, revocation and audit; arbitrary customer code execution excluded initially.  
**What must be done:** Owner product/security decision on connector tiers.  
**How to close:** Approve tier model; define OAuth/scopes and revocation; implement read-only D7 pilot first; add write actions only after threat model, negative-path, idempotency and audit tests pass.

### FD-OPEN-001 — D0 release-profile/MVP/budget decision bundle
**Source:** `governance/registers/canonical/ATLAS_FULL_DEPLOYMENT_UPDATE_REGISTER_1545_06082026.md` and `governance/implementation/ATLAS_FULL_DEPLOYMENT_IMPLEMENTATION_PLAYBOOK_1545_06082026.md`  
**Pending question:** Final release profile, MVP boundary, seven-surface delivery scope, budget envelope and prioritization.  
**What must be done:** Explicit owner D0 decision.  
**How to close:** Approve release profile and MVP, define included/excluded surfaces, budget/cost ceiling, RACI and target milestones; then authorize D1 build-ready design. Architecture/vendor selections remain separately gated.

## C. Independent source-control recovery and continuity

### ATL-DEC-20260809-043 — Secondary Git platform selection
**Source:** `governance/registers/canonical/ATLAS_SECURITY_CONTINUITY_UPDATE_REGISTER_0256_09082026.md`  
**Pending question:** Select the independent secondary Git/recovery platform; Azure DevOps Repos is preferred candidate, isolated Forgejo/GitLab is comparison candidate.  
**What must be done:** Procurement, account/identity separation and recovery architecture decision.  
**How to close:** Compare provider/account independence, admin identities, region, cost, operations, export/restore mechanics and blast radius; select platform; implement; verify restore before marking live.

### ATL-SEC-CONT-001 — Select independent secondary Git platform/account
**Source:** same security continuity register.  
**What must be done:** Choose provider, tenancy, identity/admin separation, region and cost model.  
**How to close:** Owner-approved selection documented with separated credentials/admins and no automatic authority failover.

### ATL-SEC-CONT-002 — Signed Git checkpoint process
**Source:** same security continuity register.  
**What must be done:** Implement full Git bundles, SHA-256 manifest and independent signing/verification.  
**How to close:** Generate a checkpoint, verify it outside GitHub, restore from it, preserve sanitized evidence and document ownership/rotation.

### ATL-SEC-CONT-003 — Immutable/WORM recovery storage
**Source:** same security continuity register.  
**What must be done:** Create separately protected immutable recovery storage with retention/deletion controls.  
**How to close:** Configure immutable retention, separated access, lifecycle policy and restore test; retain validation evidence without secrets.

### ATL-SEC-CONT-004 — Encrypted offline recovery copy
**Source:** same security continuity register.  
**What must be done:** Maintain an encrypted offline copy of critical source/governance and verification material.  
**How to close:** Define encrypted medium/process, custody and refresh cadence; perform offline verification/restore and record evidence.

### ATL-SEC-CONT-005 — Break-glass authority procedure
**Source:** same security continuity register.  
**What must be done:** Finalize named roles, independent access, revocation, validation and return-to-service workflow.  
**How to close:** Approve runbook; conduct tabletop/technical exercise; demonstrate authority freeze, checkpoint verification, controlled recovery and restoration of normal authority.

### ATL-SEC-CONT-006 — Quarterly recovery exercise
**Source:** same security continuity register.  
**What must be done:** Restore without GitHub and verify signatures/history/build/test plus RTO/RPO.  
**How to close:** Run first complete exercise, document measured RTO/RPO and defects, remediate failures, then schedule quarterly repetition.

### ATL-SEC-CONT-007 — GitHub-compromise detection → kill switches
**Source:** same security continuity register.  
**What must be done:** Ensure GitHub-originated deploy/write paths can be frozen independently of repository content.  
**How to close:** Implement an external trust/freeze control, test compromise simulation, confirm deploy/write rejection and audit evidence, then validate recovery/return-to-service.

## Consolidation notes

- The `PENDING_REVIEW` classification of the Workspace research source and Workspace architecture proposal is represented by ATL-DEC-20260805-034 and is not counted twice.
- The `PENDING_REVIEW` full-deployment architecture proposal/source rows are represented by ATL-DEC-20260806-036 through -039 and FD-OPEN-001.
- The secondary Git service source-authority row is represented by ATL-DEC-20260809-043 and ATL-SEC-CONT-001 through -007.
- Family remains `Utsatt`, Managed Secure remains qualification-only, and production/public purchase remains `NO_GO`; these are controlled statuses/release locks rather than PENDING_REVIEW decisions.
