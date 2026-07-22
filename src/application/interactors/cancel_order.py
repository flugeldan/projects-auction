from src.application.interfaces.user_repository import AbstractUserRepository
from src.application.interfaces.deal_repository import AbstractDealRepository
from src.application.interfaces.employee_repository import AbstractEmployeeRepository
from src.application.interfaces.transaction_manager import AbstractTransactionManager
from src.application.dto.cancel_order_dto import CancelOrderDTO
from src.domain.entities.user import User
from src.domain.entities.order import Order
from src.domain.entities.deal import Deal, DealStatus
from src.domain.service.order_assignment import OrderAssignmentService
from src.domain.exceptions import DealNotFoundOrCannotBeFailedError, DealNotFoundError
from uuid import UUID
class CancelOrderInteractor:
    def __init__(
            self, 
             deal_repo: AbstractDealRepository,
             emp_repo: AbstractEmployeeRepository,
             transaction_manager: AbstractTransactionManager,
             order_assignment_service: OrderAssignmentService
    ):
        self._deal_repo = deal_repo
        self._emp_repo = emp_repo
        self._transaction_manager = transaction_manager
        self._order_assignment_service = order_assignment_service

    async def execute(self, cancel_order_dto: CancelOrderDTO) -> None:
        async with self._transaction_manager:
            deal = await self._deal_repo.get_by_order_and_user(user_id=cancel_order_dto.user_id,
                                                                order_id=cancel_order_dto.order_id)
            if not deal:
                raise DealNotFoundError
            deal.cancel()
            await self._emp_repo.bulk_set_free_by_user_id_and_order_id(user_id=cancel_order_dto.user_id,
                                                                       order_id=cancel_order_dto.order_id)
            


            





