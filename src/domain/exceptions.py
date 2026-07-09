
class DomainError(Exception):
    pass

class InvalidOrderDataError(DomainError):
    pass

class InvalidDealError(DomainError):
    pass

class OrderAlreadyTakenError(DomainError):
    pass

class EmployeeAlreadyBusy(DomainError):
    pass

class OrderAlreadyExistsError(DomainError):
    def __init__(self, order_id):
        self.order_id = order_id
        super().__init__(f"Order {order_id} already exists")

class DealAlreadyExistsError(DomainError):
    def __init__(self, deal_id):
        self.deal_id = deal_id
        super().__init__(f"Order {deal_id} already exists")