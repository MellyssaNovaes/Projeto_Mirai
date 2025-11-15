from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.engine import init_db
from app.users.router import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
