from uuid import UUID
from sqlalchemy import select, update, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert as pg_insert  #

from src.application.interfaces.employee_repository import AbstractEmployeeRepository
from src.domain.entities.employee import Employee
from src.domain.exceptions import EmployeeAlreadyExistsError 
from datetime import datetime, timezone


class SQLAlchemyEmployeeRepository(AbstractEmployeeRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, employee_id: UUID) -> Employee | None:
        return await self._session.get(Employee, employee_id)
    
    async def get_by_user_id(self, user_id: UUID) -> list[Employee]:
        stmt = (select(Employee)
                .where(Employee.user_id == user_id))
        res = await self._session.execute(stmt)
        employees = res.scalars().all()
        return employees
    
    async def get_by_ids(self, employee_ids: list[UUID]) -> list[Employee]:
        emp_ids = set(employee_ids)
        stmt = (select(Employee)
                .where(Employee.id.in_(emp_ids)))
        res = await self._session.execute(stmt)
        return res.scalars().all()
        
    
    async def get_by_user_id_free(self, user_id: UUID) -> list[Employee]:
        now = datetime.now(timezone.utc)
        stmt = (select(Employee)
                .where(Employee.user_id == user_id)
                .where(or_(Employee.busy_until.is_(None), Employee.busy_until < now)))
        res = await self._session.execute(stmt)
        employees = res.scalars().all()
        return employees
    
    async def get_ids_by_user_id_free(self, user_id: UUID) -> set[Employee]:
        now = datetime.now(timezone.utc)
        stmt = (select(Employee)
                .where(Employee.user_id == user_id)
                .where(or_(Employee.busy_until.is_(None), Employee.busy_until < now)))
        res = await self._session.execute(stmt)
        employees = res.scalars().all()

        return set([emp.id for emp in employees])
    
    async def save(self, employee: Employee) -> None:
        self._session.add(employee)
        try:
            await self._session.flush()
        except IntegrityError as e:
            raise EmployeeAlreadyExistsError(employee.id) from e

    async def update(self, employee: Employee) -> None:
        pass
    
    async def bulk_select(self, user_id: UUID) -> set[Employee]:
        stmt = (select(Employee)
                .where(and_(Employee.user_id == user_id, Employee.work_points == 0))
                .with_for_update())
        
        res = await self._session.execute(stmt)
        employees = set(res.scalars().all())
        return employees
    
    async def bulk_save(self, employees: list[Employee]) -> None:
        emps_to_insert = [emp.to_dict() for emp in employees]
        stmt = pg_insert(Employee).values(emps_to_insert)
        upsert_stmt = stmt.on_conflict_do_update(index_elements=['id'],
                                                     set_={'work_points': stmt.excluded.work_points})
        await self._session.execute(upsert_stmt)
        await self._session.flush()

    async def bulk_set_busy(self, user_id: UUID, emp_ids: set[UUID], busy_until: datetime) -> None:
        stmt = (update(Employee)
                .where(
                    and_(Employee.user_id == user_id, Employee.id.in_(emp_ids))
                    )
                .values(busy_until=busy_until))
        await self._session.execute(stmt)
        await self._session.flush()
    
    async def bulk_set_free_by_user_id_and_order_id(self, user_id: UUID, order_id: UUID) -> None:
        stmt = (update(Employee)
                .where(Employee.user_id == user_id)
                .where(Employee.current_order_id == order_id)
                .values(busy_until = None,
                        current_order_id = None))
        await self._session.execute(stmt)

    
    