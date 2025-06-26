from sqlmodel import SQLModel,Field

class Product(SQLModel,table=True):
    id:int = Field(primary_key=True)
    title:str
    price:int