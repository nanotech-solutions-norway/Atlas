# Atlas AI Full Deployment Memory Update

**Timestamp:** 15:45, 06.08.2026 Europe/Oslo  
**Project:** Atlas Website / Atlas AI  
**Use rule:** Apply only `CANONICAL`, `APPROVED` or `AUTO_APPROVED` entries. Treat all `PENDING_REVIEW` entries as advisory.  
**Release state:** `NO_GO`.

## Approved continuity context

- Full deployment must be assessed across seven surfaces: Website, Workspace, Organisation Administration, Atlas Control Center, Support/Status, Developer/Integrations and Secure Runtime/Data Plane. `AUTO_APPROVED`.
- Website or customer Workspace completion alone is not full deployment. `AUTO_APPROVED`.
- Current approved boundary remains: Wix is public/commercial/account entry; provider routing, authoritative entitlement, usage, protected state and audit remain external and server-side. `APPROVED`/`CANONICAL` existing control.
- The operator Control Center, authoritative usage controls, support, observability, incident/recovery and accounting reconciliation are required deployment functions. `AUTO_APPROVED` completeness rule; exact architecture remains pending.
- Retrieval must enforce tenant/object/group/workflow/data-class permission before source content reaches a model. `AUTO_APPROVED`.
- Usage should be reserved atomically before provider execution and settled against an append-only event ledger. `AUTO_APPROVED` control principle; implementation architecture pending.
- Connector maturity must progress from manual/read-only to approved writes and schedules with proportionate scope, approval, idempotency, receipts, stop controls and audit. `AUTO_APPROVED` risk model.
- Platform capability, platform selection, implementation, validation, pilot approval and production release are separate states. `AUTO_APPROVED`.

## Pending architecture/procurement context

- Separately deployed Workspace, preferably `app.atlas-ai.no`.
- Separate internal Atlas Control Center.
- Microsoft Azure as preferred primary cloud.
- Next.js/React and TypeScript for protected interfaces.
- Entra External ID as preferred CIAM subject to Auth0 comparison.
- PostgreSQL, Blob Storage, managed queue/jobs, Key Vault and OpenTelemetry/Azure Monitor.
- Azure AI Search versus PostgreSQL pgvector benchmark before specialist vector procurement.
- Zendesk/Freshdesk, independent status page and privacy-controlled product analytics.
- Initial connector boundary: manual upload/export and controlled read-only; no unrestricted writes or arbitrary customer code.

All entries in this section are `PENDING_REVIEW`.

## Implementation sequence

0. Decision lock.
1. PRD, UX, diagrams, API/data contracts, threat model and test design.
2. Identity, authorization, gateway, secrets, ledger, audit and file-security foundation.
3. Non-public Workspace MVP.
4. Wix/payment/entitlement/refund/Conta integration.
5. Minimum Atlas Control Center.
6. Organisation Administration and governed knowledge.
7. Controlled connectors and Developer API.
8. Closed pilot.
9. Managed Secure evidence-gated release.

## Immediate open items

- Owner architecture and MVP approval.
- Cloud/CIAM decision and cost comparison.
- Data classes, retention and privacy scope.
- Support model, SLOs and incident ownership.
- Implementation of authoritative entitlement/metering and Control Center.
- Threat model, DPIA, negative tests, backup/restore and penetration test.
- Pilot and explicit release approval.

## Retrieval prompt

> Activate Atlas project memory. Read the canonical registers and `ATLAS_FULL_DEPLOYMENT_UPDATE_REGISTER_1545_06082026.md` plus `ATLAS_FULL_DEPLOYMENT_MEMORY_UPDATE_1545_06082026.md`. Apply only CANONICAL, APPROVED and AUTO_APPROVED entries. Treat the seven-surface completeness model as the current quality-control baseline, preserve the Wix/protected-runtime boundary and all safety locks, and keep architecture/platform/procurement choices PENDING_REVIEW until explicitly approved. Public release remains NO_GO.
