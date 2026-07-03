from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from domain.entities.deal import DealStatus, Deal

@dataclass
class OrderOutDTO:
    id: UUID
    name: str
    description: str
    time_to_complete: int
    money_reward: int 
    is_available: bool
    required_employees: dict[str, int]
    test_cases: list[dict]
    api_address: str
