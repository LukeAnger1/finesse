"""State encoding strategy placeholders."""

from __future__ import annotations

from ..core.fsm import FiniteStateMachine


def identity_encoding(fsm: FiniteStateMachine) -> FiniteStateMachine:
    """Return the FSM unchanged (placeholder for real encodings)."""

    return fsm
