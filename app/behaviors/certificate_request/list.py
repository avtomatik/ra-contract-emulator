from app.api.presenters.pagination import PaginationPresenter
from app.emulator.paginator import Paginator


class ListCertificateRequestsBehavior:
    @staticmethod
    def execute(request, state):
        repository = state.certificate_request_repository
        page = Paginator.paginate(
            items=repository.all(),
            page_token=request.get("pageToken"),
            endpoint="/api/ra/certRequests",
        )
        return PaginationPresenter.present(page.items, page.links)
