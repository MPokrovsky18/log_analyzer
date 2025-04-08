from typing import Callable

from log_analyzer.log_levels import LogLevelStats
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
        row_template = (
            "{handler:<20} {debug:<10} "
            "{info:<10} {warning:<10} "
            "{error:<10} {critical:<10}\n"
        )

        if log_stats is None:
            log_stats = {
                "DEBUG": kwargs.get("debug", ""),
                "INFO": kwargs.get("info", ""),
                "WARNING": kwargs.get("warning", ""),
                "ERROR": kwargs.get("error", ""),
                "CRITICAL": kwargs.get("critical", ""),
            }

        return row_template.format(
            handler=handler,
            debug=log_stats.get("DEBUG", 0),
            info=log_stats.get("INFO", 0),
            warning=log_stats.get("WARNING", 0),
            error=log_stats.get("ERROR", 0),
            critical=log_stats.get("CRITICAL", 0),
        )

    def get_handlers_table(
            handlers_log_level_stats: dict[str, LogLevelStats]
    ) -> str:
        table = get_fill_row(
            handler="HANDLER",
            debug="DEBUG",
            info="INFO",
            warning="WARNING",
            error="ERROR",
            critical="CRITICAL",
        )

        for handler, log_stats in handlers_log_level_stats.items():
            table += get_fill_row(
                handler=handler,
                log_stats=log_stats,
            )

        table += get_fill_row(
            handler="",
            log_stats=report.total_log_level_stats,
        )

        return table

    text = f"Total requests: {report.total_requests}\n"

    return text + get_handlers_table(report.handlers_log_level_stats)
