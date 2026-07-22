from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession
from src.application.interfaces.password_hasher import AbstractPasswordHasher
from src.application.interfaces.transaction_manager import AbstractTransactionManager
from src.application.interfaces.user_repository import AbstractUserRepository
from src.application.interfaces.order_repository import AbstractOrderRepository
from src.application.interfaces.employee_repository import AbstractEmployeeRepository
from src.application.interfaces.deal_repository import AbstractDealRepository
from src.application.interfaces.transaction_repository import AbstractTransactionRepository

from src.infrastructure.services.password_hasher import BcryptPasswordHasher
from src.infrastructure.database.transaction_manager import SQLAlchemyTransactionManager
from src.infrastructure.database.repositories.user_repository import SQLAlchemyUserRepository
from src.infrastructure.database.repositories.order_repository import SQLAlchemyOrderRepository
from src.infrastructure.database.repositories.employee_repository import SQLAlchemyEmployeeRepository
from src.infrastructure.database.repositories.deal_repository import SQLAlchemyDealRepository
from src.infrastructure.database.repositories.transaction_repository import TransactionRepository
from src.application.interfaces.password_hasher import AbstractPasswordHasher


class InfraProvider(Provider):

    @provide(scope=Scope.APP)
    def get_password_hasher(self) -> AbstractPasswordHasher:
        return BcryptPasswordHasher()


    @provide(scope=Scope.REQUEST)
    def get_transaction_manager(self, session: AsyncSession) -> AbstractTransactionManager:
        return SQLAlchemyTransactionManager(session = session)
    
    @provide(scope=Scope.REQUEST)
    def get_user_repository(self, session: AsyncSession) -> AbstractUserRepository:
        return SQLAlchemyUserRepository(session = session)

    @provide(scope=Scope.REQUEST)
    def get_order_repository(self, session: AsyncSession) -> AbstractOrderRepository:
        return SQLAlchemyOrderRepository(session = session)

    @provide(scope=Scope.REQUEST)
    def get_employee_repository(self, session: AsyncSession) -> AbstractEmployeeRepository:
        return SQLAlchemyEmployeeRepository(session = session)

    @provide(scope=Scope.REQUEST)
    def get_deal_repository(self, session: AsyncSession) -> AbstractDealRepository:
        return SQLAlchemyDealRepository(session = session)
    
    @provide(scope=Scope.REQUEST)
    def get_transaction_repository(self, session: AsyncSession) -> AbstractTransactionRepository:
        return TransactionRepository(session=session)
    

    
    
    
    


    

