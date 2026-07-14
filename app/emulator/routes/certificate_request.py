from app.behaviors.certificate_request.get import GetCertificateRequestBehavior
from app.behaviors.certificate_request.list import \
    ListCertificateRequestsBehavior
from app.emulator.router import Route

request_routes = [
    Route(
        "GET",
        "/api/ra/certRequests",
        ListCertificateRequestsBehavior.execute,
    ),
    Route(
        "GET",
        "/api/ra/certRequests/{id}",
        GetCertificateRequestBehavior.execute,
    ),
]
