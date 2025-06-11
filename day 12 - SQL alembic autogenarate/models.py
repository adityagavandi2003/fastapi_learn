from db import engine
from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped
from sqlalchemy import String,Integer

class Base(DeclarativeBase):
    pass

# user model
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
    
