from typing import Callable


ReportFormatter = Callable[[dict], str]


def format_handlers_report(data: dict) -> str:
    """
    Formats data for the 'handlers' report into text.
    """

    def get_fill_row(
            handler: str,
            logs_info: dict[str, str | int] | None = None,
            **kwargs,
    ) -> str:
        row_template = (
            "{handler:<20} {debug:<10} "
            "{info:<10} {warning:<10} "
            "{error:<10} {critical:<10}\n"
        )

        if logs_info is None:
            logs_info = {
                "DEBUG": kwargs.get("debug", ""),
                "INFO": kwargs.get("info", ""),
                "WARNING": kwargs.get("warning", ""),
                "ERROR": kwargs.get("error", ""),
                "CRITICAL": kwargs.get("critical", ""),
            }

        return row_template.format(
            handler=handler,
            debug=logs_info["DEBUG"],
            info=logs_info["INFO"],
            warning=logs_info["WARNING"],
            error=logs_info["ERROR"],
            critical=logs_info["CRITICAL"],
        )

    def get_handlers_table(handlers_info: dict[str, any]) -> str:
        titles_colomns = get_fill_row(
            handler="HANDLER",
            debug="DEBUG",
            info="INFO",
            warning="WARNING",
            error="ERROR",
            critical="CRITICAL",
        )

        table = titles_colomns

        for handler, log_types in handlers_info.items():
            table += get_fill_row(
                handler=handler,
                logs_info=log_types,
            )

        table += get_fill_row(
            handler="",
            logs_info=data["total handlers stats"],
        )

        return table

    text = f"Total requests: {data["total requests"]}\n"

    return text + get_handlers_table(data["handlers"])
