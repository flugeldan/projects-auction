from dataclasses import dataclass
from uuid import UUID, uuid4
from datetime import datetime, timezone
from enum import Enum
from typing import Self

class Direction(str, Enum):
    income = "income"
    outcome = "outcome"

class TransactionType(str, Enum):
    order_reward = "order_reward"
    employee_purchase = "employee_purchase"
    system_bonus = "system_bonus"
    


@dataclass
class Transaction:
    id: UUID
    user_id: UUID
    amount: int
    transaction_type: TransactionType
    direction: Direction
    created_at: datetime
    target_id: UUID | None = None

    @classmethod
    def create(
        cls,
        user_id: UUID,
        amount: int,
        transaction_type: TransactionType,
        direction: Direction,
        target_id: UUID | None = None) -> Self:
        now = datetime.now(timezone.utc)
        return Transaction(
            id = uuid4(),
            user_id=user_id,
            amount=amount,
            transaction_type=transaction_type,
            direction=direction,
            target_id=target_id,
            created_at=now
        )
