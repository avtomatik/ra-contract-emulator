from app.api.dto.pagination import PageResult
from app.api.presenters.user import UserPresenter
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
        return PageResult(
            items=UserPresenter.summaries(page.items), links=page.links
        )
