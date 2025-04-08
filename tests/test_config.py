import pytest
from types import SimpleNamespace

from log_analyzer import config


def test_get_config_success(monkeypatch):
    fake_args = SimpleNamespace(
        file_paths=["file1.log", "file2.log"],
        report="handlers"
    )

    monkeypatch.setattr(
        "log_analyzer.utils.get_args_from_command_line",
        lambda: fake_args
    )
    monkeypatch.setattr(
        "log_analyzer.utils.validate_file_paths_or_raise",
        lambda paths: sorted(paths)
        )

    result = config.get_config()

    assert result.file_paths == ["file1.log", "file2.log"]
    assert result.report_name == "handlers"


def test_get_config_file_validation_fails(monkeypatch):
    fake_args = SimpleNamespace(
        file_paths=["nonexistent.log"],
        report="handlers"
    )

    monkeypatch.setattr(
        "log_analyzer.utils.get_args_from_command_line",
        lambda: fake_args
    )
    monkeypatch.setattr(
        "log_analyzer.utils.validate_file_paths_or_raise",
        lambda paths: (_ for _ in ()).throw(
            FileNotFoundError("File not found")
        )
    )

    with pytest.raises(FileNotFoundError, match="File not found"):
        config.get_config()
