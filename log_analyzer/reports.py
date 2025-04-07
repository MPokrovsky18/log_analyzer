from abc import ABC
from dataclasses import dataclass
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


class Report(ABC):
    """
    An abstract class whose descendants store report data.
    """

    pass


@dataclass
class HandlersReport(Report):
    """
    The class that stores the report data is 'handlers'.
    """

    total_requests: int
    handlers_log_level_stats: dict[str, LogLevelStats]
    total_log_level_stats: LogLevelStats
