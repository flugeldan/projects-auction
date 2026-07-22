from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID
from src.domain.entities.employee import EmployeeType
from src.domain.exceptions import OrderAlreadyTakenError
from enum import Enum

class AssignmentMode(str, Enum):
    SINGLE = "single"
    SHARED = "shared"

@dataclass
class Order:
    id: UUID
    name: str
    description: str
    work_units_to_complete: int
    exp_reward: int = 0
    money_reward: int = 0
    employees_to_outsource: dict[EmployeeType, int] = field(default_factory=dict)

    def __post_init__(self):
        if self.exp_reward < 0:
            raise ValueError("Exp reward can not be negative")
        if self.money_reward < 0:
            raise ValueError("Money reward can not be negative")
        if self.work_units_to_complete <= 0:
            raise ValueError("Must set work units to complete")
