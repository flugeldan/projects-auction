from dataclasses import dataclass
from uuid import UUID, uuid4
from enum import Enum
from datetime import datetime, timezone, timedelta
from src.domain.entities.order import Order
from src.domain.entities.employee import Employee
from typing import Self
from src.domain.exceptions import InvalidDealStatusError, InvalidDealError
from src.domain.value_objects.team import EmployeeTeam
import math

class DealStatus(str, Enum):
    in_progress = "in_progress"
    completed = "completed"
    failed = "failed"

class IntegrationProtocol(str, Enum):
    REST = "rest"
    GRPC = "grpc"
    KAFKA = "kafka"

@dataclass
class Deal:
    id: UUID
    order_id: UUID
    user_id: UUID
    started_at: datetime
    with_user: bool
    worker_protocol: IntegrationProtocol
    work_units_to_complete: int
    work_units_per_tick: int = 0  
    will_end_at: datetime | None = None                      
    status: DealStatus = DealStatus.in_progress
    calculated_money_reward: int = 0
    calculated_exp_reward: int = 0

    @classmethod
    def create(cls, order_id: UUID, user_id: UUID, with_user: bool,
               worker_protocol: IntegrationProtocol, work_units_to_complete: int,
               calculated_money_reward: int, calculated_exp_reward: int) -> Self:
        return cls(
            id=uuid4(),
            order_id=order_id,
            user_id=user_id,
            started_at=datetime.now(timezone.utc),
            worker_protocol=worker_protocol,
            with_user=with_user,
            work_units_to_complete=work_units_to_complete,
            calculated_money_reward = calculated_money_reward,
            calculated_exp_reward = calculated_exp_reward
        )
    
    def complete(self) -> None:
        if self.status in (DealStatus.failed, DealStatus.completed):
            raise InvalidDealStatusError
            
        if self.will_end_at is None:
            raise InvalidDealError("Team not assigned yet")

        now = datetime.now(timezone.utc)
        if self.will_end_at > now:
            raise InvalidDealStatusError("Deal is still in progress")
            
        self.status = DealStatus.completed
    
    def cancel(self) -> None:
        if self.status != DealStatus.in_progress:
            raise InvalidDealStatusError
        self.status = DealStatus.failed
    
    def calculate_duration(self, team: EmployeeTeam) -> timedelta:
        base_speed = 1 if self.with_user else 0
        self.work_units_per_tick = team.total_work_points + base_speed
        
        if self.work_units_per_tick <= 0:
            raise InvalidDealError("Total speed must be greater than 0")
            
        minutes = math.ceil(self.work_units_to_complete / self.work_units_per_tick)
        return timedelta(minutes=minutes)

    def assign_team(self, team: EmployeeTeam) -> None:
        now = datetime.now(timezone.utc)
        duration = self.calculate_duration(team)
        self.will_end_at = now + duration

    
        


