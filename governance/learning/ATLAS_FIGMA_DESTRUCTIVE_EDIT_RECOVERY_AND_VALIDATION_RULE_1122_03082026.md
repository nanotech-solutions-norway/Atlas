# Atlas AI Figma Destructive-Edit Recovery and Validation Rule — 11:22, 03.08.2026

**Classification:** `AUTO_APPROVED`.

## Trigger

After the authorized deletion of only the first Wix-configuration slide from each of the 15 controlled v4 Figma files, the owner reported that the drafts appeared completely deleted.

## Verified state

A fresh read-only audit found:

- 15/15 controlled Figma file keys accessible;
- 119/119 expected remaining page slides present and populated;
- each deck count equal to its original count minus one;
- each current first slide equal to the canonical page hero/H1;
- no additional mutation during the corrective audit;
- all 15 newest Gamma v4 drafts unchanged;
- Atlas-AI Wix site unchanged and still Draft.

The available connector cannot authoritatively enumerate project-folder membership. The owner-visible project-browser state therefore remains an evidence limitation, not proof that the underlying files were deleted.

## Governing rule

Before any future destructive Figma operation:

1. Record every target file key and expected file count.
2. Record the complete pre-write slide grid, IDs, names, text digests and child counts.
3. Create or verify a recoverable version or duplicate where the available surface supports it.
4. State clearly before mutation when no connector-verifiable recovery point is available.
5. Require an exact target signature and abort on any mismatch.
6. Mutate only the specifically authorized node IDs.
7. Return every mutated node ID.
8. Perform a separate full post-write readback of every remaining slide.
9. Report exact before/after counts per file.
10. Never claim project-folder completeness without project-membership enumeration.
11. Never roll back or regenerate an intact file solely to resolve an unverified UI/project-browser discrepancy.

## Current disposition

No rollback was performed because the live files already match the approved target: exactly the first configuration slide is absent and all page slides remain intact.

`NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.
