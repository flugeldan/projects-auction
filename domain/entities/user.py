from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timezone
from uuid import UUID
from domain.entities.employee import Employee
class AccountStatus(str, Enum):
    deleted = "deleted"
    active = "active"
    banned = "banned"

class AccountSubscription(str, Enum):
    normal = "normal"
    vip = "vip"
    premium = "premium"

class AccountRole(str, Enum):
    player = "player"
    admin = "admin"

@dataclass
class User: #игрок
    id: UUID
    email: str
    username: str
    hashed_password: str 
    joined_at: datetime = lambda: datetime.now(timezone.utc)
    in_game_currency: int = 0
    lvl: int = 1
    role: AccountRole = AccountRole.player
    experience: int = 0
    subscription: AccountSubscription = AccountSubscription.normal
    employees: list[Employee] = field(default_factory=list) #на стадии билдера будем создавать работников 

    def reward(self, exp_reward: int, money_reward: int):
        self.in_game_currency += money_reward
        self.experience += exp_reward



    



