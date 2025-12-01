"""State minimization heuristics."""

from __future__ import annotations

from ..core.fsm import FiniteStateMachine


def no_op_minimization(fsm: FiniteStateMachine) -> FiniteStateMachine:
    """Placeholder minimization that returns the FSM unchanged."""

    return fsm
