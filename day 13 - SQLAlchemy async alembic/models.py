from sqlalchemy import String,MetaData,Integer,Column,Table
from db import engine

metadata = MetaData()
# create user table
user = Table(
    "user",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(50),nullable=True),
    Column("email",String(50),nullable=True)
)
