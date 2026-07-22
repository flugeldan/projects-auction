from abc import ABC, abstractmethod
from uuid import UUID
from src.domain.entities.user import User
class AbstractUserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> User | None:
        ...

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None:
        ...

    @abstractmethod
    async def save(user: User) -> None:
        ...
    
    @abstractmethod
    async def update(self, user: User) -> None:
        ...

