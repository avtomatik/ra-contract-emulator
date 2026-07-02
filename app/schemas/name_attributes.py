from typing import Any

from pydantic import RootModel

from .oids import OID


class NameAttributes(RootModel[dict[str, Any]]):
    # =========================================================================
    # Subject attributes
    # =========================================================================
    def common_name(self) -> str | None:
        return self.root.get(OID.CN)

    def surname(self) -> str | None:
        return self.root.get(OID.SN)

    def given_name(self) -> str | None:
        return self.root.get(OID.GIVEN_NAME)

    def country_name(self) -> str | None:
        return self.root.get(OID.C)

    def locality_name(self) -> str | None:
        return self.root.get(OID.L)

    def state_or_province_name(self) -> str | None:
        return self.root.get(OID.S)

    def street_address(self) -> str | None:
        return self.root.get(OID.STREET)

    def organization_name(self) -> str | None:
        return self.root.get(OID.O)

    def organizational_unit_name(self) -> str | None:
        return self.root.get(OID.OU)

    def title(self) -> str | None:
        return self.root.get(OID.T)

    # =========================================================================
    # Russian subject attributes
    # =========================================================================
    def inn(self) -> str | None:
        return self.root.get(OID.INN)

    def snils(self) -> str | None:
        return self.root.get(OID.SNILS)

    def guid(self) -> str | None:
        return self.root.get(OID.GUID)

    def legal_entity_inn(self) -> str | None:
        return self.root.get(OID.LEGAL_ENTITY_INN)

    def ogrn(self) -> str | None:
        return self.root.get(OID.OGRN)

    # =========================================================================
    # PKCS #9
    # =========================================================================
    def email_address(self) -> str | None:
        return self.root.get(OID.EMAIL_ADDRESS)

    def unstructured_name(self) -> str | None:
        return self.root.get(OID.UNSTRUCTURED_NAME)

    # =========================================================================
    # Microsoft
    # =========================================================================
    def user_principal_name(self) -> str | None:
        return self.root.get(OID.USER_PRINCIPAL_NAME)

    def certificate_template(self) -> str | None:
        return self.root.get(OID.CERTIFICATE_TEMPLATE)

    # =========================================================================
    # Russian certificate extensions
    # =========================================================================
    def signature_device(self) -> str | None:
        return self.root.get(OID.SIGNATURE_DEVICE)

    def issuer_signature_and_ca_tools(self) -> str | None:
        return self.root.get(OID.ISSUER_SIGNATURE_AND_CA_TOOLS)

    def identity_verification_method(self) -> str | None:
        return self.root.get(OID.IDENTITY_VERIFICATION_METHOD)

    # =========================================================================
    # GOST algorithms
    # =========================================================================
    def gost3410_2012_256_public_key(self) -> str | None:
        return self.root.get(OID.GOST3410_2012_256_PUBLIC_KEY)

    def gost3411_2012_256_signature(self) -> str | None:
        return self.root.get(OID.GOST3411_2012_256_SIGNATURE)

    # =========================================================================
    # PKIX
    # =========================================================================
    def authority_information_access(self) -> str | None:
        return self.root.get(OID.AUTHORITY_INFORMATION_ACCESS)

    def ocsp(self) -> str | None:
        return self.root.get(OID.OCSP)

    def ca_issuers(self) -> str | None:
        return self.root.get(OID.CA_ISSUERS)

    # =========================================================================
    # X.509 v3 extensions
    # =========================================================================
    def subject_key_identifier(self) -> str | None:
        return self.root.get(OID.SUBJECT_KEY_IDENTIFIER)

    def key_usage(self) -> str | None:
        return self.root.get(OID.KEY_USAGE)

    def private_key_usage_period(self) -> str | None:
        return self.root.get(OID.PRIVATE_KEY_USAGE_PERIOD)

    def crl_distribution_points(self) -> str | None:
        return self.root.get(OID.CRL_DISTRIBUTION_POINTS)

    def certificate_policies(self) -> str | None:
        return self.root.get(OID.CERTIFICATE_POLICIES)

    def authority_key_identifier(self) -> str | None:
        return self.root.get(OID.AUTHORITY_KEY_IDENTIFIER)

    def extended_key_usage(self) -> str | None:
        return self.root.get(OID.EXTENDED_KEY_USAGE)

    # =========================================================================
    # Extended Key Usage (EKU)
    # =========================================================================
    def smartcard_login(self) -> str | None:
        return self.root.get(OID.SMARTCARD_LOGIN)

    def raw(self) -> dict[str, Any]:
        return self.root
