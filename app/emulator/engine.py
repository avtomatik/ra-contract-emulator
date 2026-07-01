from app.emulator.router import EmulatorRouter
from app.emulator.serializer import serialize
from app.emulator.state import EmulatorState


class EmulatorEngine:
    def __init__(self, state: EmulatorState, router: EmulatorRouter):
        self.state = state
        self.router = router

    def handle(self, method, path, request=None):
        request = request or {}
        self.state.increment()

        handler, params = self.router.match(method, path)
        request.update(params)

        result = handler(request, self.state, self.state.dataset)
        return serialize(result)
