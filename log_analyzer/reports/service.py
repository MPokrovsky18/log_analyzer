from typing import Sequence

from log_analyzer.reports.formatters import ReportFormatter
from log_analyzer.reports.base import BaseReport, BaseReportCollector


class ReportService:
    """
    Class that outputs a report from data collected
    from files and formatted according to the function.
    """

    def __init__(
            self,
            collector: BaseReportCollector,
            formatter: ReportFormatter
    ) -> None:
        self._collector = collector
        self._formatter = formatter

    def execute(self, file_paths: Sequence[str]):
        """
        Collects, formats and outputs a report.
        """
        report = self._collector.collect(file_paths)
        self._display_report(report)

    def _display_report(self, report: BaseReport) -> None:
        """
        Output report to console.
        """
        formatted_text = self._formatter(report)
        print(formatted_text)
