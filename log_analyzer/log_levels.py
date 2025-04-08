from enum import Enum
from typing import TypedDict


class LogLevelsEnum(Enum):
    """
    Enum of logging levels.
    """
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class LogLevelStats(TypedDict):
    """
    A typed dict that stores statistics on logging levels.
    """

    DEBUG: int
    INFO: int
    WARNING: int
    ERROR: int
    CRITICAL: int


def get_default_log_level_stats() -> LogLevelStats:
    """
    Get LogLevelStats with default values.
    """
    return LogLevelStats(
        DEBUG=0,
        INFO=0,
        WARNING=0,
        ERROR=0,
        CRITICAL=0,
    )


def is_log_level(log_level: str) -> bool:
    """
    Check if a string is a log level.
    """
    return log_level in LogLevelsEnum._member_map_
