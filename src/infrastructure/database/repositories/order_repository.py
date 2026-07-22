from sqlalchemy.ext.asyncio import AsyncSession
from src.application.interfaces.order_repository import AbstractOrderRepository
from src.domain.entities.order import Order
from src.domain.entities.deal import Deal, DealStatus
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, func, or_, and_, literal
from src.domain.exceptions import OrderAlreadyExistsError
from uuid import UUID

class SQLAlchemyOrderRepository(AbstractOrderRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def get_by_id(self, order_id: UUID) -> Order | None:
        return await self._session.get(Order, order_id)
    
    
    async def save(self, order: Order) -> None:
        self._session.add(order)
        try:
            await self._session.flush()
        except IntegrityError as e:
            raise OrderAlreadyExistsError(order.id) from e

    async def update(self, order: Order) -> None:
        pass
    
    async def get_available(self) -> list[Order]:
        active_completed_orders = (select(literal(1))
                                   .where(and_(Deal.order_id == Order.id,
                                               Deal.status.in_([DealStatus.completed, DealStatus.in_progress]))
                                               )
                                   .correlate(Order))
        stmt = (select(Order)
                .where(~active_completed_orders.exists()))
        
        res = await self._session.execute(stmt)
        return res.scalars().all()
    