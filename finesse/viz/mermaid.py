"""Utilities to export FSMs as Mermaid diagrams."""

from __future__ import annotations

from ..core.fsm import FiniteStateMachine


def to_mermaid(fsm: FiniteStateMachine) -> str:
    """Render a Mermaid diagram representing the FSM."""

    lines = ["stateDiagram-v2"]
    for state in fsm.states.values():
        for transition in state.transitions.values():
            lines.append(f"    {state.name} --> {transition.target} : {transition.condition or ''}")
    return "\n".join(lines)
