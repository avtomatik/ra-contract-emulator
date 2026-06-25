from app.schemas.responses import CertificatesResponse


def validate_certificates_response(data):
    return CertificatesResponse.model_validate(data)
