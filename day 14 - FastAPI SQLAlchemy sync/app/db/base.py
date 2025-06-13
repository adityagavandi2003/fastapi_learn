from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


from app.users import models 
from app.product import models