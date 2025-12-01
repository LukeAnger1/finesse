"""Helper functions exposed in the DSL."""

from __future__ import annotations

from ..core.io import Signal
from ..types import SignalDirection


def sig(name: str, width: int = 1, *, direction: SignalDirection = SignalDirection.INPUT) -> Signal:
    """Create a signal declaration."""

    return Signal(name=name, width=width, direction=direction)


def const(value: int) -> int:
    """Return a constant literal for DSL expressions."""

    return value
