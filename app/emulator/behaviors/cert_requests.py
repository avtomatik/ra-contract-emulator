from app.schemas.responses import CertRequestsResponse


def list_cert_requests(request, state, dataset):
    return CertRequestsResponse(
        items=dataset.cert_requests, links={"next": None}
    )
