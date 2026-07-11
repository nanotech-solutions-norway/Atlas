# Atlas Error Register

Updated: 14:20, 11.07.2026 Europe/Oslo

## ERR-2026-07-11-01 — Duplicate and overlapping active-source files
- Severity: P2 governance defect
- Observation: Strategy, Phase 0-6 and SEO documents repeated common content and contained conflicting status language.
- Root cause: No enforced active-source/supersession register.
- Correction: Consolidated July active-source set and source disposition register.
- Status: CORRECTED. Superseded Drive sources were moved into the dated archive folder after reauthorization.

## ERR-2026-07-11-02 — Missing canonical Atlas learning registers
- Severity: P2 governance defect
- Observation: Expected Atlas learning, decision, error, validation, authority and session-close files were not found under prescribed names.
- Root cause: Setup playbook existed without validated operational deployment.
- Correction: Registers created on branch `atlas-source-refresh-20260711`.
- Status: CORRECTED_PENDING_MERGE.

## ERR-2026-07-11-03 — Drive archive operation initially forbidden
- Severity: P2 operational limitation
- Observation: Google Drive initially returned `403 appNotAuthorizedToFile` when attempting to move pre-existing source folders into the new archive folder.
- Root cause: The connected Google Drive app had not yet been granted write authorization for the relevant existing files.
- Correction: The user reauthorized Google Drive. The archive operation was retried successfully. Both legacy source folders and all legacy root-level files were moved into `Archive - Superseded 11.07.2026`.
- Validation: The Atlas AI Project root now contains only `Active Source - 11.07.2026` and `Archive - Superseded 11.07.2026`.
- Status: RESOLVED.

## ERR-2026-07-11-04 — ChatGPT Project Sources cannot be programmatically replaced
- Severity: P3 platform limitation
- Observation: No available tool can delete or replace attachments in the Atlas Website Project Sources panel.
- Correction: Provide manual source-panel replacement steps after GitHub/Drive readback.
- Status: RESOLVED_BY_MANUAL_UPLOAD; direct UI membership remains non-enumerable through file search.

## ERR-2026-07-11-05 — Planning language presented as approval/status
- Severity: P1 if published
- Observation: Some source files described proposed pricing, provider inclusion and secure availability as approved or operational without complete evidence.
- Correction: Reclassified as PENDING_REVIEW and added hard launch gates.
- Status: CORRECTED_IN_ACTIVE_SOURCE.

## ERR-2026-07-11-06 — Project Sources uploaded from pre-write-back package state
- Severity: P2 governance/currentness defect
- Observation: All expected active-source artifacts are present, but documents 00, 08, 09 and 11 still state that GitHub/Drive write-back or canonical-register creation had not occurred. Document 12 reports the earlier 12-DOCX/56-page validation total rather than the later 13-DOCX/59-page consolidated total.
- Root cause: The manual upload used the original 11:35 package generated before the subsequent Drive reauthorization, archive completion and GitHub register creation were written back.
- Correction: Replace both Markdown and DOCX variants of documents 00, 08, 09, 11 and 12 with post-write-back revisions and repeat source readback.
- Status: OPEN_CORRECTION_REQUIRED.
