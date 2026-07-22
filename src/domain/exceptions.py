
class DomainError(Exception):
    pass

class OrderError(DomainError):
    pass

class OrderNotFoundError(OrderError):
    def __init__(self, order_id=None) -> None:
        self.order_id = order_id
        super().__init__(f"Order {order_id} not found")

class OrderAlreadyExistsError(OrderError):
    def __init__(self, order_id=None) -> None:
        self.order_id = order_id
        super().__init__(f"Order {order_id} already exists")

class OrderAlreadyTakenError(OrderError):
    pass

class InvalidOrderDataError(OrderError):
    pass


class DealError(DomainError):
    pass

class DealNotFoundError(DealError):
    def __init__(self, deal_id=None) -> None:
        self.deal_id = deal_id
        super().__init__(f"Deal {deal_id} not found")

class DealAlreadyExistsError(DealError):
    def __init__(self, deal_id=None) -> None:
        self.deal_id = deal_id
        super().__init__(f"Deal {deal_id} already exists")

class DealAlreadyCompletedError(DealError):
    def __init__(self, deal_id=None) -> None:
        self.deal_id = deal_id
        super().__init__(f"Deal {deal_id} already completed")

class DealAlreadyFailedError(DealError):
    def __init__(self, deal_id=None) -> None:
        self.deal_id = deal_id
        super().__init__(f"Deal {deal_id} already failed")

class DealNotFoundOrCannotBeFailedError(DealError):
    pass

class InvalidDealStatusError(DealError):
    pass

class InvalidDealError(DealError):
    pass



class EmployeeError(DomainError):
    pass

class EmployeeAlreadyExistsError(EmployeeError):
    def __init__(self, employee_id=None) -> None:
        self.employee_id = employee_id
        super().__init__(f"Employee {employee_id} already exists")

class EmployeeNotFoundError(EmployeeError):
    pass

class EmployeeAlreadyBusyError(EmployeeError):
    pass

class EmployeeAccessDeniedError(EmployeeError):
    pass


class UserError(DomainError):
    pass

class UserAlreadyWorkingError(UserError):
    pass

class UserNotFoundError(UserError):
    pass

class ValidationError(DomainError):
    pass

class TransactionError(DomainError):
    pass

class TransactionAlreadyExistsError(TransactionError):
    pass

