from abc import ABC, abstractmethod
from domain.entities.deal import Deal

class AbstractDealRepository(ABC):
    @abstractmethod
    async def get_by_id(self, deal_id: UUID) -> Deal | None:
        ...
    
    
    @abstractmethod
    async def save(self, deal: Deal) -> None:
        ...
    
