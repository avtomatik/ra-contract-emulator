from fastapi import APIRouter, Request

router = APIRouter()


def get_engine(request: Request):
    return request.app.state.engine


@router.get("/api/ra/certificates")
def list_certificates(request: Request, q: str | None = None):
    engine = get_engine(request)
    return engine.handle("GET", "/api/ra/certificates", {"q": q})


@router.get("/api/ra/certificates/serialNumber/{serial}")
def get_certificate(request: Request, serial: str):
    engine = get_engine(request)
    return engine.handle(
        "GET",
        f"/api/ra/certificates/serialNumber/{serial}",
        {"serial": serial},
    )

@router.get("/api/ra/certRequests")
def list_cert_requests(request: Request):
    engine = get_engine(request)
    return engine.handle("GET", "/api/ra/certRequests")


@router.get("/api/ra/users")
def list_users(request: Request):
    engine = get_engine(request)
    return engine.handle("GET", "/api/ra/users")

