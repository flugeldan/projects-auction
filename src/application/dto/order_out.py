from dataclasses import dataclass, field
from uuid import UUID
@dataclass
class OrderOutDTO:
    id: UUID
    name: str
    description: str
    work_units_to_complete: int
    exp_reward: int | None = None
    money_reward: int | None = None
    employees_to_outsource: dict[str, int] = field(default_factory=dict)


    
