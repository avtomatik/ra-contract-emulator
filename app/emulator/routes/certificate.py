from app.behaviors.certificate.get import GetCertificateBehavior
from app.behaviors.certificate.list import ListCertificatesBehavior
from app.emulator.router import Route

certificate_routes = [
    Route("GET", "/api/ra/certificates", ListCertificatesBehavior.execute),
    Route(
        "GET",
        "/api/ra/certificates/{id}",
        GetCertificateBehavior.execute,
    ),
]
