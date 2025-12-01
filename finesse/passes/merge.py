"""State merging heuristics."""

from __future__ import annotations

from ..core.fsm import FiniteStateMachine


def no_op_merge(fsm: FiniteStateMachine) -> FiniteStateMachine:
    """Placeholder merge that returns the FSM unchanged."""

    return fsm
