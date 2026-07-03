from application.interfaces.user_repository import AbstractUserRepository
from sqlalchemy.ext.asyncio import AsyncSession
class SQLAlchemyUserRepository(AbstractUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
    
        