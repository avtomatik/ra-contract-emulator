from app.api.dto.user import UserSummaryDTO
from app.shared.models.user import User


class UserPresenter:
    @staticmethod
    def summary(user: User) -> UserSummaryDTO:
        return UserSummaryDTO.model_validate(user, from_attributes=True)

    @classmethod
    def summaries(cls, users: list[User]):
        return [cls.summary(c) for c in users]
