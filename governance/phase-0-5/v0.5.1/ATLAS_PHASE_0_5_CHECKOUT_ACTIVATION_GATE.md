# Atlas AI Phase 0.5 Checkout Activation Gate — v0.5.1

The price book is approved. Checkout remains disabled.

## Mandatory predicates

```yaml
commercialStatus: APPROVED
publicAllowed: false
purchaseAllowed: false
checkoutEnabled: false
topupsTechnicallyEnabled: false
managedSecureAvailable: false
```

Activation requires exact Wix plan IDs and prices, recurring-payment and tax configuration, approved consumer/legal terms, Members Area or approved identity, entitlement state, idempotent billing ingestion, normalized usage ledger, concurrency-safe caps/reset, top-up settlement, Family identity/age/guardian controls, production routing and explicit written release approval.

Current result: `NO_GO`.
