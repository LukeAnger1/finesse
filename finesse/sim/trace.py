"""Trace capture utilities for FSM simulations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class TraceEvent:
    """Represents a single step observed during simulation."""

    source: str
    target: str
    symbol: str


@dataclass
class Trace:
    """Container for simulation trace events."""

    events: List[TraceEvent] = field(default_factory=list)

    def record(self, source: str, target: str, symbol: str) -> None:
        """Record a new transition event."""

        self.events.append(TraceEvent(source, target, symbol))
