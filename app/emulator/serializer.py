from pydantic import BaseModel


def serialize(obj):
    if isinstance(obj, BaseModel):
        return obj.model_dump(mode="json", by_alias=True, exclude_none=True)
    return obj
