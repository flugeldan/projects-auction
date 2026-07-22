from dataclasses import dataclass
from uuid import UUID
from datetime import datetime, timezone, timedelta
from enum import Enum
from src.domain.exceptions import EmployeeAlreadyBusyError

class EmployeeType(str, Enum):
    DEVELOPER = "developer"
    DESIGNER = "designer"
    MANAGER = "manager"
    ANALYST = "analyst"

@dataclass
class Employee:
    id: UUID
    user_id: UUID
    work_points: int
    employee_type: EmployeeType
    busy_until: datetime | None = None
    current_order_id: UUID | None = None

    def start_work(self, busy_until: datetime, order_id: UUID):
        if self.is_busy:
            raise EmployeeAlreadyBusyError()
        self.busy_until = busy_until
        self.current_order_id = order_id
    
    def stop_work(self) -> None:
        self.busy_until = None
        self.current_order_id = None

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'work_points': self.work_points,
            'employee_type': self.employee_type,
            'busy_until': self.busy_until,
            'current_order_id': self.current_order_id
        }
    
    @property
    def is_busy(self) -> bool:
        if self.busy_until is None:
            return False
        return datetime.now(timezone.utc) < self.busy_until
    
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

