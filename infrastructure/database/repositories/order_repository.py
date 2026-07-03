from sqlalchemy.ext.asyncio import AsyncSession
from application.interfaces.order_repository import AbstractOrderRepository

class SQLAlchemyOrderRepository(AbstractOrderRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
    