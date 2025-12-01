"""Shared enumerations and data types for the Finesse toolkit."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping


class SignalDirection(Enum):
    """Enumeration describing the direction of an I/O signal."""

    INPUT = "input"
    OUTPUT = "output"


@dataclass(frozen=True)
class SignalSpec:
    """Represents a typed signal declaration in the DSL."""

    name: str
    width: int = 1
    metadata: Mapping[str, Any] | None = None
