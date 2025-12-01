"""Validation checks for finite state machines."""

from __future__ import annotations

from ..core.errors import ValidationError
from ..core.fsm import FiniteStateMachine


def ensure_initial_state(fsm: FiniteStateMachine) -> FiniteStateMachine:
    """Ensure the FSM defines an initial state."""

    if fsm.initial_state is None:
        raise ValidationError("FSM must define an initial state")
    return fsm


DEFAULT_VALIDATION_PASSES = [ensure_initial_state]
