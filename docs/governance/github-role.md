# GitHub Role in Atlas AI — 02:56, 09.08.2026

GitHub is the normal engineering governance and change-control plane for Atlas AI while trusted. It is not the main public website CMS, the customer-facing runtime, the credential store, or the only permitted recovery source.

## Normal purpose

GitHub's purpose is to:

1. Act as the normal canonical source for architecture decisions, naming rules, repository rules, release policy, implementation registers, schemas, claims and sanitized evidence.
2. Control website and package governance before Wix publication: sitemap, CMS schema, claims registry, bilingual content model and public-vs-secure boundaries.
3. Synchronize Wix, Gamma and protected-runtime work through page maps, CMS schemas, QA checklists, evidence links and implementation status.
4. Prevent drift and enable rollback for code-managed assets such as Velo code, route logic, schemas, release records and future Azure/IaC contracts.
5. Support security and compliance through branch rules, PR review, CODEOWNERS, release tags, secret scanning/push protection, dependency/code review and audit evidence.

## Source-control continuity boundary

GitHub must not be the only independently recoverable copy of critical Atlas/MCP source or governance.

Required independent controls are:

- an independently administered secondary Git service once implemented;
- independently signed release/security checkpoints;
- full Git bundles/checkpoints with integrity manifests;
- immutable/WORM recovery storage;
- an encrypted offline recovery copy for critical repositories;
- a tested break-glass source-authority and return-to-service procedure.

A destructive real-time mirror is replication, not sufficient backup. DNS/routing failover restores availability but does not establish source integrity.

## Compromise mode

If GitHub account, organization, repository, App, Actions, runner or platform compromise is suspected:

1. Suspend GitHub-triggered deployment and write-capable automation.
2. Activate applicable Atlas/MCP kill switches.
3. Revoke/rotate affected GitHub identities and workload trust.
4. Identify and verify the last independently signed known-good checkpoint.
5. Recover into an isolated clean control plane.
6. Run independent validation before any temporary recovered source becomes authoritative.
7. Restore GitHub authority only after explicit audited return-to-service approval.

The secondary repository is not automatically authoritative merely because GitHub is unavailable.

## Platform roles

- **GitHub:** normal canonical engineering/governance and change-control plane while trusted.
- **Google Drive:** controlled private evidence/report/memory mirror; not executable source control.
- **Wix:** commercial/public website implementation plane.
- **Protected runtime / Azure target architecture:** identity, customer data, Credential Broker, tenant authorization, audit and execution when implemented/validated.
- **Independent secondary Git:** continuity/recovery plane after selection/implementation; normally non-authoritative.
- **Immutable/offline recovery:** independent source/release evidence and disaster recovery.
- **Gamma/Figma:** design/reference input, not canonical security authority.

## Precise conclusion

GitHub remains the controlled backbone for normal governance, versioning and validation, but the Atlas security architecture deliberately removes it as a single point of recovery trust. During a declared compromise, temporary source authority may move only through the independently verified break-glass process defined in the canonical security-continuity register and incident runbook.