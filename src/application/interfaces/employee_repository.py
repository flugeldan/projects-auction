from abc import ABC, abstractmethod
from uuid import UUID
from domain.entities.employee import Employee
class AbstractEmployeeRepository(ABC):
    @abstractmethod
    async def get_by_id(self, employee_id: UUID) -> Employee | None:
        ...

    @abstractmethod
    async def get_by_user_id(self, user_id: UUID) -> list[Employee]:
        ...
    
    @abstractmethod
    async def get_available_by_user_id(self) -> list[Employee] | None:
        ...
        
    @abstractmethod
    async def bulk_save(self, employees: list[Employee]) -> None:
        ...

    @abstractmethod
    async def save(self, employee: Employee) -> None:
        ...
    

    