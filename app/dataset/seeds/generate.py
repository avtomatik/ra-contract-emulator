import json
import uuid
from datetime import datetime, timedelta, timezone
from random import choice

from faker import Faker

from app.config.paths import SEEDS_DIR
from app.core.enums import Gender
from app.schemas.oids import OID

fake = Faker("ru_RU")

def make_user():
    gender = choice(list(Gender))

    if gender == Gender.FEMALE:
        first_name = fake.first_name_female()
        middle_name = fake.middle_name_female()
        last_name = fake.last_name_female()
    elif gender == Gender.MALE:
        first_name = fake.first_name_male()
        middle_name = fake.middle_name_male()
        last_name = fake.last_name_male()

    common_name = f"{last_name} {first_name} {middle_name}"

    return {
        "id": str(uuid.uuid4()),
        "nameAttributes": {
            OID.SNILS: fake.snils(),
            OID.CN: common_name,
            OID.GIVEN_NAME: first_name,
            OID.SN: last_name,
            OID.C: "RU",
            OID.INN: fake.individuals_inn(),
        },
        "createdWhen": datetime.now(timezone.utc).isoformat(),
        "distinguishedName": f"CN={common_name},O={fake.company()}",
    }


def make_certificate(user):
    serial = fake.hexify(text="^" * 34)

    return {
        "id": str(uuid.uuid4()),
        "serialNumber": serial,
        "thumbprint": fake.sha1(),
        "nameAttributes": user["nameAttributes"],
        "createdWhen": datetime.now(timezone.utc).isoformat(),
        "notBefore": (
            datetime.now(timezone.utc) - timedelta(days=1)
        ).isoformat(),
        "notAfter": (
            datetime.now(timezone.utc) + timedelta(days=365)
        ).isoformat(),
        "keyNotAfter": (
            datetime.now(timezone.utc) + timedelta(days=365)
        ).isoformat(),
        "status": "ACTIVE",
        "userId": user["id"],
        "subject": user["distinguishedName"],
    }


def make_request(user):
    return {
        "id": str(uuid.uuid4()),
        "nameAttributes": user["nameAttributes"],
        "createdWhen": datetime.now(timezone.utc).isoformat(),
        "status": "NEW",
        "userId": user["id"],
    }


def write(name, data):
    with (SEEDS_DIR / f"{name}.json").open("w", encoding="utf8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main(number: int = 100):
    users = [make_user() for _ in range(number)]
    certificates = [make_certificate(u) for u in users]
    requests = [make_request(u) for u in users]

    write("users", users)
    write("certificates", certificates)
    write("cert_requests", requests)

    print("Dataset planted")
    print(f"users={len(users)}")
    print(f"certificates={len(certificates)}")
    print(f"requests={len(requests)}")


if __name__ == "__main__":
    main()
