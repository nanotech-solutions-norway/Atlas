"""Offline synthetic consent evidence model; no persistence/provider adapter."""
from copy import deepcopy
from datetime import datetime
from jsonschema import Draft202012Validator, FormatChecker

class ConsentEvidence:
    def __init__(self, schema, frozen_copy):
        self.validator = Draft202012Validator(schema, format_checker=FormatChecker())
        self._copy = deepcopy(frozen_copy)
        self._events = {}

    def append(self, event):
        candidate = deepcopy(event)
        self.validator.validate(candidate)
        timestamp = datetime.fromisoformat(candidate['occurredAt'].replace('Z', '+00:00'))
        if timestamp.tzinfo is None:
            raise ValueError('TIMEZONE_REQUIRED')
        key = (candidate['copyVersion'], candidate['locale'])
        if self._copy.get(key) != candidate['copyHash']:
            raise ValueError('LEGAL_COPY_DRIFT')
        if candidate['eventId'] in self._events:
            raise ValueError('IMMUTABLE_EVENT_ID')
        prior = candidate.get('supersedesEventId')
        if prior:
            parent = self._events.get(prior)
            if parent is None:
                raise ValueError('MISSING_PREDECESSOR')
            for field in ('memberId', 'orderCorrelationId', 'eventType'):
                if candidate[field] != parent[field]:
                    raise ValueError('CONSENT_SCOPE_MISMATCH')
        if candidate['eventAction'] == 'WITHDRAWN' and not prior:
            raise ValueError('WITHDRAWAL_REQUIRES_PREDECESSOR')
        self._events[candidate['eventId']] = candidate

    def snapshot(self):
        return deepcopy(self._events)
