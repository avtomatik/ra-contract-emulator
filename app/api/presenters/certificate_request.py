from app.api.dto.certificate_request import (CertificateRequestDetailDTO,
                                             CertificateRequestSummaryDTO)
from app.shared.models.certificate_request import CertificateRequest


class CertificateRequestPresenter:
    @staticmethod
    def summary(request: CertificateRequest) -> CertificateRequestSummaryDTO:
        return CertificateRequestSummaryDTO.model_validate(
            request, from_attributes=True
        )

    @classmethod
    def summaries(cls, requests: list[CertificateRequest]):
        return [cls.summary(c) for c in requests]

    @staticmethod
    def detail(request: CertificateRequest) -> CertificateRequestDetailDTO:
        return CertificateRequestDetailDTO.model_validate(
            request, from_attributes=True
        )
