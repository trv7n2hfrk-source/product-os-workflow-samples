"""Synthetic deterministic approval-state transitions."""


class ApprovalFlow:
    _TRANSITIONS = {
        "draft": {"submitted"},
        "submitted": {"approved", "rejected"},
        "approved": set(),
        "rejected": set(),
    }

    def __init__(self):
        self.state = "draft"

    def transition_to(self, next_state):
        if next_state not in self._TRANSITIONS[self.state]:
            raise ValueError(f"invalid transition: {self.state} -> {next_state}")
        self.state = next_state
        return self.state
