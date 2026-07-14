from app.api.presenters.pagination import PaginationPresenter
from app.emulator.paginator import Paginator


class ListCertificatesBehavior:
    @staticmethod
    def execute(request, state):
        repository = state.certificate_repository
        page = Paginator.paginate(
            items=repository.all(),
            page_token=request.get("pageToken"),
            endpoint="/api/ra/certificates",
        )
        return PaginationPresenter.present(page.items, page.links)
