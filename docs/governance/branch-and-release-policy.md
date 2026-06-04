# Atlas AI Branch and Release Policy — 13:02, 04.06.2026

`main` is the approved source-of-truth and deployment branch.

Material changes require review when they affect public claims, pricing, provider disclosure, trust/legal text, CMS schema, routes, forms, security posture, Managed Secure language, Azure contracts, or bilingual content.

## Release gate
1. Static validation passes.
2. No secrets or confidential files are detected.
3. Public claims are mapped to `claims_registry`.
4. Bokmål/English parity checks pass.
5. Trust/legal drafts are reviewed before production use.
6. GitHub Pages workflow publishes only public website assets.
