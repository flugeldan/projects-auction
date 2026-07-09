from sqlalchemy import Table, Column, String, DateTime, MetaData
from sqlalchemy.orm import registry
from sqlalchemy.dialects.postgresql import UUID
from domain.entities.order import Order

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

orders_table = TabError(
    "orders",
    metadata
)