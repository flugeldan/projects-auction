from src.application.interfaces.user_repository import AbstractUserRepository
from src.application.interfaces.deal_repository import AbstractDealRepository
from src.application.interfaces.order_repository import AbstractOrderRepository
from src.application.interfaces.transaction_manager import AbstractTransactionManager
from src.application.dto.order_out import OrderOutDTO
from src.domain.entities.order import Order

class GetAvailableOrdersInteractor:
    def __init__(
            self, 
            order_repo: AbstractOrderRepository,
            transaction_manager: AbstractTransactionManager):
        self._order_repo = order_repo
        self._transaction_manager = transaction_manager
    
    async def execute(self) -> list[OrderOutDTO]:
        async with self._transaction_manager:
            orders = await self._order_repo.get_available()

            return [OrderOutDTO(
                id=order.id,
                name=order.name,
                description=order.description,
                work_units_to_complete=order.work_units_to_complete,  # Напрямую из домена
                exp_reward=order.exp_reward,
                money_reward=order.money_reward,
                employees_to_outsource={
                    k.value if hasattr(k, 'value') else str(k): v 
                    for k, v in order.employees_to_outsource.items()
                }
            ) for order in orders]