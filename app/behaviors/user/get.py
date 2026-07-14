from uuid import UUID

from app.api.presenters.user import UserPresenter


class GetUserBehavior:
    @staticmethod
    def execute(request, state):
        user = state.user_repository.by_id(UUID(request["id"]))
        return UserPresenter.detail(user)
