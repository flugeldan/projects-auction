from dataclasses import dataclass
from src.domain.entities.employee import Employee
from src.domain.entities.order import Order
from src.domain.exceptions import EmployeeNotFoundError, EmployeeAlreadyBusyError, EmployeeAccessDeniedError
from uuid import UUID
from typing import Self
import math
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from uuid import UUID

@dataclass(frozen=True) 
class EmployeeTeam:
    employees: list[Employee]
    order: Order
    with_user: bool

    def validate_all_free_and_belong_to(
        self, 
        user_id: UUID,
        requested_ids: list[UUID]
    ) -> None:
        found_ids = {emp.id for emp in self.employees}
        
        missing_ids = set(requested_ids) - found_ids
        if missing_ids:
            raise EmployeeNotFoundError(f"Missing IDs: {missing_ids}")
            
        for emp in self.employees:
            if emp.id in requested_ids:
                if emp.user_id != user_id:
                    raise EmployeeAccessDeniedError()
                
                if emp.is_busy:
                    raise EmployeeAlreadyBusyError()
        

    @property
    def total_work_points(self) -> int:
        return sum(emp.work_points for emp in self.employees)

    @property
    def calculate_busy_until(self) -> datetime:
        return datetime.now(timezone.utc) + timedelta(
            minutes=math.ceil(self.order.work_units_to_complete / (self.total_work_points + self.with_user)))