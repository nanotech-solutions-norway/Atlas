# Atlas AI Security Control Matrix — 02:56, 09.08.2026

| Area | Required control | Priority | Current state |
|---|---|---|---|
| GitHub account/org | MFA/passkeys, least privilege, protected branches, required reviews, CODEOWNERS, minimal Actions permissions | Critical | Baseline policy active; platform settings require continuing verification |
| Secrets | No long-lived secrets in code, workflows, docs, forms, frontend assets, model context, memory/RAG, logs or Drive evidence | Critical | Governing rule merged; runtime secret-manager migration project-specific |
| Workload identity | Prefer OAuth/OIDC, managed/workload identity, GitHub Apps and short-lived credentials over static keys | Critical | Target architecture approved; implementation varies by provider |
| Credential Broker | Provider credentials attached server-side; no general secret-retrieval tools for AI agents | Critical | Required architecture; implementation pending |
| Tenant authorization | Server-side tenant/object/action authorization for every private Atlas/customer operation | Critical | Required; protected-runtime implementation/validation open |
| Forms | Server-side validation for future dynamic form handlers; public forms remain low-risk qualification only | Critical | Public boundary active |
| Uploads | No ordinary public upload of confidential/restricted files; protected Workspace intake required | Critical | Boundary active; protected path implementation evidence open |
| Tool/action control | Read-first; bounded schemas; R0–R5 risk classes; one-use approval for consequential writes | Critical | Governance adopted; project-specific runtime enforcement open |
| Mutation safety | Preview, pre-read where supported, idempotency/replay protection, readback, recovery evidence and kill switches | Critical | Required; implementation differs by MCP/tool |
| Source-control independence | GitHub must not be the only independently recoverable copy of critical source/governance | Critical | Policy merged; independent secondary not yet selected/live |
| Secondary Git | Independent provider/account/identity boundary; protected branches; normally non-authoritative during normal operation | Critical | `PENDING_REVIEW` platform selection; Azure DevOps preferred candidate |
| Git checkpoint integrity | Full Git bundle/checkpoint, SHA-256 manifest and independent signature/verification material | Critical | Designed; not implemented |
| Immutable recovery | WORM/immutable object storage for signed source/release checkpoints | Critical | Designed; not implemented |
| Offline recovery | Encrypted offline copy of critical source/governance and verification material | High | Designed; not implemented |
| GitHub compromise response | Freeze GitHub-originated deployment/write trust; verify last-known-good checkpoint outside GitHub before recovery authority | Critical | Runbook updated; exercise pending |
| Mirror safety | No destructive real-time mirror as sole backup; retain divergent/known-good refs/checkpoints | Critical | Governing rule active |
| DNS/routing continuity | Routing failover may restore availability but may not grant deployment/source authority | Critical | Governing rule active; implementation depends on service |
| Self-hosted recovery server | Separate admin identity, network restriction, SSH keys, patching, monitoring, encryption and off-host immutable backup | High | Required if Forgejo/GitLab/bare Git is selected |
| Domeneshop recovery use | Additional hardened recovery node allowed; not sole independent backup when sharing production DNS/hosting blast radius | High | Governing risk rule active; no recovery host claimed live |
| Claims | Evidence-backed claims registry; security/compliance claims bound to actual deployed state | High | Existing control retained |
| Logging/audit | Structured tamper-evident/privacy-minimized audit; no raw credentials or unnecessary customer payloads | Critical | Required; runtime implementation evidence open |
| Incident response | Severity, evidence preservation, kill switch, revocation/rotation, source-control modes, recovery and post-mortem | Critical | Runbook updated; exercises pending |
| Backup/restore testing | Quarterly independent restore exercise without relying on GitHub; document RTO/RPO and failures | Critical | Not yet run under new continuity model |
| Managed Secure | Identity, tenant isolation, private storage/network as applicable, logging, revocation, backup/restore, independent source recovery, incident evidence and external security validation | Critical | Qualification/architecture-review only; production evidence pending |

## Release interpretation

A control marked as required or documented is not automatically implemented. Report the relevant state separately as `DESIGNED`, `CONFIGURED`, `IMPLEMENTED`, `TESTED`, `VALIDATED`, `APPROVED`, `RELEASE_APPROVED` or `LIVE`.

No secondary source-control platform, immutable storage account, offline recovery medium or Credential Broker is claimed live solely because this matrix or the security baseline exists.