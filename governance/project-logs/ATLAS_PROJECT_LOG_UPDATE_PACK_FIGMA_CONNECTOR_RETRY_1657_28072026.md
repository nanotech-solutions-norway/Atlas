# ATLAS PROJECT LOG UPDATE PACK — Figma connector retry

**Timestamp:** 16:57, 28.07.2026 Europe/Oslo  
**Session/task:** Retry Generell kontakt v1.1 and FAQ v1.1 Figma Slides reconstruction after connector reconnection

## Issue or mistake observed

1. The existing `Atlas AI — Generell kontakt v1.1 — Recreated` file remains under the Starter/View plan `Ruben` and cannot be reopened through `use_figma` because the plan has reached the six-call monthly MCP limit.
2. `whoami` reports `Ruben A. Meyer's team` as Pro/Full with plan key `team::1466418306299765062`, but both `create_new_file` and `generate_deck` rejected or failed against that returned plan key.
3. A blank Slides file could be created under the Starter/View `Ruben` plan, but `use_figma` remained quota-blocked and the file could not be populated.
4. The write-only `generate_deck` route produced a Generell kontakt presentation widget under `Ruben`, but the FAQ generation attempt then hit the Figma prompt limit, reported to reset in 28 days.

## Root cause

Figma connector plan routing and quota state remain inconsistent: the authenticated account exposes a Pro/Full plan, but the creation/generation endpoints do not accept that plan key; the explicitly requested `Ruben` plan remains a Starter/View seat with exhausted MCP read/use limits and a separate generation prompt limit.

## Corrective rule

Do not report a Figma deck as persistently created, editable, located or validated unless a concrete Figma file key/URL is returned and the resulting file is reopened or otherwise validated. Treat generator widgets as candidate outputs until the user selects and confirms a persistent file. Preserve PPTX fallbacks as controlled artifacts when Figma persistence cannot be evidenced.

## Evidence/source

- Figma `whoami` at 16:57, 28.07.2026.
- `use_figma` error on existing file `nar5CUbnwvFGEVH8UesEE5`: Starter-plan MCP call limit reached.
- `create_new_file` rejection for Pro/Full plan key `team::1466418306299765062`: `Invalid planKey`.
- Successful blank file creation under Starter/View `Ruben`: file key `xaHZW01jlzyAOMl0Shj9yx`.
- `use_figma` error on the new blank file: Starter-plan MCP call limit reached.
- Generell kontakt `generate_deck` widget returned for `Ruben`.
- FAQ `generate_deck` error: Figma prompt limit reached; reset in 28 days.

## Action taken

- Retried authentication and verified current plans and seats.
- Tested the existing file, Pro/Full plan creation, Starter/View plan creation, `use_figma`, and the native deck generator.
- Avoided claiming completed Figma persistence or validation.
- Retained the previously generated PPTX fallbacks as the only fully controlled downloadable artifacts.

## Unresolved items

1. Reconnect or authorize the Figma connector specifically against `Ruben A. Meyer's team` so its returned Pro/Full plan key is accepted by write endpoints.
2. Confirm whether the Generell kontakt generator widget has been selected and persisted as a concrete Figma file.
3. Recreate and validate FAQ v1.1 in Figma after plan routing and prompt limits are resolved.
4. Delete or clearly label the empty file `xaHZW01jlzyAOMl0Shj9yx` if it is not needed.

## Classification

- **AUTO_APPROVED:** Exact connector errors, verified quota behaviour, blank-file creation evidence, correction against false completion claims, and the corrective reporting rule.
- **PENDING_REVIEW:** Figma plan-routing remediation, selection/persistence of the generated contact candidate, and final FAQ Figma implementation.

## Release status

`publicAllowed=false`  
`purchaseAllowed=false`  
`releaseApproved=false`  
**NO_GO**
