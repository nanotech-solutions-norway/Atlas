# Atlas AI Incident Response Runbook — 02:56, 09.08.2026

## Universal response sequence

1. Declare incident scope/severity and assign an incident owner.
2. Preserve privacy-minimized evidence and timestamps outside the suspected trust boundary where possible.
3. Activate the relevant global, environment, tenant and/or action kill switch.
4. Revoke affected sessions, tokens, Apps, deploy keys and workload trust.
5. Rotate keys/credentials through the approved vault/identity process when exposure cannot be excluded.
6. Disable or isolate the compromised form, workflow, integration, repository, runner, deployment route or service.
7. Determine affected tenants, data, provider actions and production state.
8. Reconcile consequential provider state using readback and backups before retrying or restoring.
9. Assess contractual, GDPR/data-breach, AI-governance and other notification obligations.
10. Remediate root cause and run the applicable security/regression/restore tests before re-enable.
11. Record containment, recovery, residual risk and explicit return-to-service approval.

No hacking back or unauthorized countermeasures are permitted.

## Credential or secret exposure

- Treat a committed, logged, screenshotted or otherwise exposed secret as compromised even if it is quickly deleted.
- Revoke/rotate first; repository-history cleanup is secondary.
- Search for secondary exposure in workflow logs, caches, artifacts and backups without reproducing the secret in incident records.
- Do not place replacement credentials in chat, memory, Git, Drive evidence or unrestricted agent environments.

## GitHub/source-control incident modes

### G1 — GitHub outage with no compromise evidence

- GitHub-dependent production promotion remains paused unless a previously validated independent CI/change-control path exists.
- Development may continue locally or on the independent secondary using isolated branches.
- Do not automatically elevate the secondary to production authority merely because GitHub is unavailable.
- Reconcile branch/ref history before normal GitHub authority resumes.

### G2 — GitHub account, organization, repository, App, Action or runner compromise suspected

Immediately:

1. Freeze GitHub-originated deployments and write-capable automation.
2. Activate applicable Atlas/MCP kill switches.
3. Revoke/rotate affected GitHub Apps, access tokens, deploy/SSH keys, sessions and workload-federation trust.
4. Suspend trust in GitHub-triggered release/deployment events.
5. Preserve evidence outside the suspected repository as the sole source.
6. Identify the last known-good independently signed checkpoint.
7. Verify the independent secondary and/or immutable Git bundle against its signed manifest and expected ancestry.
8. Restore into a clean isolated repository/control plane; do not blindly mirror the suspected GitHub head.
9. Rebuild and run security, dependency, code and project-specific validation on an independent path.
10. Keep consequential Atlas/MCP writes and Managed Secure release blocked until explicit return-to-service approval.

### G3 — GitHub platform or Actions supply-chain compromise suspected

- Treat GitHub-hosted workflow outputs, Actions artifacts and GitHub-only attestations as untrusted until independently validated.
- Rebuild from independently signed source on an alternative CI/runtime boundary.
- Rotate credentials that could have been available to affected GitHub-hosted workflows/runners.
- Do not ingest new GitHub-originated history into the recovery repository until the incident scope is understood.

### G4 — Repository history/ref tampering

- Compare commit ancestry and refs across GitHub, the independent secondary and immutable bundles.
- Verify signatures/release manifests using verification material stored outside GitHub.
- Preserve divergent refs for investigation.
- Recover to a new isolated origin first; validate before replacing a trusted remote.

## Break-glass source-authority conditions

A recovered/secondary repository may become temporary authoritative source only when all are true:

```text
incident_declared=true
github_trust_suspended=true
known_good_checkpoint_identified=true
signature_manifest_verified=true
repository_history_verified=true
potentially_exposed_credentials_rotated=true
independent_validation_passed=true
operator_break_glass_approval=true
audit_record_created=true
```

DNS/routing failover alone never satisfies these conditions.

## Return to GitHub authority

Before GitHub resumes normal canonical/deployment authority:

1. Re-secure account/organization ownership, MFA/passkeys and recovery methods.
2. Rotate affected credentials, Apps, SSH/deploy keys and workload-federation trust.
3. Revalidate branch protection, CODEOWNERS, environments and workflow permissions.
4. Compare GitHub history with the independently verified source.
5. Re-establish CI/CD trust and OIDC subject restrictions.
6. Run Atlas/MCP validation suites and recovery/readback checks.
7. Record explicit return-to-service approval.

## Recovery evidence

Incident records may contain hashes, commit IDs, sanitized event IDs, approval IDs and provider references. They must not contain raw credentials, unnecessary customer payloads or confidential material unrelated to incident resolution.