from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base

# user models
class products(Base):
    __tablename__ = "products"

    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(50),nullable=False)
    desc:Mapped[str] = mapped_column(String(50),nullable=True)
    price:Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<User id={self.id} title={self.title} price={self.price}>"