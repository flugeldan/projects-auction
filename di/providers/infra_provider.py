from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession
from application.interfaces.password_hasher import AbstractPasswordHasher
from application.interfaces.transaction_manager import AbstractTransactionManager
from application.interfaces.user_repository import AbstractUserRepository
from application.interfaces.order_repository import AbstractOrderRepository
from application.interfaces.employee_repository import AbstractEmployeeRepository
from application.interfaces.deal_repository import AbstractDealRepository

from infrastructure.services.password_hasher import BcryptPasswordHasher
from infrastructure.database.transaction_manager import SQLAlchemyTransactionManager
from infrastructure.database.repositories.user_repository import SQLAlchemyUserRepository
from infrastructure.database.repositories.order_repository import SQLAlchemyOrderRepository
from infrastructure.database.repositories.employee_repository import SQLAlchemyEmployeeRepository
from infrastructure.database.repositories.deal_repository import SQLAlchemyDealRepository



class Infrastructure(Provider):
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
    
    
    
    


    

