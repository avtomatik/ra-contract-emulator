from app.dataset.loader import load_dataset
from app.emulator.endpoints import ROUTES
from app.emulator.engine import EmulatorEngine
from app.emulator.router import EmulatorRouter
from app.emulator.state import EmulatorState


def main():
    print("Seeding RA Contract Emulator...")

    dataset = load_dataset()

    state = EmulatorState(dataset=dataset)

    engine = EmulatorEngine(
        state=state,
        router=EmulatorRouter(ROUTES),
    )

    # =========================================================================
    # Smoke test: simulate a few RA calls
    # =========================================================================
    print(">> certificates:", engine.handle("GET", "/api/ra/certificates"))
    print(">> users:", engine.handle("GET", "/api/ra/users"))
    print(">> certRequests:", engine.handle("GET", "/api/ra/certRequests"))

    print("SEED COMPLETE")


if __name__ == "__main__":
    main()
