import json
from pathlib import Path

from app.dataset.models import Dataset
from app.schemas.cert_request import CertificateRequest
from app.schemas.certificate import Certificate
from app.schemas.user import User

BASE = Path(__file__).resolve().parent / "seeds"


def load_json(name: str):
    with (BASE / f"{name}.json").open("r", encoding="utf-8") as f:
        return json.load(f)


def load_dataset() -> Dataset:
    return Dataset(
        certificates=[
            Certificate.model_validate(x) for x in load_json("certificates")
        ],
        users=[User.model_validate(x) for x in load_json("users")],
        cert_requests=[
            CertificateRequest.model_validate(x)
            for x in load_json("cert_requests")
        ],
    )
