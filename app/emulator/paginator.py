import base64

from app.api.dto.pagination import Links, NextLink, PageResult


class Paginator:

    DEFAULT_PAGE_SIZE = 20

    @staticmethod
    def encode(offset: int) -> str:
        return base64.urlsafe_b64encode(str(offset).encode()).decode()

    @staticmethod
    def decode(token: str | None) -> int:
        if not token:
            return 0
        return int(base64.urlsafe_b64decode(token).decode())

    @classmethod
    def paginate(
        cls,
        *,
        items,
        page_token: str | None,
        endpoint: str,
        page_size: int = DEFAULT_PAGE_SIZE,
    ):
        offset = cls.decode(page_token)
        page = items[offset : offset + page_size]
        next_offset = offset + page_size
        links = None

        if next_offset < len(items):
            token = cls.encode(next_offset)
            links = Links(next=NextLink(href=f"{endpoint}?pageToken={token}"))

        return PageResult(items=page, links=links)
