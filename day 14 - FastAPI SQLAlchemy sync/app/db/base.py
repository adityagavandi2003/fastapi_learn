from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


from app.user import models 
from app.product import models