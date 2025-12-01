"""Finite state machine core data structures."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Transition:
    """Represents a transition between states."""

    source: str
    target: str
    condition: Optional[str] = None
    actions: List[str] = field(default_factory=list)


@dataclass
class State:
    """Represents a state within an FSM."""

    name: str
    transitions: Dict[str, Transition] = field(default_factory=dict)


@dataclass
class FiniteStateMachine:
    """Container for states and transitions."""

    name: str
    states: Dict[str, State] = field(default_factory=dict)
    initial_state: Optional[str] = None
