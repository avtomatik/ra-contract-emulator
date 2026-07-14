from typing import Generic, TypeVar

from pydantic import Field

from .base import DTO


class NextLink(DTO):
    href: str


class Links(DTO):
    next: NextLink | None = None


T = TypeVar("T")


class PageResult(DTO, Generic[T]):
    items: list[T]
    links: Links | None = Field(None, serialization_alias="_links")
