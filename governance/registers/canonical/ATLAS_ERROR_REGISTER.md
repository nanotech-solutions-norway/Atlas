# ATLAS ERROR REGISTER

**Project:** Atlas Website / Atlas AI  
**Created:** 02:29, 25.07.2026 Europe/Oslo  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Repository path:** `governance/registers/canonical/`  
**Controlled branch:** `agent/canonical-governance-registers-20260725`  
**Drive mirror:** https://drive.google.com/drive/folders/1cXjuJQONMu9lEDYqk6uc62SKJqnTWKiz  

> **Authority rule:** The file is a canonical container. Each entry has its own classification. Only entries marked `CANONICAL`, `APPROVED`, or `AUTO_APPROVED` may be applied as governing instructions. `PENDING_REVIEW` entries are advisory and must not be represented as approved decisions.

## Purpose

Record verified errors, failed assumptions, connector/provider limitations, deployment defects, UI defects and contradiction patterns. The register must distinguish an observed defect from a preventive risk.

## Error entries

| ID | Observed | Root cause | Impact | Corrective action/rule | Evidence | Current status | Classification |
|---|---|---|---|---|---|---|---|
| ATL-ERR-20260723-001 | Deleted or renamed Wix pages were previously counted as active from retained Translation Content records. | Content entities were treated as active editor pages. | Incorrect page counts and readiness conclusions. | Use current Wix Studio editor evidence for page existence. | Wix page-tree correction, 23.07.2026. | Corrected; regression check required in future audits. | `AUTO_APPROVED` |
| ATL-ERR-20260723-002 | `Kontakt` had been renamed to `Om oss`, leaving no genuine Contact page. | Rename changed the role without creating the replacement route. | Phase 1 tree incomplete; contact routing cannot be assumed. | Create a separate Contact page and validate routes/forms before launch. | Authenticated Wix Studio screenshot. | Open P0 Phase 1 gap. | `AUTO_APPROVED` |
| ATL-ERR-20260725-003 | The six prescribed canonical register files were absent from active GitHub/Drive locations. | Historical branch/setup references and generic logs were treated as substitutes. | Project memory could not be reliably applied as canonical. | Create exact-name files in canonical GitHub path and controlled Drive mirror. | Governance baseline and 25.07 audit. | Corrected by this workstream; merge pending. | `AUTO_APPROVED` |
| ATL-ERR-20260725-004 | June and July phase definitions conflicted, especially Phase 3. | Historical plans were not clearly separated from the active plan. | Requirements could be assigned to the wrong phase. | July consolidated guide controls; June files are historical evidence. | 11.07 guide and June workflow files. | Corrected in current register set. | `AUTO_APPROVED` |
| ATL-ERR-20260725-005 | Gamma/Figma draft completeness risked being reported as Wix/runtime completion. | Artifact states were collapsed. | False readiness or public-availability claims. | Separate `PLANNED`, `DRAFTED`, `IMPLEMENTED`, `VALIDATED`, `APPROVED/RELEASED`. | Phase completeness audit. | Corrected in compliance matrix. | `AUTO_APPROVED` |
| ATL-ERR-20260725-006 | Duplicate and superseded Gamma instances complicated source selection. | Multiple alternatives and regeneration cycles lacked a single current-selection register. | Wrong content could be imported into Figma/Wix. | Use title/version/source mapping; preserve duplicates as superseded evidence. | Trust/Contact/Legal inventory and Gamma-to-Figma register. | Partially controlled; automated drift check outstanding. | `AUTO_APPROVED` |
| ATL-ERR-20260725-007 | Wix REST does not expose the active Wix Studio page tree as an authoritative general read endpoint. | Provider/API limitation. | Connector-only page inventories may be incomplete or stale. | Record the limitation and require editor evidence for page existence. | Wix connector documentation and read-only audit. | Open provider limitation; workaround approved. | `AUTO_APPROVED` |
| ATL-ERR-20260725-008 | Figma connector does not provide a global workspace folder/file inventory comparable to Drive. | Provider/API limitation. | Global completeness cannot be established solely through Figma search. | Use known file keys, direct reads and Drive/GitHub Figma registers; do not claim unsearched workspace completeness. | Figma connector behavior. | Open provider limitation; workaround approved. | `AUTO_APPROVED` |
| ATL-ERR-20260725-009 | Wix has zero operative Pricing Plans despite CMS package and offer records. | Content/CMS objects were created before checkout/plan activation. | Phase 0.5 checkout and entitlement contract is incomplete. | Keep checkout disabled; create plans only after commercial/legal/runtime approval. | Live Wix Plans V3 query, 25.07.2026. | Open P0 blocker. | `AUTO_APPROVED` |
| ATL-ERR-20260725-010 | Legal, provider, privacy, cookie, accessibility, retention and operational security wording is drafted but not fully approved. | Draft production preceded final legal/security sign-off. | Public claims may exceed evidence or obligations. | Preserve `PENDING_REVIEW`; do not publish until approval and versioning are recorded. | Trust/Contact/Legal workstream status, 24.07.2026. | Open P0/P1 blocker. | `PENDING_REVIEW` |

## Error handling rule

Do not delete corrected errors. Record the corrective commit, validation result and closure date while retaining the historical entry.
