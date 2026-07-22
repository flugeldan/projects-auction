from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class TakeOrderRequest(BaseModel):
    order_id: UUID
    with_user: bool
    employees_to_assign: list[UUID]

    model_config = ConfigDict(from_attributes=True)


class TakeOrderResponse(BaseModel):
    id: UUID
    order_id: UUID
    user_id: UUID
    started_at: datetime
    with_user: bool
    worker_protocol: str
    work_units_to_complete: int
    work_units_per_tick: int
    will_end_at: datetime
    status: str
    calculated_money_reward: int
    calculated_exp_reward: int

    model_config = ConfigDict(from_attributes=True)

class CancelOrderRequest(BaseModel):
    order_id: UUID

    model_config = ConfigDict(from_attributes=True)

class TakeOrderRewardRequest(BaseModel):
    order_id: UUID
    
    model_config = ConfigDict(from_attributes=True)
