from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, AsyncEngine
from collections.abc import AsyncGenerator
from config.settings import settings

class PsqlProvider(Provider):

    @provide(scope=Scope.APP)
    def get_engine(self)-> AsyncEngine:
        return create_async_engine(settings.database_url)
    
    @provide(scope=Scope.APP)
    def get_sessionmaker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit = False)
    
    @provide(scope=Scope.REQUEST)
    async def psql_connection(self, session_maker: async_sessionmaker) -> AsyncGenerator[AsyncSession, None]:
        async with session_maker() as session:
            yield session


        
    