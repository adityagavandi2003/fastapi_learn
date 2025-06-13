from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncAttrs
from db import engine

class Base(AsyncAttrs,DeclarativeBase):
    pass

# user model
class User(Base):
    __tablename__ = "user"

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(50),nullable=True)
    email:Mapped[str] = mapped_column(String(50),nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
    
async def create_tables():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)

async def drop_tables():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.drop_all)