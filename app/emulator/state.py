from dataclasses import dataclass

from app.dataset.models import Dataset


@dataclass
class EmulatorState:
    dataset: Dataset
    request_count: int = 0

    def increment(self) -> None:
        self.request_count += 1
