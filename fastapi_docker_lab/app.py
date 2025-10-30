from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Base, User
from db import engine, async_session

app = FastAPI(title="FastAPI + Docker + Postgres Demo")

# Create tables at startup
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency to get DB session
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

# POST /users  → create a new user
@app.post("/users")
async def create_user(name: str, email: str, session: AsyncSession = Depends(get_session)):
    new_user = User(name=name, email=email)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

# GET /users  → fetch all users
@app.get("/users")
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    return result.scalars().all()

