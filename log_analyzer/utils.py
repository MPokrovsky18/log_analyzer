from argparse import ArgumentParser, Namespace
from os import path
from typing import Sequence


def get_args_from_command_line() -> Namespace:
    """
    Get and parse parameters from the command line.
    """
    parser = ArgumentParser(
        description="Log analyzer from files.",
    )
    parser.add_argument("file_paths", nargs="+")
    parser.add_argument("--report", required=True)

    return parser.parse_args()


def validate_file_paths_or_raise(file_paths: Sequence[str]) -> Sequence[str]:
    """
    Check if files exist at the given paths.

    Otherwise throw an exception: FileNotFoundError.
    """
    not_exists_files = set()
    exists_files = set()

    for file_path in file_paths:
        if not path.isfile(file_path):
            not_exists_files.add(file_path)
            continue

        exists_files.add(file_path)

    if not_exists_files:
        raise FileNotFoundError(
            "No files found: {}".format(", ".join(sorted(not_exists_files)))
        )

    return sorted(exists_files)
