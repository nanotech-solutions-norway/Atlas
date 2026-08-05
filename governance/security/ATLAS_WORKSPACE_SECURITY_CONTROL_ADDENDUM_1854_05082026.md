# Atlas Workspace Security Control Addendum

**Timestamp:** 18:54, 05.08.2026 Europe/Oslo  
**Classification:** `PENDING_REVIEW` architecture and control design; control-preservation rules marked `AUTO_APPROVED`  
**Release state:** `NO_GO`  

## Security objective

The Atlas Workspace must provide an authenticated execution interface for Atlas-managed API plans without moving secrets, authoritative entitlement decisions, protected data or provider execution trust into Wix or the browser.

## Trust boundaries

1. **Public Wix plane:** untrusted public interaction, commercial presentation and controlled account entry.
2. **Workspace client:** authenticated but still untrusted client; no secret or authoritative decision storage.
3. **Identity plane:** CIAM, MFA, token issuance, session revocation and federation.
4. **Secure runtime:** authorization, policy, provider routing, metering, protected state and audit.
5. **Data plane:** tenant-isolated database, object storage, quarantine and audit stores.
6. **Provider plane:** external AI model and approved tool providers.
7. **Operations plane:** privileged administration, monitoring, incident response and key rotation.

## Mandatory control catalogue

| ID | Control | Required evidence before pilot |
|---|---|---|
| WS-SEC-001 | Provider and infrastructure secrets remain server-side in a managed vault; no secret appears in Wix, browser bundles, URLs, screenshots, logs or repositories. | Secret scan, bundle inspection, vault policy and rotation test |
| WS-SEC-002 | Every protected request validates identity, tenant, role, object ownership, entitlement and session state. | Negative authorization matrix and cross-tenant tests |
| WS-SEC-003 | Privileged accounts use MFA; administrative functions use least privilege and separate roles. | CIAM/RBAC configuration readback and access tests |
| WS-SEC-004 | Sessions are short-lived, revocable and carried through Secure, HttpOnly and appropriate SameSite cookies or equivalently protected tokens. | Session test pack, fixation/replay/logout tests |
| WS-SEC-005 | Runtime ingress uses TLS, WAF/rate controls, schema validation, request size limits and abuse detection. | Configuration evidence and load/abuse tests |
| WS-SEC-006 | Provider calls originate only from the secure runtime through allow-listed egress. | Network policy and provider-call trace |
| WS-SEC-007 | Usage is reserved atomically before provider execution and settled afterward; insufficient allowance fails closed. | Concurrency, replay, timeout and cap-boundary tests |
| WS-SEC-008 | Usage ledger events are append-only or equivalently tamper-evident and reconcile to provider and commercial records. | Ledger integrity and reconciliation evidence |
| WS-SEC-009 | Tenant data is logically isolated with object-level authorization and tenant-scoped encryption/access policies where supported. | Cross-tenant penetration and data-access tests |
| WS-SEC-010 | Uploads enter quarantine, undergo extension/MIME/signature validation, malware scanning, size limits and safe parsing before use. | Malicious-file, parser and quarantine test set |
| WS-SEC-011 | Data is encrypted in transit and at rest with managed key rotation and least-privilege service identities. | KMS/IAM configuration and rotation evidence |
| WS-SEC-012 | Retention, user deletion, account closure, backup expiration and provider-side deletion are specified and testable. | Retention schedule and end-to-end deletion test |
| WS-SEC-013 | Prompt, output, tool and file data are logged only to the minimum necessary level; sensitive content is excluded or redacted from operational logs. | Logging schema and redaction tests |
| WS-SEC-014 | Provider routing is policy-controlled, versioned and auditable; emergency provider/model disable is available. | Routing tests and kill-switch exercise |
| WS-SEC-015 | Tool use and external connectors are allow-listed, scoped and disabled by default unless separately approved. | Tool policy, OAuth-scope and denial tests |
| WS-SEC-016 | Dependencies, containers, infrastructure templates and repositories are scanned for vulnerabilities and secrets in CI/CD. | Pipeline results and remediation thresholds |
| WS-SEC-017 | Security events, administrative changes, consent, entitlement and deletion actions are auditable. | Audit event catalogue and SIEM/readback evidence |
| WS-SEC-018 | Incident response covers credential compromise, tenant exposure, provider breach, abuse, runaway cost and unavailable provider scenarios. | Tabletop exercise and runbook validation |
| WS-SEC-019 | Threat modelling is maintained from system/data-flow diagrams and reviewed whenever trust boundaries change. | Approved threat model and review record |
| WS-SEC-020 | External penetration testing and remediation are complete before public release. | Independent report and closed critical/high findings |

## Data restrictions

- Public and self-service plans must not invite special-category, confidential, regulated or export-controlled data unless a separately approved workflow supports it.
- Ordinary Wix forms remain limited to low-risk qualification data.
- Managed Secure data handling is not inherited by the Workspace and requires a separate approved control and contract set.

## Privacy and compliance gates

Before pilot, Atlas must document controller/processor roles, provider/subprocessor inventory, lawful basis, transfer safeguards, retention, data-subject request handling, breach procedures and DPIA screening. A full DPIA is required where the final processing creates high risk.

## Contradiction handling

The research report includes an optional Wix Members/Velo MVP. Under existing approved Atlas decisions, Wix may only act as a thin interface. Any design that places provider secrets, authoritative entitlement/cap logic, tenant state, protected file processing or audit authority in Wix is rejected unless an explicit approved architecture decision supersedes the existing boundary.

## Status

These controls are requirements and design records only. They are not evidence of implementation, test completion, pilot approval or production availability.
