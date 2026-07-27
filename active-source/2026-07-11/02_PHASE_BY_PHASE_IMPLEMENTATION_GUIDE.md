# Atlas AI Phase-by-Phase Implementation Guide — Security, Privacy and Trust Integrated — 23:55, 27.07.2026

> **Control status:** Active implementation baseline. Existing approved commercial and governance decisions apply. Legal interpretations, architecture selection, public availability and production activation remain approval-gated where marked `PENDING_REVIEW`.

> **Execution boundary:** This update modifies controlled project records only. It does not publish Wix, activate checkout, deploy a production secure runtime or relax release locks.

## Program rule

A phase is complete only when:

1. required controls are implemented for the exact scope;
2. evidence is captured and linked;
3. defects and exceptions are recorded;
4. validation passes;
5. the designated owner approves the exact release candidate.

Security, privacy, GDPR and trust controls begin in Phase 0 and continue through all phases. Phase 6 closes and assures the programme; it is not the first security phase.

## Integrated dependency sequence

| Phase | Objective | Security/privacy output | Blocking dependency |
|---|---|---|---|
| 0 | Architecture, source authority and route lock | Security/privacy charter, data classes, platform boundaries, control register | None |
| 0.5 | Product and commercial object contract | Lane risk class, provider/role/retention fields, release-state separation | Phase 0 |
| 1 | Public informational shell | Admin-IAM evidence, privacy/cookie/trust pages, low-risk forms, claims validation | Phase 0 and 0.5 |
| 2 | Identity, account and structured handoff | CIAM, roles, sessions, age/payer controls, DSAR/deletion paths | Approved Phase 2 architecture |
| 3 | Entitlement, routing and secure control plane | Server-side proxy, secrets, authorization, caps, logs, private storage | Phase 2 |
| 4 | Pilot and Managed Secure MVP | Secure intake, tenant isolation, incident/restore evidence, one named journey | Phase 3 where runtime applies |
| 5 | Productization and operations | Repeated reviews, drift checks, supplier/claims control, support security | Stable Phase 1-4 workflows |
| 6 | Assurance and release closure | Complete security/privacy acceptance, tabletop, restore, risk acceptance, GO record | Runs throughout; closes last |

## Cross-cutting control families

Every phase must map work to the controlled catalogue:

- GOV — governance and release control
- IAM — identity and access
- DAT — data classification and handling
- PRV — privacy and GDPR operations
- APP/API — application and API security
- AI/RAG — AI, retrieval, tool and agent security
- SDLC/GIT — secure development and GitHub
- SUP — suppliers, DPA and transfers
- LOG — logging and alerting
- IR/BCM — incidents, continuity and recovery
- WIX/AZR/DB — platform controls
- REL/TRU — release and trust claims

## Phase 0 — Architecture, governance and canonical control lock

### Implementation actions

1. Apply the current source-authority hierarchy and retrieve all six canonical registers.
2. Approve the governed solution-layer positioning and the three-plane architecture.
3. Lock Wix to public/low-risk responsibilities.
4. Lock GitHub to engineering/governance and sanitized evidence.
5. Require a separate secure execution plane for authenticated, AI-routed, entitled, confidential or restricted workflows.
6. Define Public, Internal, Confidential, Restricted, Special-category/highly sensitive and Secret classifications.
7. Create the security/privacy programme charter and 80-control register.
8. Name security, privacy, incident, release and test-data owners.
9. Create claims, decision, error, validation, learning, authority and session-close records.
10. Preserve safety and release locks.

### Exit criteria

- Three-plane responsibilities are approved and non-conflicting.
- All controls have an owner role, status and evidence requirement.
- No public/frontend system is designated as the secure system of record.
- Named owners and escalation routes exist.
- `publicAllowed`, `purchaseAllowed`, `releaseApproved` remain false unless a separate exact release decision changes them.

## Phase 0.5 — Product, pricing, provider and processing contract

### Required records

- business package records;
- Student Basic, Student Plus and Everyday Basic;
- Family blocked/deferred record;
- Managed Secure qualification-only record;
- provider capability and approved-provider classes;
- routing policy versions;
- controller/processor role;
- data classification and permitted inputs;
- DPA/TIA and subprocessor status;
- retention/deletion reference;
- terms and disclosure versions;
- risk and release profile.

### Minimum fields

| Group | Required fields |
|---|---|
| Identity | `plan_id`, version, segment, status, effective date |
| Commercial | gross/net price, MVA treatment, billing period, cancellation/refund |
| Entitlement | capabilities, allowance, hard cap, named users, reset, no automatic paid overage |
| Data/privacy | data class, purpose, role, provider, transfer, retention, DPIA status |
| Security | required auth, storage class, logging, upload policy, incident tier |
| Governance | terms, claims, owner, evidence, approval and expiry |
| Runtime | routing policy, meter, fallback, outage, ledger and kill switch |

### Exit criteria

- Public plan, terms, provider, privacy and runtime records reconcile.
- Unapproved or blocked plans cannot be public or purchased.
- Provider terms and DPA/TIA status support the intended delivery.
- No permanent model, unlimited use, Norway-only processing or zero-retention promise is made without evidence.

## Phase 1 — Public informational shell and low-risk qualification

### Canonical page roles

1. Home
2. Solutions
3. Business
4. Students
5. Consumers
6. Managed Secure
7. Pricing
8. Trust
9. Platform Lanes
10. Onboarding
11. Resources
12. FAQ
13. About
14. Contact
15. Legal

### Build controls

- Bokmål root and reciprocal English `/en/`.
- Accurate routes, canonical links, hreflang, sitemap and structured data.
- Administrative MFA/passkey and collaborator-role evidence.
- Cookie/tracker inventory and valid consent for non-essential technologies.
- Privacy, cookie, retention, provider, AI-output and acceptable-use content.
- Security contact and controlled escalation wording.
- No-confidential-upload warning on every relevant form.
- No confidential/restricted file field in ordinary public forms.
- Claims linked to approved evidence and public-allowed status.
- Checkout and purchase routes disabled.
- Managed Secure wording limited to qualification/architecture review.
- Keyboard, screen-reader, focus, contrast, reflow and responsive validation.
- Security/privacy page content is not treated as proof of control implementation.

### Blocking validation

- fresh authoritative Wix page tree;
- Contact and FAQ exist as separate page roles;
- forms, notifications and collaborator access verified;
- cookie banner/consent log behavior verified;
- no secrets or sensitive data in Velo/public assets;
- claim scan clean;
- no public plan or production entitlement;
- explicit Phase 1 release decision.

### Exit criteria

A Phase 1 PASS authorizes only the approved public informational scope. It does not authorize member service, payment, AI routing, confidential intake or Managed Secure data handling.

## Phase 2 — Identity, account and structured handoff

### Architecture decision

Select and approve the customer identity model. Microsoft Entra External ID is the preferred candidate for a new dedicated CIAM architecture, but remains `PENDING_REVIEW`. Wix Members may be used only within its approved risk and capability boundary.

### Components

- verified account identity;
- secure sign-up, sign-in, recovery and session lifecycle;
- account owner/member roles;
- age-16 minimum and fail-closed age-16/17 payer/contract/privacy model;
- consent and notice versions;
- cancellation and data-rights links;
- low-risk intake classification;
- secure-escalation trigger;
- no public confidential upload;
- revocation and offboarding.

### Blocking tests

- duplicate identity;
- insecure recovery;
- session fixation/timeout/revocation;
- unauthorized plan or object view;
- age/eligibility bypass;
- wrong payer/guardian state;
- wrong-plan provisioning;
- secure-required request blocked from ordinary intake;
- deletion and rights-request path.

## Phase 3 — Secure execution, entitlement, routing and reconciliation

### Required control plane

1. Server-side provider gateway/proxy.
2. No frontend provider credentials.
3. Managed secret storage and rotation.
4. Tenant/object authorization.
5. Private storage and protected network paths where justified.
6. Idempotent billing/event ingestion.
7. Exactly-once entitlement transitions.
8. Normalized usage/cost ledger.
9. Hard caps under concurrency.
10. Deterministic reset and retry.
11. Provider policy, region, retention and training-use mapping.
12. Rate limits, cost alarms, suspension and kill switches.
13. Metadata-first centralized logging.
14. Prompt-injection, tool/egress and structured-output controls.
15. Provider outage/fallback.
16. Deletion propagation and audit evidence.

### Exit criteria

- no entitlement or authorization bypass;
- no exposed secret;
- no cross-tenant access;
- hard cap cannot be bypassed;
- no silent chargeable overage;
- provider/accounting/entitlement states reconcile;
- prompt-injection and exfiltration tests pass;
- data retention/deletion tests pass;
- current DPA/TIA and provider approvals exist.

## Phase 4 — Controlled pilot and Managed Secure MVP

### Subscription pilot

- invited cohort only;
- sandbox/non-public or explicitly approved production scope;
- usage, support, refund, abuse and cost measurement;
- privacy/security incidents and near misses recorded;
- one full reset/cancellation/refund cycle where applicable.

### Managed Secure minimum journey

- qualified architecture review;
- contract and DPA;
- authenticated invitation;
- private storage;
- per-customer isolation;
- secure file quarantine/malware scanning;
- least-privilege support access;
- audit logging;
- retention/deletion;
- revocation;
- provider kill switch;
- incident workflow;
- immutable/protected backup;
- successful restore test.

### Exit criteria

No general availability until one named journey passes all security, privacy, contractual, incident and recovery gates and public wording exactly matches the implemented scope.

## Phase 5 — Productization and secure operations

- governed CMS and claims publishing;
- bilingual, privacy and provider drift checks;
- recurring access review;
- vulnerability and dependency management;
- supplier/DPA/subprocessor monitoring;
- retention and deletion review;
- incident and near-miss review;
- support knowledge base with secure handling;
- release tags, provenance and rollback;
- security KPIs;
- quarterly governance review;
- customer due-diligence response pack.

## Phase 6 — Security, privacy, incident and final acceptance

### Required closure evidence

- security/privacy charter and owner map;
- complete control register;
- admin MFA/passkey evidence;
- access review and offboarding test;
- clean secret/repository/frontend scan;
- GitHub ruleset/CODEOWNERS/review/CI evidence;
- Wix form/cookie/collaborator evidence;
- ROPA, role matrix, lawful-basis and retention records;
- DPA, supplier and TIA/SCC packs;
- DPIA decisions;
- rights-request test;
- protected runtime/security test results;
- prompt-injection and tenant-isolation tests;
- incident plan and tabletop;
- backup and restore test;
- claims register and public-copy validation;
- exact release-candidate manifest;
- residual risk/exception record;
- explicit written GO.

### Final exit criteria

- no open P0/P1 defect;
- no missing blocking evidence;
- no exposed secret or customer-sensitive evidence;
- no unsupported public claim;
- no unapproved processing or provider route;
- rollback and incident owners acknowledge readiness;
- exact release candidate is approved in writing.

## Evidence format

Each control/gate record must contain:

- control/gate ID;
- release profile;
- owner and tester;
- environment;
- source commit/configuration/legal-copy versions;
- date and procedure;
- expected and actual result;
- sanitized evidence location;
- defects/exceptions;
- result and approver.

## Current next workstream

1. Fresh Wix Phase 1 security/privacy/trust audit.
2. GitHub organization/repository security-settings audit.
3. Owner appointment.
4. ROPA, role matrix, supplier register, retention, DSAR and DPIA screening.
5. Staging trust/legal/privacy copy implementation.
6. CIAM and secure-runtime ADR preparation.
7. Preserve `NO_GO` and all release booleans.

## Release effect

No public checkout, real payment, production entitlement, provider credential, confidential intake or Managed Secure activation is authorized.
