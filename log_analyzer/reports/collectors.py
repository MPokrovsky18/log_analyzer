from typing import NamedTuple
from log_analyzer.log_levels import (
    get_default_log_level_stats,
    is_log_level,
    LogLevelStats,
)
from log_analyzer.reports.base import BaseReportCollector
from log_analyzer.reports.reports import HandlersReport


class HandlerInfo(NamedTuple):
    handler: str
    log_level: str


class HandlersReportCollector(BaseReportCollector):
    """
    The class collects data for the 'handlers' report.
    """

    def _process_file(self, path: str) -> dict[str, LogLevelStats]:
        data = {}

        with open(path, "r") as file:
            for line in file:
                handler_info = self._parse_line(line)

                if not handler_info:
                    continue

                handler = handler_info.handler
                log_level = handler_info.log_level

                if handler not in data:
                    data[handler] = get_default_log_level_stats()

                data[handler][log_level] += 1

        return data

    def _parse_line(self, line: str) -> HandlerInfo | None:
        if "django.request" in line:
            parts = line.split()

            try:
                handler = next(part for part in parts if part.startswith("/"))
                log_level = next(part for part in parts if is_log_level(part))
            except StopIteration:
                return

            return HandlerInfo(
                handler=handler,
                log_level=log_level,
            )

    def _aggregate_data(
            self, data: list[dict[str, LogLevelStats]]
    ) -> HandlersReport:
        total_requests = 0
        handlers_log_level_stats = {}
        total_log_level_stats = get_default_log_level_stats()

        for file_data in data:
            for handler, logs_stats in file_data.items():
                if handler not in handlers_log_level_stats:
                    handlers_log_level_stats[
                        handler
                    ] = get_default_log_level_stats()

                for log_level, count in logs_stats.items():
                    handlers_log_level_stats[handler][log_level] += count
                    total_log_level_stats[log_level] += count
                    total_requests += count

        return HandlersReport(
            total_requests=total_requests,
            handlers_log_level_stats=handlers_log_level_stats,
            total_log_level_stats=total_log_level_stats
        )
