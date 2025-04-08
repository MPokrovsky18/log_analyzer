import sys

import pytest

from log_analyzer import utils


def test_validate_file_paths_or_raise_success(tmp_path):
    file = tmp_path / "test.log"
    file.write_text("test content")
    result = utils.validate_file_paths_or_raise([str(file)])
    assert result == [str(file)]


def test_validate_file_paths_or_raise_failure():
    with pytest.raises(FileNotFoundError):
        utils.validate_file_paths_or_raise(["not_exists.log"])


def test_get_args_from_command_line(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["prog", "file1.log", "file2.log", "--report", "handlers"]
    )
    args = utils.get_args_from_command_line()

    assert args.file_paths == ["file1.log", "file2.log"]
    assert args.report == "handlers"
