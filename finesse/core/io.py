"""Signal declaration utilities for FSM interfaces."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from ..types import SignalDirection


@dataclass(frozen=True)
class Signal:
    """Represents an I/O signal attached to an FSM."""

    name: str
    width: int = 1
    direction: SignalDirection = SignalDirection.INPUT
    default: Optional[int] = None
