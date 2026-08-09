# Atlas AI Branch and Release Policy — 02:56, 09.08.2026

`main` is the normal approved source-of-truth and deployment branch **while the GitHub control plane is trusted**.

Material changes require review when they affect public claims, pricing, provider disclosure, trust/legal text, CMS schema, routes, forms, security posture, Managed Secure language, protected-runtime contracts, identity/tenant authorization, MCP/tool capabilities, credentials/secrets boundaries, source-control recovery or bilingual content.

## Normal release gate

1. Static/project validation passes.
2. No secrets or confidential files are detected.
3. Public claims are mapped to the controlled claims registry.
4. Bokmål/English parity checks pass where applicable.
5. Trust/legal drafts are reviewed before production use.
6. GitHub Pages workflow publishes only public website assets.
7. Security-relevant tool/schema/route/release-manifest drift is understood and approved.
8. Consequential Atlas/MCP writes remain independently gated by runtime authorization/approval; repository merge is never action authorization.
9. Applicable backup/readback/rollback/recovery evidence exists for the release profile.

## Source-control trust gate

No production deployment or write-capable activation may proceed from GitHub when any of these are true:

- GitHub account/organization/repository/App/Actions/runner compromise is suspected;
- expected branch protection or workflow permissions cannot be verified;
- release/tag/history integrity conflicts with an independently signed checkpoint;
- a source-control kill switch is active;
- required incident/audit evidence cannot be preserved.

During a declared GitHub compromise, use `docs/security/GITHUB_COMPROMISE_CONTINUITY.md` and the canonical security-continuity register. A secondary repository or mirror becomes temporary authoritative source only after the independently signed known-good checkpoint, history, credentials, validation and operator break-glass approval have been verified.

## Recovery requirements

Critical releases/security changes should create an independently verifiable recovery checkpoint containing the relevant Git history/bundle, integrity manifest and independent signature. The checkpoint must be retained outside GitHub in the approved immutable/offline recovery chain once that infrastructure is implemented.

A live mirror alone is not acceptable recovery evidence, and DNS/routing failover never substitutes for source-integrity validation.

## Status separation

Repository policy may be `APPROVED/MERGED` while secondary Git, immutable storage, offline recovery, Credential Broker or protected-runtime controls remain `DESIGNED` or `PENDING_REVIEW`. Report these states separately and do not infer `LIVE` from documentation or merge status.