from app.api.dto.pagination import PageResult
from app.api.presenters.certificate import CertificatePresenter
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
        return PageResult(
            items=CertificatePresenter.summaries(page.items), links=page.links
        )
