from app.db.config import SessionLocal
from sqlalchemy import select,insert,update,delete
from app.user.models import User


# create user
async def create_user(name:str,email:str):
    async with SessionLocal() as session:
        user = User(name=name,email=email)
        session.add(user)
        await session.commit()

# read all users
async def read_all_user():
    async with SessionLocal() as session:
        stmt = select(User)
        users = await session.scalars(stmt)
        return users.all()
    