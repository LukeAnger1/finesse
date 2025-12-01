# Finesse FSM Toolkit

Finesse is a Python-based DSL for describing, analyzing, and generating hardware finite-state machines (FSMs). It provides:

- A compact Python interface for defining states, transitions, and inputs.
- A small expression DSL for writing transition conditions that simultaneously evaluate in Python and emit Verilog expressions.
- Built-in simulation for stepping an FSM through input sequences.
- Mermaid diagram generation for visualization. (use with https://mermaid.live/)
- Verilog code generation (enum-based, single-process style) with ready/done signals.
- Hooks for future optimizations such as state encoding or merging.

The goal is to make FSM development faster, clearer, and less error-prone than directly writing Verilog (especially designed for ParaDPLL FPGA SAT solver)

---

## Directory Structure

```

finesse/
core/
   fsm.py            # FSM, State, Transition classes
   expr.py           # Small expression DSL for conditions
export/
   verilog.py        # Verilog code generation
test1.py             # Minimal usage example
backtrack_example.py # Real-world FSM example
README.md            # This file :)

```

---

## Core Concepts

### FSM
Represents a finite-state machine.

Important fields:
- `name`: name of the FSM
- `inputs`: dictionary of input signals and bitwidths
- `states`: internal map of State objects
- `transitions`: flat list of Transition objects
- `default_state`: reset/idle state
- `current_state`: state during simulation

Key operations:
- `add_state`, `add_states`
- `add_transition`
- `reset()`
- `step(inputs)`
- `multi_step(list_of_inputs)`
- `visualize(outfile, show_conditions=True)`
- `to_mermaid(show_conditions=True)`

### State
Represents a named FSM state.

Fields:
- `name`: identifier
- `side_effect`: optional flag for user logic
- `default`: True if this is the reset/idle state
- `transitions`: list of outgoing transitions (internal)

### Transition
Represents a directed edge between states.

Fields:
- `src`: source state name
- `dst`: destination state name
- `cond`: expression built with the small DSL in `expr.py`

Example condition:
```python
from finesse.core.expr import sig
cond = (sig("start") == 1) & (sig("busy") == 0)
````

This condition:

* Evaluates in Python using `.eval(inputs)`
* Emits valid Verilog using `.to_verilog()`

### Expression DSL

Located in `finesse/core/expr.py`.

Supports:

* Signals: `sig("start")`
* Constants: `const(1)`
* Logical ops: `&`, `|`, `^`, `~`
* Comparisons: `==`, `!=`, `<`, `<=`, `>`, `>=`

Expressions can be directly used as FSM transition conditions.

---

## Verilog Generation

The emitter creates a single-process FSM with:

* `typedef enum logic [...]` for state names
* One `always_ff @(posedge clk)` block
* A `case (state_q)` statement for transitions
* Explicit “stay in same state” fallthrough
* Auto-generated:

  * `ready_o` high in the idle state
  * `done_o` high for one cycle in terminal states

Usage:

```python
from finesse.export.verilog import emit_fsm_oneprocess_enum

verilog = emit_fsm_oneprocess_enum(fsm)
print(verilog)
```

---

## Next Steps

* State encoding optimization (one-hot, binary, Gray, custom) from simulation
* Automatic state minimization
* Automatic coverage analysis and warnings for transitions
* Interactive editor with warnings and live FSM visualization
* Hooks for integrating with hardware testbenches (cocotb)