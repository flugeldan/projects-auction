from pydantic import BaseModel, ConfigDict
from uuid import UUID
from src.application.dto.order_out import OrderOutDTO

class OrderResponse(BaseModel):
    id: UUID
    name: str
    description: str
    work_units_to_complete: int 
    exp_reward: int
    money_reward: int
    employees_to_outsource: dict[str, int]

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_dto(cls, dto: OrderOutDTO) -> "OrderResponse":
        return cls(
            id=dto.id,
            name=dto.name,
            description=dto.description,
            work_units_to_complete=dto.work_units_to_complete,
            exp_reward=dto.exp_reward if dto.exp_reward is not None else 0,
            money_reward=dto.money_reward if dto.money_reward is not None else 0,
            employees_to_outsource=dto.employees_to_outsource
        )

class OrderRewardResponse(BaseModel):
    order_id: UUID
    user_id: UUID
    money_reward: int
    exp_reward: int

    model_config = ConfigDict(from_attributes=True)

