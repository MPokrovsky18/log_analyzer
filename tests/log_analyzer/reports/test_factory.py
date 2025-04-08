import tempfile

from log_analyzer.reports.factory import ReportServiceCreator

from tests.constants import EXISTS_REPORT_NAME, REVIEWS_HANDLER, LOG_LINE_1


def test_report_service_execute_outputs_report(capfd):
    """
    Test that ReportService correctly prints formatted output
    from a log file.
    """
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_log:
        temp_log.write(LOG_LINE_1)
        path = temp_log.name

    service = ReportServiceCreator.create(EXISTS_REPORT_NAME)
    service.execute([path])

    out, _ = capfd.readouterr()
    assert "Total requests: 1" in out
    assert REVIEWS_HANDLER in out
