"""Boolean and bitvector expression abstract syntax tree nodes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class Literal:
    """Represents a literal value in an expression."""

    value: Union[int, bool]


@dataclass(frozen=True)
class Identifier:
    """Represents a named reference in an expression."""

    name: str


@dataclass(frozen=True)
class UnaryOp:
    """Represents a unary operation."""

    op: str
    operand: "Expression"


@dataclass(frozen=True)
class BinaryOp:
    """Represents a binary operation."""

    op: str
    left: "Expression"
    right: "Expression"


Expression = Union[Literal, Identifier, UnaryOp, BinaryOp]
