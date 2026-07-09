from sqlalchemy.ext.asyncio import AsyncSession
from application.interfaces.employee_repository import AbstractEmployeeRepository
from domain.entities.employee import Employee
class SQLAlchemyEmployeeRepository(AbstractEmployeeRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def ge

    def batch_save(employees: list[Employee]) -> None:

    
    