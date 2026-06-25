from app.schemas.responses import CertificatesResponse


def list_certificates(request, state, dataset):
    items = dataset.certificates

    q = request.get("q") or request.get("value")
    if q:
        q = q.lower()
        items = [
            c
            for c in items
            if q in c.serial_number.lower()
            or (c.subject or "").lower().find(q) >= 0
        ]

    return CertificatesResponse(items=items, links={"next": None})


def get_certificate(request, state, dataset):
    serial = request["serial"]

    for c in dataset.certificates:
        if c.serial_number == serial:
            return c

    raise KeyError(f"Certificate not found: {serial}")
