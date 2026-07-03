from abc import ABC, abstractmethod
from uuid import UUID
from domain.entities.order import Order
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

    