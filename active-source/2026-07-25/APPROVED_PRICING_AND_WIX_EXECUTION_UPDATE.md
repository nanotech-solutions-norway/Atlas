# Atlas AI Approved Pricing and Wix Execution Update — 25.07.2026

**Authority:** Explicit current user instruction adopting the Atlas AI Pricing, Budget, Unit Economics and Turnover Report — 13:01, 25.07.2026.  
**Commercial contract version:** `0.5.1`  
**Release state:** `NO_GO`

## Supersession

This update supersedes earlier student/consumer prices of NOK 119, NOK 149 and NOK 349 and the conflicting unmerged pricing proposal. It also supersedes historical/TBD business price bands where they conflict with the price book below. Historical records remain evidence only.

## Approved price structure

- Student Basic: NOK 129/month incl. MVA.
- Student Plus: NOK 169/month incl. MVA.
- Everyday Basic: NOK 159/month incl. MVA.
- Family: NOK 399/month incl. MVA for up to four named household users.
- AI Readiness Assessment: from NOK 19,000 ex. MVA.
- Agent Workflow Mapping Sprint: from NOK 39,000 ex. MVA.
- Platform Setup Pack: from NOK 29,000 ex. MVA.
- Atlas AI Starter: from NOK 69,000 ex. MVA.
- Atlas AI Professional: from NOK 129,000 ex. MVA.
- Research Multi-Engine: from NOK 159,000 ex. MVA plus usage.
- Managed Workflow Lite: from NOK 39,000 setup + NOK 19,000/month ex. MVA.
- Managed Secure Standard: from NOK 175,000 setup + NOK 85,000/month ex. MVA; qualification only.
- Managed Secure Enterprise: from NOK 300,000 setup + NOK 125,000/month ex. MVA; qualification only.

## Wix implementation state

A private admin-only `AtlasPricingContract` CMS collection contains 13 versioned records. All records remain `publicAllowed=false` and `purchaseAllowed=false`. Wix Pricing Plans count remains zero. Members Area is not installed.

## Architecture boundary

Wix owns the public/CMS/plan/order/member interface. A controlled backend owns provider credentials, routing, normalized usage ledger, reservations, hard caps, reset, boost settlement, reconciliation and audit. Managed Secure requires a separate evidenced secure runtime.

## Remaining gates

Legal/consumer terms, MVA application, provider accounts/DPA, Members Area and Family controls, payment/tax configuration, Phase 3 runtime, Managed Workflow Lite pilot evidence, Managed Secure evidence, Wix Studio page implementation and explicit release approval.
