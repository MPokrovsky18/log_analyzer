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

        return self._combine_results(partial_results)

    @abstractmethod
    def _process_file(self, path: str) -> dict:
        """
        Process data from file.
        """
        raise NotImplementedError(
            f"Subclasses must implement {self._process_file.__name__} method."
        )

    @abstractmethod
    def _combine_results(self, data: list[dict]) -> dict:
        """
        Aggregate data from different files.
        """
        raise NotImplementedError(
            "Subclasses must implement "
            f"{self._combine_results.__name__} method."
        )
