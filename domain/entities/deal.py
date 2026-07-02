from dataclasses import dataclass
from uuid import UUID
from enum import Enum
from datetime import datetime
class DealStatus(str, Enum):
    in_progress = "in_progress"
    completed = "completed"
    failed = "failed"

@dataclass
class Deal:
    id: UUID
    order_id: UUID
    user_id: UUID
    started_at: datetime
    status: DealStatus.in_progress 
    deadline: datetime