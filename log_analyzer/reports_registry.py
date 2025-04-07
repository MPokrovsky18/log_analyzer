from typing import NamedTuple

from log_analyzer.formatters import format_handlers_report, ReportFormatter
from log_analyzer.report_collectors import (
    BaseReportCollector,
    HandlersReportCollector,
)


class Report(NamedTuple):
    """
    A named tuple containing a collector and formatter pair for reporting.
    """

    report_collector: BaseReportCollector
    formatter: ReportFormatter


HANDLERS_REPORT = Report(
    report_collector=HandlersReportCollector,
    formatter=format_handlers_report
)


REPORTS: dict[str, Report] = {
    "handlers": HANDLERS_REPORT,
}
