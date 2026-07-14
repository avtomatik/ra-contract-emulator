from app.api.presenters.pagination import PaginationPresenter
from app.emulator.paginator import Paginator


class ListUsersBehavior:
    @staticmethod
    def execute(request, state):
        repository = state.user_repository
        page = Paginator.paginate(
            items=repository.all(),
            page_token=request.get("pageToken"),
            endpoint="/api/ra/users",
        )
        return PaginationPresenter.present(page.items, page.links)
