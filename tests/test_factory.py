import pytest

from log_analyzer.reports.exceptions import ReportNameError
from log_analyzer.reports.factory import ReportServiceCreator
from log_analyzer.reports.service import ReportService


def test_report_service_creator_creates_valid_service():
    service = ReportServiceCreator.create("handlers")
    assert isinstance(service, ReportService)
    assert hasattr(service, "_collector")
    assert hasattr(service, "_formatter")


def test_report_service_creator_raises_on_invalid_name():
    with pytest.raises(ReportNameError):
        ReportServiceCreator.create("non_existing_report")
