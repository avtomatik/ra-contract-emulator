from pydantic import Field

from .base import DomainModel


class Extension(DomainModel):
    oid: str
    oid_description: str | None = Field(
        None, validation_alias="oidDescription"
    )
    value: str
