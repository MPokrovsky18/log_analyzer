from log_analyzer.report_service import ReportService
from log_analyzer.report_registry import REPORTS


class ReportServiceCreator:
    """
    The class creates a ReportService.
    """

    @staticmethod
    def create(report_name: str) -> ReportService:
        """
        Create ReportService by report name.
        """
        report_attrs = REPORTS[report_name]

        return ReportService(
            collector=report_attrs.report_collector(),
            formatter=report_attrs.formatter,
        )
