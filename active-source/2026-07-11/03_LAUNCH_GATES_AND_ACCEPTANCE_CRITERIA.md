# Atlas AI Launch Gates and Acceptance Criteria — Security, Privacy and Trust Integrated — 23:55, 27.07.2026

> **Control status:** Active gate baseline. A report, policy, platform feature or drafted page does not pass a gate without exact implementation and test evidence.

> **Release boundary:** `publicAllowed=false`, `purchaseAllowed=false`, `releaseApproved=false` and `NO_GO` remain controlling.

## Hard release rule

Any failed blocking criterion, missing evidence, unresolved P0/P1 defect, exposed secret, incorrect charge, authorization or entitlement bypass, hard-cap failure, unsupported public claim, unapproved processing flow, missing DPA/TIA, failed restore, or unverified provider-delivery right produces **NO-GO**.

## Release profiles

| Profile | Scope | Explicit exclusions until separately approved |
|---|---|---|
| A — Public informational | Public pages, low-risk qualification, legal/trust/cookie content | Member service, payment, AI routing, confidential intake, production entitlement, Managed Secure delivery |
| B — Controlled non-public testing | Hidden test routes/plans, sandbox transactions, sanitized evidence | Public discovery, real charge, production credentials, automatic production provisioning |
| C — Paid member/subscription | Identity, payment, entitlement, usage, cancellation and support | Any function without passed legal, privacy, security, tax and runtime gates |
| D — Managed Secure pilot | One named contract-bound secure journey | General availability or absolute security/compliance claims |

## Defect classification

| Class | Definition | Release treatment |
|---|---|---|
| P0 | Active exposure, credential compromise, unrestricted access, cross-tenant disclosure, repeated incorrect charging or severe harm | Stop, contain and trigger incident process |
| P1 | Authorization/entitlement bypass, cap failure, broken cancellation/deletion, sensitive logging, critical route/privacy failure, failed restore | No release |
| P2 | Material usability, performance or non-critical workflow defect with controlled workaround | Conditional, dated remediation only |
| P3 | Cosmetic or low-impact defect | May release if documented and approved |

## Gate register

| ID | Gate | Blocking evidence |
|---|---|---|
| G00 | Source and decision integrity | Source register, classifications, contradiction log |
| G01 | Canonical routes and navigation | Current Wix tree, route/link/redirect scan |
| G02 | Public content, pricing and claims | Approved copy export and claims references |
| G03 | CMS/configuration integrity | CMS/configuration export and diff |
| G04 | Administrative and customer identity | MFA/passkeys, roles, recovery, session and revocation tests |
| G05 | Billing, MVA and subscription lifecycle | Charge, invoice, renewal, cancellation, refund and reconciliation |
| G06 | Entitlement provisioning and revocation | Idempotency, wrong-plan, suspension and revocation tests |
| G07 | Usage/cost ledger and reconciliation | Provider, entitlement and accounting reconciliation |
| G08 | Hard caps, resets and premium-use controls | Concurrency, reset, warning and no-overage tests |
| G09 | Provider routing and resilience | Approved provider register, route, outage, fallback and kill-switch tests |
| G10 | Family/named-user controls | Deferred/blocked for initial scope; future invite/remove/limit tests |
| G11 | Safety and acceptable use | Policy tests and boundary copy |
| G12 | Privacy operations | ROPA, role matrix, lawful basis, rights workflow, retention/deletion |
| G13 | Secrets, repository and SDLC | Secret scan, rulesets, reviews, CI scans, workflow permissions |
| G14 | Logging, alerting and incident response | Log coverage, alerts, IR plan and tabletop |
| G15 | Accessibility, performance and device support | Legal baseline plus approved internal target tests |
| G16 | SEO, AEO/GEO and indexing | Canonical, hreflang, schema, sitemap and robots |
| G17 | Support and operational readiness | Owners, secure support routing and customer communications |
| G18 | Pilot economics and scale readiness | Actual cohort cost, usage, support and margin evidence |
| G19 | Deployment, smoke test and rollback | Release manifest, protected promotion, smoke and rollback |
| G20 | Managed Secure control evidence | Identity, isolation, storage, upload, audit, deletion, incident and restore |
| G21 | Provider commercial and processing eligibility | Terms, DPA, subprocessors, TIA/SCC, region and provisioning route |
| G22 | Consumer, student and age readiness | Terms, age 16/17 controls, payer, privacy, academic-integrity and cancellation |
| G23 | Wix public-plane security/privacy | Collaborators, forms, notices, cookie/tracker and Velo/public-asset review |
| G24 | AI, RAG and tool security | Prompt injection, provenance, tenant isolation, output and tool/egress tests |
| G25 | Data classification and system placement | Classification, approved storage, encryption and deletion propagation |
| G26 | Business continuity and recovery | Backup policy, immutable/protected copy, RTO/RPO and restore test |
| G27 | Trust Center and claims discipline | Security/privacy/provider claim matrix and page scan |
| G28 | Exact release-candidate authorization | Bound commit/config/legal/provider/test versions and signed GO |

## Profile A — Public informational acceptance

All of the following are blocking:

- current authoritative Wix page tree;
- all 15 Phase 1 page roles, including separate Contact and FAQ;
- Bokmål/English parity;
- admin MFA/passkey evidence for site and source-control administrators;
- collaborator-role and form-submission access review;
- no confidential/restricted upload fields;
- clear no-confidential-upload warning;
- cookie/tracker inventory and valid consent behavior for non-essential technology;
- privacy, cookie, provider, retention, AI-output and security-contact content;
- claim scan clean;
- no public plan, payment, entitlement or provider credential;
- keyboard, screen-reader, focus, contrast, reflow and responsive tests;
- exact Phase A release-candidate approval.

A Profile A PASS does not authorize Profiles B-D.

## Profile B — Controlled non-public testing acceptance

In addition to relevant Profile A controls:

- non-discoverable/allowlisted test route;
- sandbox/test payment only;
- no production provider credentials or production entitlements;
- distinct test offers and test data;
- stable fail-closed reason codes;
- test-data retention and deletion;
- sanitized evidence storage;
- negative-path tests for missing/mismatched approvals;
- immutable release/test candidate identifier.

## Profile C — Paid member/subscription acceptance

### Identity and privacy

- approved CIAM/member architecture;
- secure sign-up, recovery, session and revocation;
- age 16 minimum and fail-closed age-16/17 payer/contract/privacy implementation;
- privacy notice and consent/version records;
- rights-request and account deletion test;
- ROPA, role, lawful-basis and DPIA decisions.

### Payment and entitlement

- provider onboarding and settlement evidence;
- exact price/MVA/terms match;
- durable confirmation;
- duplicate event/idempotency tests;
- cancellation, withdrawal, refund and credit-note reconciliation;
- hard caps and no automatic paid overage;
- provider/accounting/entitlement state agreement.

### Security and provider

- server-side provider proxy;
- no frontend credentials;
- approved provider register;
- DPA/subprocessor/TIA evidence;
- rate/cost controls;
- authorization and tenant tests;
- logging/alerts;
- incident and rollback evidence.

## Profile D — Managed Secure pilot acceptance

- named customer/use case and signed scope;
- controller/processor role and DPA;
- DPIA decision;
- authenticated invitation and least privilege;
- private storage and tenant isolation;
- secure upload, quarantine and malware scanning where files are accepted;
- retrieval provenance and deletion;
- support access logging;
- provider kill switch and fallback;
- incident/misdelivery runbooks;
- protected/immutable backup and successful restore;
- provider-revocation exercise;
- public wording limited to the exact evidenced journey.

## Critical gate criteria

### G00 — Source and decision integrity

- 100% of release-critical sources have owner, version and classification.
- Raw research is `EVIDENCE_ONLY` until reconciled.
- No report assumption overrides current canonical or implementation evidence.
- Missing companion artifacts are recorded, not silently assumed.

### G04 — Identity

- administrators use approved MFA/passkeys;
- no shared administrator accounts;
- least-privilege roles;
- recovery does not bypass security;
- sessions rotate and revoke;
- quarterly access review completed for Profiles C/D.

### G12 — Privacy operations

- ROPA and lane role analysis complete;
- purpose/lawful basis recorded;
- notices match actual processing;
- cookie consent valid where required;
- DPA/TIA and subprocessors controlled;
- retention and deletion test pass;
- rights-request workflow tested;
- DPIA completed where triggered.

### G13 — Repository and SDLC

- protected branch/ruleset;
- required reviews and sensitive-path owners;
- secret scanning/push protection or documented compensating scan;
- dependency/code scan;
- explicit least-privilege workflow permissions;
- protected deployment environment;
- no secrets or customer data in repository, issues, logs or screenshots.

### G14 — Logging and incident

- metadata-first log standard approved;
- raw prompts/files excluded by default unless a documented exception exists;
- alerts tested;
- incident and breach decision procedures complete;
- session/key rotation runbooks tested;
- tabletop completed for Profiles C/D.

### G20 — Managed Secure

- one named journey passes end to end;
- identity, authorization, storage, quarantine, logging, revocation, deletion and restore work;
- customer isolation test passes;
- misdelivery and provider-compromise scenarios tested;
- claims match exact controls.

### G21 — Provider eligibility

- provider/service/endpoint identified;
- delivery model contractually permitted;
- DPA and subprocessor record complete;
- transfer and region assessment complete;
- retention/training/abuse-monitoring settings documented;
- fallback and exit plan documented;
- public disclosures match the exact lane.

### G23 — Wix public plane

- Wix scope limited to public/low-risk responsibilities;
- collaborator roles reviewed;
- form viewers/notifications restricted;
- no sensitive upload;
- consent log and cookie behavior tested;
- Velo/public assets contain no production secret;
- public/legal/trust content version aligned.

### G24 — AI/RAG/tool security

- prompt-injection and indirect-injection tests pass;
- no secret in prompt/context;
- retrieval provenance recorded;
- tenant isolation passes;
- uploads scanned before ingestion;
- structured outputs validated;
- tools and egress limited;
- human approval for consequential actions;
- provider kill switch works.

### G26 — Recovery

- backup configuration protected;
- restoration completes within approved objective;
- backup does not reintroduce deleted access or unsupported data;
- recovery actions and exceptions are recorded.

### G27 — Claims

- no "fully GDPR compliant", "completely secure", "zero risk", "all data stays in Norway", "zero retention", "24/7 monitoring", unsupported certification or guaranteed outcome claim;
- vendor certifications/SLAs are attributed to the vendor;
- conditional claims state scope and dependencies;
- every published claim is present in the claims register with `publicAllowed=true`.

## Evidence record schema

Each gate record includes:

- gate/control ID;
- release profile;
- owner, tester and approver;
- environment;
- source commit and configuration versions;
- legal/privacy/provider document versions;
- procedure, expected and actual result;
- sanitized evidence location;
- defect/exception references;
- result;
- approval timestamp and expiry/review trigger.

## Go/no-go authority

- **GO:** every blocking gate for the exact profile passes.
- **CONDITIONAL GO:** P2/P3 only, with named approver, expiry, residual risk, compensating control and rollback trigger.
- **NO-GO:** any P0/P1, missing evidence, unresolved `PENDING_REVIEW` dependency or mismatched release candidate.

## Current aggregate decision

Profiles A-D remain `NO_GO`. The next executable profile is Profile A validation only. Profiles B-D remain blocked.

## Release effect

No current release flag or platform activation is changed by this document update.
