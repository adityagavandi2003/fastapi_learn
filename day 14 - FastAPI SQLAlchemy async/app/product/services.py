from app.db.config import SessionLocal
from sqlalchemy import select,insert,update,delete
from app.product.models import Product


# create product
async def create_product(title:str,price:int):
    async with SessionLocal() as session:
        product = Product(title=title,price=price)
        session.add(product)
        await session.commit()

# read all product
async def read_all_product():
    async with SessionLocal() as session:
        stmt = select(Product)
        product = await session.scalars(stmt)
        return product.all()
    