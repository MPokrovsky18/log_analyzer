from log_analyzer.log_levels import (
    get_default_log_level_stats,
    is_log_level,
    LogLevelsEnum,
)


INCORRECT_LOG_LEVEL_NAME = "SOMETHING"


def test_get_default_log_level_stats():
    """
    Test getting LogLevelStats with default values.
    """
    stats = get_default_log_level_stats()

    for level in LogLevelsEnum:
        assert stats[level.name] == 0

    assert len(stats) == len(LogLevelsEnum)


def test_is_log_level_true():
    """
    The test will return True if the correct logging levels are passed.
    """
    for level in LogLevelsEnum:
        assert is_log_level(level.name) is True


def test_is_log_level_false():
    """
    The test will return False if incorrect logging levels are passed.
    """
    assert is_log_level(INCORRECT_LOG_LEVEL_NAME) is False
