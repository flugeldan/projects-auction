from src.domain.entities.deal import Deal
from src.domain.entities.user import User
from src.domain.exceptions import InvalidDealStatusError
from uuid import UUID
from datetime import datetime, timezone

class RewardService:
    def reward_for_order(
            self,
            user: User,
            deal: Deal) -> None:
        now = datetime.now(timezone.utc)
        user.balance += deal.calculated_money_reward
        user.experience += deal.calculated_exp_reward
        
        