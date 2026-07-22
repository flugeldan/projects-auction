import asyncio
import random
from uuid import uuid4

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config.settings import settings
from src.infrastructure.orm.mapping import start_mappers
from src.domain.entities.order import Order
from src.domain.entities.employee import EmployeeType

ORDER_NAMES = [
    "Landing page redesign",
    "Payment integration",
    "Mobile app MVP",
    "Admin dashboard",
    "API rate limiter",
    "Chat widget",
    "Analytics pipeline",
    "Auth service migration",
    "Recommendation engine",
    "Notification system",
]


def random_employees_to_outsource() -> dict[str, int]:
    types = random.sample(list(EmployeeType), k=random.randint(1, 3))
    return {t.value: random.randint(1, 3) for t in types}


async def seed_orders():
    start_mappers()

    engine = create_async_engine(settings.database_url)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async with session_factory() as session:
        for name in ORDER_NAMES:
            order = Order(
                id=uuid4(),
                name=name,
                description=f"Auto-generated order: {name}",
                work_units_to_complete=random.randint(10, 200),
                exp_reward=random.randint(50, 500),
                money_reward=random.randint(100, 2000),
                employees_to_outsource=random_employees_to_outsource(),
            )
            session.add(order)

        await session.commit()
        print(f"Seeded {len(ORDER_NAMES)} orders")

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(seed_orders())