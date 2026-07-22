from abc import ABC, abstractmethod
from uuid import UUID
from src.domain.entities.order import Order
from src.domain.entities.user import User
class AbstractOrderRepository(ABC):
    @abstractmethod
    async def get_by_id(self, order_id: UUID) -> Order | None:
        ...
    
    @abstractmethod
    async def get_available(self) -> list[Order] | None:
        ...

    @abstractmethod
    async def save(self, user: Order) -> None:
        ...

    @abstractmethod
    async def update(self, order: Order) -> None:
        ...
    


    