from uuid import UUID

from fastapi import APIRouter, Request

router = APIRouter()


def get_engine(request: Request):
    return request.app.state.engine


@router.get("/api/ra/certificates")
def list_certificates(
    request: Request,
    q: str | None = None,
    pageToken: str | None = None,
):
    engine = get_engine(request)
    return engine.handle(
        "GET",
        "/api/ra/certificates",
        {"q": q, "pageToken": pageToken},
    )


@router.get("/api/ra/certificates/{id}")
def get_certificate(request: Request, id: UUID):
    engine = get_engine(request)
    return engine.handle("GET", f"/api/ra/certificates/{id}", {"id": str(id)})


@router.get("/api/ra/certRequests")
def list_cert_requests(
    request: Request,
    q: str | None = None,
    pageToken: str | None = None,
):
    engine = get_engine(request)
    return engine.handle(
        "GET",
        "/api/ra/certRequests",
        {"q": q, "pageToken": pageToken},
    )


@router.get("/api/ra/certRequests/{id}")
def get_cert_request(request: Request, id: UUID):
    engine = get_engine(request)
    return engine.handle("GET", f"/api/ra/certRequests/{id}", {"id": str(id)})


@router.get("/api/ra/users")
def list_users(
    request: Request,
    q: str | None = None,
    pageToken: str | None = None,
):
    engine = get_engine(request)
    return engine.handle(
        "GET",
        "/api/ra/users",
        {"q": q, "pageToken": pageToken},
    )


@router.get("/api/ra/users/{id}")
def get_user(request: Request, id: UUID):
    engine = get_engine(request)
    return engine.handle("GET", f"/api/ra/users/{id}", {"id": str(id)})
