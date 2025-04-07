from abc import ABC, abstractmethod
from typing import Sequence


class BaseReportCollector(ABC):
    """
    A base abstract class that implements an interface
    for collecting data from files into a report.
    """

    def collect(self, file_paths: Sequence[str]) -> dict:
        """
        Collect data from files.
        """
        partial_results = []

        for file in file_paths:
            data = self._process_file(file)
            partial_results.append(data)

        return self._aggregate_data(partial_results)

    @abstractmethod
    def _process_file(self, path: str) -> dict:
        """
        Process data from file.
        """
        raise NotImplementedError(
            f"Subclasses must implement {self._process_file.__name__} method."
        )

    @abstractmethod
    def _aggregate_data(self, data: list[dict]) -> dict:
        """
        Aggregate data from different files.
        """
        raise NotImplementedError(
            "Subclasses must implement "
            f"{self._aggregate_data.__name__} method."
        )


class HandlersReportCollector(BaseReportCollector):
    """
    The class collects data for the 'handlers' report.
    """

    def _process_file(self, path: str) -> dict:
        data = {}

        with open(path, "r") as file:
            for line in file:
                handler_info = self._parse_line(line)

                if not handler_info:
                    continue

                handler = handler_info["handler"]
                log_level = handler_info["log_level"]

                if handler not in data:
                    data[handler] = {}

                if log_level not in data[handler]:
                    data[handler][log_level] = 0

                data[handler][log_level] += 1

        return data

    def _parse_line(self, line: str) -> dict | None:
        if line.find("django.request") < 0:
            return

        data = line.split()
        handler = list(filter(lambda x: x.startswith("/"), data))[0]

        log_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

        log_level = list(filter(lambda x: x in log_levels, data))[0]

        return {
            "handler": handler,
            "log_level": log_level,
        }

    def _aggregate_data(self, data: list[dict]) -> dict:
        total_requests = 0
        handlers = {}
        total_handlers_stats = {
            "DEBUG": 0,
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        }

        for file_data in data:
            for handler, logs_info in file_data.items():
                if handler not in handlers:
                    handlers[handler] = {
                        "DEBUG": 0,
                        "INFO": 0,
                        "WARNING": 0,
                        "ERROR": 0,
                        "CRITICAL": 0,
                    }

                for log_level, count in logs_info.items():
                    handlers[handler][log_level] += count
                    total_handlers_stats[log_level] += count
                    total_requests += count

        return {
            "total requests": total_requests,
            "handlers": handlers,
            "total handlers stats": total_handlers_stats,
        }
