from app.db.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column


# product model
class Product(Base):
    __tablename__ = "products"

    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(50),nullable=False)
    price:Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<User id={self.id} name={self.name} email={self.email}"
    
    