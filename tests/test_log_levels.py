from log_analyzer.log_levels import get_default_log_level_stats, is_log_level


def test_is_log_level_true():
    assert is_log_level("ERROR") is True


def test_is_log_level_false():
    assert is_log_level("SOMETHING") is False


def test_get_default_log_level_stats():
    stats = get_default_log_level_stats()
    assert stats["DEBUG"] == 0
    assert stats["INFO"] == 0
    assert stats["WARNING"] == 0
    assert stats["ERROR"] == 0
    assert stats["CRITICAL"] == 0
    assert len(stats) == 5
