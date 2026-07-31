# ATLAS WIX NON-HOME CONTENT ALIGNMENT VALIDATION

Timestamp: 00:50, 31.07.2026 Europe/Oslo  
Project: Atlas Website / Atlas AI  
Wix site ID: `1448ccad-68f0-43ea-8f0e-c9d8c0366082`  
Classification: AUTO_APPROVED for exact user-directed terminology and verified draft-content corrections; PENDING_REVIEW for public claims, legal/pricing publication and release approval.  
Release state: `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.

## Scope

Updated the current Norwegian design-time/translatable Wix draft content on every non-home page. The Home page (`fca96`) was explicitly excluded. Images and Gamma asset/image-placeholder tokens were not modified.

Pages in scope:
- Business
- Solutions
- Managed Secure
- Pricing
- Getting Started
- Individuals
- Students
- Platforms
- Resources
- Legal
- Trust
- About
- FAQ
- Contact

The low-risk Phase 1 qualification form was also translated and aligned.

## Controlling business alignment

- Atlas AI is a Norway-first governed AI solution-layer company.
- Businesses and professionals are the primary commercial route.
- Student and private-user offers are controlled secondary routes.
- Managed Secure is a controlled qualification and architecture-review route, not an available production service.
- No public purchase, subscription activation, provider resale promise or production entitlement is enabled.
- Standard public forms accept low-risk information only and no files or sensitive/confidential content.
- Student Basic and Student Plus are consolidated into one controlled student route, minimum age 16.
- Family, child and shared-household access is not approved.

## Implemented corrections

1. Removed unsupported or premature claims concerning production availability, automatic processing, direct document uploads, guaranteed accuracy, complete GDPR compliance, Norwegian-only storage, inherited certifications and operational Managed Secure controls.
2. Replaced internal editorial and validation instructions with visitor-facing status language.
3. Removed proposed prices, early-access labels and obsolete plan names.
4. Standardized non-home terminology on `AI` as explicitly directed by the user.
5. Applied Norwegian terms including `etterlevelse`, `løsningsgjennomgang`, `omfang`, `leverandørlisenser`, `drift`, `driftskostnader`, `viderefakturert etter avtale`, `brukerstøtte`, `håndtering av sikkerhetshendelser`, `sikkerhetskopi`, `tilbakekalling av tilgang`, `faglig godkjenning`, `hvor data behandles og lagres`, and `skrivearbeid på vegne av studenten`.
6. Replaced the Contact implementation specification with concise visitor instructions and a low-risk submission journey.
7. Translated the low-risk qualification form, navigation controls, field labels and confirmation message to Norwegian.

## Validation evidence

- Every Wix write returned success with `published=false` and `publishStatus=UNPUBLISHED`.
- No Wix publish endpoint or command was invoked.
- Home query readback showed only pre-session update timestamps; no Home record was changed.
- Searches were run for residual `PENDING_REVIEW`, `Foreslått`, Student Basic/Plus, Family/Everyday Basic, manual validation markers, GDPR, ISO and SOC claims.
- Residual Home-only claims were left untouched by instruction.
- Non-home unsupported certification searches returned no actual ISO/SOC certification claim.
- Norwegian plain-language review used official Språkrådet and Digdir guidance: clear structure, short active sentences, understandable terms, and interface text aligned with user action.
- Språkrådet normally recommends `KI`; the project-specific user instruction to use `AI` on all non-home pages is controlling for this implementation.

## Remaining validation

- Rendered Wix Studio/Preview validation at desktop, tablet and mobile breakpoints.
- Text overflow, wrapping, button length, hierarchy and accessibility review.
- Route, link, dataset and form-behaviour tests.
- Exact public legal, privacy, trust and pricing approval.
- Home-page rewrite in a separate controlled workstream.
- English reciprocal localisation and translation-pair validation.
- Publication and release acceptance.

## Result

Content alignment: PASS at draft data/write-readback level.  
Rendered visual acceptance: PENDING.  
Public release: NOT PERFORMED / NO_GO.
