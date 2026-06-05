# GitHub Settings Hardening Checklist — 13:42, 04.06.2026

Status: manual platform verification required. File-level governance exists, but GitHub settings must be confirmed in repository/organization settings.

## Required checks

- [ ] Organization/repository MFA or passkeys enforced for administrators.
- [ ] Secret scanning enabled where available.
- [ ] Push protection enabled where available.
- [ ] Default branch `main` protected by ruleset or branch protection.
- [ ] Pull request review required for material changes.
- [ ] CODEOWNERS active for relevant paths.
- [ ] GitHub Actions workflow permissions minimized.
- [ ] Pages deployment environment has approval settings if required.
- [ ] Dependency review / Dependabot enabled where applicable.
- [ ] Release tags used for public launch versions.

## Evidence to store

Do not store screenshots containing secrets, private emails, tokens, or sensitive admin data. Store sanitized screenshots or text summaries only.
