from dataclasses import dataclass
from uuid import UUID
@dataclass
class DealInDTO:
    order_id: UUID
    user_id: UUID

