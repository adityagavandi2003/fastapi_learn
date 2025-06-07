from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import String
from db import engine

class Base(DeclarativeBase):
    pass

# user table
class Users(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(50),nullable=False)
    email: Mapped[str] = mapped_column(String(50),nullable=False)
    phone_number:Mapped[int] = mapped_column(String(50),nullable=False)

    def __repre__(self):
        return f"<User(id={self.id},name={self.name},email={self.email},phone number={self.phone_number})>"
    
# address table
class Address(Base):
    __tablename__ = "Address"

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(50), nullable=False)
    dist: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    country: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    def __repr__(self) -> str:
      return f"Address(id={self.id!r}, street={self.street!r})"
    
def create_table():
    Base.metadata.create_all(engine)

def drop_table():
    Base.metadata.drop_all(engine)
