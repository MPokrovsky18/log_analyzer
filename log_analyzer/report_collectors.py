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
        # data after file processing.
        return {"data": "data"}

    def _aggregate_data(self, data: list[dict]) -> dict:
        return {
            "total requests": 1000,
            "handlers": {
                "handler1": {
                    "DEBUG": 100,
                    "INFO": 100,
                    "WARNING": 100,
                    "ERROR": 100,
                    "CRITICAL": 100,
                },
                "handler2": {
                    "DEBUG": 100,
                    "INFO": 100,
                    "WARNING": 100,
                    "ERROR": 100,
                    "CRITICAL": 100,
                },
            },
            "total handlers stats": {
                "DEBUG": 200,
                "INFO": 200,
                "WARNING": 200,
                "ERROR": 200,
                "CRITICAL": 200,
            }
        }
