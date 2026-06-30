import json
import random
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

from faker import Faker

fake = Faker()

BASE = Path(__file__).resolve().parent


def make_user():
    return {
        "id": str(uuid.uuid4()),
        "nameAttributes": {
            "2.5.4.3": fake.name(),
            "2.5.4.42": fake.first_name(),
            "2.5.4.4": fake.last_name(),
            "2.5.4.6": "RU",
            "1.2.643.3.131.1.1": str(random.randint(1000000000, 9999999999)),
        },
        "createdWhen": datetime.now(timezone.utc).isoformat(),
        "distinguishedName": f"CN={fake.name()},O=Example",
    }


def make_certificate(user):
    serial = str(random.randint(100000, 999999))

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
