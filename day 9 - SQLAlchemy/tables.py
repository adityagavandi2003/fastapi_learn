from db import engine
from sqlalchemy import MetaData,Table,Column,Integer,String

metadata = MetaData()

# user table
user = Table(
    'user',
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email",String,nullable=False,unique=True),
    Column("phone",Integer,nullable=False,unique=True)
)
# address Table
address = Table(
  "address",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("street", String(length=50), nullable=False),
  Column("dist", String, nullable=False, unique=True),
  Column("country", String, nullable=False, unique=True)
  )

# create table in databases
def create_table():
    metadata.create_all(engine)
