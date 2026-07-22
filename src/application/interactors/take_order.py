from src.application.interfaces.user_repository import AbstractUserRepository
from src.application.interfaces.deal_repository import AbstractDealRepository
from src.application.interfaces.order_repository import AbstractOrderRepository
from src.application.interfaces.employee_repository import AbstractEmployeeRepository
from src.application.interfaces.transaction_manager import AbstractTransactionManager
from src.application.dto.take_order_in_dto import TakeOrderInDTO
from src.application.dto.take_order_out_dto import TakeOrderOutDTO
from src.domain.entities.user import User
from src.domain.entities.order import Order
from src.domain.entities.deal import Deal, DealStatus
from src.domain.value_objects.team import EmployeeTeam
from src.domain.service.order_assignment import OrderAssignmentService
from src.domain.exceptions import UserNotFoundError, DealAlreadyCompletedError, DealAlreadyFailedError, DealNotFoundError
from src.domain.exceptions import OrderNotFoundError, OrderAlreadyTakenError
from uuid import UUID
class TakeOrderInteractor:
    def __init__(self, 
             user_repo: AbstractUserRepository, 
             deal_repo: AbstractDealRepository,
             order_repo: AbstractOrderRepository,
             emp_repo: AbstractEmployeeRepository,
             transaction_manager: AbstractTransactionManager,
             order_assignment_service: OrderAssignmentService
    ):
        self._deal_repo = deal_repo
        self._order_repo = order_repo
        self._emp_repo = emp_repo
        self._transaction_manager = transaction_manager
        self._order_assignment_service = order_assignment_service
    
    async def execute(self, take_order_in_dto: TakeOrderInDTO) -> TakeOrderOutDTO:
        async with self._transaction_manager:            
            order = await self._order_repo.get_by_id(order_id=take_order_in_dto.order_id)
            if not order:
                raise OrderNotFoundError
            
            if take_order_in_dto.with_user:
                personal_deals = await self._deal_repo.get_by_id_personal_deals(user_id=take_order_in_dto.user_id)
                self._order_assignment_service.validate_user_can_take_deal(
                    active_personal_deals_count=len(personal_deals)
                )
            
            emps = await self._emp_repo.get_by_ids(take_order_in_dto.employees_to_assign)
            team = EmployeeTeam(employees=emps,
                                order=order,
                                with_user=take_order_in_dto.with_user)
            team.validate_all_free_and_belong_to(
                user_id=take_order_in_dto.user_id,
                requested_ids=take_order_in_dto.employees_to_assign
            )
            self._order_assignment_service.assign_employees(team=team)

            deal = Deal.create(
                order_id=order.id,
                user_id=take_order_in_dto.user_id,
                with_user=take_order_in_dto.with_user,
                worker_protocol=take_order_in_dto.worker_protocol,
                work_units_to_complete=order.work_units_to_complete,
                calculated_money_reward=order.money_reward,
                calculated_exp_reward=order.exp_reward)
            
            deal.assign_team(
                team=team
            )

            
            await self._deal_repo.save(deal)
            await self._emp_repo.bulk_save(team.employees)

            return TakeOrderOutDTO(
                id=deal.id,
                order_id=order.id,
                user_id=deal.user_id,
                started_at=deal.started_at,
                with_user=deal.with_user,
                worker_protocol=deal.worker_protocol,
                work_units_to_complete=deal.work_units_to_complete,
                work_units_per_tick=deal.work_units_per_tick,
                will_end_at=deal.will_end_at,
                status=deal.status,
                calculated_money_reward=deal.calculated_money_reward,
                calculated_exp_reward=deal.calculated_exp_reward,
            )