from src.application.interfaces.employee_repository import AbstractEmployeeRepository
from src.application.interfaces.transaction_manager import AbstractTransactionManager
from src.application.dto.employee_out import EmployeeOutDTO
from uuid import UUID
class GetAllEmployeesInteractor:
    def __init__(
            self, 
            emp_repo: AbstractEmployeeRepository,
            transaction_manager: AbstractTransactionManager
            ):
        self._emp_repo = emp_repo
        self._transaction_manager = transaction_manager
    
    async def execute(self, user_id: UUID) -> list[EmployeeOutDTO]:
        async with self._transaction_manager:
            employees = await self._emp_repo.get_by_user_id(user_id=user_id)
            return [EmployeeOutDTO(
                id=emp.id,
                user_id=emp.user_id,
                work_points=emp.work_points,
                busy_until=emp.busy_until,
                employee_type=emp.employee_type,
                current_order_id=emp.current_order_id
                ) for emp in employees]
        

        