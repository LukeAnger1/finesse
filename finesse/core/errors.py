"""Custom error and warning types for the FSM toolkit."""


class FinesseError(Exception):
    """Base class for Finesse-specific errors."""


class ValidationError(FinesseError):
    """Raised when validation passes detect an issue."""


class SimulationError(FinesseError):
    """Raised when the simulator encounters an unexpected condition."""
