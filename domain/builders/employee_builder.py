from domain.entities.employee import Employee, Designer, Developer, Manager, Analyst
from uuid import UUID, uuid4
_BASIC_EMPLOYEE_TYPES = (Designer, Manager, Analyst, Developer)

class EmployeeBuilder:
    @staticmethod
    def build_basic_set(user_id: UUID) -> list[Employee]:
        return [emp(id = uuid4(),user_id=user_id) for emp in _BASIC_EMPLOYEE_TYPES]



