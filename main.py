from contextlib import asynccontextmanager

from fastapi import FastAPI

from database_01 import delete_tables, create_tables
from routers_01 import router as router_tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(router_tasks)
