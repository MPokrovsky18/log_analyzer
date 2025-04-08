from log_analyzer.log_levels import LogLevelsEnum
from log_analyzer.reports.collectors import HandlersReportCollector

from tests.constants import USERS_HANDLER, REVIEWS_HANDLER


def test_collect_log_stats_from_log_file(create_handler_log_file):
    """
    Test collecting statistics from a log file with various entries,
    including valid django.request lines, invalid lines, and lines
    from other modules.
    """
    path = create_handler_log_file
    collector = HandlersReportCollector()
    report = collector.collect([path])

    assert report.total_requests == 4

    assert report.handlers_log_level_stats[
        REVIEWS_HANDLER
    ][LogLevelsEnum.INFO.name] == 1
    assert report.handlers_log_level_stats[
        REVIEWS_HANDLER
    ][LogLevelsEnum.ERROR.name] == 1
    assert report.handlers_log_level_stats[
        USERS_HANDLER
    ][LogLevelsEnum.WARNING.name] == 1
    assert report.handlers_log_level_stats[
        USERS_HANDLER
    ][LogLevelsEnum.CRITICAL.name] == 1

    assert report.total_log_level_stats[LogLevelsEnum.INFO.name] == 1
    assert report.total_log_level_stats[LogLevelsEnum.ERROR.name] == 1
    assert report.total_log_level_stats[LogLevelsEnum.WARNING.name] == 1
    assert report.total_log_level_stats[LogLevelsEnum.CRITICAL.name] == 1
    assert report.total_log_level_stats[LogLevelsEnum.DEBUG.name] == 0


def test_collect_combines_data_from_multiple_files(
        create_two_log_files_with_overlap
):
    """
    Test that collector aggregates data from multiple files
    with overlapping handler paths.
    """
    collector = HandlersReportCollector()
    report = collector.collect(create_two_log_files_with_overlap)

    assert report.total_requests == 2

    reviews_stats = report.handlers_log_level_stats[REVIEWS_HANDLER]
    assert reviews_stats[LogLevelsEnum.INFO.name] == 1
    assert reviews_stats[LogLevelsEnum.WARNING.name] == 1

    total_stats = report.total_log_level_stats
    assert total_stats[LogLevelsEnum.INFO.name] == 1
    assert total_stats[LogLevelsEnum.WARNING.name] == 1
