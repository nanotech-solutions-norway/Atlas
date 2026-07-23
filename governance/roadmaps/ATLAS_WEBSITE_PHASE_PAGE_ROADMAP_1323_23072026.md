# Atlas AI Website Phase Page Roadmap

**Timestamp:** 13:23, 23.07.2026 Europe/Oslo  
**Site:** Atlas-AI  
**Wix site ID:** `1448ccad-68f0-43ea-8f0e-c9d8c0366082`  
**Status:** Planning and current-state reconciliation; no Wix mutation or publication performed

## Source authority

1. User-confirmed Wix Studio page deletions and planned manual rename of `Kontakt` to `Om oss`.
2. Current Wix Translation Content read as supporting content/entity evidence only.
3. `02_Atlas_AI_Phase_by_Phase_Implementation_Guide_1135_11072026` as the controlling Phase 0-6 execution plan.
4. Canonical Figma sources for About v3, Trust v3, Onboarding v3 and Platform Lanes v3.
5. Earlier GitHub and Drive reports as historical evidence where not superseded.

## Current active-page candidates after the planned Kontakt → Om oss rename

1. Hjem
2. Tjenester
3. Bedrift AI - Tjenester
4. Student AI - Tjenester
5. Privatperson AI - Tjenester
6. Privatperson - Pakker
7. Managed Secure
8. Priser
9. Tillit
10. Plattform
11. Atlas Plattformen
12. Team Arbeidsområde
13. Oppstart
14. Ressurser
15. Om oss
16. Juridisk

A genuine `Kontakt` page will then be absent and must be created for Phase 1.

## Phase 1 canonical public pages

The controlling guide requires 14 public page roles:

1. Hjem
2. Tjenester
3. Bedrift
4. Studenter
5. Privatpersoner / Privat og familie
6. Managed Secure
7. Priser
8. Tillit
9. Plattformspor
10. Oppstart
11. Ressurser
12. Om oss
13. Kontakt
14. Juridisk

Bokmål is the root locale and English is a localized `/en/` mirror, not a second independent page tree.

### Existing pages to retain and canonicalize

| Current page | Canonical Phase 1 role | Required action |
|---|---|---|
| Hjem | Hjem | Replace legacy body and validate routes/claims |
| Tjenester | Tjenester | Keep as Solutions hub; remove duplicate/internal content |
| Bedrift AI - Tjenester | Bedrift | Rename/canonicalize and replace legacy claims |
| Student AI - Tjenester | Studenter | Rename/canonicalize; keep early-access gates |
| Privatperson - Pakker | Privatpersoner / Privat og familie | Use as the canonical Consumer source; rename/canonicalize |
| Managed Secure | Managed Secure | Keep hidden or qualification-only until evidence gate passes |
| Priser | Priser | Keep checkout disabled; resolve commercial gates |
| Tillit | Tillit | Remove placeholders and validation notes |
| Plattform | Plattformspor | Use as the canonical Platform Lanes page |
| Oppstart | Oppstart | Bind and test low-risk forms and routing |
| Ressurser | Ressurser | Add verified working destinations |
| Kontakt (planned rename) | Om oss | Rename to Om oss; align route, metadata and CTAs |
| Juridisk | Juridisk | Link approved versioned legal documents or sections |

### Missing Phase 1 page

- `Kontakt`: create a genuine low-risk Contact page with contact options, form entry, privacy/consent notice, success/error states and routing to Oppstart where appropriate.

### Pages to merge, redirect or remove from the Phase 1 public tree

- `Privatperson AI - Tjenester`: legacy duplicate; merge into the canonical consumer page.
- `Atlas Plattformen`: legacy/duplicate platform page; merge into `Plattformspor`.
- `Team Arbeidsområde`: merge relevant public content into `Bedrift`; reserve authenticated workspace functionality for Phase 2 or later.

### No standalone Phase 1 page required

- Prosess / Slik arbeider Atlas: process content is already present in canonical About v3 and Onboarding v3. The controlling Phase 1 build scope does not list a separate Process page.
- Casestudier, Demo-bibliotek or standalone FAQ.
- Provider-specific pages.
- Separate legal shells, provided `Juridisk` exposes approved, accessible, versioned terms, privacy, AUP, cancellation and related notices through sections or linked documents.

## Phase 2 — authenticated identity, portal and structured handoff

Phase 2 is primarily an authenticated application layer, not additional public marketing pages.

### Minimum consolidated surfaces

1. Authentication system pages: sign in, registration/invitation, password reset and session recovery.
2. Customer portal home/dashboard.
3. Account, identity and security.
4. Plan, subscription, billing and cancellation/data-request links.
5. Members: owner/member roles and Family invitations/removal where applicable.
6. Requests and onboarding status, including low-risk intake classification.
7. Qualified secure-escalation handoff without public file upload.

These may be implemented as portal tabs rather than seven separate SEO pages.

## Phase 3 — entitlement, usage, routing and reconciliation

No new public marketing page is required.

### Customer-facing portal surfaces

1. Usage and limits: allowance, premium-use units, reset date, warnings and suspension state.
2. Access and entitlements: active capabilities, plan state and provisioning status.
3. Usage history and billing reconciliation summary, which may extend the Phase 2 billing page.
4. Service/outage status and fallback communication, which may be a portal module or external status surface.

### Internal-only surfaces

- normalized usage ledger
- billing/provider reconciliation
- cap and concurrency controls
- routing-policy administration
- cost alerts and suspension controls
- immutable audit references without prompt content

## Phase 4 — pilot and Managed Secure MVP

No new public marketing page is required. The public Managed Secure page remains qualification-only.

### Private/invited surfaces

1. Pilot invitation and acceptance.
2. Pilot/customer status dashboard.
3. Qualified architecture-review workflow.
4. Authenticated secure handoff/workspace.
5. Private file transfer only after qualification, with quarantine/malware controls where applicable.
6. Support, feedback, revocation and retention/deletion controls.

## Phase 5 — productization and optimization

### Explicit page-like requirements

1. Support knowledge base / Help Center.
2. Package finder and platform-lane comparison after manual workflows are stable.

### Recommended operational surfaces

- authenticated support/ticket page
- service updates or status history
- release notes/changelog where useful

Case studies and a demo library are optional and should only be added after evidence, consent and claim review.

## Phase 6 — security, privacy, incident and final acceptance

No additional marketing page is automatically required. Existing Trust, Legal, Contact and portal surfaces must expose the approved controls.

### Required public or authenticated information surfaces

- current terms and provider disclosures
- privacy and data-request route
- acceptable-use boundaries
- cancellation/refund rules
- cookie information/settings where applicable
- accessibility information where approved/required
- security or incident contact route
- retention/deletion and account-revocation information
- service status and incident communications where applicable

These can remain consolidated under `Juridisk`, `Tillit`, `Kontakt` and the customer portal unless legal review requires separate routes.

## Phase 0 and 0.5 prerequisites

No public pages are required. These phases lock source authority, routes, safety boundaries, product records, pricing objects, terms references and CMS/runtime contracts before Phase 1-3 activation.

## Key contradiction resolved

The prior GitHub Wix assessment treated a standalone `Prosess` page as a possible Phase 1 gap. The controlling consolidated Phase-by-Phase Implementation Guide explicitly lists the Phase 1 build scope and does not include Process. Canonical Figma About v3 and Onboarding v3 already contain the Atlas process and handoff content. Therefore Process is consolidated, not a required standalone Phase 1 page.

## Decision summary

- Phase 1 target: 14 canonical public pages.
- After renaming Kontakt to Om oss: create one new genuine Kontakt page.
- Merge/remove three legacy duplicates: Privatperson AI - Tjenester, Atlas Plattformen and Team Arbeidsområde.
- Phase 2 onward adds authenticated portal and operational surfaces rather than expanding the public marketing tree aggressively.
- Deleted stale Wix Translation Content records remain excluded from the active page tree.

## Classification

- **AUTO_APPROVED:** page-role mapping to the controlling phase guide; duplicate consolidation; Process consolidation; phase surface separation; no-public-page conclusion for control-plane phases.
- **PENDING_REVIEW:** final routes/slugs, pricing and provider rights, legal document structure, paid activation, Managed Secure availability, portal architecture, cookie/accessibility legal determinations and production publication.