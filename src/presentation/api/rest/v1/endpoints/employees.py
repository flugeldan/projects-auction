from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.presentation.api.rest.v1.schemas.employee import EmployeeResponse, EmployeeTypeSchema
from src.presentation.api.rest.v1.dependencies.auth import get_current_user, CurrentUser

from src.di.providers.app_provider import GetAvailableEmployeesInteractor, GetAllEmployeesInteractor

from dishka.integrations.fastapi import FromDishka, inject

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get('/all', status_code=status.HTTP_200_OK, response_model=list[EmployeeResponse])
@inject
async def get_all_employees(
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    interactor: FromDishka[GetAllEmployeesInteractor]
) -> list[EmployeeResponse]:
    all_employees = await interactor.execute(user_id=current_user.id)

    return [EmployeeResponse(
        id=emp.id,
        user_id=emp.user_id,
        work_points=emp.work_points,
        busy_until=emp.busy_until,
        current_order_id=emp.current_order_id,
        employee_type=EmployeeTypeSchema(emp.employee_type)
    ) for emp in all_employees]


@router.get('/available', status_code=status.HTTP_200_OK, response_model=list[EmployeeResponse])
@inject
async def get_available_employees_endpoint(
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    interactor: FromDishka[GetAvailableEmployeesInteractor]
) -> list[EmployeeResponse]:
    available_employees = await interactor.execute(user_id=current_user.id)

    return [EmployeeResponse(
        id=emp.id,
        user_id=emp.user_id,
        work_points=emp.work_points,
        busy_until=emp.busy_until,
        current_order_id=emp.current_order_id,
        employee_type=EmployeeTypeSchema(emp.employee_type)
    ) for emp in available_employees]




