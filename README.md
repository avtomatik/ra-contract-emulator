# RA Contract Emulator

A lightweight FastAPI-based emulator for RA contract API schemas.
It loads a seeded dataset of certificates, certificate requests, and users, then exposes them via a contract-aligned REST API.

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
uv sync
```

### 2. Activate environment

```bash
source .venv/bin/activate
```

### 3. Generate seed dataset

```bash
uv run python -m app.seed
```

This creates JSON seed files in:

```
app/dataset/seeds/
```

---

### 4. Run the API server

```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Server will be available at:

```
http://localhost:8000
```

---

## 📦 Architecture Overview

The emulator is split into four main layers:

### 1. Dataset Layer (`app/dataset`)

* Loads JSON seed data
* Converts raw JSON into Pydantic models
* Entry point: `load_dataset()`

Entities:

* `Certificate`
* `CertificateRequest`
* `User`

---

### 2. Schema Layer (`app/schemas`)

Defines all contract models using Pydantic:

* Strongly typed API models (`APIModel`)
* CamelCase aliasing via `to_camel`
* Response wrappers (`CertificatesResponse`, etc.)
* Certificate and request domain models

---

### 3. Emulator Layer (`app/emulator`)

Core runtime logic:

* **Engine**

  * Executes requests
  * Tracks request count
  * Routes to handlers

* **Router**

  * Matches HTTP method + path
  * Extracts path parameters

* **Behaviors**

  * Business logic per endpoint:

    * `certificates.py`
    * `cert_requests.py`
    * `users.py`

---

### 4. Interface Layer (`app/interfaces`)

FastAPI routes that forward requests into the emulator engine.

Example flow:

```
FastAPI route → EmulatorEngine → Router → Behavior → Response model → Serializer
```

---

## 📡 API Endpoints

### Certificates

#### List certificates

```
GET /api/ra/certificates
```

Query params:

* `q` (optional) – filters by serial number or subject

---

#### Get certificate by serial

```
GET /api/ra/certificates/serialNumber/{serial}
```

---

### Certificate Requests

```
GET /api/ra/certRequests
```

---

### Users

```
GET /api/ra/users
```

---

## 🧪 Dataset Generation

Seed data is generated using Faker (`ru_RU` locale).

Run:

```bash
uv run python -m app.dataset.seeds.generate
```

It generates:

| File                 | Content                      |
| -------------------- | ---------------------------- |
| `users.json`         | Fake users                   |
| `certificates.json`  | Certificates linked to users |
| `cert_requests.json` | Certificate requests         |

---

## 🧠 Key Design Decisions

### 1. Pydantic-first contract modeling

All API entities are strict Pydantic models with alias mapping to match external contract formats.

---

### 2. Root-based NameAttributes

Certificate subject attributes are stored as OID-keyed dictionaries:

```python
"2.5.4.3" -> Common Name
"2.5.4.4" -> Surname
```

Accessed via helper methods like:

```python
user.name_attributes.common_name()
```

---

### 3. Emulator engine abstraction

Instead of directly using FastAPI logic, requests go through:

```
Engine → Router → Behavior → Dataset
```

This allows:

* deterministic contract testing
* replayable behavior
* easier diff/validation later

---

### 4. Serialization layer

All Pydantic responses are normalized via:

```python
model_dump(mode="json", by_alias=True, exclude_none=True)
```

Ensures strict contract output formatting.

---

## 🧩 Project Structure

```
app/
├── contract/        # validation + diff tools
├── dataset/         # seed loader + generator
├── emulator/        # runtime engine + behaviors
├── interfaces/      # FastAPI routes
├── schemas/         # Pydantic models (contract layer)
└── main.py          # app entrypoint
```

---

## 🛠 Development Notes

### Regenerate dataset after schema changes

Always run:

```bash
uv run python -m app.dataset.seeds.generate
```

---

### Common debugging flow

1. Check dataset JSON in `app/dataset/seeds/`
2. Validate schema parsing via:

   ```python
   model_validate()
   ```
3. Inspect emulator behavior in:

   ```
   app/emulator/behaviors/
   ```

---

## 📌 Future Improvements (optional ideas)

* Add pagination to all list endpoints
* Implement proper `NotFoundError → HTTP 404 mapping`
* Add contract diff CLI runner
* Add OpenAPI tagging per domain
* Add versioned datasets
