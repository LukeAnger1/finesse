"""KISS2 format import/export utilities."""

from __future__ import annotations

from typing import Iterable

from ..core.fsm import FiniteStateMachine


def export_kiss2(fsm: FiniteStateMachine) -> Iterable[str]:
    """Yield lines representing the FSM in KISS2 format."""

    yield f".i {len(fsm.states)}"
    yield ".p 0"
    yield ".e"
