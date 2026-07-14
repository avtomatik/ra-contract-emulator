from uuid import UUID

from app.repositories.base import InMemoryRepository
from app.shared.models.user import User


class UserRepository(InMemoryRepository[User]):
    def by_id(self, user_id: UUID):
        return self.find(lambda u: u.id == user_id)
