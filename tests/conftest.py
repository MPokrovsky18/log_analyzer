import sys

import pytest

from tests.constants import FILE_1, FILE_2, EXISTS_REPORT_NAME


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
