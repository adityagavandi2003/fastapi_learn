from db import engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import String,ForeignKey


class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    email:Mapped[str] = mapped_column(String(50),nullable=False,unique=True)

    # One-to-Many: User to Post
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user", cascade="all, delete")

    def __repr__(self) -> str:
        return f"<id={self.id} Name={self.name}>"

class Post(Base):
    __tablename__ = "post"

    post_id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id",ondelete="CASCADE"),nullable=True)
    title:Mapped[str]=mapped_column(String(50),nullable=False)
    caption:Mapped[str]=mapped_column(String(50),nullable=True)

    user: Mapped["Users"] = relationship("Users", back_populates="posts")
  
    def __repr__(self) -> str:
        return f"<Post id={self.post_id} title={self.title}>"
    

#  Create Table
def create_tables():
  Base.metadata.create_all(engine)

#  Drop Table
def drop_tables():
  Base.metadata.drop_all(engine)