from uuid import UUID

from app.api.presenters.certificate import CertificatePresenter


class GetCertificateBehavior:
    @staticmethod
    def execute(request, state):
        certificate = state.certificate_repository.by_id(UUID(request["id"]))
        return CertificatePresenter.detail(certificate)
