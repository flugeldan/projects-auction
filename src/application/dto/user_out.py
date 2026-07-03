from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from domain.entities.user import User

@dataclass
class UserOutDTO:
    id: UUID
    email: str
    username: str
    joined_at: datetime
    in_game_currency: int
    lvl: int

    @staticmethod
    def from_entity(user: User) -> "UserOutDTO":
        return UserOutDTO(id=user.id,
                          email=user.email,
                          username=user.username,
                          joined_at=user.joined_at,
                          in_game_currency=user.in_game_currency,
                          lvl=user.lvl)

    

