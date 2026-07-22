from abc import ABC, abstractmethod
from uuid import UUID
from src.domain.entities.transaction import Transaction
class AbstractTransactionRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: UUID) -> Transaction | None:
        ...
    
    @abstractmethod
    async def save(self, transaction: Transaction) -> None:
        ...