# Synthetic approval-flow design

`ApprovalFlow` stores one current state and an explicit transition table. The table is deterministic: `draft -> submitted`, `submitted -> approved`, and `submitted -> rejected`. Any other requested transition raises `ValueError`.
