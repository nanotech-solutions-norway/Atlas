# Atlas AI Launch Gates and Acceptance Criteria — 11:35, 11.07.2026

> **Control status:** Recommended consolidated working baseline. Commercial pricing, provider-delivery rights, legal interpretation, public availability, production routing and site identity remain approval-gated where identified as PENDING_REVIEW.

> **Execution boundary:** No Wix publication, Gamma editing, Azure deployment, subscription activation or production change was performed.

## Hard release rule

Any failed blocking criterion, missing evidence, unresolved P0/P1 defect, exposed secret, incorrect charge, entitlement bypass, hard-cap failure, unsupported public claim, unapproved data-processing flow or unverified provider-delivery right produces **NO-GO**.

## Release profiles

| Gate group | A: Public early access | B: Paid subscription | C: Managed Secure |
|---|---|---|---|
| Governance/routes/content | Required | Required | Required |
| Billing/entitlement/usage | Checkout disabled | Required | Required where access exists |
| Provider routing/cost | Disclosure only | Required | Required if runtime included |
| Secure intake/storage | No confidential intake | Qualification only | Required |
| Legal/privacy/incident | Website baseline | Consumer/subscription baseline | Full secure-delivery baseline |

## Defect classification

| Class | Definition | Release treatment |
|---|---|---|
| P0 | Active exposure, security compromise, repeated incorrect charging, unrestricted access or severe harm | Stop and incident process |
| P1 | Entitlement bypass, material billing error, cap failure, broken cancellation, sensitive logging, critical route failure | No release |
| P2 | Material usability, analytics or non-critical workflow defect with workaround | Conditional, dated remediation |
| P3 | Cosmetic or low-impact defect | May release if documented |

## Gate register

| ID | Gate | Blocking evidence |
|---|---|---|
| G00 | Source and decision integrity | Source register, approval statuses, contradiction log |
| G01 | Canonical routes and navigation | Route scan, redirects, link inventory |
| G02 | Public content, pricing and claims | Approved copy export, claims references |
| G03 | CMS/configuration integrity | CMS export and configuration diff |
| G04 | Identity and account security | Authentication, recovery and revocation tests |
| G05 | Billing, MVA and subscription lifecycle | Charge, invoice, renewal, refund and cancellation tests |
| G06 | Entitlement provisioning and revocation | Idempotency, wrong-plan and revocation tests |
| G07 | Usage ledger and reconciliation | Provider/accounting reconciliation |
| G08 | Hard caps, resets and premium-use units | Concurrency, reset and warning tests |
| G09 | Model routing and provider resilience | Routing policy, outage/fallback tests |
| G10 | Family named-user controls | Invite/remove/limit and credential-sharing controls |
| G11 | Safety and acceptable use | Policy tests and boundary copy |
| G12 | Privacy, retention and provider disclosure | Data inventory, retention/deletion test, disclosure |
| G13 | Security, secrets and dependencies | Secret scan, dependency scan, least privilege |
| G14 | Observability, cost alarms and incident response | Alerts, runbooks and tabletop |
| G15 | Accessibility, performance and device support | WCAG 2.2 AA target tests, CWV/device results |
| G16 | SEO, AEO/GEO and indexing | Canonical, hreflang, schema, sitemap, robots |
| G17 | Support and operational readiness | Owners, support routes, customer communications |
| G18 | Pilot economics and scale readiness | Cohort costs, usage, support and margin evidence |
| G19 | Deployment, smoke test and rollback | Release record, smoke test, rollback |
| G20 | Managed Secure evidence | Identity, private storage, audit, revocation, restore |
| G21 | Provider commercial and delivery eligibility | Contract/terms assessment and provisioning route |
| G22 | Consumer, age and education-policy readiness | Terms, age treatment, academic-integrity and cancellation review |

## Acceptance criteria by critical gate

### G00 — Source and decision integrity

- 100% of release-critical inputs have owner, version and status.
- No unresolved contradiction exists in routes, availability, pricing or provider delivery.
- PENDING_REVIEW items cannot silently enter production.

### G02 — Public content, pricing and claims

- Prices match checkout and terms.
- “Included” provider capabilities match the actual delivery mechanism.
- No permanent model-version promise.
- No inherited certification, SLA, privacy, compliance or residency claim.
- Early-access status is visible wherever paid capability is described.

### G05 — Billing and subscription lifecycle

- Gross consumer price, net revenue and MVA treatment reconcile.
- Duplicate webhook/event processing does not duplicate charges or entitlements.
- Failed payment, grace period, cancellation and refund paths are tested.
- Customer can identify renewal date, price and cancellation route.

### G07/G08 — Usage and caps

- Every metered request produces one attributable ledger event.
- Customer balance cannot become negative.
- Parallel requests cannot bypass the hard cap.
- Monthly reset is deterministic and idempotent.
- Premium-use units have a documented cost and routing definition.
- No chargeable top-up occurs without affirmative customer action.

### G09/G21 — Provider routing and eligibility

- Atlas documents whether access is seat-based, customer-owned or API/runtime-based.
- Provider terms permit the chosen service model.
- Routing policy identifies approved providers, capability classes and fallback.
- Public copy does not promise an unavailable provider/model.
- Provider pricing and policy review is dated.

### G10 — Family plan

- Maximum four named users including owner.
- Invitation acceptance and removal are authorized.
- Shared allowance is atomic under concurrency.
- Password/credential sharing is prohibited.
- A removed member loses access promptly.

### G11/G22 — Student and consumer safety

- Younger-school-pupil marketing and use are excluded unless separately approved.
- Student use is framed as planning, explanation, revision and source discipline.
- Cheating, ghostwriting and direct assignment submission are prohibited.
- Consumer use excludes emergency and regulated-decision reliance.
- Age, guardian and institution requirements are reviewed before launch.

### G12/G13 — Privacy and security

- Public forms reject confidential file submission.
- Customer prompts and files are absent from public logs and GitHub evidence.
- Secrets are stored outside code/frontends and scanned before release.
- Retention/deletion can be executed and evidenced.
- Provider disclosures describe data handling by delivery mode.

### G15/G16 — Accessibility and discovery

- Keyboard access, focus visibility, labels, errors, contrast, reflow, reduced motion and target size pass against the WCAG 2.2 AA target [W8].
- LCP, INP and CLS are monitored.
- Every indexable page self-canonicalizes and has a reciprocal language peer.
- Structured data matches visible content; eligibility is not described as guaranteed [W7].
- AI search optimization follows helpful, crawlable, source-grounded content principles [W5-W6].

### G18 — Economics

- Provider and variable cost remain within approved plan caps.
- Support cost and refund rate are included.
- At least one full reset cycle is observed.
- Scale decision is based on actual cohort data, not modelled assumptions alone.

### G20 — Managed Secure

- One named journey is tested end to end.
- Identity, authorization, private storage, logging, revocation, deletion and restore work.
- Incident and misdelivery scenarios are tested.
- Public wording is limited to implemented controls.

## Evidence record

Every gate record must contain: gate ID, release profile, owner, tester, environment, version/commit, date, procedure, expected result, actual result, sanitized evidence location, defect references, result and approver.

## Go/no-go authority

- **GO:** all blocking gates pass.
- **CONDITIONAL GO:** P2/P3 only, with named approver, expiry, residual risk and rollback trigger.
- **NO-GO:** any P0/P1, missing blocking evidence or unresolved PENDING_REVIEW release dependency.

## Source basis

Updates the attached July launch-gates blueprint by adding provider-commercial eligibility, age/education-policy readiness, WCAG 2.2 and current AI Act/AI-search considerations.
