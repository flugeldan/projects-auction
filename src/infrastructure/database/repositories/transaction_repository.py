from src.application.interfaces.transaction_repository import AbstractTransactionRepository
from src.domain.entities.transaction import Transaction
from src.domain.exceptions import TransactionAlreadyExistsError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

class TransactionRepository(AbstractTransactionRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def get_by_id(self, transaction_id) -> Transaction | None:
        return self._session.get(Transaction, transaction_id)
    
    async def save(self, transaction: Transaction) -> None:
        self._session.add(transaction)
        try:
            await self._session.flush()
        except IntegrityError as e:
            raise TransactionAlreadyExistsError
    


    
