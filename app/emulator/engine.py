from app.emulator.router import EmulatorRouter
from app.emulator.state import EmulatorState


class EmulatorEngine:

    def __init__(self, state: EmulatorState, router: EmulatorRouter):
        self.state = state
        self.router = router

    def handle(self, method: str, path: str, request: dict | None = None):
        request = request or {}
        self.state.increment()
        handler = self.router.match(method, path)
        return handler(request, self.state, self.state.dataset)
