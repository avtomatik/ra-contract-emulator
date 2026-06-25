from fastapi import FastAPI

from app.dataset.loader import load_dataset
from app.emulator.endpoints import ROUTES
from app.emulator.engine import EmulatorEngine
from app.emulator.router import EmulatorRouter
from app.emulator.state import EmulatorState
from app.interfaces.routes import router


def create_app() -> FastAPI:
    app = FastAPI(title="RA Contract Emulator")

    # =========================================================================
    # BOOTSTRAP EMULATOR CORE
    # =========================================================================
    dataset = load_dataset()
    state = EmulatorState(dataset=dataset)

    engine = EmulatorEngine(
        state=state,
        router=EmulatorRouter(ROUTES),
    )

    app.state.engine = engine

    app.include_router(router)

    return app


app = create_app()
