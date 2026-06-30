from app.emulator.behaviors.cert_requests import list_cert_requests
from app.emulator.behaviors.certificates import (get_certificate,
                                                 list_certificates)
from app.emulator.behaviors.users import list_users
from app.emulator.router import Route

ROUTES = [
    Route("GET", "/api/ra/certificates", list_certificates),
    Route(
        "GET", "/api/ra/certificates/serialNumber/{serial}", get_certificate
    ),
    Route("GET", "/api/ra/users", list_users),
    Route("GET", "/api/ra/certRequests", list_cert_requests),
]
