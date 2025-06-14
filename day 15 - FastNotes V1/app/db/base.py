from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs,DeclarativeBase):
    pass

from app.notes import models as note_models