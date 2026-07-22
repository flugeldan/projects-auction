from src.application.interfaces.deal_repository import AbstractDealRepository
from src.application.interfaces.transaction_repository import AbstractTransactionRepository
from src.application.interfaces.transaction_manager import AbstractTransactionManager
from src.application.interfaces.order_repository import AbstractOrderRepository
from src.application.interfaces.user_repository import AbstractUserRepository
from src.application.dto.order_reward_in_dto import TakeOrderRewardDTO
from src.application.dto.order_reward_out_dto import OrderRewardOutDTO

from src.domain.entities.transaction import Transaction, TransactionType, Direction
from src.domain.service.reward_service import RewardService
from src.domain.exceptions import DealNotFoundError, UserNotFoundError
from uuid import UUID

class TakeOrderRewardInteractor:
    def __init__(
            self,
            deal_repo: AbstractDealRepository,
            transaction_repo: AbstractTransactionRepository,
            user_repo: AbstractUserRepository,
            order_repo: AbstractOrderRepository,
            transaction_manager: AbstractTransactionManager,
            reward_service: RewardService):
        self._deal_repo = deal_repo
        self._transaction_repo = transaction_repo
        self._user_repo = user_repo
        self._order_repo = order_repo
        self._transaction_manager = transaction_manager
        self._reward_service = reward_service
    
    async def execute(self, take_order_reward_dto: TakeOrderRewardDTO) -> OrderRewardOutDTO:
        async with self._transaction_manager:
            deal = await self._deal_repo.get_by_order_and_user(order_id=take_order_reward_dto.order_id,
                                                               user_id=take_order_reward_dto.user_id)
            if not deal:
                raise DealNotFoundError
            user = await self._user_repo.get_by_id(user_id=take_order_reward_dto.user_id)
            if not user:
                raise UserNotFoundError
            deal.complete()
            self._reward_service.reward_for_order(user=user,
                                 deal=deal)
            transaction = Transaction.create(
                user_id=user.id,
                amount=deal.calculated_money_reward,
                transaction_type=TransactionType.order_reward,
                direction=Direction.income,
                target_id=take_order_reward_dto.order_id
            )

            await self._transaction_repo.save(transaction=transaction)

            #возможно уберу, они изза identity map алхимии ниче не сохраняет в репо 
            await self._deal_repo.update(deal=deal)
            await self._user_repo.update(user=user)

            return OrderRewardOutDTO(
                order_id=take_order_reward_dto.order_id,
                user_id=user.id,
                money_reward= deal.calculated_money_reward,
                exp_reward=deal.calculated_exp_reward
            )



            
            

            
