from abc import ABC, abstractmethod
from uuid import UUID
from src.domain.entities.employee import Employee
class AbstractEmployeeRepository(ABC):
    @abstractmethod
    async def get_by_id(self, employee_id: UUID) -> Employee | None:
        ...

    @abstractmethod
    async def get_by_user_id(self, user_id: UUID) -> list[Employee]:
        ...
    
    @abstractmethod
    async def get_by_user_id_free(self, user_id: UUID) -> list[Employee]:
        ...
    
    @abstractmethod
    async def get_ids_by_user_id_free(self, user_id: UUID) -> set[Employee]:
        ...
    
    @abstractmethod
    async def bulk_set_free_by_user_id_and_order_id(self, user_id: UUID, order_id: UUID) -> None:
        ...
    
    @abstractmethod
    async def bulk_select(self, user_id: UUID) -> list[Employee]:
        ...
    
    @abstractmethod
    async def get_by_ids(self, employee_ids: list[UUID]) -> list[Employee]:
        ...
        
    @abstractmethod
    async def bulk_save(self, emps: list[Employee]) -> None:
        ...
    
    @abstractmethod
    async def bulk_set_busy(self, user_id: UUID, emp_ids: set[UUID], units_of_work: int) -> None:
        ...

    @abstractmethod
    async def save(self, employee: Employee) -> None:
        ...

    @abstractmethod
    async def update(self, employee: Employee) -> None:
        ...
    

    