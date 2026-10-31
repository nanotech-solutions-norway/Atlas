"""Fictional, in-memory evidence regression; never grants checkout permission."""
import json
import unittest
from pathlib import Path
from checkout_consent_contract import ConsentEvidence

class ConsentTests(unittest.TestCase):
    def setUp(self):
        schema = json.loads((Path(__file__).resolve().parents[1] / 'governance/implementation/contracts/atlas-consent-event.schema.json').read_text())
        self.copy = {('synthetic-v1', 'en'): 'a' * 64}
        self.store = ConsentEvidence(schema, self.copy)
        self.event = dict(schemaVersion='0.1.0', eventId='fictional-1', eventType='TERMS_ACCEPTANCE', eventAction='GRANTED', occurredAt='2026-10-31T00:00:00Z', memberId='fictional-member', orderCorrelationId='fictional-order', locale='en', copyVersion='synthetic-v1', copyHash='a'*64, affirmativeAction=True, preselected=False, evidenceState='RECORDED')
    def test_immutable_event_and_snapshot(self):
        self.store.append(self.event)
        self.event['memberId'] = 'other'
        self.assertEqual(self.store.snapshot()['fictional-1']['memberId'], 'fictional-member')
        snap = self.store.snapshot(); snap.clear()
        self.assertEqual(len(self.store.snapshot()), 1)
        with self.assertRaises(ValueError): self.store.append(self.event)
    def test_copy_registry_is_frozen(self):
        self.copy.clear(); self.store.append(self.event)
    def test_drift_denied_without_write(self):
        for field, value in [('copyHash', 'b'*64), ('copyVersion', 'unknown'), ('locale', 'nb-NO')]:
            with self.subTest(field=field):
                with self.assertRaises(ValueError): self.store.append(dict(self.event, **{field:value}))
                self.assertEqual(self.store.snapshot(), {})
    def test_withdrawal_is_new_scoped_event(self):
        self.store.append(self.event)
        withdrawal = dict(self.event, eventId='fictional-2', eventAction='WITHDRAWN', affirmativeAction=False, supersedesEventId='fictional-1')
        for field in ('memberId', 'orderCorrelationId', 'eventType'):
            with self.subTest(field=field):
                with self.assertRaises(Exception): self.store.append(dict(withdrawal, **{field:'other'}))
        self.store.append(withdrawal)
        self.assertEqual(self.store.snapshot()['fictional-1']['eventAction'], 'GRANTED')
    def test_invalid_consent_fails_before_write(self):
        for change in [dict(preselected=True), dict(affirmativeAction=False), dict(occurredAt='invalid'), dict(eventAction='WITHDRAWN'), dict(supersedesEventId='missing')]:
            with self.subTest(change=change):
                with self.assertRaises(Exception): self.store.append(dict(self.event, **change))
                self.assertEqual(self.store.snapshot(), {})

if __name__ == '__main__': unittest.main()
