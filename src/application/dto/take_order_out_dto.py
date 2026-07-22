from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from src.domain.entities.deal import DealStatus, Deal

@dataclass
class TakeOrderOutDTO:
    id: UUID
    order_id: UUID
    user_id: UUID
    started_at: datetime
    with_user: bool

    worker_protocol: str
    work_units_to_complete: int
    will_end_at: datetime | None
    status: str
    calculated_money_reward: int
    calculated_exp_reward: int
    work_units_per_tick: int = 0  