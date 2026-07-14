from uuid import UUID

from app.repositories.base import InMemoryRepository
from app.shared.models.certificate import Certificate


class CertificateRepository(InMemoryRepository[Certificate]):
    def by_id(self, certificate_id: UUID) -> Certificate:
        return self.find(lambda c: c.id == certificate_id)

    def by_serial(self, serial: str) -> Certificate:
        return self.find(lambda c: c.serial_number == serial)
