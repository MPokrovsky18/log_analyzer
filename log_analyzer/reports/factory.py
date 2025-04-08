from log_analyzer.reports.validators import validate_report_name_or_raise
from log_analyzer.reports.report_registry import REPORTS
from log_analyzer.reports.service import ReportService


class ReportServiceCreator:
    """
    The class creates a ReportService.
    """

    @staticmethod
    def create(report_name: str) -> ReportService:
        """
        Create ReportService by report name.
        """
        report_name = validate_report_name_or_raise(report_name)
        report_attrs = REPORTS[report_name]

        return ReportService(
            collector=report_attrs.report_collector(),
            formatter=report_attrs.formatter,
        )
