from app.db.base import Base
from sqlalchemy import String,Text
from sqlalchemy.orm import Mapped,mapped_column


# note model
class Notes(Base):
    __tablename__ = "notes"

    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(50))
    content:Mapped[str] = mapped_column(Text)

    def __repr__(self):
        return f"<Note title={self.title} content={self.content}>"

