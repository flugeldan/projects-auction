from dataclasses import dataclass

@dataclass
class RegisterUserInDTO:
    username: str
    email: str
    password: str
