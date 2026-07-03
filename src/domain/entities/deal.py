from dataclasses import dataclass
from uuid import UUID
from enum import Enum
from datetime import datetime, timezone, timedelta
from domain.entities.order import Order
class DealStatus(str, Enum):
    in_progress = "in_progress"
    completed = "completed"
    failed = "failed"

@dataclass
class Deal:
    id: UUID
    order_id: UUID
    user_id: UUID
    started_at: datetime
    status: DealStatus.in_progress 
    deadline: datetime

    @staticmethod
    def create(order: Order, user_id: UUID) -> "Deal":
        deal_id = uuid4()
        return Deal(id=deal_id,
                    order_id=order.id,
                    started_at= datetime.now(timezone.utc),
                    deadline= datetime.now(timezone.utc) + timedelta(minutes=order.time_to_complete))

