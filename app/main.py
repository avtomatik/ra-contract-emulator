from fastapi import FastAPI

from app.dataset.ensure import ensure_dataset_exists
from app.dataset.loader import load_dataset
from app.emulator.endpoints import ROUTES
from app.emulator.engine import EmulatorEngine
from app.emulator.router import EmulatorRouter
from app.emulator.state import EmulatorState
from app.interfaces.routes import router
from app.repositories.certificate import CertificateRepository
from app.repositories.certificate_request import CertificateRequestRepository
from app.repositories.user import UserRepository


def create_app() -> FastAPI:
    ensure_dataset_exists()

    app = FastAPI(title="RA Contract Emulator", version="0.1.0")
    dataset = load_dataset()
    state = EmulatorState(
        dataset=dataset,
        certificate_repository=CertificateRepository(dataset.certificates),
        certificate_request_repository=CertificateRequestRepository(
            dataset.cert_requests
        ),
        user_repository=UserRepository(dataset.users),
    )
    engine = EmulatorEngine(state=state, router=EmulatorRouter(ROUTES))
    app.state.engine = engine
    app.include_router(router)
    return app


app = create_app()
