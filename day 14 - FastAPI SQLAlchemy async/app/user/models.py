from app.db.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column


# usermodel
class User(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(50),nullable=False)
    email:Mapped[str] = mapped_column(String(50),nullable=False)

    def __repr__(self):
        return f"<User id={self.id} name={self.name} email={self.email}"
    
    