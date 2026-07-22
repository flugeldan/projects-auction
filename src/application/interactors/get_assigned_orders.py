from src.application.interfaces.user_repository import AbstractUserRepository
from src.application.interfaces.deal_repository import AbstractDealRepository
from src.application.interfaces.transaction_manager import AbstractTransactionManager
from src.application.dto.order_out import OrderOutDTO
from src.domain.entities.order import Order
from uuid import UUID

class GetAssignedOrdersInteractor:
    def __init__(
            self, 
            deal_repo: AbstractDealRepository,
            transaction_manager: AbstractTransactionManager):
        self._deal_repo = deal_repo
        self._transaction_manager = transaction_manager
    
    async def execute(self, user_id: UUID) -> list[OrderOutDTO]:
        async with self._transaction_manager:
            orders = await self._deal_repo.get_all_in_progress_by_user(user_id=user_id)

            return [OrderOutDTO(
                id=order.id,
                work_units_to_complete=order.work_units_to_complete,
                name=order.name,
                description=order.description,
                exp_reward=order.exp_reward,
                money_reward=order.money_reward,
                employees_to_outsource=order.employees_to_outsource
            ) for order in orders]
        