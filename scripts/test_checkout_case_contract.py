import json
import unittest
from pathlib import Path
from checkout_case_contract import validate_case_update, consume_prepaid

class CaseTests(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads((Path(__file__).resolve().parents[1] / 'governance/implementation/contracts/atlas-cancellation-refund-state.schema.json').read_text())
        self.case = dict(schemaVersion='0.1.0',caseId='fictional-case',caseType='CANCELLATION',createdAt='2026-10-31T00:00:00Z',updatedAt='2026-10-31T00:00:00Z',memberId='fictional-member',orderId='fictional-order',currentState='REQUEST_RECEIVED',legalDecision='PENDING',wixOrderState='NOT_REQUESTED',paymentRefundState='NOT_REQUESTED',entitlementState='UNCHANGED',accountingState='NOT_STARTED',closed=False)
    def test_receipt_is_not_completion(self):
        for patch in [dict(closed=True,currentState='CLOSED'),dict(legalDecision='FULL_REFUND'),dict(legalDecision='PARTIAL_REFUND',approvedRefundAmount=-1,currency='NOK',legalReasonCode='synthetic')]:
            with self.subTest(patch=patch):
                with self.assertRaises(Exception): validate_case_update(self.schema,self.case,dict(self.case,**patch))
                self.assertFalse(self.case['closed'])
    def test_binding_and_time_denial(self):
        for field in ('caseId','memberId','orderId','caseType','createdAt','updatedAt'):
            with self.subTest(field=field):
                with self.assertRaises(Exception): validate_case_update(self.schema,self.case,dict(self.case,**{field:'invalid'}))
    def test_defensive_snapshot(self):
        result=validate_case_update(self.schema,self.case,self.case);result.clear();self.assertTrue(self.case)
    def test_prepaid_never_creates_overage(self):
        for balance in range(8):
            for units in range(10):
                if units<=balance: self.assertEqual(consume_prepaid(balance,units),balance-units)
                else:
                    with self.assertRaises(ValueError): consume_prepaid(balance,units)
    def test_contradictory_closed_state_is_denied(self):
        with self.assertRaises(ValueError):
            validate_case_update(self.schema,self.case,dict(self.case,currentState='CLOSED',closed=False))
    def test_fully_reconciled_closure_and_time_bounds(self):
        complete=dict(self.case,currentState='CLOSED',closed=True,closedAt='2026-10-31T01:00:00Z',updatedAt='2026-10-31T02:00:00Z',reconciliationState='MATCHED',wixOrderState='CANCELED',paymentRefundState='SUCCEEDED',entitlementState='ENDED',accountingState='CORRECTED')
        self.assertTrue(validate_case_update(self.schema,self.case,complete)['closed'])
        for stamp in ('2026-10-30T23:00:00Z','2026-10-31T03:00:00Z'):
            with self.assertRaises(ValueError): validate_case_update(self.schema,self.case,dict(complete,closedAt=stamp))
        with self.assertRaises(ValueError): validate_case_update(self.schema,complete,complete)
    def test_invalid_units(self):
        for balance,units in [(-1,0),(1,-1),(True,1),(1,False),(1,1.5),(1,float('nan'))]:
            with self.assertRaises(ValueError): consume_prepaid(balance,units)

if __name__=='__main__':unittest.main()
