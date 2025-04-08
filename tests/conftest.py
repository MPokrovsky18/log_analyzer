import sys
import tempfile
from types import SimpleNamespace

import pytest

from tests.constants import (
    EXISTS_REPORT_NAME,
    FILE_1,
    FILE_2,
    LOG_FILE_CONTENT,
    LOG_LINE_1,
    LOG_LINE_2,
    NOT_EXISTS_FILE,
)


@pytest.fixture
def set_correct_argv_parameters(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["prog", FILE_1, FILE_2, "--report", EXISTS_REPORT_NAME]
    )


@pytest.fixture
def create_temp_exists_paths(tmp_path):
    paths = []

    for file in (FILE_1, FILE_2):
        new_file = tmp_path / file
        new_file.write_text("test content")
        paths.append(str(new_file))

    return paths


@pytest.fixture
def set_success_fake_args_for_config(monkeypatch):
    fake_args = SimpleNamespace(
        file_paths=[FILE_1, FILE_2],
        report=EXISTS_REPORT_NAME,
    )

    monkeypatch.setattr(
        "log_analyzer.utils.get_args_from_command_line",
        lambda: fake_args,
    )
    monkeypatch.setattr(
        "log_analyzer.utils.validate_file_paths_or_raise",
        lambda paths: sorted(paths),
        )


@pytest.fixture
def set_unsuccess_fake_args_for_config(monkeypatch):
    fake_args = SimpleNamespace(
        file_paths=[NOT_EXISTS_FILE],
        report=EXISTS_REPORT_NAME,
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


@pytest.fixture
def create_handler_log_file():
    """
    Create a temporary log file for testing HandlersReportCollector.
    """
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_log:
        temp_log.write(LOG_FILE_CONTENT)
        return temp_log.name


@pytest.fixture
def create_two_log_files_with_overlap(tmp_path):
    file1 = tmp_path / FILE_1
    file2 = tmp_path / FILE_2

    file1.write_text(LOG_LINE_1)
    file2.write_text(LOG_LINE_2)

    return [str(file1), str(file2)]
