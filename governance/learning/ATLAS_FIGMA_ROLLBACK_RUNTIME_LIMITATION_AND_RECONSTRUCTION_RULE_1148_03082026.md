# Atlas Figma Rollback Runtime Limitation and Reconstruction Rule — 11:48, 03.08.2026

**Learning ID:** ATL-LRN-20260803-027  
**Classification:** `AUTO_APPROVED`

## Observed limitation

The current Figma MCP `use_figma` runtime rejects both `triggerUndo` and `saveVersionHistoryAsync`, despite those methods appearing in generic plugin API references. Therefore connector-driven historical rollback cannot be assumed available.

## Corrective rule

Before destructive Figma changes, create a provider-visible duplicate or other recoverable artifact when the available tools support it. When the owner later requires rollback and native history restore is unavailable:

- distinguish historical-version restore from content-state restoration;
- use the approved pre-state inventory as the reconstruction baseline;
- preserve all unaffected nodes and original IDs;
- reconstruct only the changed/deleted portion;
- insert through an explicit slide-grid update;
- perform separate count, signature, node-ID and visual validation;
- disclose any object-level fidelity limitation.

## Validated application

The rule was applied to 15 Atlas AI v4 Figma Slides files. The recorded pre-deletion total of 134 slides was restored, all 119 existing page slides remained populated, and every original hero node remained at position 2 with its original ID.
