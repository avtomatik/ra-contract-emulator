from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class InMemoryRepository(Generic[T]):
    def __init__(self, items: list[T]):
        self._items = items

    def all(self) -> list[T]:
        return list(self._items)

    def count(self) -> int:
        return len(self._items)

    def find(self, predicate: Callable[[T], bool]) -> T:
        for item in self._items:
            if predicate(item):
                return item
        raise LookupError()

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]
