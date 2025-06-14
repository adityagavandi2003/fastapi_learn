from fastapi import FastAPI
from pydantic import BaseModel
from app.user import services as user_services
from app.product import services as product_services


app = FastAPI()

class UserCreate(BaseModel):
    name:str
    email:str

class ProductCreate(BaseModel):
    title:str
    price:str

@app.post("/user")
async def create_user(user:UserCreate):
    await user_services.create_user(name=user.name,email=user.email)
    return {"status":"created"}

@app.get("/users")
async def get_users():
    users = await user_services.read_all_user()
    return users

@app.post("/product")
async def create_product(product:ProductCreate):
    await product_services.create_product(title=product.title,price=product.price)
    return {"status":"created"}

@app.get("/products")
async def get_product():
    product = await product_services.read_all_product()
    return product