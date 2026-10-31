"""Offline snapshot validation only. Never executes cancellation/refund/usage."""
from copy import deepcopy
from datetime import datetime
from jsonschema import Draft202012Validator


def validate_case_update(schema, previous, proposed):
    """Return a defensive snapshot only after schema and identity/time checks."""
    candidate = deepcopy(proposed)
    Draft202012Validator(schema).validate(candidate)
    for field in ('caseId', 'memberId', 'orderId', 'caseType', 'createdAt'):
        if previous[field] != candidate[field]:
            raise ValueError('CASE_BINDING_CHANGED')
    if previous['closed']:
        raise ValueError('CASE_ALREADY_CLOSED')
    def instant(value):
        stamp = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if stamp.tzinfo is None: raise ValueError('TIMEZONE_REQUIRED')
        return stamp
    if instant(candidate['updatedAt']) < instant(previous['updatedAt']):
        raise ValueError('STALE_CASE_UPDATE')
    if candidate['closed']:
        required = ('closedAt', 'reconciliationState')
        if any(candidate.get(k) is None for k in required):
            raise ValueError('CLOSURE_EVIDENCE_MISSING')
        if instant(candidate['closedAt']) < instant(candidate['createdAt']):
            raise ValueError('INVALID_CLOSURE_TIME')
    if candidate['legalDecision'] in ('FULL_REFUND', 'PARTIAL_REFUND'):
        if any(candidate.get(k) is None for k in ('approvedRefundAmount', 'currency', 'legalReasonCode')):
            raise ValueError('REFUND_DECISION_INCOMPLETE')
    return candidate


def consume_prepaid(balance, units):
    """Synthetic integer-unit invariant; insufficient funds never buy overage."""
    if type(balance) is not int or type(units) is not int or balance < 0 or units < 0:
        raise ValueError('INVALID_UNITS')
    if units > balance:
        raise ValueError('INSUFFICIENT_PREPAID_BALANCE')
    return balance - units
