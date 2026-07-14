from app.api.dto.pagination import PageResult
from app.api.presenters.certificate_request import CertificateRequestPresenter
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
        return PageResult(
            items=CertificateRequestPresenter.summaries(page.items),
            links=page.links,
        )
