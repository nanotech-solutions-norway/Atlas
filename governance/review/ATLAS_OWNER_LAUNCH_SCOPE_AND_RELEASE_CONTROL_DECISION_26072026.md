# Atlas AI Owner Launch-Scope and Release-Control Decision

**Version:** `0.6.0-DRAFT`  
**Prepared:** 26.07.2026  
**Release:** `NO_GO`

> `[[MANUAL INPUT REQUIRED]]` fields require explicit owner completion. This document does not itself authorize public launch.

## Decision owner

- Owner name: `[[MANUAL INPUT REQUIRED]]`
- Role/title: `[[MANUAL INPUT REQUIRED]]`
- Decision date: `[[MANUAL INPUT REQUIRED]]`
- Release-candidate ID: `[[MANUAL INPUT REQUIRED]]`
- Commercial contract version: `[[MANUAL INPUT REQUIRED]]`
- Legal approval reference: `[[MANUAL INPUT REQUIRED]]`
- Tax/accounting approval reference: `[[MANUAL INPUT REQUIRED]]`

## Initial launch-scope decisions

| Decision | Recommended controlled option | Owner decision | Conditions/notes |
|---|---|---|---|
| Geography | Norway only | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Plans | Monthly Student Basic, Student Plus and Everyday Basic only | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Student minimum age | 16 | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Users aged 16–17 | Counsel-approved eligibility, payer/guardian and privacy model | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Family/minors below 16 | Excluded | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Annual/semester | Excluded | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Top-ups/premium boosts | Excluded | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Foreign B2C/OSS | Excluded and technically denied | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Free trial | Excluded | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Automatic overage | Prohibited | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Usage | Hard caps; no negative balance | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Activation | Delayed by default; early start only after legal approval and implementation | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Accessibility | WCAG 2.1 AA internal target, subject to legal confirmation | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Test environment | Non-public, allowlisted and sandbox-only | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |
| Managed Secure | Excluded/remains blocked | `[[APPROVE / MODIFY / REJECT]]` | `[[INPUT]]` |

## Mandatory release predicates

The owner must record evidence and PASS/FAIL for exact legal approval, exact MVA/accounting approval, privacy/security, legal-copy hashes, Members Area/identity controls, recurring payment, consent ledger, durable confirmation, entitlement/usage ledger, hard caps/reset, cancellation/refund/accounting reconciliation, bilingual parity, accessibility, controlled Wix testing, rollback and monitoring.

## Final release decision

- Final decision: `[[MANUAL INPUT REQUIRED]]`
- `publicAllowed`: `[[MANUAL INPUT REQUIRED]]`
- `purchaseAllowed`: `[[MANUAL INPUT REQUIRED]]`
- `releaseApproved`: `[[MANUAL INPUT REQUIRED]]`
- Effective timestamp: `[[MANUAL INPUT REQUIRED]]`
- Known limitations accepted: `[[MANUAL INPUT REQUIRED]]`
- Rollback owner: `[[MANUAL INPUT REQUIRED]]`
- Monitoring owner: `[[MANUAL INPUT REQUIRED]]`
- Owner signature/date: `[[MANUAL INPUT REQUIRED]]`

`publicAllowed`, `purchaseAllowed` and `releaseApproved` must remain false unless every applicable predicate is PASS and the owner records an explicit written GO for the exact release candidate.
