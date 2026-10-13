from fastapi import FastAPI 
from app.model import posts, get_async_session, create_db_tables
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_tables
    yield

app=FastAPI(lifespan=lifespan)

