from dataclasses import dataclass

from app.repositories.certificate import CertificateRepository
from app.repositories.certificate_request import CertificateRequestRepository
from app.repositories.user import UserRepository


@dataclass(slots=True)
class BehaviorContext:
    certificate_repository: CertificateRepository
    certificate_request_repository: CertificateRequestRepository
    user_repository: UserRepository
