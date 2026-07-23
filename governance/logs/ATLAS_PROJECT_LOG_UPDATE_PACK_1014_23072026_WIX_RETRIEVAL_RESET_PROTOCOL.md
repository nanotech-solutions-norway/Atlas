# ATLAS PROJECT LOG UPDATE PACK

**Timestamp:** 10:14, 23.07.2026 Europe/Oslo  
**Session/task:** Define the correct method for receiving, refreshing and resetting information retrieved from Wix

## Issue or mistake observed

The Wix Translation Content API retained page-title records for nine pages that the user had already deleted in Wix Studio. A prior audit treated those retained records as active empty pages.

## Root cause

Translation Content was used as a proxy for the active Wix Studio page tree. The API is authoritative for translation items, but not sufficient by itself to prove that a Studio page still exists.

## Corrective rule

For page existence, prefer the current Wix Studio editor state and exact user corrections. Use Translation Content only as supporting evidence for titles, text, buttons, parent entity IDs and translation status. Exclude records that are absent from the verified active editor tree.

A refresh must discard the previous analytical baseline, re-query Wix and recalculate results from active pages only. A destructive Translation Content cleanup requires exact content IDs and explicit user authorization.

## Evidence/source

- Current Atlas-AI Wix Translation Content query.
- User confirmation that nine named pages were deleted in Wix Studio.
- Official Wix Translation Content `Delete Content` method.
- Official Wix Translation Content `Bulk Delete Content` method.
- Google Drive protocol: `Atlas AI Wix Retrieval and Reset Protocol — 10:14, 23.07.2026`.
- GitHub runbook: `governance/runbooks/WIX_RETRIEVAL_REFRESH_AND_STALE_TRANSLATION_RESET_PROTOCOL_1014_23072026.md`.

## Action taken

- Defined a four-level source-authority rule for Wix page existence and page content.
- Defined a standard refresh instruction for future Wix audits.
- Separated analysis reset, governance supersession and destructive Translation Content cleanup.
- Documented that Wix Multilingual must not be toggled as a cleanup shortcut.
- Preserved the corrected 16-page active candidate inventory.
- No Wix records were deleted or modified.

## Unresolved items

- Exact stale Translation Content content IDs may be prepared for review.
- Destructive cleanup remains unapproved.
- A supported authoritative Wix Studio page-tree API remains unavailable through the current connector.
- Previous GitHub and Drive reports that counted deleted records should be treated as superseded for active-page counts.

## Classification

**AUTO_APPROVED:** retrieval hierarchy, refresh procedure, supersession procedure and non-destructive workflow correction.

**PENDING_REVIEW:** deletion of stale Translation Content records and any change to multilingual configuration.