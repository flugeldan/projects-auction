from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timezone
from uuid import UUID
from src.domain.entities.employee import Employee
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
class User:
    id: UUID
    email: str
    username: str
    hashed_password: str 
    joined_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    in_game_currency: int = 0
    lvl: int = 1
    role: AccountRole = AccountRole.player
    experience: int = 0
    balance: int = 0
    subscription: AccountSubscription = AccountSubscription.normal
    employees: list[Employee] = field(default_factory=list)

    def reward(self, exp_reward: int, money_reward: int) -> None:
        self.in_game_currency += money_reward
        self.experience += exp_reward
        self.lvl += self.experience // 1000
        self.experience = self.experience % 1000
    
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'hashed_password': self.hashed_password,
            'joined_at': self.joined_at,
            'in_game_currency': self.in_game_currency,
            'lvl': self.lvl,
            'role': self.role.value,
            'experience': self.experience,
            'subscription': self.subscription.value,
            'employees': self.employees
        }



    



