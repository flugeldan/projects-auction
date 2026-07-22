import uvicorn
from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

# Импорты из папки di
# 1. Импорты провайдеров из di/providers
from src.di.providers.psql_provider import PsqlProvider
from src.di.providers.infra_provider import InfraProvider
from src.di.providers.app_provider import AppProvider
from src.presentation.api.rest.v1.endpoints.order import router as orders_router
from src.infrastructure.orm.mapping import start_mappers
from src.presentation.api.rest.v1.endpoints.employees import router as employees_router
def create_app() -> FastAPI:
    start_mappers()

    app = FastAPI(title="Game Backend")
    

    app.include_router(orders_router, prefix="/api")
    app.include_router(employees_router, prefix='/api')

    container = make_async_container(
        PsqlProvider(),
        InfraProvider(),
        AppProvider(),
    )
    
    # 4. Женим Дишку с FastAPI
    setup_dishka(container, app)

    @app.on_event("shutdown")
    async def on_shutdown():
        await container.close()

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)