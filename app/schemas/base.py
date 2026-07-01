from pydantic import BaseModel, ConfigDict


def to_camel(string: str) -> str:
    parts = string.split("_")
    return parts[0] + "".join(p.title() for p in parts[1:])


class APIModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        extra="ignore",
        from_attributes=True,
        alias_generator=to_camel,
        validate_by_name=True,
    )
