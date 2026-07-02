from uuid import uuid4
from domain.entities.user import User
from domain.builders.employee_builder import EmployeeBuilder
class UserBuilder:
    @staticmethod
    def build(username: str, email: str,  hashed_password: str) -> User:
        user_id = uuid4()
        return User(id=id, email=email, username=username,
                    employees=EmployeeBuilder.build_basic_set(user_id=user_id))


