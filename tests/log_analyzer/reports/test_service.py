import pytest

from log_analyzer.reports.exceptions import ReportNameError
from log_analyzer.reports.factory import ReportServiceCreator
from log_analyzer.reports.service import ReportService

from tests.constants import EXISTS_REPORT_NAME, NOT_EXISTS_REPORT_NAME


def test_report_service_creator_creates_valid_service():
    """
    Test that a ReportService is successfully created
    by a valid report name.
    """
    service = ReportServiceCreator.create(EXISTS_REPORT_NAME)

    assert isinstance(service, ReportService)
    assert hasattr(service, "_collector")
    assert hasattr(service, "_formatter")


def test_report_service_creator_raises_on_invalid_name():
    """
    Test that creating ReportService with an invalid name
    raises a ReportNameError.
    """
    with pytest.raises(ReportNameError):
        ReportServiceCreator.create(NOT_EXISTS_REPORT_NAME)
