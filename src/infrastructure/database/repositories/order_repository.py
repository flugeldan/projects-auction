from sqlalchemy.ext.asyncio import AsyncSession
from application.interfaces.order_repository import AbstractOrderRepository
from domain.entities.order import Order
from domain.entities.deal import Deal, DealStatus
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, func, outerjoin, or_, and_
from sqlalchemy.orm import aliased
from domain.exceptions import OrderAlreadyExistsError

class SQLAlchemyOrderRepository(AbstractOrderRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def get_by_id(self, order_id) -> Order | None:
        return await self._session.get(Order, order_id)
    
    async def save(self, order: Order) -> None:
        self._session.add(order)
        try:
            await self._session.flush()
        except IntegrityError as e:
            raise OrderAlreadyExistsError(order.id) from e
    
    async def get_available(self) -> list[Order]:
        row_numming = (
            func.row_number().over(partition_by=Order.id, order_by=Deal.started_at.desc())
            .label("num"))

        row_num = (
            select(Order, Deal.status.label("status"), row_numming)
            .outerjoin(Deal, Deal.order_id == Order.id)
            .subquery())

        orm_map = aliased(Order, row_num)

        stmt = select(orm_map).where(row_num.c.num == 1,
                                     or_(row_num.c.status == DealStatus.failed, row_num.c.status.is_(None)))
        
        result = await self._session.execute(stmt)
        return list(result.scalars().all())
    