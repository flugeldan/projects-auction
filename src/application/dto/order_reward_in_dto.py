from dataclasses import dataclass
from uuid import UUID

@dataclass
class TakeOrderRewardDTO:
    order_id: UUID
    user_id: UUID
