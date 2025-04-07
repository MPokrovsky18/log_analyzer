from typing import Callable


ReportFormatter = Callable[[dict], str]


def format_handlers_report(data: dict) -> str:
    """
    Formats data for the 'handlers' report into text.
    """
    return "The formatted data from the 'handlers' report will be here."
