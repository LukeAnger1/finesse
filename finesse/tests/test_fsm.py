"""Placeholder tests for the Finesse FSM toolkit."""

from __future__ import annotations

import pytest

from ..core.fsm import FiniteStateMachine


@pytest.mark.skip(reason="FSM behaviors not yet implemented")
def test_placeholder() -> None:
    """Placeholder test to keep the suite green until real tests exist."""

    fsm = FiniteStateMachine(name="example")
    assert fsm.name == "example"
