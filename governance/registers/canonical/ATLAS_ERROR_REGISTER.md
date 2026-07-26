# ATLAS ERROR REGISTER

**Project:** Atlas Website / Atlas AI  
**Created:** 02:29, 25.07.2026 Europe/Oslo  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Repository path:** `governance/registers/canonical/`  
**Current update branch:** `agent/consumer-law-mva-readiness-20260726`  
**Drive mirror:** https://drive.google.com/drive/folders/1cXjuJQONMu9lEDYqk6uc62SKJqnTWKiz

> **Authority rule:** The file is a canonical container. Each entry has its own classification. Only entries marked `CANONICAL`, `APPROVED`, or `AUTO_APPROVED` may be applied as governing instructions. `PENDING_REVIEW` entries are advisory and must not be represented as approved decisions.

## Purpose

Record verified errors, failed assumptions, connector/provider limitations, deployment defects, UI defects and contradiction patterns. Distinguish an observed defect from a preventive risk.

## Error entries

| ID | Observed | Root cause | Impact | Corrective action/rule | Evidence | Current status | Classification |
|---|---|---|---|---|---|---|---|
| ATL-ERR-20260723-001 | Deleted or renamed Wix pages were previously counted as active from retained Translation Content records. | Content entities were treated as active editor pages. | Incorrect page counts and readiness conclusions. | Use current Wix Studio editor evidence for page existence. | Wix page-tree correction, 23.07.2026. | Corrected; regression check required. | `AUTO_APPROVED` |
| ATL-ERR-20260723-002 | `Kontakt` had been renamed to `Om oss`, leaving no genuine Contact page. | Rename changed the role without creating the replacement route. | Phase 1 tree incomplete. | Create a separate Contact page and validate routes/forms before launch. | Authenticated Wix Studio screenshot. | Open P0 Phase 1 gap. | `AUTO_APPROVED` |
| ATL-ERR-20260725-003 | The six prescribed canonical register files were absent from active GitHub/Drive locations. | Historical references and generic logs were treated as substitutes. | Project memory could not be reliably applied. | Create exact-name files in canonical GitHub path and controlled Drive mirror. | Governance baseline and 25.07 audit. | Corrected; canonical history retained. | `AUTO_APPROVED` |
| ATL-ERR-20260725-004 | June and July phase definitions conflicted, especially Phase 3. | Historical plans were not separated from the active plan. | Requirements could be assigned to the wrong phase. | July consolidated guide controls; June files are historical evidence. | 11.07 guide and June workflow files. | Corrected in register set. | `AUTO_APPROVED` |
| ATL-ERR-20260725-005 | Gamma/Figma draft completeness risked being reported as Wix/runtime completion. | Artifact states were collapsed. | False readiness/public-availability claims. | Separate planned, drafted, implemented, validated and released states. | Phase completeness audit. | Corrected in compliance matrix. | `AUTO_APPROVED` |
| ATL-ERR-20260725-006 | Duplicate and superseded Gamma instances complicated source selection. | Multiple alternatives lacked one selection register. | Wrong content could be imported. | Use title/version/source mapping; preserve superseded evidence. | Trust/Contact/Legal inventory. | Partially controlled; drift check outstanding. | `AUTO_APPROVED` |
| ATL-ERR-20260725-007 | Wix REST does not expose the active Wix Studio page tree as an authoritative general read endpoint. | Provider/API limitation. | Connector-only page inventories may be incomplete/stale. | Require editor evidence for page existence. | Wix connector documentation. | Open provider limitation. | `AUTO_APPROVED` |
| ATL-ERR-20260725-008 | Figma connector lacks a global workspace folder/file inventory comparable to Drive. | Provider/API limitation. | Global completeness cannot be established solely through Figma. | Use known keys and controlled registers; do not claim global completeness. | Figma connector behavior. | Open provider limitation. | `AUTO_APPROVED` |
| ATL-ERR-20260725-009 | Wix has zero operative Pricing Plans despite CMS offer records. | Content/CMS preceded checkout activation. | Checkout and entitlement contract is incomplete. | Keep checkout disabled; create plans only after all gates pass. | Live Wix Plans V3 query, 25–26.07.2026. | Open P0 blocker. | `AUTO_APPROVED` |
| ATL-ERR-20260725-010 | Legal, provider, privacy, cookie, accessibility, retention and security wording is drafted but not fully approved. | Draft production preceded final sign-off. | Public claims may exceed evidence. | Preserve pending states; do not publish without approval/versioning. | Trust/Contact/Legal workstream. | Open P0/P1 blocker. | `PENDING_REVIEW` |
| ATL-ERR-20260726-011 | `ATL-DEC-20260725-015` uses `APPROVED_CONTROL`, which is outside the decision-register status vocabulary. | An ad hoc status was introduced in a canonical container. | Automated/manual authority filtering may reject or misread the entry. | Do not silently normalise; rely on explicit current user baseline and request approval to change the stored status to an allowed value. | Decision-register schema and entry readback. | Open governance correction. | `PENDING_REVIEW` |
| ATL-ERR-20260726-012 | The consumer-law prompt status could remain `MANDATE_CREATED_NOT_EXECUTED` after the research was completed. | Wix private metadata was not automatically linked to research deliverables. | Readiness reporting would be stale. | Update only research and draft-terms fields after verified deliverables; preserve all release locks. | Four successful CMS patches and readback. | Corrected 26.07.2026. | `AUTO_APPROVED` |
| ATL-ERR-20260726-013 | Native Wix Pricing Plans capability could be mistaken for complete legal/tax evidence. | Platform order/cancellation features do not cover immutable consent, durable medium, jurisdiction, entitlement and accounting controls. | Premature checkout activation risk. | Allocate controls across native Wix, Velo, external backend and manual review; require end-to-end evidence. | Official Wix docs and implementation matrix. | Preventive control added; implementation open. | `AUTO_APPROVED` |

## Error handling rule

Do not delete corrected errors. Record the corrective commit, validation result and closure date while retaining the historical entry.