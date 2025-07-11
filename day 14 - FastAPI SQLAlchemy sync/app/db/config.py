from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db_path = os.path.join(BASEDIR,"sqlite.db")
DATABASE_URL = f"sqlite:///{db_path}"
engine = create_engine(DATABASE_URL,echo=True)
SessionLocal = sessionmaker(bind=engine,expire_on_commit=False)