from dataclasses import dataclass
from uuid import UUID
from datetime import datetime, timezone, timedelta
from enum import Enum
from domain.exceptions import EmployeeAlreadyBusy

class EmployeeType(str, Enum):
    DEVELOPER = "developer"
    DESIGNER = "designer"
    MANAGER = "manager"
    ANALYST = "analyst"

@dataclass
class Employee:
    id: UUID
    player_id: UUID
    is_busy: bool = False
    busy_until: datetime | None = None

    def start_work(self, minutes_to_work: int):
        if self.is_busy:
            raise EmployeeAlreadyBusy()
        self.is_busy = True
        self.busy_until = datetime.now(timezone.utc) + timedelta(minutes=minutes_to_work)


@dataclass
class Developer(Employee):
    pass

@dataclass
class Analyst(Employee):
    pass

@dataclass
class Designer(Employee):
    pass

@dataclass
class Manager(Employee):
    pass

