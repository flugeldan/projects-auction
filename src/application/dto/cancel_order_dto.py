from dataclasses import dataclass
from uuid import UUID
@dataclass
class CancelOrderDTO:
    order_id: UUID
    user_id: UUID


