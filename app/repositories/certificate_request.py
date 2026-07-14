from uuid import UUID

from app.repositories.base import InMemoryRepository
from app.shared.models.certificate_request import CertificateRequest


class CertificateRequestRepository(InMemoryRepository[CertificateRequest]):
    def by_id(self, request_id: UUID):
        return self.find(lambda r: r.id == request_id)
