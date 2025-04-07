from typing import Sequence

from log_analyzer.formatters import ReportFormatter
from log_analyzer.report_collectors import BaseReportCollector


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
        data = self._collector.collect(file_paths)
        formatted_text = self._formatter(data)
        print(formatted_text)
