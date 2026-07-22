from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.presentation.api.rest.v1.schemas.deal import TakeOrderRequest, TakeOrderResponse, CancelOrderRequest, TakeOrderRewardRequest
from src.presentation.api.rest.v1.schemas.order import OrderRewardResponse, OrderResponse
from src.presentation.api.rest.v1.dependencies.auth import CurrentUser, get_current_user
from src.application.dto.take_order_in_dto import TakeOrderInDTO
from src.application.dto.take_order_out_dto import TakeOrderOutDTO
from src.application.dto.order_reward_in_dto import TakeOrderRewardDTO
from src.application.dto.cancel_order_dto import CancelOrderDTO
from src.di.providers.app_provider import TakeOrderInteractor, CancelOrderInteractor, TakeOrderRewardInteractor, GetAssignedOrdersInteractor, GetAvailableOrdersInteractor


from dishka.integrations.fastapi import FromDishka, inject

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post('/take', status_code=status.HTTP_200_OK, response_model=TakeOrderResponse)
@inject
async def take_order_endpoint(
    body: TakeOrderRequest,
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    interactor: FromDishka[TakeOrderInteractor],
) -> TakeOrderResponse:
    
    take_order_in_dto = TakeOrderInDTO(
        user_id=current_user.id,
        order_id=body.order_id,
        worker_protocol="REST",
        with_user=body.with_user,
        employees_to_assign=body.employees_to_assign)
    
    take_order_out_dto = await interactor.execute(take_order_in_dto=take_order_in_dto)
    return TakeOrderResponse(
        id=take_order_out_dto.id,
        order_id=take_order_out_dto.order_id,
        user_id=take_order_out_dto.user_id,
        started_at=take_order_out_dto.started_at,
        with_user=take_order_out_dto.with_user,
        worker_protocol=take_order_out_dto.worker_protocol,
        work_units_to_complete=take_order_out_dto.work_units_to_complete,
        work_units_per_tick=take_order_out_dto.work_units_per_tick,
        will_end_at=take_order_out_dto.will_end_at,
        status=take_order_out_dto.status,
        calculated_money_reward=take_order_out_dto.calculated_money_reward,
        calculated_exp_reward=take_order_out_dto.calculated_exp_reward
    )

@router.post('/cancel', status_code=status.HTTP_204_NO_CONTENT)
@inject
async def cancel_order_endpoint(
    body: CancelOrderRequest,
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    interactor: FromDishka[CancelOrderInteractor]
):
    cancel_order_dto = CancelOrderDTO(
        order_id=body.order_id,
        user_id=current_user.id
    )
    
    await interactor.execute(cancel_order_dto=cancel_order_dto)

@router.post('/reward', status_code=status.HTTP_200_OK, response_model=OrderRewardResponse)
@inject
async def take_reward_endpoint(
    body: TakeOrderRewardRequest,
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    interactor: FromDishka[TakeOrderRewardInteractor]
):
    take_order_reward_dto = TakeOrderRewardDTO(
        order_id=body.order_id,
        user_id=current_user.id
    )

    order_reward_out_dto = await interactor.execute(take_order_reward_dto=take_order_reward_dto)
    return OrderRewardResponse(
        order_id=order_reward_out_dto.order_id,
        user_id=order_reward_out_dto.user_id,
        money_reward=order_reward_out_dto.money_reward,
        exp_reward=order_reward_out_dto.exp_reward)

@router.get('/assigned', status_code=status.HTTP_200_OK, response_model=list[OrderResponse])
@inject
async def get_assigned_orders_endpoint(
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    interactor: FromDishka[GetAssignedOrdersInteractor]
):
    assigned_orders = await interactor.execute(user_id=current_user.id)

    return [OrderResponse(
        id=order.id,
        name=order.name,
        description=order.description,
        work_units_to_complete=order.work_units_to_complete,
        exp_reward=order.exp_reward,
        money_reward=order.money_reward,
        employees_to_outsource=order.employees_to_outsource
    ) for order in assigned_orders]

@router.get('/available', status_code=status.HTTP_200_OK, response_model=list[OrderResponse])
@inject
async def get_available_orders_endpoint(
    interactor: FromDishka[GetAvailableOrdersInteractor]
):
    available_orders = await interactor.execute()

    return [OrderResponse(
        id=order.id,
        name=order.name,
        description=order.description,
        work_units_to_complete=order.work_units_to_complete,
        exp_reward=order.exp_reward,
        money_reward=order.money_reward,
        employees_to_outsource=order.employees_to_outsource
    ) for order in available_orders]

