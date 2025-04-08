import pytest

from log_analyzer.reports.exceptions import ReportNameError
from log_analyzer.reports.validators import validate_report_name_or_raise

from tests.constants import EXISTS_REPORT_NAME, NOT_EXISTS_REPORT_NAME


def test_valid_report_name():
    """
    Test to ensure that the report name is valid.
    """
    assert validate_report_name_or_raise(
        EXISTS_REPORT_NAME
    ) == EXISTS_REPORT_NAME


def test_invalid_report_name_raises():
    """
    Test to ensure that if the report name is invalid, we get an exception.
    """
    with pytest.raises(ReportNameError):
        validate_report_name_or_raise(NOT_EXISTS_REPORT_NAME)
