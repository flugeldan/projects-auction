from sqlalchemy import Table, Column, String, DateTime, Integer, Boolean, ForeignKey, MetaData, JSON
from sqlalchemy.orm import registry, relationship
from sqlalchemy.dialects.postgresql import UUID

from src.domain.entities.order import Order
from src.domain.entities.deal import Deal
from src.domain.entities.employee import Employee
from src.domain.entities.user import User
from src.domain.entities.transaction import Transaction

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

GAME_SCHEMA = "game"


orders_table = Table(
    "orders",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("name", String(100), nullable=False),
    Column("description", String(500), nullable=False),
    Column("work_units_to_complete", Integer, nullable=False),
    Column("exp_reward", Integer, nullable=False, default=0),
    Column("money_reward", Integer, nullable=False, default=0),
    Column("employees_to_outsource", JSON, nullable=False),
    schema=GAME_SCHEMA,
)

users_table = Table(
    "users",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("email", String(255), nullable=False, unique=True),
    Column("username", String(100), nullable=False, unique=True),
    Column("hashed_password", String(255), nullable=False),
    Column("joined_at", DateTime(timezone=True), nullable=False),
    Column("in_game_currency", Integer, nullable=False, default=0),
    Column("lvl", Integer, nullable=False, default=1),
    Column("role", String(20), nullable=False),
    Column("experience", Integer, nullable=False, default=0),
    Column("balance", Integer, nullable=False, default=0),
    Column("subscription", String(20), nullable=False),
    schema="public",
)

employees_table = Table(
    "employees",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("public.users.id", ondelete="CASCADE"), nullable=False),
    Column("employee_type", String(20), nullable=False),
    Column("work_points", Integer, nullable=False),
    Column("busy_until", DateTime(timezone=True), nullable=True),
    Column("current_order_id", UUID(as_uuid=True), ForeignKey(f"{GAME_SCHEMA}.orders.id"), nullable=True),
    schema=GAME_SCHEMA,
)

deals_table = Table(
    "deals",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("order_id", UUID(as_uuid=True), ForeignKey(f"{GAME_SCHEMA}.orders.id"), nullable=False),
    Column("user_id", UUID(as_uuid=True), ForeignKey("public.users.id"), nullable=False),
    Column("started_at", DateTime(timezone=True), nullable=False),
    Column("with_user", Boolean, nullable=False),
    Column("calculated_money_reward", Integer, nullable=False, default=0),
    Column("calculated_exp_reward", Integer, nullable=False, default=0),
    Column("worker_protocol", String(20), nullable=False),
    Column("work_units_to_complete", Integer, nullable=False),
    Column("work_units_per_tick", Integer, nullable=False, default=0),
    Column("will_end_at", DateTime(timezone=True), nullable=True),
    Column("status", String(30), nullable=False),
    schema=GAME_SCHEMA,
)


transactions_table = Table(
    "transactions",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("public.users.id", ondelete="CASCADE"), nullable=False),
    Column("amount", Integer, nullable=False),
    Column("transaction_type", String(30), nullable=False),
    Column("direction", String(10), nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False),
    Column("target_id", UUID(as_uuid=True), nullable=True),
    schema="public",
)


def start_mappers():
    mapper_registry.map_imperatively(Order, orders_table)
    mapper_registry.map_imperatively(Employee, employees_table)
    mapper_registry.map_imperatively(
        User,
        users_table,
        properties={
            "employees": relationship(Employee, backref="user", lazy="selectin")
        }
    )
    mapper_registry.map_imperatively(Deal, deals_table)
    mapper_registry.map_imperatively(Transaction, transactions_table)
