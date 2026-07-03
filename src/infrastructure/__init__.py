from passlib.context import CryptContext
from application.interfaces.password_hasher import AbstractPasswordHasher

class BcryptPasswordHasher(AbstractPasswordHasher):
    def __init__(self) -> None:
        self._context = CryptContext(schemes=["bcrypt"])

    def hash(self, password: str) -> str:
        return self._context.hash(password)

    def verify(self, password: str, hashed: str) -> bool:
        return self._context.verify(password, hashed)