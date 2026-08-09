# Atlas AI Security Continuity Canonical Update Register — 02:56, 09.08.2026

**Project:** Atlas Website / Atlas AI  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Authority:** Supplemental append-only canonical register. Apply only entries marked `CANONICAL`, `APPROVED` or `AUTO_APPROVED`. `PENDING_REVIEW` remains advisory.  
**Trigger:** Universal Atlas/MCP security baseline and GitHub-compromise continuity controls merged 09.08.2026.  
**Release state:** Existing Atlas release locks remain unchanged; governance adoption does not prove runtime implementation.

## Decision entries

| ID | Decision | Scope | Evidence | Review trigger | Status |
|---|---|---|---|---|---|
| ATL-DEC-20260809-040 | The merged universal Atlas AI/MCP security baseline applies to Atlas AI, Atlas Workspace, Atlas operators, every Atlas customer tenant, all current MCP projects and future MCP projects. More restrictive project controls prevail. Raw secrets must not enter model context, memory, RAG, tool output, logs, Drive evidence or Git. | Entire Atlas/MCP estate | Merged Atlas PR #57 and `SECURITY.md`; merged `ntsn-mcp-integrations` PR #8 universal standard | Explicit owner-approved replacement with equivalent or stronger control | `APPROVED` |
| ATL-DEC-20260809-041 | GitHub remains the normal engineering/change-control authority while trusted, but critical Atlas/MCP source and governance must have an independently verifiable recovery path outside GitHub. Suspected source-control compromise freezes GitHub-originated deploy/write trust until a known-good checkpoint is independently verified and authority is explicitly restored. | GitHub, CI/CD, release governance, Atlas/MCP recovery | Merged `docs/security/GITHUB_COMPROMISE_CONTINUITY.md`; universal continuity standard | Explicit owner-approved replacement or validated stronger recovery architecture | `APPROVED` |
| ATL-DEC-20260809-042 | A simple destructive real-time Git mirror is replication, not sufficient security backup. Continuity requires retained independent checkpoints plus immutable/offline recovery evidence. A Domeneshop/private server may be an additional recovery node, but must not be the sole independent recovery platform when it shares production DNS/hosting account or provider blast radius. | Source backup, hosting, DNS, disaster recovery | Git continuity design; provider-diversity/common-mode-risk review | Hosting/account architecture materially changes | `APPROVED` |
| ATL-DEC-20260809-043 | Azure DevOps Repos is the preferred managed secondary candidate for the current Atlas architecture; isolated Forgejo/GitLab is an approved comparison candidate for provider diversity. No secondary platform is to be described as selected, configured or live until procurement/identity/network/backup design is approved and implementation evidence passes. | Procurement and continuity implementation | Security continuity report and architecture comparison | Explicit platform selection and implementation evidence | `PENDING_REVIEW` |

## Learning entries

| ID | Learning / corrective rule | Evidence | Status |
|---|---|---|---|
| ATL-LEARN-20260809-010 | High availability and trustworthy recovery are different controls. A second live Git endpoint can reproduce malicious deletion or history tampering; immutable independently verifiable checkpoints are required. | Git mirror semantics and continuity threat analysis | `AUTO_APPROVED` |
| ATL-LEARN-20260809-011 | Source-control recovery must have an independent root of trust. GitHub-only workflow outputs, GitHub-only attestations and a GitHub-derived mirror cannot be the sole proof of a known-good release during a suspected GitHub/platform compromise. | Compromise-mode analysis | `AUTO_APPROVED` |
| ATL-LEARN-20260809-012 | DNS or routing failover restores availability, not source integrity. Production authority must never move automatically to an unverified backup repository merely because GitHub is unavailable. | Break-glass recovery design | `AUTO_APPROVED` |
| ATL-LEARN-20260809-013 | Governance adoption, secondary-platform selection, backup configuration, restore testing and live recovery readiness are separate states and must be reported separately. | Existing Atlas status-separation rules plus merged security baseline | `AUTO_APPROVED` |

## Error / risk entries

| ID | Issue observed | Root cause | Corrective rule | Evidence | Status |
|---|---|---|---|---|---|
| ATL-ERR-20260809-003 | A GitHub-only source/control model or a blindly synchronized mirror can create a single/common-mode compromise path for source, policy and release evidence. | Primary source control, CI and backup can inherit one identity/platform trust domain. | Maintain independent secondary recovery plus signed immutable/offline checkpoints and fail-closed authority transition. | Security continuity assessment and merged continuity standard | `AUTO_APPROVED` |
| ATL-ERR-20260809-004 | Hosting the sole recovery repository under the same Domeneshop/provider account used for production DNS/hosting could expand a provider-account compromise into both production and recovery loss. | Shared administrative/provider blast radius. | Use a different provider/account for the primary independent secondary where feasible; Domeneshop may remain an additional hardened node with off-provider immutable backup. | Common-mode-risk analysis | `AUTO_APPROVED` |

## Validation entries

| ID | Validation performed | Result | Open evidence | Status |
|---|---|---|---|---|
| ATL-VAL-20260809-005 | Verified Atlas PR #57 merge and security/continuity files on merged history. | `PASS_GOVERNANCE_ADOPTION` | Runtime credential broker, secondary Git, immutable storage, offline copy and recovery exercise remain implementation-pending. | `AUTO_APPROVED` |
| ATL-VAL-20260809-006 | Verified universal MCP baseline PR #8, Conta PR #24 and Domeneshop PR #14 were merged. | `PASS_CROSS_PROJECT_ADOPTION` | Per-project runtime migration and recovery infrastructure remain open. | `AUTO_APPROVED` |
| ATL-VAL-20260809-007 | Reconciled continuity controls with existing Atlas status-separation and release locks. | `PASS_NO_RELEASE_EFFECT` | No security policy merge constitutes production/Managed Secure release evidence. | `CANONICAL` state confirmation |
| ATL-VAL-20260809-008 | Classified Azure DevOps/Forgejo/GitLab/Domeneshop options separately from mandatory controls. | `PASS_CLASSIFICATION` | Platform selection, cost, tenancy, identity, region, operations and restore tests remain open. | `AUTO_APPROVED` |

## Source-authority entries

| Source / state | Role | Authority | Conflict / failover rule | Classification |
|---|---|---|---|---|
| GitHub `main` while trusted | Normal canonical engineering/governance source | Existing canonical hierarchy | Remains primary unless a declared compromise/outage procedure suspends trust | `CANONICAL` |
| `docs/security/GITHUB_COMPROMISE_CONTINUITY.md` and universal NTSN continuity standard | Source-control incident/recovery policy | Governing security requirement | Does not by itself make a secondary repository live or authoritative | `APPROVED` |
| Independently signed last-known-good checkpoint | Recovery integrity anchor during declared compromise | Temporary recovery authority only after verification and break-glass approval | Must be verified outside the suspected GitHub trust domain | `APPROVED` control rule |
| Secondary Git service | Recovery/continuation source | Non-authoritative during normal operation unless explicitly selected and validated | Must not automatically overwrite retained known-good history or auto-deploy | `PENDING_REVIEW` implementation |
| Immutable Git bundle / signed manifest / offline copy | Independent recovery evidence | Evidence/recovery source after verification | Never contains runtime secrets or customer data that does not belong in Git | `APPROVED` control requirement |

## Implementation and task register

| ID | Task | Required outcome | Current state | Classification |
|---|---|---|---|---|
| ATL-SEC-CONT-001 | Select independent secondary Git platform/account | Approved provider, tenancy, identity/admin separation, region and cost decision | Not selected | `PENDING_REVIEW` |
| ATL-SEC-CONT-002 | Implement signed Git checkpoint process | Full bundles, SHA-256 manifest and independent signing/verification process | Not implemented | `PENDING_REVIEW` |
| ATL-SEC-CONT-003 | Implement immutable/WORM recovery storage | Separate protected storage with retention and deletion controls | Not implemented | `PENDING_REVIEW` |
| ATL-SEC-CONT-004 | Establish encrypted offline recovery copy | Offline copy of critical source/governance and verification material | Not implemented | `PENDING_REVIEW` |
| ATL-SEC-CONT-005 | Implement break-glass authority procedure | Named roles, independent access, revocation, validation and return-to-service workflow | Designed; not exercised | `PENDING_REVIEW` |
| ATL-SEC-CONT-006 | Quarterly recovery exercise | Restore without GitHub; verify signatures/history/build/test and document RTO/RPO evidence | Not run | `PENDING_REVIEW` |
| ATL-SEC-CONT-007 | Integrate GitHub-compromise detection with Atlas/MCP kill switches | GitHub-originated deploy/write paths freeze independently of repository content | Not implemented | `PENDING_REVIEW` |

## Session update

| Session ID | Task | Completed | Remaining | Classification |
|---|---|---|---|---|
| ATL-SESSION-20260809-003 | Propagate merged universal security and GitHub-compromise continuity across Atlas/MCP governance and memory | Security baseline and continuity policy merged; supplemental decisions/learnings/risks/validations/source-authority/tasks recorded; Drive mirror/writeback and project-specific propagation initiated | Secondary platform selection, immutable/offline backup implementation, Credential Broker/runtime controls and recovery exercises | `AUTO_APPROVED` task record; implementation/procurement remains evidence-gated |

## Permanent security boundary

- Never store API keys, refresh/access tokens, passwords, private keys, signing secrets or customer confidential data in this register, Git, Drive mirror records or model memory.
- GitHub/Drive governance records contain policy, references, hashes and sanitized evidence only.
- Production/customer credentials remain in the approved protected credential/secret boundary.
- A source-control incident never relaxes write, customer-data, financial, Managed Secure or release gates.
