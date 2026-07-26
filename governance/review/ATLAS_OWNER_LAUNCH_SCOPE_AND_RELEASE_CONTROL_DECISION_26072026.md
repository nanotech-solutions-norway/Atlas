# Atlas AI Owner Launch-Scope and Release-Control Decision

**Version:** `0.6.1-DRAFT`  
**Prepared:** 26.07.2026  
**Contracting company:** NanoTech Solutions Norway AS  
**Organisation number:** `925 367 869`  
**MVA identifier:** `NO925367869MVA`  
**Decision owner:** Ruben A. Meyer, CEO / daglig leder and chair of the board  
**Commercial contract:** `0.5.1`  
**Release:** `NO_GO`

> This document records owner decisions and management authorisation. It does not replace external legal, tax, privacy, security, accessibility, accounting or technical evidence.

## 1. Operator prompt convention

- `PREFILLED_VERIFIED`: verified public or canonical fact.
- `APPROVED_OWNER_FACT`: explicit current owner statement.
- `PENDING_OWNER_INPUT`: Ruben A. Meyer must decide, initial or sign.
- `PENDING_PROFESSIONAL_REVIEW`: external professional decision required.
- `PENDING_IMPLEMENTATION_EVIDENCE`: release operator must provide exact evidence.

## 2. Verified owner and company profile

| Field | Prefilled value | State |
|---|---|---|
| Legal contracting entity | NanoTech Solutions Norway AS | `PREFILLED_VERIFIED` |
| Organisation number | `925 367 869` | `PREFILLED_VERIFIED` |
| MVA identifier | `NO925367869MVA` | `PREFILLED_VERIFIED` |
| Registered address | Vestsideveien 279, 3648 Passebekk, Kongsberg, Norway | `PREFILLED_VERIFIED` |
| Owner/authorising signatory | Ruben A. Meyer | `PREFILLED_VERIFIED` |
| Role | CEO / daglig leder and chair of the board | `PREFILLED_VERIFIED` |
| Signing authority | CEO/managing director or chair may sign individually | `PREFILLED_VERIFIED` |
| Atlas AI status | Internal department/business line of NanoTech Solutions Norway AS; not a separate legal entity | `APPROVED_OWNER_FACT` |
| Student minimum age | 16 | `APPROVED_USER_CORRECTION` |
| Current public/purchase state | `publicAllowed=false`, `purchaseAllowed=false`, checkout disabled | `CANONICAL` |

## 3. Decision references

| Field | Operator prompt |
|---|---|
| Release-candidate ID | `[[PENDING_OWNER_INPUT — RUBEN/RELEASE OPERATOR: enter immutable release-candidate ID after registry creation.]]` |
| Legal approval reference | `[[PENDING_OWNER_INPUT — enter exact signed counsel memorandum reference or retain NO_GO.]]` |
| Tax/accounting approval reference | `[[PENDING_OWNER_INPUT — enter exact signed accountant/tax-adviser memorandum reference or retain NO_GO.]]` |
| Privacy/security approval reference | `[[PENDING_OWNER_INPUT — enter accepted review/evidence reference or retain NO_GO.]]` |
| Acceptance-test run ID | `[[PENDING_IMPLEMENTATION_EVIDENCE — exact passed run.]]` |

## 4. Initial launch-scope decisions

| Decision | Controlled recommendation | Current state/operator action | Conditions |
|---|---|---|---|
| Contracting entity | NanoTech Solutions Norway AS | `APPROVED_FACT` | Atlas AI is not a separate legal entity. |
| Initial geography | Norway only | `[[PENDING_OWNER_INPUT — RUBEN TO APPROVE/MODIFY/REJECT]]` | Foreign B2C remains technically denied. |
| Initial plans | Monthly Student Basic, Student Plus and Everyday Basic | `[[PENDING_OWNER_INPUT — RUBEN TO APPROVE/MODIFY/REJECT]]` | Exact offer IDs and approved configuration required. |
| Student minimum age | 16 | `APPROVED_PRODUCT_CORRECTION` | Legal mechanism for 16–17 remains pending counsel. |
| Users aged 16–17 | Counsel-approved payer/guardian, identity, consent, privacy and remedy model | `[[PENDING_LEGAL_REVIEW + PENDING_OWNER_INPUT]]` | Checkout fails closed until implemented and tested. |
| Under 16 / Family | Excluded | `[[PENDING_OWNER_INPUT — CONFIRM]]` | No subordinate accounts. |
| Annual / semester | Excluded | `[[PENDING_OWNER_INPUT — CONFIRM]]` | No binding or prepaid plans. |
| Top-ups / boosts | Excluded | `[[PENDING_OWNER_INPUT — CONFIRM]]` | No paid add-ons. |
| Foreign B2C / OSS | Excluded | `[[PENDING_OWNER_INPUT — CONFIRM]]` | No OSS/local registration or configuration approved. |
| Free trial | Excluded | `[[PENDING_OWNER_INPUT — CONFIRM]]` | No trial conversion path. |
| Automatic overage | Prohibited | `[[PENDING_OWNER_INPUT — CONFIRM]]` | Hard caps and no negative balance. |
| Activation | Delayed by default | `[[PENDING_LEGAL_REVIEW + PENDING_OWNER_INPUT]]` | Early start only after approved consent/refund model. |
| Accessibility target | WCAG 2.1 AA internal target, subject to legal confirmation | `[[PENDING_OWNER_INPUT]]` | Statutory minimum and internal target remain distinct. |
| Test environment | Non-public, allowlisted and sandbox-only | `[[PENDING_MULTI_OWNER_APPROVAL]]` | No public discovery, real payment or production entitlement. |
| Managed Secure | Excluded/remains blocked | `[[PENDING_OWNER_INPUT — CONFIRM]]` | Separate secure-service release gate. |

## 5. Mandatory release predicates

The release operator must enter a `PASS` evidence reference for each applicable predicate. Missing, unknown or conditional evidence remains `FAIL/NO_GO`.

1. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` signed version-specific legal memorandum.
2. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` signed version-specific MVA/accounting memorandum.
3. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` approved exact legal-copy versions and hashes.
4. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` Members Area, identity, age-band and Student eligibility controls validated.
5. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` recurring-payment, tax and settlement configuration validated.
6. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` consent ledger and durable-medium confirmation validated.
7. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` entitlement, usage, hard-cap and monthly-reset controls validated.
8. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` cancellation, withdrawal, refund, credit-note and accounting reconciliation validated.
9. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` Bokmål/English semantic parity and accessibility acceptance suite passed.
10. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` security, privacy, provider configuration, rollback and monitoring approved.
11. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` controlled hidden-plan and sandbox transaction tests passed.
12. `[[PENDING_IMPLEMENTATION_EVIDENCE]]` complete release-candidate manifest and evidence pack.

## 6. Final owner decision

| Field | Value/input |
|---|---|
| Decision owner | Ruben A. Meyer |
| Final decision | `[[PENDING_OWNER_INPUT — GO / CONDITIONAL_GO / NO_GO]]` |
| `publicAllowed` | `[[PENDING_OWNER_INPUT — TRUE ONLY AFTER EVERY APPLICABLE PASS]]` |
| `purchaseAllowed` | `[[PENDING_OWNER_INPUT — TRUE ONLY AFTER EVERY APPLICABLE PASS]]` |
| `releaseApproved` | `[[PENDING_OWNER_INPUT — TRUE ONLY FOR EXACT RELEASE CANDIDATE]]` |
| Effective timestamp | `[[PENDING_OWNER_INPUT — EUROPE/OSLO]]` |
| Known limitations accepted | `[[PENDING_OWNER_INPUT]]` |
| Rollback owner | `[[PENDING_OWNER_INPUT]]` |
| Post-release monitoring owner | `[[PENDING_OWNER_INPUT]]` |
| Signature | `[[PENDING_OWNER_INPUT — RUBEN A. MEYER SIGNATURE]]` |
| Date | `[[PENDING_OWNER_INPUT]]` |

`publicAllowed`, `purchaseAllowed` and `releaseApproved` remain false unless every applicable predicate is `PASS` and Ruben A. Meyer records an explicit written decision for the exact release candidate.
