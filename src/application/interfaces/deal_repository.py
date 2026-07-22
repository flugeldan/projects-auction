from abc import ABC, abstractmethod
from uuid import UUID
from src.domain.entities.deal import Deal, DealStatus
from src.domain.entities.order import Order
class AbstractDealRepository(ABC):
    @abstractmethod
    async def get_by_id(self, deal_id: UUID) -> Deal | None:
        ...
    
    @abstractmethod
    async def get_by_id_personal_deals(self, user_id: UUID) -> list[Deal]:
        ...
    
    @abstractmethod
    async def save(self, deal: Deal) -> None:
        ...
    
    @abstractmethod
    async def update(self, deal: Deal) -> None:
        ...

    @abstractmethod
    async def get_all_in_progress_by_user(self, user_id: UUID) -> list[Order]:
        ...
    
    @abstractmethod
    async def _change_status(self, deal_id: UUID, new_status: DealStatus) -> None:
        ...
    
    @abstractmethod
    async def get_by_order_id(self, order_id: UUID) -> Deal | None:
        ...
    
    @abstractmethod
    async def get_by_order_and_user(self, order_id: UUID, user_id: UUID) -> Deal | None:
        ...
    
    @abstractmethod
    async def mark_as_failed(self, order_id: UUID, user_id: UUID) -> None:
        ...
    
    @abstractmethod
    async def mark_as_completed(self, order_id: UUID, user_id: UUID) -> None:
        ...
    