from dataclasses import dataclass

from app.shared.models.certificate import Certificate
from app.shared.models.certificate_request import CertificateRequest
from app.shared.models.user import User


@dataclass
class Dataset:
    certificates: list[Certificate]
    cert_requests: list[CertificateRequest]
    users: list[User]
