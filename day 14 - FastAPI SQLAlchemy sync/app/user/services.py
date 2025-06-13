from app.db.config import SessionLocal
from app.user.models import User
from sqlalchemy import insert,select,update,delete


# insert data
def create_user(name:str,email:str):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()

# Read All User
def read_users():
    with SessionLocal() as session:
        stmt = select(User)
        user = session.scalars(stmt)
        return user.all()