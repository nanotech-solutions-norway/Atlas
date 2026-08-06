# Atlas AI Full Deployment Implementation Playbook

**Timestamp:** 15:45, 06.08.2026 Europe/Oslo  
**Classification:** Mixed; item-level classifications apply  
**Release state:** `NO_GO`

## Delivery objective

Convert the current public website, commercial controls, Workspace concept and governance baseline into an integrated and supportable AI service. Delivery is controlled through separate product, architecture, security, commerce, operations and release workstreams.

## Workstreams

| Workstream | Principal outputs |
|---|---|
| Product and UX | PRD, roles, journeys, information architecture, feature priorities and acceptance criteria |
| Architecture and platform | ADRs, system/data-flow diagrams, services, API contracts, data model and environments |
| Security and privacy | Threat model, DPIA, control matrix, retention, deletion, incident and recovery evidence |
| Commerce and finance | Plans, tax, checkout, payment, refund, credit note, entitlement and Conta reconciliation |
| Website and content | Wix implementation, bilingual routes, legal/trust, SEO/AEO/GEO and accessibility |
| QA and release | Test strategy, automated suites, evidence index, defect management and GO/NO_GO |
| Operations and support | Control Center, observability, helpdesk, status, runbooks, SLOs and incident communication |
| Customer success | Onboarding, training, adoption, quality review and renewal evidence |

## Phases

### Phase 0 — Decision lock

- Approve release profile, MVP, seven-surface model, hosting boundary and RACI.
- Approve data classes and excluded workflows.
- Select cloud and CIAM for detailed design.
- Preserve all public/purchase/production locks.

**Exit:** written owner decision and controlled ADRs.

### Phase 1 — Build-ready design

- Workspace and Organisation Administration PRD.
- Control Center specification.
- UX flows and accessibility specification.
- System context, container and data-flow diagrams.
- API, event, entitlement, ledger and deletion contracts.
- Threat model, DPIA screening and test strategy.

**Exit:** design review PASS.

### Phase 2 — Security foundation

- OIDC/CIAM, sessions, MFA for privileged roles and revocation.
- Tenant/object authorization and policy engine.
- Gateway/WAF, rate limits, secrets and managed identity.
- PostgreSQL tenant/entitlement/ledger schemas.
- Object storage quarantine, malware/type checks and deletion workflow.
- Append-only audit, OpenTelemetry and CI/CD scanning.

**Exit:** security-foundation acceptance PASS.

### Phase 3 — Workspace MVP

- Dashboard, projects and conversation history.
- Approved workflow catalogue and version display.
- Streaming and asynchronous jobs with cancel/retry.
- Files, artifacts, usage display, notifications and feedback.
- Account sessions, consent, export and deletion entry.

**Exit:** functional, accessibility and negative-path PASS.

### Phase 4 — Commerce and entitlement integration

- Verified Wix/payment events and idempotent provisioning.
- Plan-to-entitlement mapping.
- Reservation, settlement, reversal and adjustment ledger.
- Cancellation, refund, credit note and account-deletion state machines.
- Conta adapter or controlled manual pilot reconciliation.

**Exit:** payment, entitlement and accounting reconciliation PASS.

### Phase 5 — Atlas Control Center

- Tenant lifecycle.
- Entitlement and allowance management.
- Provider/model registry, cost ceiling, fallback and kill switch.
- Workflow registry, evaluation evidence, staged rollout and rollback.
- Support, incident, quarantine, cost and audit modules.

**Exit:** operations and privileged-access PASS.

### Phase 6 — Business Workspace

- Organisation users, groups, roles and budgets.
- Shared projects, knowledge bases and retention policies.
- SSO readiness and SCIM for eligible tiers.
- Organisation audit, usage and adoption reports.

**Exit:** closed business-pilot PASS.

### Phase 7 — Connectors and Developer API

- OAuth connection and revocation.
- Read-only connector tier first.
- Consequential writes only with preview, approval, idempotency and receipt.
- Scoped service accounts, signed webhooks and sandbox.

**Exit:** connector/API security PASS.

### Phase 8 — Closed pilot

- Named users and low-risk/synthetic data.
- Monitored provider costs, caps, incidents and support.
- Defect remediation and pilot closure report.

**Exit:** explicit pilot acceptance.

### Phase 9 — Managed Secure

- Contract-bound identity, isolation, storage, logging, recovery and incident controls.
- Independent security assessment and external penetration test.
- Customer-specific acceptance evidence.

**Exit:** explicit written release GO for the defined scope.

## Minimum backlog

### P0

- Architecture ADR and diagrams.
- Workspace/Control Center PRDs.
- CIAM and tenant/object authorization.
- Entitlement, reservation, ledger and hard caps.
- Provider router and secrets management.
- File quarantine and deletion.
- Audit, observability and incident runbooks.
- Wix/payment provisioning and reconciliation.
- Privacy operations and objective release evidence.

### P1

- Organisation Administration.
- Persistent knowledge and citations.
- Workflow registry and automated evaluation.
- Help Center, ticketing and status page.
- Read-only connectors.

### P2

- Controlled write actions.
- Developer API, service accounts and webhooks.
- Advanced schedules and conditional workflows.

## First 90 days

| Window | Required outcome |
|---|---|
| Days 1–15 | Architecture, MVP, data classes, roles and release-profile decisions |
| Days 16–30 | PRD, UX, diagrams, contracts, threat model, DPIA screening and test plan |
| Days 31–55 | Identity, gateway, authorization, secrets, ledger, audit, quarantine and CI/CD |
| Days 56–75 | Non-public Workspace MVP |
| Days 76–90 | Wix sandbox integration, minimum Control Center, observability and pilot preparation |

## Status rules

- `PLANNED`, `DESIGNED`, `IMPLEMENTED`, `VALIDATED`, `PILOT_APPROVED` and `RELEASED` must be reported separately.
- Vendor capability is not implementation evidence.
- A successful happy path is not release evidence without negative-path and reconciliation tests.
- Any cross-tenant access, secret exposure, entitlement bypass, hard-cap failure, incorrect charge or unresolved release-blocking defect preserves `NO_GO`.
