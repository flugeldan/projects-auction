from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from src.domain.entities.employee import EmployeeType

@dataclass
class EmployeeOutDTO:
    id: UUID
    user_id: UUID
    work_points: int
    employee_type: EmployeeType
    busy_until: datetime | None
    current_order_id: UUID | None