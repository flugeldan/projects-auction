from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from src.application.interfaces.deal_repository import AbstractDealRepository
from src.domain.entities.deal import Deal, DealStatus
from src.domain.entities.order import Order
from uuid import UUID
from src.domain.exceptions import DealAlreadyExistsError

from sqlalchemy import update

class SQLAlchemyDealRepository(AbstractDealRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, deal_id: UUID) -> Deal | None:
        return await self._session.get(Deal, deal_id)
    
    async def get_by_id_personal_deals(self, user_id: UUID) -> list[Deal]:
        stmt = (select(Deal)
                .where(Deal.user_id == user_id)
                .where(Deal.with_user.is_(True)))
        res = await self._session.execute(stmt)
        deals = list(res.scalars().all())
        return deals

    async def get_all_in_progress_by_user(self, user_id: UUID) -> list[Order]:
        stmt = (select(Order)
                .join(Deal, Order.id == Deal.order_id)
                .where(Deal.user_id == user_id)
                .where(Deal.status == DealStatus.in_progress))
        res = await self._session.execute(stmt)
        return list(res.scalars().unique().all())
    
    async def save(self, deal: Deal) -> None:
        self._session.add(deal)
        try:
            await self._session.flush()
        except IntegrityError as e:
            raise DealAlreadyExistsError(deal.id) from e
    
    async def update(self, deal: Deal) -> None:
        pass
    
    async def get_by_order_and_user(self, order_id: UUID, user_id: UUID) -> Deal | None:
        stmt = (select(Deal)
                .where(Deal.order_id == order_id)
                .where(Deal.user_id == user_id))
        res = await self._session.execute(stmt)
        return res.scalar_one_or_none()
    
    
    async def get_by_order_id(self, order_id: UUID):
        stmt = (select(Deal)
                .where(Deal.order_id == order_id))
        res = await self._session.execute(stmt)
        return res.scalar_one_or_none()
    
    
    async def _change_status(self, order_id: UUID, user_id: UUID, from_status: DealStatus, new_status: DealStatus) -> bool:
        stmt = (update(Deal)
                .where(Deal.order_id == order_id)
                .where(Deal.user_id == user_id)
                .where(Deal.status == from_status)
                .values(status = new_status.value)) 
        res = await self._session.execute(stmt)
        await self._session.flush()
        return res.rowcount > 0
    
    async def mark_as_failed(self, order_id : UUID, user_id: UUID) -> bool:
        return await self._change_status(order_id=order_id, user_id=user_id, from_status=DealStatus.in_progress, new_status=DealStatus.failed)
    
    async def mark_as_completed(self, order_id : UUID, user_id: UUID) -> bool:
        return await self._change_status(order_id=order_id, user_id=user_id, from_status=DealStatus.in_progress,new_status=DealStatus.completed)

    