from abc import ABC, abstractmethod

class AbstractPasswordHasher(ABC):
    
    @abstractmethod
    def hash(self, password: str) -> str:
        ...

    @abstractmethod
    def verify(self, password: str, hashed: str) -> bool:
        ...