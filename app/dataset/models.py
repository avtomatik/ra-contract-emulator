from dataclasses import dataclass

from app.schemas.cert_request import CertificateRequest
from app.schemas.certificate import Certificate
from app.schemas.user import User


@dataclass
class Dataset:
    certificates: list[Certificate]
    users: list[User]
    cert_requests: list[CertificateRequest]
