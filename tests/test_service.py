import tempfile

from log_analyzer.reports.factory import ReportServiceCreator


def test_report_service_execute_outputs_report(capfd):
    log_content = "2025-03-28 INFO django.request: GET /some/ 200 OK\n"

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_log:
        temp_log.write(log_content)
        path = temp_log.name

    service = ReportServiceCreator.create("handlers")
    service.execute([path])

    out, _ = capfd.readouterr()
    assert "Total requests: 1" in out
    assert "/some/" in out
