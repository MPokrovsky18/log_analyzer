from argparse import ArgumentParser, Namespace
from os import path
from typing import Sequence

from log_analyzer.exceptions import ReportNameError
from log_analyzer.reports_registry import REPORTS


def get_args_from_command_line() -> Namespace:
    """
    Get and parse parameters from the command line.
    """
    parser = ArgumentParser(
        description="Log analyzer from files.",
        epilog="epilos here"
    )
    parser.add_argument("file_paths", nargs="+")
    parser.add_argument("--report", required=True)

    return parser.parse_args()


def validate_report_name_or_raise(report_name: str) -> str:
    """
    Check if the report name is among the valid ones.

    Otherwise throw an exception: ReportNameError.
    """
    if report_name not in REPORTS:
        raise ReportNameError(f"Incorrect report name: {report_name}")

    return report_name


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
