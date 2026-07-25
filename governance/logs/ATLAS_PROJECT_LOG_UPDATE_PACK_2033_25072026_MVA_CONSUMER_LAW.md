# ATLAS PROJECT LOG UPDATE PACK — 20:33, 25.07.2026 Europe/Oslo

## Session/task

Convert the remaining Atlas AI MVA treatment and the consumer-law deep research mandate into controlled GitHub, Drive and Wix records, update all related gates and logs, and preserve the current release locks.

## Issue or mistake observed

1. The standard 25% Norwegian MVA rate could be read as final treatment across all offers, countries, customer types, top-ups, refunds and provider purchases.
2. A complete research prompt could be read as equivalent to completed legal research or approved consumer terms.
3. Phase 0.5 recorded consumer-law requirements but did not yet contain a complete executable research mandate or a granular legal-readiness matrix.

## Root cause

Rate, transaction treatment, accounting implementation and sign-off were grouped under one MVA status. Research scope, legal interpretation, drafting, Wix implementation, testing and release approval were not separately represented.

## Corrective rules

- Use 25% only as the controlled domestic working baseline until the offer/jurisdiction treatment is signed off.
- Record MVA finalisation through MVA-001–MVA-020.
- Record consumer-law work through separate states: mandate created, research completed, legal approved, implemented, tested and release approved.
- Do not create Wix Pricing Plans or checkout while any applicable tax/legal gate remains open.

## Evidence/source

- Atlas Phase 0.5 contract v0.5.1.
- Atlas approved pricing pack.
- Official Norwegian Tax Administration guidance for remotely deliverable services, software, hosting, IT and consultancy.
- Current Angrerettloven requirements governing payment-obligation acknowledgement, durable-medium confirmation, early service commencement, withdrawal and digital content.
- Official Wix CMS documentation and current Atlas-AI implementation evidence.

## Actions taken

- Created `governance/tax/` with the MVA finalisation register and offer/jurisdiction CSV.
- Created `governance/legal/` with the consumer-law deep research prompt and checkout-readiness matrix.
- Updated the Phase 0.5 terms/disclosure register and pricing release gate.
- Added canonical decisions ATL-DEC-20260725-015 through -018.
- Added validations ATL-VAL-20260725-018 through -021.
- Added learnings ATL-LRN-20260725-008 and -009.
- Added session-close entry ATL-CLS-20260725-003.
- Created Drive folder `02_MVA_and_Consumer_Law_Readiness` with README, MVA register, research prompt, readiness matrix and project log.
- Updated the approved pricing document, financial-model validation gate and canonical Drive mirrors.
- Added eight private tax/legal readiness fields to Wix `AtlasPricingContract`.
- Patched and read back all 13 v0.5.1 pricing records.
- Confirmed `professionalSignoffRequired=true` for all 13 records.
- Confirmed `publicAllowed=false` and `purchaseAllowed=false` for all 13 records.
- Confirmed Wix Pricing Plans count remains zero.
- Created `governance/validation/WIX_MVA_CONSUMER_LAW_READINESS_25072026.md`.

## Validation result

- GitHub artifact coverage: `PASS`.
- Drive folder/file creation and controlled mirrors: `PASS`.
- Wix schema update: `PASS`.
- Wix record update: `PASS` — 13/13.
- Consumer checkout activation: `NOT_PERFORMED`.
- Public/purchase lock preservation: `PASS`.
- Overall release: `NO_GO`.

## Unresolved items

- Norwegian accountant/tax-adviser sign-off.
- Offer and jurisdiction classification.
- Non-Union OSS decision and registration.
- Reverse-charge and accounting-code implementation.
- Invoice, credit-note, refund and reconciliation tests.
- Execution of the consumer-law research mandate.
- Bokmål/English consumer terms and checkout copy.
- Norwegian lawyer sign-off.
- Wix Members Area, consent logs, confirmation, cancellation and refund implementation.
- Phase 3 entitlement, cap and ledger implementation.
- Written release approval.

## Classification

- `APPROVED_CONTROL`: domestic 25% working rate, not universal final tax treatment.
- `AUTO_APPROVED`: research mandate, control structure, readiness matrices and safe private metadata.
- `PENDING_REVIEW`: final MVA treatment, legal conclusions, terms, checkout, paid commencement and public activation.

## Next executable workstream

Execute the consumer-law deep research mandate and create the complete Bokmål/English legal implementation pack. In parallel, obtain accountant/tax-adviser approval for the launch-country and offer-level MVA matrix.

## Release state

`NO_GO`.
