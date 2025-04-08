from typing import Callable

from log_analyzer.log_levels import LogLevelsEnum, LogLevelStats
from log_analyzer.reports.base import BaseReport
from log_analyzer.reports.reports import HandlersReport


ReportFormatter = Callable[[BaseReport], str]


def format_handlers_report(report: HandlersReport) -> str:
    """
    Formats data for the 'handlers' report into text.
    """

    def get_fill_row(
            handler: str,
            log_stats: LogLevelStats | None = None,
            **kwargs,
    ) -> str:
        """
        Get a row with filled columns.
        """
        row_template = (
            "{handler:<20} {debug:<10} "
            "{info:<10} {warning:<10} "
            "{error:<10} {critical:<10}\n"
        )

        log_stats = log_stats or {
            level.name: kwargs.get(level.name.lower(), "")
            for level in LogLevelsEnum
        }

        return row_template.format(
            handler=handler,
            debug=log_stats.get(LogLevelsEnum.DEBUG.name, 0),
            info=log_stats.get(LogLevelsEnum.INFO.name, 0),
            warning=log_stats.get(LogLevelsEnum.WARNING.name, 0),
            error=log_stats.get(LogLevelsEnum.ERROR.name, 0),
            critical=log_stats.get(LogLevelsEnum.CRITICAL.name, 0),
        )

    def get_handlers_table(
            handlers_log_level_stats: dict[str, LogLevelStats]
    ) -> str:
        """
        Get table of handlers and log statistics.
        """
        table = get_fill_row(
            handler="HANDLER",
            debug=LogLevelsEnum.DEBUG.name,
            info=LogLevelsEnum.INFO.name,
            warning=LogLevelsEnum.WARNING.name,
            error=LogLevelsEnum.ERROR.name,
            critical=LogLevelsEnum.CRITICAL.name,
        )

        handlers = sorted(handlers_log_level_stats.keys())

        for handler in handlers:
            table += get_fill_row(
                handler=handler,
                log_stats=handlers_log_level_stats[handler]
            )

        table += get_fill_row(
            handler="",
            log_stats=report.total_log_level_stats,
        )

        return table

    text = f"Total requests: {report.total_requests}\n"

    return text + get_handlers_table(report.handlers_log_level_stats)
