# domain/entities/order_builder.py
from uuid import uuid4, UUID
from domain.entities.order import Order, TestCase
from domain.entities.employee import EmployeeType


class OrderBuilder:
    def __init__(self, name: str, time_to_complete: int) -> None:
        self._id: UUID = uuid4()
        self._name: str = name
        self._time_to_complete: int = time_to_complete
        self._exp_reward: int = 0
        self._money_reward: int = 0
        self._required_employees: dict[EmployeeType, int] = {}
        self._test_cases: list[TestCase] = []
        self._api_address: str = "localhost:8000"

    def with_exp_reward(self, exp: int) -> "OrderBuilder":
        self._exp_reward = exp
        return self

    def with_money_reward(self, money: int) -> "OrderBuilder":
        self._money_reward = money
        return self

    def with_api_address(self, address: str) -> "OrderBuilder":
        self._api_address = address
        return self

    def add_required_employee(self, employee_type: EmployeeType, count: int) -> "OrderBuilder":
        self._required_employees[employee_type] = count
        return self

    def add_test_case(self, test_case: TestCase) -> "OrderBuilder":
        self._test_cases.append(test_case)
        return self

    def build(self) -> Order:
        
        return Order(
            id=self._id,
            name=self._name,
            time_to_complete=self._time_to_complete,
            exp_reward=self._exp_reward,
            money_reward=self._money_reward,
            required_employees=self._required_employees,
            test_cases=self._test_cases,
            api_address=self._api_address,
        )