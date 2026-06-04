# Atlas AI Website Security Control Matrix — 13:02, 04.06.2026

| Area | Required control | Priority | Status |
|---|---|---|---|
| GitHub | MFA/passkeys, push protection, branch rules, required reviews, CODEOWNERS | Critical | Manual platform setting required |
| Secrets | No long-lived secrets in code, workflows, docs, forms or frontend assets | Critical | Repo policy active |
| Forms | Server-side validation required for any future dynamic form handler; static site has no upload path | Critical | Public notice active |
| Uploads | No ordinary public upload of confidential/restricted files | Critical | Boundary active |
| Claims | Evidence-backed claims registry | High | Seed created |
| Incident response | Contact list, severity model, session revocation and key rotation runbook | Critical | Draft created |
| Managed Secure | Identity, private storage, logging, revocation, backup/restore and incident evidence | Critical | Pending Phase 3/6 evidence |
