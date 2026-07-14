from uuid import UUID

from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()


def get_engine(request: Request):
    return request.app.state.engine


def dispatch(request: Request, method, path, payload):
    engine = get_engine(request)
    result = engine.handle(method, path, payload)
    return JSONResponse(content=jsonable_encoder(result, exclude_none=True))


@router.get("/api/ra/certificates")
def list_certificates(
    request: Request,
    q: str | None = None,
    pageToken: str | None = None,
):
    return dispatch(
        request,
        "GET",
        "/api/ra/certificates",
        {"q": q, "pageToken": pageToken},
    )


@router.get("/api/ra/certificates/{id}")
def get_certificate(request: Request, id: UUID):
    return dispatch(
        request, "GET", f"/api/ra/certificates/{id}", {"id": str(id)}
    )


@router.get("/api/ra/certRequests")
def list_cert_requests(
    request: Request,
    q: str | None = None,
    pageToken: str | None = None,
):
    return dispatch(
        request,
        "GET",
        "/api/ra/certRequests",
        {"q": q, "pageToken": pageToken},
    )


@router.get("/api/ra/certRequests/{id}")
def get_cert_request(request: Request, id: UUID):
    return dispatch(
        request, "GET", f"/api/ra/certRequests/{id}", {"id": str(id)}
    )


@router.get("/api/ra/users")
def list_users(
    request: Request,
    q: str | None = None,
    pageToken: str | None = None,
):
    return dispatch(
        request,
        "GET",
        "/api/ra/users",
        {"q": q, "pageToken": pageToken},
    )


@router.get("/api/ra/users/{id}")
def get_user(request: Request, id: UUID):
    return dispatch(request, "GET", f"/api/ra/users/{id}", {"id": str(id)})
