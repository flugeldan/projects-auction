from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from enum import Enum

class EmployeeTypeSchema(str, Enum):
    developer = "developer"
    designer = "designer"
    manager = "manager"
    analyst = "analyst"

class EmployeeResponse(BaseModel):
    id: UUID
    user_id: UUID
    work_points: int
    employee_type: EmployeeTypeSchema
    busy_until: datetime | None
    current_order_id: UUID | None

    model_config = ConfigDict(from_attributes=True)
