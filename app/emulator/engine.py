from app.behaviors.context import BehaviorContext
from app.emulator.router import EmulatorRouter
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

        context = BehaviorContext(
            certificate_repository=self.state.certificate_repository,
            certificate_request_repository=self.state.certificate_request_repository,
            user_repository=self.state.user_repository,
        )

        return handler(request, context)
