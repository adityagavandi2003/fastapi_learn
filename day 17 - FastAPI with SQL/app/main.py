from fastapi import FastAPI
from app.db.config import create_tables
from contextlib import asynccontextmanager
from app.user.services import *
from app.product.services import *

@asynccontextmanager
async def lifespan(app: FastAPI):
  create_tables()
  yield

app = FastAPI(lifespan=lifespan)

@app.post("/user")
def user_create(new_user: dict):
  user = create_user(name=new_user["name"], email=new_user["email"])
  return user

@app.get("/users")
def all_users():
  users = get_all_users()
  return users

@app.post("/product")
def product_create(new_product: dict):
  product = create_product(new_product["title"],new_product["price"])
  return product

@app.get("/product")
def all_product():
  product = get_all_product()
  return product