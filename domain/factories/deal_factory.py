from domain.entities.employee import Employee
from domain.entities.user import User
from domain.entities.order import Order
from domain.entities.deal import Deal
from datetime import datetime, timezone, timedelta
from uuid import UUID, uuid4
class DealFactory:
    @staticmethod
    def create(order: Order, user_id: UUID):
        deal_id = uuid4()
        return Deal(id=deal_id,
                    order_id=order.id,
                    started_at= datetime.now(timezone.utc),
                    deadline= datetime.now(timezone.utc) + timedelta(minutes=order.time_to_complete))


