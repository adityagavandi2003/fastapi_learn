from sqlalchemy import MetaData,String,Table,Column,Integer
from db import engine

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(50),nullable=False),
    Column("email",String(50),nullable=False,unique=True),
)

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)