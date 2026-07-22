from src.domain.entities.user import User
from src.domain.value_objects.team import EmployeeTeam
from src.domain.exceptions import UserAlreadyWorkingError

class OrderAssignmentService:
    @staticmethod
    def validate_user_can_take_deal(active_personal_deals_count: int) -> None:
        if active_personal_deals_count >= 1:
            raise UserAlreadyWorkingError("Can't take more than 1 deal at the same time")
    
    @staticmethod
    def assign_employees(team: EmployeeTeam):
        busy_until = team.calculate_busy_until
        for emp in team.employees:
            emp.start_work(busy_until=busy_until,
                           order_id=team.order.id)
            
    
    @staticmethod
    def deassign_employees(team: EmployeeTeam):
        for emp in team.employees:
            emp.stop_work()
    
        