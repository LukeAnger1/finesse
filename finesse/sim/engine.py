"""Simulation engine for stepping through FSM executions."""

from __future__ import annotations

from typing import Iterable, List

from ..core.fsm import FiniteStateMachine
from ..core.errors import SimulationError
from .trace import Trace


class Simulator:
    """Provides utilities to simulate FSM transitions."""

    def __init__(self, fsm: FiniteStateMachine) -> None:
        self._fsm = fsm
        self._trace = Trace()

    def step(self, input_symbol: str) -> str:
        """Advance the FSM by one step using the provided input symbol."""

        state_name = self._fsm.initial_state
        if state_name is None:
            raise SimulationError("FSM has no initial state defined")
        state = self._fsm.states[state_name]
        transition = state.transitions.get(input_symbol)
        if transition is None:
            raise SimulationError(f"No transition for symbol {input_symbol!r}")
        self._trace.record(state_name, transition.target, input_symbol)
        self._fsm.initial_state = transition.target
        return transition.target

    def run(self, inputs: Iterable[str]) -> List[str]:
        """Run the FSM over an iterable of input symbols."""

        outputs: List[str] = []
        for symbol in inputs:
            outputs.append(self.step(symbol))
        return outputs

    @property
    def trace(self) -> Trace:
        """Return the simulation trace captured so far."""

        return self._trace
