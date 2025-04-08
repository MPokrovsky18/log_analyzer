import pytest

from log_analyzer import utils

from tests.constants import (
    FILE_1,
    FILE_2,
    NOT_EXISTS_FILE,
    EXISTS_REPORT_NAME,
)


@pytest.mark.usefixtures("set_correct_argv_parameters")
def test_get_args_from_command_line():
    """
    Test get parameters from argv.
    """
    args = utils.get_args_from_command_line()

    assert args.file_paths == [FILE_1, FILE_2]
    assert args.report == EXISTS_REPORT_NAME


def test_validate_file_paths_or_raise_success(create_temp_exists_paths):
    """
    Test to check that the files from the parameters exist.
    """
    paths = create_temp_exists_paths
    result = utils.validate_file_paths_or_raise(paths)

    assert result == paths


def test_validate_file_paths_or_raise_failure():
    """
    Test to get exception if file does not exist.
    """
    with pytest.raises(FileNotFoundError):
        utils.validate_file_paths_or_raise([NOT_EXISTS_FILE])
