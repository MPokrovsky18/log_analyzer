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
        return super()._process_file(path)

    def _aggregate_data(self, data: list[dict]) -> dict:
        return super()._aggregate_data(data)
