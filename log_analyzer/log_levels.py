from typing import TypedDict


class LogLevelStats(TypedDict):
    """
    A typed dict that stores statistics on logging levels.
    """

    DEBUG: int
    INFO: int
    WARNING: int
    ERROR: int
    CRITICAL: int
