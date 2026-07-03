from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID
from employee import EmployeeType
from domain.exceptions import OrderAlreadyTakenError

@dataclass
class TestCase:
    method: str
    path: str
    expected_status: int

    def __post_init__(self):
        if self.method not in ("GET", "POST", "PUT", "DELETE", "PATCH"):
            raise ValueError(f"Invalid method: {self.method}")
        if not (100 <= self.expected_status < 600):
            raise ValueError(f"Invalid status code: {self.expected_status}")
        if not self.path or not self.path.startswith("/"):
            raise ValueError(f"Invalid path: {self.path}")

@dataclass
class Order:
    id: UUID
    name: str
    description: str
    time_to_complete: int
    exp_reward: int = 0
    money_reward: int = 0
    is_available: bool = True
    required_employees: dict[EmployeeType, int] = field(default_factory=dict)
    test_cases: list[TestCase] = field(default_factory=list)
    api_address: str = "localhost:8000"

    def __post_init__(self):
        if self.time_to_complete <= 0:
            raise ValueError("Time to complete must be positive")
        if self.exp_reward < 0:
            raise ValueError("Exp reward can not be negative")
        if self.money_reward < 0:
            raise ValueError("Money reward can not be negative")
        if not self.required_employees:
            raise ValueError("You must require some employees!")
        if not self.test_cases:
            raise ValueError("You must provide test cases to validate api")
    
    def reserve(self) -> None:
        if not self.is_available:
            raise OrderAlreadyTakenError()
        self.is_available = False
