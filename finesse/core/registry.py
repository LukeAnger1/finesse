"""Optional registry for tracking defined FSMs."""

from __future__ import annotations

from typing import Dict

from .fsm import FiniteStateMachine


class FSMRegistry:
    """Simple in-memory registry for FSM definitions."""

    def __init__(self) -> None:
        self._fsms: Dict[str, FiniteStateMachine] = {}

    def register(self, fsm: FiniteStateMachine) -> None:
        """Register an FSM by name."""

        self._fsms[fsm.name] = fsm

    def get(self, name: str) -> FiniteStateMachine:
        """Retrieve a registered FSM."""

        return self._fsms[name]

    def clear(self) -> None:
        """Clear all registered FSMs."""

        self._fsms.clear()
