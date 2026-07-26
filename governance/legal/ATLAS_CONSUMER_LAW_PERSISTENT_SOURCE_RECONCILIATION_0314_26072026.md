# Atlas AI Consumer-Law Persistent Source Reconciliation — 03:14, 26.07.2026

**Project:** Atlas Website / Atlas AI  
**Scope:** Load-bearing statutory and Wix-platform propositions in the original 20:37 report  
**Evidence classification:** `AUTO_APPROVED_EVIDENCE_STATE`  
**Legal conclusions:** `PENDING_LEGAL_REVIEW`  
**Release effect:** `NONE`  
**Release state:** `NO_GO`

> The original research files preserve conversation-local citation tokens. This register provides persistent official source locations for the load-bearing requirements independently rechecked in the 03:14 validation. It does not recreate every citation in the original report and does not constitute professional legal approval.

## Persistent official sources

| Source ID | Authority | Persistent location | Atlas proposition checked | Result |
|---|---|---|---|---|
| SRC-CL-001 | Norwegian Right of Withdrawal Act (`angrerettloven`, law 20 June 2014 no. 27) | https://lovdata.no/dokument/NL/lov/2014-06-20-27 | Pre-contract information; electronic order and payment-obligation button; durable-medium confirmation; early commencement; withdrawal; refund and proportional payment | `PASS_CORE_REQUIREMENTS` |
| SRC-CL-002 | Norwegian Digital Services Act (`digitalytelsesloven`, law 17 June 2022 no. 56) | https://lovdata.no/dokument/NL/lov/2022-06-17-56 | Conformity, updates, remedies, price changes, cancellation, binding periods, six-month reminders and service modifications | `PASS_CORE_REQUIREMENTS` |
| SRC-CL-003 | Norwegian E-commerce Act (`ehandelsloven`, law 23 May 2003 no. 35) | https://lovdata.no/dokument/NL/lov/2003-05-23-35 | Supplier identity, electronic-contract information, ordering steps and electronic confirmation | `PASS_REQUIREMENT / IMPLEMENTATION_PENDING` |
| SRC-CL-004 | Law 19 June 2026 no. 34 | https://lovdata.no/dokument/NL/lov/2026-06-19-34 | Future electronic withdrawal function and effective-date status | `PASS_NOT_IN_FORCE_AS_OF_25_07_2026` |
| SRC-CL-005 | CJEU Case C-234/25, Sky Österreich | https://curia.europa.eu/juris/liste.jsf?num=C-234/25 | Streaming/adaptive subscription and digital-content withdrawal-exception analysis | `PASS_PERSUASIVE_SOURCE / ATLAS_APPLICATION_PENDING` |
| SRC-WIX-001 | Wix Pricing Plans cancellation support | https://support.wix.com/en/article/pricing-plans-allowing-clients-to-cancel-plans | Self-service cancellation requires Members Area and My Subscriptions; cancellation does not itself create a refund | `PASS_PLATFORM_REQUIREMENT` |
| SRC-WIX-002 | Wix Pricing Plans checkout-customisation limitation | https://support.wix.com/en/article/pricing-plans-request-ability-to-customize-the-checkout-page | Native Pricing Plans checkout layout, design and text are not customizable | `PASS_PLATFORM_LIMITATION` |
| SRC-WIX-003 | Wix Pricing Plans frontend checkout API | https://dev.wix.com/docs/velo/apis/wix-pricing-plans-frontend/checkout/introduction | A custom Velo/API checkout orchestration route is technically available in principle | `PASS_DESIGN_CAPABILITY / IMPLEMENTATION_NOT_VALIDATED` |

## Requirement-level reconciliation

| Requirement | Controlling provision/source | Verified position | Remaining Atlas evidence |
|---|---|---|---|
| Payment-obligation button | Angrerettloven § 16 | Final order action must clearly state the payment obligation; non-compliance means the consumer is not bound | Counsel-approved exact wording and rendered functional test |
| Durable-medium confirmation | Angrerettloven § 18 | Contract information and confirmation must be supplied on a durable medium before performance begins | Delivered email/PDF, immutable snapshot and delivery log |
| Early commencement | Angrerettloven § 19 | Separate express request required; acknowledgement of loss applies to full performance conditions | Unchecked control, exact text/version, timestamp and activation evidence |
| Proportional payment | Angrerettloven § 26 | Available only when statutory information and commencement conditions are satisfied | Counsel-approved calculation and entitlement/payment test |
| Simple cancellation and reminder | Digitalytelsesloven § 33 | Suitable cancellation route, binding controls and active six-month reminder required | Members Area/equivalent, email fallback, reminder delivery evidence |
| Price/service changes | Digitalytelsesloven §§ 28, 41–42 | Contractual basis, clear notice and exit/remedy rules apply | Versioned notice engine and end-to-end change test |
| Future electronic withdrawal function | Law 19.06.2026 no. 34 | Enacted but not in force on 25.07.2026 | Recheck immediately before implementation and release |
| Wix native checkout | Wix official support | Native Pricing Plans checkout cannot supply full Atlas-controlled text/layout evidence | Custom Wix/Velo/API or external flow, then acceptance testing |
| Wix native cancellation | Wix official support | Requires Members Area and My Subscriptions | Install/configure or implement approved equivalent |

## Citation-control rule

1. Preserve the raw research file unchanged as source evidence.
2. Do not treat `turn...search...` or `turn...view...` tokens as persistent citations.
3. Use official statute/case/provider URLs and stable identifiers in all canonical validation and lawyer-review packs.
4. When a report proposition cannot be mapped to a stable source, classify it as `UNVERIFIED`, `INFERENCE` or `PENDING_REVIEW`.
5. Recheck effective dates and current platform documentation immediately before implementation and release.

**Control outcome:** load-bearing citation portability is mitigated by persistent official sources; full citation-by-citation reconstruction of the raw report remains incomplete and is not required to preserve the current `NO_GO` state.
