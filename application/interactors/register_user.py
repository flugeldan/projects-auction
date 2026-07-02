from application.interfaces.unit_of_work import AbstractUnitOfWork
from application.interfaces.password_hasher import AbstractPasswordHasher
from application.dto.user_in import RegisterUserInDTO
from application.dto.user_out import UserOutDTO
from domain.builders.user_builder import UserBuilder
class RegisterUserInteractor:
    def __init__(self, uow: AbstractUnitOfWork, password_hasher : AbstractPasswordHasher) -> None:
        self._uow = uow
        self._password_hasher = password_hasher
    
    async def execute(self, dto: RegisterUserInDTO) -> UserOutDTO:
        hashed_password = self._password_hasher.hash(password=dto.password)
        user = UserBuilder.build(username = dto.username,
                                 hashed_password = hashed_password,
                                 email = dto.email
                                 )
        async with self._uow as uow:
            uow.users.save(user = user)
            
        return UserOutDTO.from_entity(user = user)

