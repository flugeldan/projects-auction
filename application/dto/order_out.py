from dataclasses import dataclass, field
from domain.entities.employee import EmployeeType
from uuid import UUID
@dataclass
class OrderOutDTO:
    id: UUID
    name: str
    description: str
    time_to_complete: int
    exp_reward: int | None = None
    money_reward: int | None = None
    required_employees: dict[str, int] = field(default_factory=dict)
    test_cases: list[dict] = field(default_factory=list)
    api_address: str = "localhost:8000"



    
