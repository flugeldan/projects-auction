from sqlalchemy.ext.asyncio import AsyncSession
from application.interfaces.employee_repository import AbstractEmployeeRepository

class SQLAlchemyEmployeeRepository(AbstractEmployeeRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
    
    