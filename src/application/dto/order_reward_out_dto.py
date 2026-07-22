from dataclasses import dataclass
from uuid import UUID

@dataclass
class OrderRewardOutDTO:
    order_id: UUID
    user_id: UUID
    money_reward: int
    exp_reward: int

