from app.api.dto.certificate import CertificateDetailDTO, CertificateSummaryDTO
from app.shared.models.certificate import Certificate


class CertificatePresenter:
    @staticmethod
    def summary(certificate: Certificate) -> CertificateSummaryDTO:
        return CertificateSummaryDTO.model_validate(
            certificate, from_attributes=True
        )

    @classmethod
    def summaries(cls, certificates: list[Certificate]):
        return [cls.summary(c) for c in certificates]

    @staticmethod
    def detail(certificate: Certificate) -> CertificateDetailDTO:
        return CertificateDetailDTO.model_validate(
            certificate, from_attributes=True
        )
