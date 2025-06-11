from db import engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import Integer, String,ForeignKey

class Base(DeclarativeBase):
    pass

# User Model
class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
  
  def __repr__(self) -> str:
    return f"<User(id={self.id}, name={self.name}, email={self.email})>"

# Post Model
class Post(Base):
  __tablename__ = "post"

  id: Mapped[int] = mapped_column(primary_key=True)
  caption: Mapped[str] = mapped_column(String(50), nullable=False)
  user_id:Mapped[int] = mapped_column(Integer,nullable=False)
  
  def __repr__(self) -> str:
    return f"<User(id={self.id}, name={self.name}, email={self.email})>"