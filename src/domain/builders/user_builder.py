from uuid import uuid4
from src.domain.entities.user import User
class UserBuilder:
    @staticmethod
    def build(username: str, email: str,  hashed_password: str) -> User:
        pass


