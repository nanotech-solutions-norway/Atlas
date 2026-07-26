#!/usr/bin/env python3
"""Validate Atlas consumer-checkout contract schemas and negative-path vectors.

This script is intentionally non-operational. It performs local/static validation only
and never calls Wix, payment providers, customer systems, or production endpoints.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]
IMPLEMENTATION_ROOT = ROOT / "governance" / "implementation"
CONTRACTS = IMPLEMENTATION_ROOT / "contracts"
VECTORS_PATH = (
    IMPLEMENTATION_ROOT
    / "test-vectors"
    / "consumer-checkout-negative-paths.v0.1.json"
)

SCHEMA_PATHS = {
    "gate": CONTRACTS / "atlas-consumer-checkout-gate.schema.json",
    "consent": CONTRACTS / "atlas-consent-event.schema.json",
    "case": CONTRACTS / "atlas-cancellation-refund-state.schema.json",
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError as exc:
        raise RuntimeError(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise RuntimeError(f"Expected a JSON object in {path}")
    return data


def assert_schema_valid(schema: dict[str, Any], path: Path) -> None:
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # jsonschema raises schema-specific subclasses
        raise RuntimeError(f"Invalid Draft 2020-12 schema {path}: {exc}") from exc


def assert_invalid(
    validator: Draft202012Validator,
    instance: dict[str, Any],
    label: str,
) -> None:
    errors = sorted(validator.iter_errors(instance), key=lambda err: list(err.path))
    if not errors:
        raise RuntimeError(f"Expected invalid instance passed validation: {label}")


def validate_gate_safeguards(schema: dict[str, Any]) -> None:
    validator = Draft202012Validator(schema)

    deny_instance = {
        "schemaVersion": "0.1.0",
        "decisionId": "test-deny-001",
        "evaluatedAt": "2026-07-26T03:08:00+02:00",
        "action": "ORDER",
        "offerId": "student-basic",
        "commercialContractVersion": "0.5.1",
        "decision": "DENY",
        "reasonCodes": ["PURCHASE_NOT_ALLOWED"],
        "dependencyState": {
            "releaseApproved": False,
            "publicAllowed": False,
            "purchaseAllowed": False,
            "legalApproved": False,
            "taxApproved": False,
            "legalCopyApproved": False,
            "consentStoreAvailable": False,
            "taxPreviewAvailable": False,
            "paymentConfigured": False,
            "durableMediumAvailable": False,
            "entitlementControlAvailable": False,
            "reconciliationAvailable": False,
        },
    }
    validator.validate(deny_instance)

    unsafe_allow = json.loads(json.dumps(deny_instance))
    unsafe_allow["decision"] = "ALLOW"
    unsafe_allow["reasonCodes"] = ["ALL_REQUIRED_CONTROLS_PASSED"]
    assert_invalid(validator, unsafe_allow, "ALLOW with false dependencies")

    missing_purchase_permission = json.loads(json.dumps(deny_instance))
    missing_purchase_permission["decision"] = "ALLOW"
    missing_purchase_permission["reasonCodes"] = ["ALL_REQUIRED_CONTROLS_PASSED"]
    for key in missing_purchase_permission["dependencyState"]:
        missing_purchase_permission["dependencyState"][key] = True
    missing_purchase_permission["dependencyState"]["purchaseAllowed"] = False
    assert_invalid(validator, missing_purchase_permission, "ORDER allow without purchaseAllowed")


def validate_consent_safeguards(schema: dict[str, Any]) -> None:
    validator = Draft202012Validator(schema)

    valid_event = {
        "schemaVersion": "0.1.0",
        "eventId": "consent-001",
        "eventType": "DELAYED_START_SELECTION",
        "eventAction": "GRANTED",
        "occurredAt": "2026-07-26T03:08:00+02:00",
        "memberId": "test-member",
        "orderCorrelationId": "test-order",
        "offerId": "student-basic",
        "commercialContractVersion": "0.5.1",
        "locale": "nb-NO",
        "copyVersion": "0.1-DRAFT",
        "copyHash": "a" * 64,
        "affirmativeAction": True,
        "preselected": False,
        "sourceChannel": "WIX_CHECKOUT",
        "evidenceState": "RECORDED",
    }
    validator.validate(valid_event)

    preselected = json.loads(json.dumps(valid_event))
    preselected["preselected"] = True
    assert_invalid(validator, preselected, "preselected consent")

    nonaffirmative_early_start = json.loads(json.dumps(valid_event))
    nonaffirmative_early_start["eventType"] = "EARLY_START_REQUEST"
    nonaffirmative_early_start["affirmativeAction"] = False
    assert_invalid(validator, nonaffirmative_early_start, "non-affirmative early start")


def validate_case_safeguards(schema: dict[str, Any]) -> None:
    validator = Draft202012Validator(schema)

    open_case = {
        "schemaVersion": "0.1.0",
        "caseId": "case-001",
        "caseType": "CANCELLATION",
        "createdAt": "2026-07-26T03:08:00+02:00",
        "updatedAt": "2026-07-26T03:08:00+02:00",
        "memberId": "test-member",
        "orderId": "test-order",
        "requestChannel": "EMAIL",
        "currentState": "WIX_CANCELLATION_PENDING",
        "legalDecision": "PENDING",
        "wixOrderState": "PENDING_CANCELLATION",
        "paymentRefundState": "NOT_REQUESTED",
        "entitlementState": "UNCHANGED",
        "accountingState": "NOT_STARTED",
        "reconciliationState": "NOT_RUN",
        "closed": False,
    }
    validator.validate(open_case)

    premature_close = json.loads(json.dumps(open_case))
    premature_close["currentState"] = "CLOSED"
    premature_close["closed"] = True
    premature_close["closedAt"] = "2026-07-26T03:09:00+02:00"
    assert_invalid(validator, premature_close, "closed case without reconciliation")


def validate_negative_vectors(data: dict[str, Any]) -> None:
    if data.get("releaseState") != "NO_GO":
        raise RuntimeError("Negative-path suite must preserve releaseState=NO_GO")
    if data.get("executionMode") != "NON_PUBLIC_CONTRACT_TESTS_ONLY":
        raise RuntimeError("Negative-path suite must remain non-public contract tests only")

    vectors = data.get("vectors")
    if not isinstance(vectors, list) or not vectors:
        raise RuntimeError("Negative-path suite must contain vectors")

    ids: list[str] = []
    for vector in vectors:
        if not isinstance(vector, dict):
            raise RuntimeError("Every negative-path vector must be an object")
        vector_id = vector.get("id")
        if not isinstance(vector_id, str) or not vector_id:
            raise RuntimeError("Every negative-path vector must have a stable id")
        ids.append(vector_id)
        if vector.get("expectedDecision") == "ALLOW":
            raise RuntimeError(f"Negative vector {vector_id} must not expect ALLOW")

    if len(ids) != len(set(ids)):
        raise RuntimeError("Negative-path vector IDs must be unique")

    required_ids = {
        "NEG-GATE-001",
        "NEG-GATE-002",
        "NEG-GATE-003",
        "NEG-GATE-004",
        "NEG-GATE-014",
        "NEG-GATE-017",
        "NEG-CONSENT-001",
        "NEG-CASE-001",
        "NEG-CASE-005",
        "NEG-SEC-001",
        "NEG-ACC-001",
        "NEG-LANG-001",
    }
    missing = sorted(required_ids.difference(ids))
    if missing:
        raise RuntimeError(f"Required negative-path vectors missing: {', '.join(missing)}")


def main() -> int:
    schemas = {name: load_json(path) for name, path in SCHEMA_PATHS.items()}
    for name, schema in schemas.items():
        assert_schema_valid(schema, SCHEMA_PATHS[name])

    validate_gate_safeguards(schemas["gate"])
    validate_consent_safeguards(schemas["consent"])
    validate_case_safeguards(schemas["case"])
    validate_negative_vectors(load_json(VECTORS_PATH))

    print("Atlas consumer-checkout contracts: PASS (static, non-public, NO-GO preserved)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValidationError) as exc:
        print(f"Atlas consumer-checkout contracts: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)