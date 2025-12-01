"""Unique identifier generation helpers."""

from __future__ import annotations

import itertools
from typing import Iterator


def sequential_ids(prefix: str = "id") -> Iterator[str]:
    """Yield an infinite sequence of unique identifiers."""

    for idx in itertools.count():
        yield f"{prefix}_{idx}"
