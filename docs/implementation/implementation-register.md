# Atlas AI Implementation Register — 13:02, 04.06.2026

**Last controlled update:** 15:45, 06.08.2026 Europe/Oslo

| Platform | Asset / Page | Status | Next action | Evidence |
|---|---|---|---|---|
| GitHub | Bilingual static website | Updated | Enable/verify Pages Actions | `index.html`, `/en/index.html`, workflow |
| GitHub | CMS schema and seeds | Updated | Validate against Wix CMS before import | `schemas/*`, `cms-seeds/*` |
| GitHub | Claims registry | Created/expanded | Legal/security review of public claims | `cms-seeds/claims_registry.json` |
| GitHub | Trust/legal drafts | Created | External legal/security review before launch | `docs/legal/*`, `docs/security/*` |
| Wix | Commercial shell | External / not modified here | Apply CMS/page strategy in Wix | Pending connector/editor evidence |
| Gamma | Design references | External / not inventoried here | Map deck URLs/IDs to page roles | Pending exact IDs |
| Azure | Secure runtime | Not started | Select qualified Managed Secure use case | `future-azure/*` |
| Domeneshop | DNS/HTTPS | External | Verify after Pages/custom domain setup | Pending evidence |
| GitHub / Drive | Atlas Workspace research and controlled records | Recorded; architecture `PENDING_REVIEW` | Approve/reject `ATL-DEC-20260805-034`; then create PRD, UX, CIAM, data-flow, threat-model and entitlement specifications | `active-source/2026-08-05/`, `governance/*ATLAS_WORKSPACE*`, Drive Workspace report/memory records |
| Wix | Workspace commercial/member gateway | Boundary defined; not implemented | Design secure handoff to external Workspace without moving authoritative controls into Wix | ATL-DEC-20260725-014; Workspace addendum |
| Secure runtime | Workspace identity, routing, ledger, caps, storage and audit | Not implemented or validated | Non-public architecture and security foundation only; preserve `NO_GO` | Workspace security and validation addenda |
| Product architecture | Seven-surface full deployment model | Controlled planning baseline added; architecture choices `PENDING_REVIEW` | Owner decision on Workspace, Organisation Administration, Control Center, Support/Status, Developer/Integration and secure runtime scope | `ATLAS_FULL_DEPLOYMENT_UPDATE_REGISTER_1545_06082026.md` |
| Atlas Workspace | End-user dashboard, workflows, projects, files, artifacts, usage, notifications and feedback | Specified; not implemented | Complete PRD/UX and Phase 3 MVP after security foundation | Full deployment report and implementation playbook |
| Customer administration | Organisation users, groups, roles, policy, budgets, retention, knowledge and audit | Missing | Design in Phase 1; implement in Phase 6 for Business Workspace | Full deployment implementation playbook |
| Atlas Control Center | Tenant, entitlement, provider, workflow, support, security, incident and cost operations | Missing; P0 prerequisite | Specify and implement minimum Control Center before real-customer production pilot | Architecture proposal; security addendum |
| Entitlement/runtime | Identity, tenant/object authorization, atomic reservations, ledger/settlement and hard caps | Required; not implemented or validated | Implement in Phase 2 and test race, reversal, expiry and reconciliation paths | Full deployment validation gates FD-04/FD-05 |
| Knowledge/RAG | Persistent source lifecycle, retrieval authorization, citations and deletion | Missing | Implement after core Workspace; enforce document authorization before model access | Security addendum; FD-06 |
| Connectors/API | OAuth, read-only connectors, approved writes, service accounts and webhooks | Deferred; not implemented | Begin with controlled read-only after Business Workspace controls; no initial unrestricted writes | ATL-DEC-20260806-039 proposal |
| Operations | Observability, support, service status, incident and recovery | Incomplete | Implement before pilot and validate alerts, runbooks, backup/restore and customer communication | FD-11/FD-12 |
| Commerce/accounting | Wix/payment provisioning, cancellation, refund, credit note, entitlement and Conta reconciliation | Foundation/planning only | Complete sandbox and negative-path tests before paid release | FD-08; existing consumer/MVA controls |
| Release | Closed pilot and production profiles | `NO_GO` | Pass profile-specific gates and obtain explicit written GO | Full deployment validation record |
