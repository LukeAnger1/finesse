"""Live visualization hooks for notebooks and CLIs."""

from __future__ import annotations

from ..core.fsm import FiniteStateMachine
from .mermaid import to_mermaid


def render_inline(fsm: FiniteStateMachine) -> str:
    """Return an embeddable representation for interactive environments."""

    return to_mermaid(fsm)
