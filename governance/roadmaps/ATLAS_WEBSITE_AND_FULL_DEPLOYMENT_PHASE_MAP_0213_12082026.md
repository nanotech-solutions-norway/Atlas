# Atlas AI Website and Full Deployment Phase Map

**Timestamp:** 02:13, 12.08.2026 Europe/Oslo  
**Status:** Controlled roadmap alias map  
**Authority:** `ATL-DEC-20260812-040`  

## W1 — Public Website Phase 1

Canonical public website scope remains the 15-page Atlas AI public information architecture. W1 is a website/content/route namespace and must not be confused with full-deployment D1.

| Page | Route | Phase |
|---|---|---|
| Hjem | `/` | W1 |
| Tjenester | `/solutions/` | W1 |
| Bedrift | `/solutions/business-ai/` | W1 |
| Studenter | `/solutions/students/` | W1 |
| Privatpersoner | `/solutions/consumers/` | W1 |
| Managed Secure | `/managed-secure/` | W1; qualification-only public page |
| Priser | `/pricing/` | W1 |
| Tillit | `/trust/` | W1 |
| Plattformer | `/platform-lanes/` | W1 |
| Oppstart | `/onboarding/` | W1 |
| Ressurser | `/resources/` | W1 |
| FAQ | `/resources/faq/` | W1 |
| Om oss | `/about/` | W1 |
| Kontakt | `/contact/` | W1 |
| Juridisk | `/legal/` | W1 |

## D0–D9 — Full Deployment

| Phase | Name | Principal surface/output |
|---|---|---|
| D0 | Decision lock | Release profile, MVP, architecture boundary, RACI and data-class decisions |
| D1 | Build-ready design | Workspace/Organisation PRD, Control Center spec, UX, diagrams, contracts, threat model and test strategy |
| D2 | Security foundation | CIAM, authorization, gateway, secrets, tenant/ledger schemas, quarantine, audit and observability |
| D3 | Workspace MVP | Customer execution interface, projects, history, approved workflows, artifacts, usage and account controls |
| D4 | Commerce and entitlement integration | Wix/payment events, entitlements, usage reservation/settlement, cancellation/refund and reconciliation |
| D5 | Atlas Control Center | Tenant, entitlement, provider/model, workflow, support, incident, quarantine, cost and audit controls |
| D6 | Business Workspace | Organisation users/groups/roles, budgets, shared projects, knowledge, retention, SSO/SCIM readiness and reporting |
| D7 | Connectors and Developer API | OAuth, read-only connectors first, controlled writes, service accounts, signed webhooks and sandbox |
| D8 | Closed pilot | Named users, low-risk/synthetic data, monitored costs/caps/incidents/support and defect closure |
| D9 | Managed Secure | Contract-bound high-control implementation, independent security assessment and explicit scope-specific release GO |

## Reporting rule

All new Atlas status, roadmap, implementation and validation records must state the phase namespace explicitly. Examples: `W1 / Kontakt`, `D3 / Workspace MVP`, `D6 / Organisation Administration`.

Legacy documents are not retroactively rewritten; they remain evidence and should be annotated with the modern alias when referenced.
