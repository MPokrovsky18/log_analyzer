from log_analyzer.report_collectors import (
    BaseReportCollector,
    HandlersReportCollector,
)

REPORTS: dict[str, BaseReportCollector] = {
    "handlers": HandlersReportCollector,
}
