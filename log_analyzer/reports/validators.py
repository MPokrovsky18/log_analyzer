from log_analyzer.reports.exceptions import ReportNameError
from log_analyzer.reports.report_registry import REPORTS


def validate_report_name_or_raise(report_name: str) -> str:
    """
    Check if the report name is among the valid ones.

    Otherwise throw an exception: ReportNameError.
    """
    if report_name not in REPORTS:
        raise ReportNameError(f"Incorrect report name: {report_name}")

    return report_name
