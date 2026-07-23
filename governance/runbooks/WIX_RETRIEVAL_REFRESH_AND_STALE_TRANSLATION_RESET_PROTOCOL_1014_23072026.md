# Atlas AI Wix Retrieval, Refresh and Stale Translation Reset Protocol

**Timestamp:** 10:14, 23.07.2026 Europe/Oslo  
**Site:** Atlas-AI  
**Wix site ID:** `1448ccad-68f0-43ea-8f0e-c9d8c0366082`

## Purpose

Define how Atlas work must retrieve fresh Wix information, distinguish active Studio pages from retained Translation Content records, and reset stale analysis without damaging Wix content.

## Source authority

### Page existence

1. Current Wix Studio editor page tree.
2. Exact user correction based on the editor.
3. Verified current active-page evidence.
4. Translation Content records only as supporting evidence.

Translation Content must not be used alone to prove that a Studio page exists. Deleted Studio pages can remain present as translation records.

### Page content

1. Current Wix Studio page body or verified current editor-content record.
2. Approved canonical Figma or source document.
3. Approved GitHub and Google Drive governance records.
4. Legacy reports and stale translation records.

## Refresh procedure

1. Discard the previous Wix inventory as the analysis baseline.
2. Re-query the Atlas-AI site by site ID.
3. Retrieve Translation Content records with entity IDs and updated timestamps.
4. Compare those records with the current Wix Studio page list or the user's confirmed editor inventory.
5. Mark records absent from the active editor tree as stale translation records.
6. Recalculate page counts, empty-page counts, rankings and gaps from active pages only.
7. Create a dated supersession record in GitHub and Google Drive.
8. Do not carry forward an old count merely because the Translation Content API returns retained records.

### Standard refresh instruction

> Discard all previous Wix page inventories and re-query the current Atlas-AI site. Treat the Wix Studio editor or my confirmed editor page list as authoritative for page existence. Use Translation Content only for content inspection. Exclude deleted or stale translation entities. Supersede the previous GitHub and Drive reports.

## Reset levels

### 1. Analysis reset — preferred

Re-query Wix, exclude stale entities and replace the working baseline. Nothing is deleted from Wix.

### 2. Governance reset

Create a corrected GitHub and Google Drive record that explicitly supersedes the incorrect report. Preserve the old report for audit history and mark it non-current.

### 3. Translation-record cleanup — destructive

Wix officially supports:

- `Delete Content`: `DELETE /translation-content/v1/contents/{contentId}`
- `Bulk Delete Content`: `POST /translation-content/v1/bulk/contents/delete`

These methods delete selected Translation Content records. They do not delete or restore a Wix Studio page.

Before cleanup:

1. Confirm the page is deleted in Wix Studio.
2. Record/export all affected content IDs.
3. Verify that no active page uses the entity.
4. Obtain explicit approval for destructive cleanup.
5. Delete only the verified stale records.
6. Re-query and validate the result.

Do not disable and re-enable Wix Multilingual as a cleanup shortcut. Locale-setting changes can affect SEO, content and structure.

## Current Atlas correction

The nine user-confirmed deleted pages remain visible in Wix Translation Content as retained records. They must not be counted as active pages. The corrected active inventory is 16 page candidates until a more authoritative current editor export or page-tree read becomes available.

## Classification

- Refreshing analysis and superseding inaccurate reports: **AUTO_APPROVED**.
- Deleting Translation Content records: **PENDING_REVIEW** until exact IDs are reviewed and the user explicitly authorizes deletion.