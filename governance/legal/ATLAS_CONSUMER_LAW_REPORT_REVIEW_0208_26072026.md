# Atlas AI Consumer-Law Report Review — 02:08, 26.07.2026

**Report referenced:** `Atlas AI Consumer Terms, Withdrawal, Cancellation, Refunds, Digital-Service Commencement and Checkout Compliance Report 20:37, 25.07.2026`  
**Review jurisdiction/date:** Norway, law in force on 25.07.2026  
**Release state:** `NO_GO`  
**Classification:** Verified statutory checkpoints `AUTO_APPROVED` as evidence; Atlas-specific legal interpretations and final terms `PENDING_LEGAL_REVIEW`.

## 1. Evidence boundary

The report title and generation time are known from the project thread, but the complete report artifact was not found in the canonical GitHub repository or the controlled Google Drive legal folder during this review. Therefore:

- a line-by-line report-content review cannot be represented as completed;
- no report conclusion is promoted to `APPROVED` or `CANONICAL` solely because the report was generated;
- the statutory checkpoints below were independently re-verified against current primary Norwegian sources;
- the report must be ingested, hash/version recorded and compared against this review before legal sign-off.

## 2. Controlled legal conclusions

### 2.1 Working classification

Atlas consumer subscriptions are most plausibly continuing digital-service agreements under digitalytelsesloven § 1 because the service enables users to generate, process, store or access data digitally. Generated outputs may be digital content, but this does not make the complete recurring subscription a discrete digital-content supply for withdrawal purposes. Top-ups and premium boosts remain separately `PENDING_LEGAL_REVIEW` because their classification depends on the exact entitlement, delivery and expiry design.

### 2.2 Electronic checkout

Angrerettloven § 16 requires the prescribed information to be clear and prominent immediately before an electronic paid order. The consumer must expressly acknowledge the payment obligation. A button or equivalent function must use `bestilling med forpliktelse til å betale` or equally unambiguous wording. Failure to comply means the consumer is not bound by the agreement or order.

### 2.3 Immediate commencement

For a paid service that starts during the withdrawal period, angrerettloven § 19 requires an express request for early commencement and acknowledgement that the withdrawal right is lost only after the trader has fully performed all obligations. Immediate account activation does not by itself eliminate the withdrawal right for a continuing service.

The separate digital-content exception in § 22 first paragraph letter n applies only when all statutory conditions for non-physical digital content are met, including express prior consent, acknowledgement of loss and durable-medium confirmation. Atlas must not use that exception as a blanket subscription rule.

### 2.4 Withdrawal and proportional payment

The ordinary withdrawal period for a service agreement is 14 days from conclusion under § 21. Missing withdrawal information can extend the period by up to 12 months. If a consumer withdraws after expressly requesting early commencement, Atlas may retain only a proportionate amount for service supplied, and only where the information and express-request conditions in §§ 8, 19 and 26 are satisfied.

### 2.5 Cancellation and recurring agreements

Digitalytelsesloven § 33 governs consumer cancellation of continuing digital services. Monthly advance-paid agreements normally end from the next payment period. Cancellation must be simple and possible through the contracting communication method or another suitable method used by the supplier. The supplier must send at least six-monthly reminders that the agreement continues and explain how to cancel. Binding periods require a proportionate economic benefit and are restricted by the statute.

### 2.6 Price and service changes

Digitalytelsesloven § 28 permits price changes in continuing agreements only where the right and consumer protections are included in the agreement and reasonable advance notice is given. Increases beyond CPI can trigger cost-free cancellation. Sections 41–42 require a contractual basis, no added consumer cost and clear notice for service changes; materially adverse changes require durable-medium notice and may give a right to terminate.

### 2.7 Content after withdrawal or termination

Angrerettloven § 24 a and digitalytelsesloven settlement rules limit continued supplier use of consumer-provided or consumer-created non-personal content and can require content to be made available to the consumer, subject to statutory exceptions. Privacy deletion and portability duties must be implemented separately under data-protection law.

### 2.8 2026 amendment status

Law 19 June 2026 no. 34 introduced, among other matters, an electronic withdrawal function, but Lovdata states that the relevant amendments enter into force when the King determines. They were therefore not treated as law in force on 25.07.2026. The electronic withdrawal function must remain a forward implementation requirement and be rechecked before launch.

## 3. Offer-level working result

| Offer/component | Working classification | Withdrawal treatment | Current result |
|---|---|---|---|
| Student Basic | Continuing digital service | 14-day service withdrawal model; early activation does not automatically remove right | `PENDING_LEGAL_REVIEW` / `NO_GO` |
| Student Plus | Continuing digital service | Same | `PENDING_LEGAL_REVIEW` / `NO_GO` |
| Everyday Basic | Continuing digital service | Same | `PENDING_LEGAL_REVIEW` / `NO_GO` |
| Family | Continuing digital service with multi-user account controls | Same; payer/member and minor controls unresolved | `BLOCKED` / `NO_GO` |
| Standard top-up | Additional prepaid entitlement to service, working view only | Separate disclosure and withdrawal/refund analysis required | `BLOCKED` |
| Premium boost | Additional prepaid entitlement or discrete digital supply, unresolved | Separate classification and consent flow required | `BLOCKED` |
| Promotional/rollover units | Contractual entitlement, not separately sold in all cases | Expiry and termination effects must be stated and tested | `BLOCKED` |

## 4. Wix implementation conclusion

Native Wix capability is not sufficient by itself to evidence the complete Atlas flow. At minimum the implementation requires:

- Wix pricing/plan and checkout surfaces configured only after approval;
- Members Area or equivalent identity/account capability;
- Velo/backend consent and terms-version logging;
- immutable order, offer, contract and acknowledgement evidence;
- durable-medium confirmation with the withdrawal notice and form;
- simple cancellation with an email fallback when account access fails;
- refund, pause and Family-account workflows;
- external entitlement/usage ledger, hard-cap enforcement and reconciliation;
- Bokmål/English parity, accessibility and end-to-end acceptance evidence.

No public plan, checkout or immediate paid activation was created or authorized by this review.

## 5. Readiness decision

| Area | Result |
|---|---|
| Primary-source legal requirement verification | `PARTIAL` |
| Exact generated-report review | `BLOCKED` — artifact not ingested |
| Consumer terms and copy pack | `BLOCKED` |
| Wix implementation | `BLOCKED` |
| Acceptance tests | `NOT_RUN` |
| Norwegian lawyer approval | `ABSENT` |
| MVA/accounting approval | `PARTIAL / BLOCKED` |
| Public B2C checkout | `NO_GO` |

## 6. Evidence required before `GO`

1. Complete report artifact stored in GitHub and Drive with stable filename, timestamp, version and checksum.
2. Line-by-line source and effective-date review, including the 2026 amendment status.
3. Signed Norwegian legal classification for subscriptions, onboarding, outputs, top-ups and premium boosts.
4. Approved Bokmål/English consumer terms, checkout copy, withdrawal notice/form, cancellation and refund packs.
5. Accountant/tax-adviser approval of offer, jurisdiction, refund and credit-note MVA treatment.
6. Implemented identity, Family/minor, consent, durable-medium, cancellation, refund and data-lifecycle controls.
7. Implemented external entitlement ledger, caps, rollover, top-ups and reconciliation.
8. Wix desktop/tablet/mobile and language-parity acceptance evidence.
9. Legal, accessibility, privacy, payment-provider and release-owner sign-off.
10. Explicit written decision changing `publicAllowed` and `purchaseAllowed` from false.

## 7. Primary sources verified

- Angrerettloven, especially §§ 8, 16, 18–22 and 24 a–29.
- Digitalytelsesloven, especially §§ 1, 28, 33 and 41–45.
- Lov 19.06.2026 nr. 34, including its not-yet-effective commencement rule.
- Prop. 66 LS (2021–2022) and Prop. 38 LS (2025–2026) for statutory context only.
