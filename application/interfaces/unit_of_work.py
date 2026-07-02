from abc import ABC, abstractmethod
from application.interfaces.user_repository import AbstractUserRepository
from application.interfaces.order_repository import AbstractOrderRepository

class AbstractUnitOfWork(ABC):
    users: AbstractUserRepository
    orders: AbstractOrderRepository

    @abstractmethod
    async def __aenter__(self) -> "AbstractUnitOfWork":
        ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb):
        ...

    @abstractmethod
    async def commit(self) -> None:
        ...

    @abstractmethod
    async def rollback(self) -> None:
        ...
    