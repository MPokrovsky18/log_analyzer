from typing import NamedTuple, Sequence

from log_analyzer import utils


class Config(NamedTuple):
    """
    Named tuple with configuration data.
    """

    file_paths: Sequence[str]
    report_name: str


def get_config() -> Config:
    """
    Get configuration data.
    """
    parsed_args = utils.get_args_from_command_line()
    file_paths = utils.validate_file_paths_or_raise(parsed_args.file_paths)

    return Config(
        file_paths=file_paths,
        report_name=parsed_args.report,
    )
