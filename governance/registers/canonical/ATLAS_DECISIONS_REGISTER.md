# ATLAS DECISIONS REGISTER

**Project:** Atlas Website / Atlas AI  
**Created:** 02:29, 25.07.2026 Europe/Oslo  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Repository path:** `governance/registers/canonical/`  
**Controlled branch:** `agent/canonical-governance-registers-20260725`  
**Drive mirror:** https://drive.google.com/drive/folders/1cXjuJQONMu9lEDYqk6uc62SKJqnTWKiz  

> **Authority rule:** The file is a canonical container. Each entry has its own classification. Only entries marked `CANONICAL`, `APPROVED`, or `AUTO_APPROVED` may be applied as governing instructions. `PENDING_REVIEW` entries are advisory and must not be represented as approved decisions.

## Decision schema

| Field | Requirement |
|---|---|
| Decision ID | Stable `ATL-DEC-YYYYMMDD-NNN` identifier |
| Decision | Exact governing choice |
| Scope | Systems, phases, routes or artifacts affected |
| Rationale | Why the decision exists |
| Evidence | Approved or verified source |
| Owner | Responsible decision owner |
| Review trigger | Event that requires re-evaluation |
| Status | `CANONICAL`, `APPROVED`, `AUTO_APPROVED`, `PENDING_REVIEW`, `SUPERSEDED` or `REJECTED` |

## Active decisions

| ID | Date | Decision | Scope | Rationale / evidence | Owner | Review trigger | Status |
|---|---|---|---|---|---|---|---|
| ATL-DEC-20260725-001 | 25.07.2026 | The active execution plan is the 11.07.2026 consolidated phase guide, supplemented by the 23.07.2026 website page roadmap. Separate June Phase 0–6 files are historical evidence. | All phases | Prevent phase-numbering conflicts and silent merges. | Project owner | Explicit replacement plan approved | `AUTO_APPROVED` |
| ATL-DEC-20260725-002 | 25.07.2026 | Source authority order is: explicit current user approval; approved/canonical decision register; approved governance records; current implementation evidence; official external sources; project reports; prior chat; labelled inference. | All systems and reports | Matches the Atlas learning protocol. | Project owner | User approves a revised hierarchy | `CANONICAL` |
| ATL-DEC-20260725-003 | 25.07.2026 | GitHub Markdown is the canonical register source. Drive mirrors the controlled files. Gamma, Wix and Figma may contain non-public reference/index artifacts but do not become competing canonical sources. | Governance registers | Prevent cross-platform drift. | Governance owner | Repository or operating model changes | `AUTO_APPROVED` |
| ATL-DEC-20260725-004 | 23.07.2026 | Phase 1 uses 14 canonical public page roles. The current Wix Studio tree contains 13 visible pages because a separate `Kontakt` page is absent. | Phase 1, Wix | Verified editor evidence and page roadmap. | Website owner | Current Wix editor tree changes | `AUTO_APPROVED` |
| ATL-DEC-20260725-005 | 25.07.2026 | Bokmål is the root-language experience and English is a reciprocal `/en/` localized mirror, not an independent tree. | Phase 1+, Wix, SEO | Approved website model. | Website owner | Explicit multilingual architecture change | `APPROVED` |
| ATL-DEC-20260725-006 | 25.07.2026 | Managed Secure remains qualification/architecture-review only until identity, private storage, logging, revocation, backup/restore, incident and acceptance evidence is approved. | Phase 1 and Phase 4 | Preserve the secure-delivery claim boundary. | Security owner | Phase 4/6 evidence pack approved | `CANONICAL` |
| ATL-DEC-20260725-007 | 25.07.2026 | Ordinary public Wix forms may collect low-risk qualification data only and must not request confidential or restricted files. | Phase 1, 2, 4, 6 | Atlas safety and privacy lock. | Privacy/security owner | Approved controlled secure-intake implementation | `CANONICAL` |
| ATL-DEC-20260725-008 | 25.07.2026 | No real-money betting, auto-betting, bookmaker execution, public write endpoint, frontend provider token or unapproved production availability is permitted. | Entire Atlas program | Preserved Atlas safety locks. | Project owner | Only explicit user-approved safety-posture change | `CANONICAL` |
| ATL-DEC-20260725-009 | 25.07.2026 | Content/design status must be reported separately from implementation, validation and release approval. | All audits and registers | Prevent false completion claims. | Validation owner | None; permanent quality-control rule | `AUTO_APPROVED` |
| ATL-DEC-20260725-010 | 25.07.2026 | Public prices, MVA treatment, provider-delivery rights, plan allowances, Family conditions, legal interpretation, production routing and Managed Secure activation remain unresolved. | Phase 0.5–6 | Current evidence does not support approval. | Project owner / legal / commercial | Explicit approval with evidence | `PENDING_REVIEW` |

## Superseded decisions

None recorded in this initial canonical version. When a decision changes, preserve the old row and set its status to `SUPERSEDED`; do not delete it.
