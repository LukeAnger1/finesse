from finesse.core import FSM, State, Transition
from finesse.export.verilog import emit_fsm_oneprocess_enum


def build_simple_fsm() -> FSM:
    fsm = FSM(name="example_fsm", inputs={"start": 1, "done": 1})

    idle = State("S_IDLE", side_effect=False)
    busy = State("S_BUSY")
    done = State("S_DONE", side_effect=False)

    fsm.add_states([idle, busy, done], default="S_IDLE")

    fsm.add_transition(Transition("S_IDLE", "S_BUSY", lambda inp: inp["start"] == 1))
    fsm.add_transition(Transition("S_BUSY", "S_DONE", lambda inp: inp["done"] == 1))
    fsm.add_transition(Transition("S_DONE", "S_IDLE", lambda inp: True))

    return fsm


def my_cond_str(t: Transition) -> str:
    # Temporary hand-written mapping from transitions to Verilog exprs
    if t.src == "S_IDLE" and t.dst == "S_BUSY":
        return "start"
    if t.src == "S_BUSY" and t.dst == "S_DONE":
        return "done"
    if t.src == "S_DONE" and t.dst == "S_IDLE":
        return "1'b1"
    return "1'b0"


if __name__ == "__main__":
    fsm = build_simple_fsm()
    verilog = emit_fsm_oneprocess_enum(fsm, cond_str=my_cond_str)
    print(verilog)