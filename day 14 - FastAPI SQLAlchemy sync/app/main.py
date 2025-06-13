from fastapi import FastAPI
from pydantic import BaseModel
from app.user import services as user_services
from app.product import services as product_services

app = FastAPI()

class UserCreate(BaseModel):
    name : str
    email : str

class ProductCreate(BaseModel):
    title:str
    desc:str
    price:int

@app.post('/user')
def user_create(user: UserCreate):
    user_services.create_user(name=user.name,email=user.email)
    return {"status":"created"}

@app.get("/users")
def all_users():
  users = user_services.read_users()
  return users

@app.post("/product")
def product_create(product:ProductCreate):
   product_services.create_product(title=product.title,desc=product.desc,price=product.price)
   return {"status":"created"}

@app.get("/products")
def get_all_products():
   product = product_services.read_products()
   return product