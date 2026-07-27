# Atlas AI Master Strategy and Commercial Baseline — Security, Privacy and Trust Integrated — 23:55, 27.07.2026

> **Control status:** Updated active working baseline. Existing approved commercial decisions and canonical release controls apply. Architecture selections, legal interpretations, public claims and production activation remain approval- and evidence-gated where marked `PENDING_REVIEW`.

> **Execution boundary:** This update changes controlled project documents and governance records only. It does not publish Wix, enable checkout, create real-money plans, deploy Azure, activate provider credentials or release Managed Secure.

## Executive decision

Atlas AI operates as a **Norway-first governed AI solution and integration layer**. Atlas owns problem framing, workflow design, knowledge architecture, onboarding, data and safety boundaries, provider selection, configuration, QA, support and lifecycle governance. Third-party providers supply model, cloud, website, identity and development capabilities.

Security, privacy, GDPR accountability and trustworthy public claims are part of the business model and delivery method. They are not optional marketing additions and must be evidenced before paid, authenticated, AI-routed or confidential services are released.

Atlas must not be positioned as:

- a proprietary foundation-model company;
- an unrestricted custom-GPT storefront;
- a provider-subscription reseller;
- a generic AI consultancy without defined scope and controls;
- a certified or guaranteed-secure provider without Atlas-specific evidence.

## Current release posture

The following remain controlling:

- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
- public checkout and real-money production charging disabled
- production provider credentials and automatic production entitlements prohibited
- public write endpoints and frontend provider tokens prohibited
- ordinary public forms limited to low-risk qualification
- Managed Secure limited to qualification and architecture review
- overall release state `NO_GO`

## Audience and commercial hierarchy

| Lane | Priority | Commercial model | Current status |
|---|---|---|---|
| Professional / Business | Primary | Fixed-scope implementation, customer-owned licences where applicable, or explicitly itemised provider/infrastructure costs | Discovery and scoped delivery subject to data/provider review |
| Student Basic | Secondary controlled | NOK 129/month incl. MVA; monthly; Atlas-managed API with hard cap | Approved commercial baseline; hidden/non-public testing only |
| Student Plus | Secondary controlled | NOK 169/month incl. MVA; monthly; Atlas-managed API with hard cap | Approved commercial baseline; hidden/non-public testing only |
| Everyday Basic | Secondary controlled | NOK 159/month incl. MVA; monthly; Atlas-managed API with hard cap | Approved commercial baseline; hidden/non-public testing only |
| Family | Deferred | Earlier price concept retained as historical/commercial evidence only | Blocked from initial restricted launch |
| Managed Secure | Premium qualified | Quote-controlled architecture and secure-delivery service | Qualification/architecture review only |

Commercial approval is not activation approval. No plan may be public or purchasable until legal, payment, identity, entitlement, privacy, security, accounting and acceptance evidence passes.

## Canonical public architecture

- Root language: Bokmål.
- English mirror: `/en/`.
- Primary navigation: Solutions, Managed Secure, Pricing, Trust, Resources, About, Contact.
- Phase 1 uses **15 canonical public page roles**, including FAQ under Resources.
- Canonical audience routes:
  - `/solutions/business-ai/`
  - `/solutions/students/`
  - `/solutions/consumers/`
- Supporting routes:
  - `/platform-lanes/`
  - `/onboarding/`
  - `/legal/`
  - `/resources/faq/`
  - reciprocal English routes under `/en/`

Legacy routes are redirected only after the destination is complete, tested and approved.

## Three-plane operating architecture

### 1. Wix public-commercial plane

Permitted scope:

- public pages and CMS;
- low-risk qualification forms;
- consent and cookie interfaces;
- legal, trust and provider-disclosure pages;
- SEO, multilingual and accessible presentation;
- limited member-facing status or account presentation after separate approval.

Prohibited scope:

- provider secrets;
- confidential/restricted customer artifacts;
- authoritative cross-provider usage or cost ledger;
- protected entitlement decisions;
- confidential Managed Secure processing;
- public or frontend production write credentials.

### 2. GitHub engineering-governance plane

Permitted scope:

- canonical decisions, controls, specifications and release history;
- source code and CI/CD;
- sanitized evidence references;
- claims, route, schema and validation controls.

Prohibited scope:

- production credentials;
- customer prompts/files;
- confidential customer or supplier data;
- private accounting/banking data;
- protected artifacts or secret-bearing screenshots/logs.

### 3. Secure execution/control plane

Required before authenticated, entitled, AI-routed, confidential or audit-sensitive services:

- dedicated identity and session controls;
- server-side provider proxy;
- secrets management and managed identities;
- private storage and tenant/object authorization;
- hard caps, cost controls and usage ledger;
- logging and alerts;
- secure upload quarantine and malware scanning where files are accepted;
- deletion, revocation, backup, restore and incident response.

**Architecture candidates:** Microsoft Entra External ID for customer CIAM and Microsoft Azure for the secure runtime are supported candidates but remain `PENDING_REVIEW` until owner, cost, feature, region, contract and implementation decisions are recorded.

## Product and delivery architecture

### Business solutions

Business packages are named by outcomes rather than providers:

- executive and decision-support workflows;
- commercial growth workflows;
- finance and operations support;
- research and multi-engine workflows;
- team adoption and governance;
- Managed Secure architecture and controlled delivery.

Provider names are disclosed as dependencies or implementation choices, not as Atlas-owned products.

### Student and consumer solutions

Public wording uses **monthly AI usage allowance**, hard caps and no automatic chargeable overage. Internal token, premium-use, reset and routing details belong in versioned terms and runtime configuration.

Student Basic and Student Plus have a product minimum age of 16. Users under 16 are excluded. Users aged 16-17 require the approved fail-closed identity, adult-payer/contract, privacy and support model before activation. Norway's GDPR child-consent threshold is a separate legal concept and does not replace the Atlas product and contract controls.

## Security, privacy and GDPR operating model

Before a service lane processes personal, confidential or restricted data, Atlas must establish:

- data classification and approved system placement;
- processing purpose and lawful basis;
- controller/processor role;
- provider, DPA, subprocessor and transfer assessment;
- retention and deletion;
- rights-request handling;
- DPIA screening and full DPIA where required;
- access, logging, incident and backup controls;
- release-specific evidence and approval.

Public forms must collect only what is necessary for low-risk qualification. Confidential, restricted, special-category or highly sensitive data is not accepted through ordinary public forms.

## AI, RAG and tool-control baseline

Protected AI services require:

- approved provider/model inventory;
- server-side prompts and provider routing;
- no secrets in prompts or client code;
- prompt-injection and data-exfiltration testing;
- retrieval provenance and tenant isolation;
- staged/quarantined ingestion and malware scanning;
- structured-output validation;
- tool and outbound-domain allowlists;
- human approval for consequential actions;
- provider kill switch and fallback;
- metadata-first, privacy-aware logs.

## Trust and claims position

Atlas may describe its operating model and third-party provider use, but public claims must remain bounded by implementation evidence.

Defensible wording includes:

- governed integration and delivery controls;
- low-risk public qualification;
- privacy-by-design or GDPR-aligned workflows **subject to scope, provider, configuration, contract and evidence**;
- human review for important outputs;
- processing location and retention depend on the selected lane and provider.

Prohibited without exact evidence:

- fully GDPR compliant;
- completely secure or zero risk;
- all data stays in Norway;
- zero retention;
- 24/7 monitoring;
- guaranteed accuracy, uptime, ROI, grades or outcomes;
- Atlas-owned ISO/SOC certification;
- inherited vendor certification, SLA or data-residency claims.

## Release profiles

| Profile | Permitted outcome | Blocking boundary |
|---|---|---|
| A — Public informational | Approved public pages, low-risk qualification, trust/legal/cookie content | No member service, payment, provider routing, confidential intake or secure-delivery claim |
| B — Controlled non-public testing | Hidden routes/plans, sandbox transactions and sanitized test evidence after entry gates | No public discovery, real charge, production provider credential or automatic production entitlement |
| C — Paid member/subscription | Identity, payment, entitlement, caps, cancellation, refund and support after complete PASS | No manual/unverifiable ledger, consent, tax or access state |
| D — Managed Secure pilot | One named, contract-bound secure journey after identity/storage/logging/incident/restore evidence | No general availability or absolute security/compliance claim |

## Phase 1 publication position

A limited public informational Phase 1 can be reconsidered only after:

- fresh authoritative Wix page-tree and implementation evidence;
- separate Contact and FAQ implementation;
- Bokmål/English parity;
- current admin MFA/access evidence;
- privacy/cookie/form validation;
- claim and provider-disclosure review;
- security contact and incident-routing content;
- responsive/accessibility/SEO validation;
- explicit release approval for the exact candidate.

Until then, Phase 1 and the overall website remain `NO_GO`.

## Strategic security roadmap

### 0-30 days

- appoint security, privacy, incident, release and test-data owners;
- verify administrative MFA/passkeys and least privilege;
- verify GitHub rulesets/reviews/secrets/security scans;
- complete Wix form/cookie/collaborator evidence;
- create ROPA, role matrix, supplier register, DPA/TIA workflow, retention and rights-request controls;
- complete DPIA screening;
- implement approved trust/security/privacy staging copy;
- create incident and backup policies.

### 31-90 days

Subject to separate architecture approval:

- customer CIAM;
- secure server-side API gateway/proxy;
- managed identity/secret storage;
- private data stores and authorization;
- secure intake/quarantine/malware scanning;
- metadata-first logging and alerts;
- deletion propagation;
- AI/RAG/tool security tests;
- OIDC/protected deployment pipeline.

### 3-6 months

- one named Managed Secure pilot;
- tenant-isolation, revocation and deletion tests;
- incident tabletop and provider-revocation exercise;
- restore test;
- full release-gate rerun.

### 6-12 months

- recurring assurance and customer due-diligence pack;
- certification business-case review after stable operations;
- no certification claim unless formally awarded.

## Current unresolved decisions

1. Named security/privacy/incident/release owners.
2. Entra External ID or alternative CIAM.
3. Azure or alternative secure runtime.
4. Exact provider primary/fallback model.
5. DPA/TIA and transfer decisions for each lane.
6. Exact retention periods and raw-prompt logging exceptions.
7. DPO requirement and external specialist support.
8. Certification roadmap.
9. Current Wix implementation evidence.
10. Final public release approval.

## Source and evidence rule

The attached security report is preserved as research evidence. Its recommendations become governing only through explicit classification in Atlas records. Canonical GitHub and current implementation evidence override report assumptions that were caused by unavailable internal connector access.

## Release effect

No public plan, checkout, real-money charge, production entitlement, provider credential, public write endpoint or Managed Secure activation is authorised by this update.
