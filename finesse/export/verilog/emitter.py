"""Verilog/SystemVerilog code generation helpers."""

from __future__ import annotations

from ..core.fsm import FiniteStateMachine


def emit_verilog(fsm: FiniteStateMachine) -> str:
    """Return a placeholder Verilog module for the FSM."""

    return f"// Verilog for FSM {fsm.name}\nmodule {fsm.name}();\nendmodule"
