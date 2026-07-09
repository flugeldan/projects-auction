from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from application.interfaces.deal_repository import AbstractDealRepository
from domain.entities.deal import Deal
from uuid import UUID
from domain.exceptions import DealAlreadyExistsError

class SQLAlchemyDealRepository(AbstractDealRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, deal_id: UUID) -> Deal | None:
        return await self._session.get(Deal, deal_id)
    
    async def save(self, deal: Order) -> None:
        self._session.add(deal)
        try:
            await self._session.flush()
        except IntegrityError as e:
            raise DealAlreadyExistsError(deal.id) from e
        

    