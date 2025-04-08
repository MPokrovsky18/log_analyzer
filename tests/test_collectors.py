import tempfile

from log_analyzer.reports.collectors import HandlersReportCollector


def test_collect_log_stats_from_log_file():
    log_content = """\
2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK
2025-03-28 12:44:47,000 ERROR django.request: GET /api/v1/reviews/ 500

2025-03-28 12:44:48,000 WARNING django.request: GET /api/v1/users/ 403
2025-03-28 12:44:49,000 DEBUG other.module: GET /api/v1/ignore/ 200 OK
2025-03-28 12:44:50,000 CRITICAL django.request: GET /api/v1/users/ 500
"""

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_log:
        temp_log.write(log_content)
        path = temp_log.name

    collector = HandlersReportCollector()
    report = collector.collect([path])

    assert report.total_requests == 4

    assert report.handlers_log_level_stats["/api/v1/reviews/"]["INFO"] == 1
    assert report.handlers_log_level_stats["/api/v1/reviews/"]["ERROR"] == 1
    assert report.handlers_log_level_stats["/api/v1/users/"]["WARNING"] == 1
    assert report.handlers_log_level_stats["/api/v1/users/"]["CRITICAL"] == 1

    assert report.total_log_level_stats["INFO"] == 1
    assert report.total_log_level_stats["ERROR"] == 1
    assert report.total_log_level_stats["WARNING"] == 1
    assert report.total_log_level_stats["CRITICAL"] == 1
    assert report.total_log_level_stats["DEBUG"] == 0
