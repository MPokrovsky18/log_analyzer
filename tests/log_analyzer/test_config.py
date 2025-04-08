import pytest

from log_analyzer import config

from tests.constants import FILE_1, FILE_2, EXISTS_REPORT_NAME


@pytest.mark.usefixtures("set_success_fake_args_for_config")
def test_get_config_success():
    """
    Test to get correct Config.
    """
    result = config.get_config()

    assert isinstance(result, config.Config)
    assert result.file_paths == [FILE_1, FILE_2]
    assert result.report_name == EXISTS_REPORT_NAME


@pytest.mark.usefixtures("set_unsuccess_fake_args_for_config")
def test_get_config_file_validation_fails():
    """
    Test when trying to get config, get exception.
    """
    with pytest.raises(FileNotFoundError, match="File not found"):
        config.get_config()
