import math
from dishka import Scope, Provider, provide


from src.application.interfaces.user_repository import AbstractUserRepository
from src.application.interfaces.deal_repository import AbstractDealRepository
from src.application.interfaces.employee_repository import AbstractEmployeeRepository
from src.application.interfaces.order_repository import AbstractOrderRepository
from src.application.interfaces.transaction_manager import AbstractTransactionManager
from src.application.interfaces.transaction_repository import AbstractTransactionRepository

from src.application.interactors.get_all_employees import GetAllEmployeesInteractor
from src.application.interactors.get_available_employees import GetAvailableEmployeesInteractor
from src.application.interactors.get_available_orders import GetAvailableOrdersInteractor
from src.application.interactors.get_assigned_orders import GetAssignedOrdersInteractor
from src.application.interactors.cancel_order import CancelOrderInteractor
from src.application.interactors.take_order import TakeOrderInteractor
from src.application.interactors.take_order_reward import TakeOrderRewardInteractor


from src.domain.service.order_assignment import OrderAssignmentService
from src.domain.service.reward_service import RewardService


class AppProvider(Provider):
    @provide(scope=Scope.APP)
    def order_assignment_service(self) -> OrderAssignmentService:
        return OrderAssignmentService()
    
    @provide(scope=Scope.APP)
    def reward_service(self) -> RewardService:
        return RewardService()

    @provide(scope=Scope.REQUEST)
    def get_all_employees_interactor(
        self,
        emp_repo: AbstractEmployeeRepository,
        transaction_manager: AbstractTransactionManager
    ) -> GetAllEmployeesInteractor:
        return GetAllEmployeesInteractor(
            emp_repo=emp_repo,
            transaction_manager=transaction_manager
        )
    
    @provide(scope=Scope.REQUEST)
    def get_available_employees_interactor(
        self,
        emp_repo: AbstractEmployeeRepository,
        transaction_manager: AbstractTransactionManager
    ) -> GetAvailableEmployeesInteractor:
        return GetAvailableEmployeesInteractor(
            emp_repo=emp_repo,
            transaction_manager=transaction_manager
        )
    
    @provide(scope=Scope.REQUEST)
    def get_available_orders_interactor(
        self,
        order_repo: AbstractOrderRepository,
        transaction_manager: AbstractTransactionManager
    ) -> GetAvailableOrdersInteractor:
        return GetAvailableOrdersInteractor(
            order_repo=order_repo,
            transaction_manager=transaction_manager
        )
    
    @provide(scope=Scope.REQUEST)
    def get_assigned_orders_interactor(
        self,
        deal_repo: AbstractDealRepository,
        transaction_manager: AbstractTransactionManager
    ) -> GetAssignedOrdersInteractor:
        return GetAssignedOrdersInteractor(
            deal_repo=deal_repo,
            transaction_manager=transaction_manager
        ) 
    
    @provide(scope=Scope.REQUEST)
    def take_order_interactor(
        self,
        user_repo: AbstractUserRepository,
        deal_repo: AbstractDealRepository,
        order_repo: AbstractOrderRepository,
        emp_repo: AbstractEmployeeRepository,
        transaction_manager: AbstractTransactionManager,
        order_assignment_service: OrderAssignmentService
    ) -> TakeOrderInteractor:
        return TakeOrderInteractor(
            user_repo=user_repo,
            deal_repo=deal_repo,
            order_repo=order_repo,
            emp_repo=emp_repo,
            transaction_manager=transaction_manager,
            order_assignment_service=order_assignment_service
        )
    
    @provide(scope=Scope.REQUEST)
    def refuse_order_interactor(
        self,
        deal_repo: AbstractDealRepository,
        emp_repo: AbstractEmployeeRepository,
        transaction_manager: AbstractTransactionManager,
        order_assignment_service: OrderAssignmentService
    ) -> CancelOrderInteractor:
        return CancelOrderInteractor(
            deal_repo=deal_repo,
            emp_repo=emp_repo,
            transaction_manager=transaction_manager,
            order_assignment_service=order_assignment_service

            
        )
    @provide(scope=Scope.REQUEST)
    def take_order_reward_interactor(
        self,
        deal_repo: AbstractDealRepository,
        transaction_repo: AbstractTransactionRepository,
        user_repo: AbstractUserRepository,
        order_repo: AbstractOrderRepository,
        transaction_manager: AbstractTransactionManager,
        reward_service: RewardService
    ) -> TakeOrderRewardInteractor:
        return TakeOrderRewardInteractor(
            deal_repo=deal_repo,
            transaction_repo=transaction_repo,
            user_repo=user_repo,
            order_repo=order_repo,
            transaction_manager=transaction_manager,
            reward_service=reward_service
        )