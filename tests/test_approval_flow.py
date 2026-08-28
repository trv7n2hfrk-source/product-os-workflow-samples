import unittest

from src.approval_flow import ApprovalFlow


class ApprovalFlowTests(unittest.TestCase):
    def test_positive_transition(self):
        flow = ApprovalFlow()
        self.assertEqual(flow.transition_to("submitted"), "submitted")
        self.assertEqual(flow.transition_to("approved"), "approved")

    def test_invalid_transition(self):
        with self.assertRaises(ValueError):
            ApprovalFlow().transition_to("approved")


if __name__ == "__main__":
    unittest.main()
