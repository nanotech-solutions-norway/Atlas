# Atlas AI Full Deployment Architecture Decision Proposal

**Timestamp:** 15:45, 06.08.2026 Europe/Oslo  
**Status:** `PENDING_REVIEW`  
**Release state:** `NO_GO` — unchanged

## Proposed decision

Adopt a seven-surface Atlas AI operating model:

1. Wix public/commercial/account-entry surface.
2. Separately deployed Atlas Workspace.
3. Customer Organisation Administration.
4. Internal Atlas Control Center.
5. Support and independent service-status surface.
6. Developer/API and connector-management surface.
7. Protected runtime/data plane.

Wix and browser code remain non-authoritative for provider credentials, routing, entitlements, usage reservations, hard caps, protected state and audit.

## Proposed preferred implementation

- Workspace: protected web application, preferably `app.atlas-ai.no`.
- Control Center: separately protected internal application.
- Primary cloud: Microsoft Azure.
- Frontend: Next.js/React with TypeScript.
- Identity: Microsoft Entra External ID, compared with Auth0 before procurement.
- Runtime: Container Apps with Functions/Jobs where appropriate.
- Edge/API: Front Door/WAF and API Management.
- Data: PostgreSQL, Blob Storage, managed queue and vault-backed secrets.
- Observability: OpenTelemetry with Azure Monitor/Application Insights.
- Knowledge: benchmark Azure AI Search and PostgreSQL pgvector before specialist procurement.

## Mandatory conditions

- Deny-by-default tenant and object authorization.
- Atomic usage reservation before provider execution.
- Immutable usage/adjustment ledger and reconciliation.
- Provider/model registry, cost ceilings, fallback and kill switches.
- Minimum Control Center before real-customer production pilot.
- File quarantine, malware/type checks and deletion propagation.
- Threat model, DPIA screening, incident/recovery controls and acceptance evidence.
- No write connectors in the initial release unless separately approved and tested.

## Alternatives considered

- Wix/Velo-hosted execution: rejected as governing architecture where it would place authoritative state, secrets, metering or protected execution in Wix/client code.
- Kubernetes: deferred because it creates avoidable operational complexity for the initial scale.
- Self-hosted IAM: deferred without dedicated IAM operations capability.
- Multiple vector databases or broad automation marketplace: deferred until measured need.

## Approval questions

1. Approve the seven-surface operating model?
2. Approve separate Workspace and Control Center deployment?
3. Approve Azure as the primary cloud for detailed design and cost validation?
4. Approve Entra External ID as preferred CIAM subject to Auth0 comparison?
5. Approve the initial connector boundary: manual upload/export and controlled read-only only?
6. Approve the nine-phase implementation sequence?

No recommendation in this proposal activates public, purchase, pilot or production availability.
