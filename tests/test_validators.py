import pytest

from log_analyzer.reports.exceptions import ReportNameError
from log_analyzer.reports.validators import validate_report_name_or_raise


def test_valid_report_name():
    assert validate_report_name_or_raise("handlers") == "handlers"


def test_invalid_report_name_raises():
    with pytest.raises(ReportNameError):
        validate_report_name_or_raise("nonexistent")
