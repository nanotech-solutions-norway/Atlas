# Atlas AI Full Deployment Functional Architecture and Implementation Playbook

**Report timestamp:** 10:43, 06.08.2026 Europe/Oslo  
**Controlled integration timestamp:** 15:45, 06.08.2026 Europe/Oslo  
**Project:** Atlas Website / Atlas AI  
**Release posture:** `NO_GO` — unchanged  
**Authority:** Controlled research and implementation-planning evidence. Item-level classifications apply. Platform procurement, architecture selections and release decisions remain `PENDING_REVIEW` unless separately approved.

## Purpose

Define the missing and recommended components required for Atlas AI to operate as a complete, secure and supportable AI service, not merely as a public website or chat interface.

## Governing boundaries preserved

- Wix remains the public website, CMS, pricing, order, member and account-entry surface.
- Provider credentials, provider routing, authoritative entitlements, usage reservations, metering, hard caps, protected state and audit remain outside Wix and browser code.
- No public write endpoint, frontend provider token, real-money betting, auto-betting, bookmaker execution or unapproved production availability is permitted.
- Managed Secure remains qualification and architecture-review only until its separate identity, storage, logging, revocation, recovery, incident and acceptance evidence is approved.
- `publicAllowed=false`, `purchaseAllowed=false`, `releaseApproved=false` and `NO_GO` remain unchanged.

## Target product model — seven operating surfaces

1. **Atlas Website** — public information, pricing, qualification, checkout, trust/legal content and account entry.
2. **Atlas Workspace** — authenticated AI task execution, projects, workflows, files, history, artifacts, usage and support entry.
3. **Organisation Administration** — users, groups, roles, policies, budgets, retention, knowledge and audit access.
4. **Atlas Control Center** — Atlas tenant, entitlement, provider, workflow, support, incident, security and cost operations.
5. **Support and Service Status** — help content, tickets, service health, incident communication and maintenance.
6. **Developer and Integration Interface** — service accounts, APIs, webhooks, connector configuration and sandbox.
7. **Secure Runtime and Data Plane** — identity validation, authorization, entitlement, reservations, ledger, workflow execution, provider routing, storage, retrieval, audit and telemetry.

## Material missing components

### P0 — required before paid or production AI execution

- Separately deployed protected Workspace and secure multi-tenant runtime.
- Identity/session architecture, tenant and object-level authorization, privileged-role MFA and revocation.
- Authoritative plan-to-entitlement mapping, reservation-based usage control, immutable usage ledger, settlement, reversals and atomic hard caps.
- Minimum Atlas Control Center covering tenants, entitlements, providers/models, workflows, support, security and emergency kill switches.
- Secure provider abstraction and routing with approved model registry, region policy, cost ceilings, fallback controls and credential rotation.
- File quarantine, malware scanning, type verification, size limits, safe parsing, isolated storage and deletion propagation.
- Metrics, traces, logs, alerts, SLOs, incident runbooks, backup/restore validation and operational dashboards.
- Verified Wix/payment-to-runtime provisioning, cancellation, refund, invoice/credit-note and Conta reconciliation.
- Privacy operations: data inventory, RoPA, DPA/subprocessor controls, retention, deletion, DSAR and incident processes.
- Threat model, DPIA screening, negative-path tests and objective release evidence.

### P1 — required for Business Workspace

- Customer Organisation Administration.
- Persistent knowledge-base lifecycle, retrieval authorization, source freshness, citations and deletion.
- Shared projects and governed artifacts.
- Workflow registry, test datasets, automated evaluation, staged rollout and rollback.
- Help Center, ticketing and independent service-status interface.
- Controlled read-only connector framework.
- Organisation usage, budget, adoption and audit reporting.

### P2 — later controlled expansion

- Approved write connectors with preview, explicit approval, idempotency and execution receipts.
- Developer API, scoped service accounts, signed webhooks, sandbox and API documentation.
- Scheduled and conditional workflows with stop controls, caps and periodic review.
- Advanced customer-authored workflow tooling only after the controlled registry is stable.

## Recommended logical architecture

```text
Wix website / checkout / member entry
        ↓ verified server-side handoff
Atlas Workspace + Organisation Administration
        ↓ OIDC and tenant/object authorization
API gateway / WAF / rate limits
        ↓
Identity | Policy | Entitlement | Reservation/Ledger | Jobs
Knowledge/RAG | Connectors | Provider Router | Audit | Notifications
        ↓
PostgreSQL | object storage/quarantine | queue | cache | append-only audit
        ↓
Approved AI, cloud, identity, payment, accounting and support providers
```

The browser may request operations and display synchronized state but must never be authoritative for entitlement, tenant policy, provider credentials, usage limits, audit evidence or privileged configuration.

## Workspace minimum feature set

- Home dashboard with recent projects, quick starts, plan/usage status and service notices.
- Project and conversation creation, search, rename, archive and retention states.
- Approved workflow catalogue describing purpose, permitted inputs, plan eligibility, data rules, provider policy, expected outputs and human-review requirements.
- Streaming and asynchronous execution with cancel, retry, bounded timeout and safe failure states.
- File upload, processing status, quarantine, scan, parsing and deletion.
- Artifact review, copy, edit, export and version history.
- Allowance, reservation, settled usage and remaining-cap display.
- Task, usage, subscription, security, retention and support notifications.
- Helpful/unhelpful, error, safety and human-review feedback paths.
- Account profile, active sessions, connected applications, consent, data export and deletion request.
- WCAG 2.2 AA internal design target subject to separate legal-baseline wording and approval.

## Organisation Administration minimum feature set

- Organisation ownership, user invitation, seat allocation, suspension, removal and transfer.
- Teams/groups and least-privilege role templates.
- MFA enforcement and session revocation; SSO and SCIM for eligible enterprise tiers.
- Workflow, model/provider, connector, export and data-class policies.
- Per-user/team budgets, warnings and hard caps.
- Retention, deletion, region and knowledge-source controls.
- Usage, adoption, cost and audit reports.
- Separation of owner, administrator, knowledge manager, workflow manager, auditor and member permissions.

## Atlas Control Center minimum feature set

- Tenant provisioning, activation, suspension, closure, environment, region and offboarding.
- Entitlement versioning, allowances, boosts, exceptions and reconciliation.
- Provider/model registry, credentials, limits, regional endpoints, cost ceilings, fallback and kill switch.
- Workflow version, prompt/configuration, tools, data rules, evaluation set, approval, rollout and rollback.
- Reservation/settlement monitoring, provider cost, margin alarms, refund adjustments and monthly close.
- Ticket-linked support operations, diagnostic metadata, session revocation and safe reprocessing.
- Security alerts, file quarantine, suspicious activity, emergency suspension and incident timeline.
- Append-only privileged-action audit with actor, reason, target, before/after state and ticket.

## Entitlement and usage execution sequence

1. Validate identity, tenant and workflow permission.
2. Resolve the effective entitlement and policy.
3. Estimate bounded worst-case usage.
4. Atomically reserve allowance before provider execution.
5. Execute only through an approved provider route.
6. Measure actual provider and internal resource consumption.
7. Settle actual usage and release unused reservation.
8. Persist user-visible state and append audit evidence.
9. Apply explicit billable/non-billable policy for failure cases.
10. Reconcile provider invoice, runtime ledger, commerce record and accounting.

## Knowledge and retrieval controls

- Each knowledge base requires purpose, owner, tenant, data classification, retention and permissions.
- Ingestion requires checksum, duplicate detection, malware scan, safe parsing, indexing state and freshness/expiry controls.
- Retrieval authorization must be applied by tenant, user/group, document permission, workflow and data class before content reaches the model.
- Outputs should identify source title/location, retrieval date and workflow/model version where applicable.
- Source deletion must propagate to index/vector store, caches, derived artifacts and backup lifecycle.
- Prompt-injection and indirect-injection tests are mandatory for retrieval and tool-enabled workflows.

## Connector and action risk tiers

- `C0`: manual upload/export.
- `C1`: metadata/read-only.
- `C2`: controlled content read.
- `C3`: draft or write preview requiring explicit approval.
- `C4`: controlled write with idempotency, receipt and compensating action where possible.
- `C5`: scheduled/conditional execution with policy, caps, monitoring, stop control and periodic review.

No broad write connector or arbitrary customer code execution is recommended for the initial release.

## Platform recommendations — PENDING_REVIEW

- Public/commercial plane: existing Wix Studio and approved Wix applications.
- Workspace and Control Center: Next.js/React with TypeScript.
- Primary cloud: Microsoft Azure, subject to formal architecture and procurement approval.
- Compute: Azure Container Apps; Functions/Jobs for event and background workloads.
- Edge/API: Azure Front Door/WAF and API Management.
- CIAM: Microsoft Entra External ID, compared against Auth0 before procurement.
- Database/storage: Azure Database for PostgreSQL and Azure Blob Storage.
- Secrets: Azure Key Vault and managed identities.
- Queue/jobs: Azure Service Bus and Container Apps Jobs/Functions; evaluate Temporal only if workflow complexity justifies it.
- Search/RAG: benchmark Azure AI Search and PostgreSQL pgvector before adding a specialist vector database.
- Observability: OpenTelemetry with Azure Monitor/Application Insights.
- Security operations: Microsoft Sentinel only when Managed Secure maturity and economics justify it.
- Support: Zendesk or Freshdesk; independent Statuspage or Better Stack status service.
- Product analytics: PostHog EU/self-hosted or another privacy-controlled implementation.
- Feature flags: Azure App Configuration or equivalent.
- Engineering security: GitHub secret scanning, Dependabot, CodeQL and Advanced Security where licensed.
- Accounting: controlled Conta adapter; manual reconciliation remains acceptable during a closed pilot.

Kubernetes, self-hosted IAM, multiple vector databases, native mobile apps, unrestricted automation marketplaces and an additional billing platform are not recommended initially without measured need.

## Implementation playbook

| Phase | Objective | Exit condition |
|---|---|---|
| 0 — Decision lock | Approve boundary, MVP, data classes, cloud/CIAM and RACI | Written owner decision; `NO_GO` remains |
| 1 — Design | PRD, UX, API/data contracts, diagrams, threat model and test strategy | Design review PASS |
| 2 — Security foundation | CIAM, authorization, gateway, secrets, ledger, audit and quarantine | Security foundation PASS |
| 3 — Workspace MVP | Dashboard, workflows, files, projects, artifacts, usage and support entry | Functional/accessibility PASS |
| 4 — Commerce integration | Wix handoff, payment, entitlement, cancellation, refund and Conta | Billing/entitlement PASS |
| 5 — Control Center | Tenant, provider, workflow, support, incident and cost operations | Operations PASS |
| 6 — Business features | Organisation admin, RBAC, SSO readiness, knowledge and reporting | Business pilot PASS |
| 7 — Connectors/API | OAuth hub, read-only connectors, approved writes and API/webhooks | Connector/API security PASS |
| 8 — Closed pilot | Named users, monitored caps, support and remediation | Pilot acceptance |
| 9 — Managed Secure | Advanced IAM, isolation, SIEM, recovery and penetration-test closure | Explicit release GO |

## 90-day priority sequence

- **Days 1–15:** approve architecture ADR, MVP, data classes, CIAM/cloud, roles and release profile.
- **Days 16–30:** complete PRD, UX, API/data model, threat model, DPIA screening, test plan and procurement shortlist.
- **Days 31–55:** implement identity, gateway, tenant authorization, secrets, reservation/ledger, audit, quarantine and CI/CD.
- **Days 56–75:** implement non-public Workspace MVP.
- **Days 76–90:** integrate Wix handoff and commerce sandbox; implement minimum Control Center and observability; complete negative tests and pilot preparation.

## Blocking release conditions

Any of the following preserves or returns `NO_GO`:

- exposed secret or provider credential;
- cross-tenant access or privilege escalation;
- entitlement bypass or hard-cap race failure;
- incorrect charge, refund or unreconciled accounting state;
- uncontrolled confidential upload or failed deletion path;
- unsafe consequential connector action;
- unsupported public claim;
- critical/high exploitable security defect;
- unresolved P0 or release-blocking P1 defect;
- missing incident, support, backup/restore or rollback evidence.

## Decision status

| Decision | Recommendation | Classification |
|---|---|---|
| Workspace boundary | Separate protected app, preferably `app.atlas-ai.no`; Wix remains commercial/account entry | `PENDING_REVIEW` |
| Primary cloud | Microsoft Azure | `PENDING_REVIEW` |
| CIAM | Entra External ID, compare Auth0 | `PENDING_REVIEW` |
| Core data services | PostgreSQL plus object storage; specialist services only after benchmark | `PENDING_REVIEW` |
| Initial connectors | Manual upload and controlled read-only only | `PENDING_REVIEW` |
| Release posture | Maintain `NO_GO` until the exact release profile passes objective gates | `CANONICAL` / unchanged |

## Source basis

Internal source set includes the Atlas master strategy, implementation guide, launch gates, pricing/entitlement baseline, governance/source-authority baseline, SEO/AEO/GEO blueprint, Workspace report and Workspace controlled update pack. External source categories include official EU AI Act, EDPB/Datatilsynet, NIST, W3C WCAG 2.2, OWASP, Wix, Microsoft, GitHub, OpenAI, Anthropic and Google documentation current in the report source corpus through 06.08.2026. Vendor pricing, licensing, availability, region support and product terms must be revalidated before procurement or publication.

## Original artifact set

- `Atlas_AI_Full_Deployment_Functional_Architecture_and_Implementation_Playbook_1043_06082026.docx`
- `Atlas_AI_Full_Deployment_Functional_Architecture_and_Implementation_Playbook_1043_06082026.pdf`
- Markdown controlled integration record: this file.

The DOCX and PDF are mirrored to the controlled Google Drive report folder. This Markdown record carries the complete governing recommendations, classifications, implementation structure and open decisions required for GitHub control and review.
