"""Pass manager for orchestrating FSM transformations."""

from __future__ import annotations

from typing import Callable, Iterable, List

from ..core.fsm import FiniteStateMachine

Pass = Callable[[FiniteStateMachine], FiniteStateMachine]


class PassManager:
    """Applies a sequence of passes to an FSM."""

    def __init__(self, passes: Iterable[Pass] | None = None) -> None:
        self._passes: List[Pass] = list(passes or [])

    def add_pass(self, transform: Pass) -> None:
        """Add a new pass to the manager."""

        self._passes.append(transform)

    def run(self, fsm: FiniteStateMachine) -> FiniteStateMachine:
        """Run all registered passes on the FSM."""

        for transform in self._passes:
            fsm = transform(fsm)
        return fsm
