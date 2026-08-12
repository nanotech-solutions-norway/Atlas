# Atlas AI Phase Terminology Update Register

**Timestamp:** 02:13, 12.08.2026 Europe/Oslo  
**Project:** Atlas Website / Atlas AI  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Classification:** `APPROVED` terminology control  
**Release state:** `NO_GO` — unchanged

## Approved decision

| ID | Decision | Scope | Evidence | Review trigger | Status |
|---|---|---|---|---|---|
| ATL-DEC-20260812-040 | Retain the public website build as **W1 — Public Website Phase 1** and retain the broader full-deployment programme as **D0–D9 — Full Deployment Phases 0–9**. Future Atlas records, status reports, roadmaps, implementation documents and operator communications must use these prefixes where phase ambiguity is possible. Legacy dated records remain historically unchanged and are interpreted by context. | Website, Workspace, runtime, Control Center, organisation administration, connectors, support/status, Managed Secure, governance and reporting | Explicit owner instruction on 12.08.2026 following reconciliation of the approved 15-page website baseline with the full-deployment playbook | Explicit owner-approved terminology replacement | `APPROVED` |

## Canonical terminology map

### W1 — Public Website Phase 1

W1 contains the 15 approved public page roles:

1. Hjem
2. Tjenester
3. Bedrift
4. Studenter
5. Privatpersoner
6. Managed Secure
7. Priser
8. Tillit
9. Plattformer
10. Oppstart
11. Ressurser
12. FAQ
13. Om oss
14. Kontakt
15. Juridisk

The reciprocal English `/en/` experience is a localized mirror and not a second page tree.

### D0–D9 — Full Deployment

- **D0 — Decision lock**
- **D1 — Build-ready design**
- **D2 — Security foundation**
- **D3 — Workspace MVP**
- **D4 — Commerce and entitlement integration**
- **D5 — Atlas Control Center**
- **D6 — Business Workspace / Organisation Administration**
- **D7 — Connectors and Developer API**
- **D8 — Closed pilot**
- **D9 — Managed Secure**

## Interpretation rule

- A legacy reference to `Phase 1` that concerns the public Wix website, page roles, routes, copy, SEO, navigation or public forms means **W1**.
- A reference to `Phase 0–9` in the full-deployment implementation playbook means **D0–D9**.
- Do not silently renumber historical evidence.
- When citing an older record, preserve its original wording and add the modern alias where needed, for example: `Phase 1 (now W1)` or `Full Deployment Phase 3 (now D3)`.
- This naming control changes terminology only. It does not approve architecture, procurement, production availability, public purchase, Workspace release or Managed Secure release.

## Learning entry

| ID | Learning / corrective rule | Evidence | Status |
|---|---|---|---|
| ATL-LEARN-20260812-010 | Separate phase namespaces must be used when two valid roadmaps reuse the same phase numbers. Public website work uses W-prefixes and full-deployment work uses D-prefixes; status reports must not collapse them into one sequence. | Website Phase 1 control and full-deployment D0–D9 playbook | `AUTO_APPROVED` |

## Validation entry

| ID | Validation performed | Result | Open evidence | Status |
|---|---|---|---|---|
| ATL-VAL-20260812-005 | Reconciled the approved 15-page website phase model with the D0–D9 full-deployment programme and checked that the aliases do not alter scope or release state. | PASS. `W1` and `D0–D9` remove ambiguity without superseding either roadmap. | Architecture, implementation, security, pilot and release evidence remain subject to their existing gates. | `AUTO_APPROVED` |

## Safety and release preservation

- `publicAllowed=false` remains unchanged.
- `purchaseAllowed=false` remains unchanged.
- `releaseApproved=false` remains unchanged.
- Managed Secure remains qualification/architecture-review only on the public website.
- No public write endpoint.
- No provider credentials or protected runtime logic in frontend code.
