from db import engine
from sqlalchemy import MetaData,Table,Column,Integer,String,ForeignKey

metadata = MetaData()

user = Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(length=50),nullable=True),
    Column("email",String,unique=True,nullable=True),
    Column("phone_number",Integer,unique=True,nullable=True),
)

# one to many
posts = Table(
    "posts",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("user_id",Integer,ForeignKey("users.id",ondelete="CASCADE")),
    Column("title",String,nullable=False),
    Column("content",String,nullable=False)
)

# one to one (add unique true)
profile = Table(
  "profile",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True),
  Column("bio", String, nullable=False),
  Column("address", String, nullable=False),
)

# Many to Many (add association table)
address = Table(
  "address",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("street", String, nullable=False),
  Column("country", String, nullable=False),
)

user_address_association = Table(
  "user_address_association",
  metadata,
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
  Column("address_id", Integer, ForeignKey("address.id", ondelete="CASCADE"), primary_key=True),
)

def create_table():
    metadata.create_all(engine)