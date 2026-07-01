from typing import Any

from pydantic import RootModel

from .oids import OID


class NameAttributes(RootModel[dict[str, Any]]):
    def common_name(self) -> str | None:
        return self.root.get(OID.CN)

    def surname(self) -> str | None:
        return self.root.get(OID.SN)

    def given_name(self) -> str | None:
        return self.root.get(OID.GIVEN_NAME)

    def country(self) -> str | None:
        return self.root.get(OID.C)

    def locality(self) -> str | None:
        return self.root.get(OID.L)

    def organization(self) -> str | None:
        return self.root.get(OID.O)

    def organization_unit(self) -> str | None:
        return self.root.get(OID.OU)

    def inn(self) -> str | None:
        return self.root.get(OID.INN)

    def guid(self) -> str | None:
        return self.root.get(OID.GUID)

    def snils(self) -> str | None:
        return self.root.get(OID.SNILS)

    def email(self) -> str | None:
        return self.root.get(OID.EMAIL_PKCS)

    def upn(self) -> str | None:
        return self.root.get(OID.USER_PRINCIPAL_NAME)

    def raw(self) -> dict[str, Any]:
        return self.root
