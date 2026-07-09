from application.interfaces.user_repository import AbstractUserRepository
from domain.entities.user import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID
class SQLAlchemyUserRepository(AbstractUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def get_by_id(self, user_id: UUID):
        return self._session.get(User, user_id)
    
    async def get_by_email(self, email: str):
        stmt = (select(User)
                .where(User.email == email))
        res = await self._session.execute(stmt)

        return res.scalar_one_or_none()
    
    async def save(self, user: User):
        return await self._session.add(user)

        
        