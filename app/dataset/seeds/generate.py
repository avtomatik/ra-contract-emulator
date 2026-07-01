import json
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

from faker import Faker

fake = Faker("ru_RU")

BASE = Path(__file__).resolve().parent


def make_user():
    first_name = fake.first_name()
    last_name = fake.last_name()
    common_name = f"{last_name} {first_name} {fake.middle_name()}"
    return {
        "id": str(uuid.uuid4()),
        "nameAttributes": {
            "1.2.643.100.3": fake.snils(),
            "2.5.4.3": common_name,
            "2.5.4.42": first_name,
            "2.5.4.4": last_name,
            "2.5.4.6": "RU",
            "1.2.643.3.131.1.1": fake.individuals_inn(),
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
    with (BASE / f"{name}.json").open("w", encoding="utf8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    users = [make_user() for _ in range(20)]

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
