from abc import ABC, abstractmethod
from typing import Self
from application.interfaces.transaction_manager import AbstractTransactionManager
from sqlalchemy.ext.asyncio import AsyncSession

class SQLAlchemyTransactionManager(AbstractTransactionManager):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()
    
    async def rollback(self) -> None:
        await self._session.rollback()
    
    async def __aenter__(self) -> Self:
        return self
    
    async def __aexit__(self, exc_type, exc, tb) -> None:
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

