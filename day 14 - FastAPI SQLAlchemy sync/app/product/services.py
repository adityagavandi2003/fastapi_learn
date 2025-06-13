from app.db.config import SessionLocal
from sqlalchemy import select,insert
from app.product.models import Product

# insert data
def create_product(title:str,desc:str,price:int):
    with SessionLocal() as session:
        product = Product(title=title, desc=desc,price=price)
        session.add(product)
        session.commit()

# Read All product
def read_products():
    with SessionLocal() as session:
        stmt = select(Product)
        product = session.scalars(stmt)
        return product.all()