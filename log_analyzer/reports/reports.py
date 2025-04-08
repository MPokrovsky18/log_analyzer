from dataclasses import dataclass

from log_analyzer.log_levels import LogLevelStats
from log_analyzer.reports.base import BaseReport


@dataclass
class HandlersReport(BaseReport):
    """
    The class that stores the report data is 'handlers'.
    """

    total_requests: int
    handlers_log_level_stats: dict[str, LogLevelStats]
    total_log_level_stats: LogLevelStats
