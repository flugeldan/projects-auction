from dataclasses import dataclass, field
from uuid import UUID

@dataclass(frozen=True)
class TakeOrderInDTO:
    order_id: UUID
    user_id: UUID
    with_user: bool
    worker_protocol: str
    employees_to_assign: list[UUID] = field(default_factory=list)
