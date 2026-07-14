from uuid import UUID

from app.api.presenters.certificate_request import CertificateRequestPresenter


class GetCertificateRequestBehavior:
    @staticmethod
    def execute(request, state):
        certificate_request = state.certificate_request_repository.by_id(
            UUID(request["id"])
        )
        return CertificateRequestPresenter.detail(certificate_request)
