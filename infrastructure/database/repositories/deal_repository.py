from sqlalchemy.ext.asyncio import AsyncSession
from application.interfaces.deal_repository import AbstractDealRepository

class SQLAlchemyDealRepository(AbstractDealRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    