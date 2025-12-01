"""Core data structures for the Finesse FSM toolkit."""

from .fsm import FiniteStateMachine, State, Transition
from .io import Signal

__all__ = ["FiniteStateMachine", "State", "Transition", "Signal"]
