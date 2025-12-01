"""Pass framework for transforming FSMs."""

from .encoding import identity_encoding
from .manager import PassManager
from .merge import no_op_merge
from .minimize import no_op_minimization
from .validate import DEFAULT_VALIDATION_PASSES, ensure_initial_state

__all__ = [
    "PassManager",
    "identity_encoding",
    "no_op_merge",
    "no_op_minimization",
    "DEFAULT_VALIDATION_PASSES",
    "ensure_initial_state",
]
