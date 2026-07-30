# Atlas Wix Repository Sitemap Validation — 01:47, 30.07.2026

## 1. Scope

Validate the current `nanotech-solutions-norway/atlas_wix` repository as a controlled source of Wix engineering evidence, extract repository-only information, reconcile page-entity coverage with the approved Atlas page-role model and identify limitations or contradictions without changing Wix runtime or release state.

## 2. Evidence assessed

- Private GitHub repository `nanotech-solutions-norway/atlas_wix`.
- Current default branch `main` at commit `692a38a70c6b24e6745ec4251972587aebbab61c`.
- Initial Wix/Velo-generated commit `1c3680ab56b9cf1b737e3f0b9436b2dca5dc3040`.
- Authenticated Wix site context for `Atlas-AI`.
- Current approved/canonical Atlas source hierarchy, decisions and validation records.
- Existing screenshot evidence for FAQ and Generell kontakt page existence.

## 3. Validation results

| ID | Validation target | Method | Result | Evidence / output | Required follow-up | Classification |
|---|---|---|---|---|---|---|
| ATL-VAL-20260730-067 | `atlas_wix` repository and Atlas-AI site identity | GitHub repository metadata, `wix.config.json` and authenticated Wix context comparison | `PASS` | Private repo, default `main`, matching site ID, Studio and Velo enabled | Repeat after connection/config change | `AUTO_APPROVED` |
| ATL-VAL-20260730-068 | Repository-backed page-code inventory | Initial/current commit file inventory and source-path review | `PASS_REPOSITORY_SNAPSHOT / HIERARCHY_NOT_AVAILABLE` | 16 named page-code entities plus global page code; 15 public-role candidates and one system account-settings page | Synchronize authorized local editor; capture current routes/menu separately | `AUTO_APPROVED` |
| ATL-VAL-20260730-069 | Repository-only code/configuration extraction | Full source/configuration review | `PASS` | Page associations, Velo logic, custom element, site UI version, runtime requirements, CI and permission defaults extracted into private manifest | Maintain private technical record and sanitized public register | `AUTO_APPROVED` |
| ATL-VAL-20260730-070 | Percentage metric consistency | Cross-file source comparison | `FAIL_CONSISTENCY / CLAIM_PENDING_REVIEW` | One implementation targets 73%; another targets 87%; no approved substantiation in repo | Approve one supported metric or remove both; validate rendered page | `AUTO_APPROVED` evidence / `PENDING_REVIEW` claim |
| ATL-VAL-20260730-071 | Backend fail-closed permission baseline | `permissions.json` and backend-source inventory review | `FAIL_FAIL_CLOSED_DEFAULT / NO_CURRENT_WEB_METHOD` | Anonymous wildcard invocation is enabled for future web methods; no web module or public endpoint currently present | Tighten before any backend web method is introduced; test permissions | `AUTO_APPROVED` evidence / governed implementation change |
| ATL-VAL-20260730-072 | Release-lock effect of repository integration | GitHub/Wix/Drive action review | `PASS_NO_RELEASE_EFFECT / NO_GO` | Documentation, manifest, source registration and validation only; no Wix runtime mutation | Preserve locks until acceptance and written release approval | `CANONICAL` lock outcome |

## 4. Reconciled page-role coverage

The repository snapshot contains entities corresponding to:

1. Home
2. Solutions/services
3. Business
4. Students
5. Individuals
6. Platforms
7. Managed Secure
8. Pricing
9. Trust
10. Legal
11. Resources
12. FAQ
13. About
14. Contact
15. Getting started

A separate Account Settings entity is classified as a Wix Members Area system page.

This validates repository-level **entity coverage**, not current Wix menu nesting, route paths, visibility, copy, CMS binding, SEO, multilingual parity, responsive implementation or runtime acceptance.

## 5. Conflict and limitation findings

### 5.1 Repository versus navigation export

The repository does not contain a native Wix menu/page-tree manifest. Any hierarchy shown in the private audit is a reconciliation against approved Atlas page-role records and is explicitly not represented as a current Studio navigation export.

### 5.2 Contact label

Repository evidence uses `Kontakt`; current screenshot evidence used `Generell kontakt`. Page existence is supported, but current display label, menu label, route and purpose require Wix Studio readback.

### 5.3 About page naming

The Wix-generated source association contains trailing whitespace in the About page-name component. The generated file must not be renamed directly.

### 5.4 Repository freshness

Current editor state can diverge from the repository until an authorized Wix CLI/local-editor sync. This validation is exact only for the assessed GitHub commit.

## 6. Security and confidentiality result

- Full internal page identifiers and detailed source inventory are retained only in the private `atlas_wix` repository and controlled Drive evidence.
- The public Atlas governance repository contains a sanitized source register and validation result.
- No API keys, tokens, credentials, private customer data, bank/accounting data or provider secrets were copied or exposed.
- No public write endpoint or backend business method was identified in the assessed source.

## 7. Aggregate outcome

`atlas_wix` is now formally integrated into the Atlas source-authority model as the private Wix engineering evidence repository. It materially extends the standard Wix connector by exposing source associations, code, configuration, CI and permission defaults. It does not replace authenticated Wix implementation evidence for current menu structure, routes, rendering, CMS/form bindings or runtime acceptance.

The page-code snapshot materially supports coverage of the fifteen approved public page roles plus a system account-settings page. The competing 73%/87% metric implementations and permissive wildcard backend default are recorded as defects requiring resolution before applicable release gates can pass.

## 8. Preserved controls

- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
- Wix site remains Draft.
- No Wix publication performed.
- No payment or checkout activation performed.
- No public write endpoint added.
- No frontend provider token added.
- Release state remains `NO_GO`.
