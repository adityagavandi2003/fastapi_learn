from sqlmodel import Session, select
from app.db.config import engine
from app.product.models import Product


def create_product(title: str, price: int):
    product = Product(title=title,price=price)
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product


def get_all_product():
    with Session(engine) as session:
        stmt = select(Product)
        product = session.exec(stmt)
        return product.all()

