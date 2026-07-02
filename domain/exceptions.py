
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