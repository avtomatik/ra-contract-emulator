from typing import TypeVar

from app.api.dto.pagination import Links, PageResult

T = TypeVar("T")


class PaginationPresenter:
    @staticmethod
    def present(items: list[T], links: Links | None) -> PageResult[T]:
        return PageResult(items=items, links=links)
