# Atlas AI Student Minimum Age 16 — Controlled Legal Amendment

**Date:** 26.07.2026  
**Classification:** `AUTO_APPROVED_USER_CORRECTION` for product scope; `PENDING_LEGAL_REVIEW` for the legal mechanism  
**Release:** `NO_GO`  
**Publication:** `PROHIBITED`

## Approved correction

The minimum age for an Atlas AI Student plan is **16**, not 18.

This correction supersedes every current planning, terms, launch-scope, implementation, Gamma/Figma validation or Wix-readiness statement that describes Student plans as adult-only or requires the Student user to be at least 18.

## Controlled interpretation

- Ages 16–17 may be eligible for Student Basic or Student Plus.
- Users below 16 remain excluded from the initial launch.
- Family, subordinate accounts and child accounts remain excluded.
- The correction does not itself decide whether a 16–17-year-old may be the contracting party, payer or sole consenting party.
- Norwegian consumer-law counsel must determine contractual capacity, payer and guardian involvement, consent, information, privacy, cancellation, refunds, remedies and transition at age 18.
- Checkout must fail closed for ages 16–17 until the approved legal and technical rule set is present.

## Superseding draft eligibility language

### Bokmål

Student Basic og Student Plus kan tilbys fra fylte 16 år. For brukere mellom 16 og 17 år kan Atlas kreve at en myndig betaler eller verge/foresatt deltar i avtaleinngåelsen eller gir den bekreftelsen som følger av godkjent juridisk og teknisk løsning. Atlas kan kreve dokumentasjon av alder, studentstatus og betalingsmyndighet, men skal begrense innsamlingen til det som er nødvendig. Brukere under 16 år kan ikke kjøpe eller bruke Student-planen i den første lanseringen.

### English

Student Basic and Student Plus may be offered from age 16. For users aged 16–17, Atlas may require an adult payer or guardian/parent to participate in contracting or provide the confirmation required by the approved legal and technical model. Atlas may require evidence of age, student status and payment authority, but must limit collection to what is necessary. Users below age 16 may not purchase or use a Student plan in the initial launch.

## Required system controls

- age-band gate;
- under-16 denial;
- separate 16–17 status;
- approved payer/guardian decision and evidence fields;
- data-minimised verification and retention schedule;
- transition at age 18;
- negative-path tests;
- no ordinary public upload of identity documents;
- immutable version and consent evidence.

## Governance effect

This correction does not change `publicAllowed=false`, `purchaseAllowed=false`, `checkoutEnabled=false` or the overall `NO_GO` status.
