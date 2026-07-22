# scripts/init_db.py
import asyncio
import random
from uuid import UUID, uuid4

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config.settings import settings
from src.infrastructure.orm.mapping import metadata, start_mappers, GAME_SCHEMA
from src.domain.entities.user import User, AccountRole, AccountSubscription
from src.domain.entities.employee import Employee, EmployeeType

FIXED_USER_ID = UUID("11111111-1111-1111-1111-111111111111")


async def init_db():
    start_mappers()

    engine = create_async_engine(settings.database_url)

    async with engine.begin() as conn:
        # схема game не создаётся автоматически, только public встроена
        await conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {GAME_SCHEMA}"))
        await conn.run_sync(metadata.create_all)

    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async with session_factory() as session:
        user = User(
            id=FIXED_USER_ID,
            email="test@test.com",
            username="testuser",
            hashed_password="fakehash",
            role=AccountRole.player,
            subscription=AccountSubscription.normal,
        )
        session.add(user)

        for _ in range(5):
            session.add(Employee(
                id=uuid4(),
                user_id=FIXED_USER_ID,
                employee_type=random.choice(list(EmployeeType)),
                work_points=random.randint(1, 10),
            ))

        await session.commit()
        print(f"DB initialized. Seeded user {FIXED_USER_ID} with 5 employees")

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(init_db())