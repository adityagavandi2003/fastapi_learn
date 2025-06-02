from fastapi import FastAPI
from typing import Annotated, Any, List, Optional
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
  id: int
  name: str
  price : float
  stock: int | None = None

class ProductOut(BaseModel):
  name: str
  price : float


# # Without Return Type
@app.get("/products/")
async def get_products():
    return [
       {"status": "OK"},
       {"status": 200}
    ]

## Return type annotation
@app.get("/products/type-annotation")
async def get_products_type_annotation() -> Product:
    return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}

@app.get("/products/missing/")
async def get_products_missing() -> Product:
    return {"id": 1, "name": "Moto E", "price": 33.44} # stock missing so gives null

@app.get("/products/missing/name")
async def get_products_missing_name() -> Product:
    return {"id": 1, "price": 33.44, "stock": 5} # name missing so gives Internal Server Error

@app.get("/products/extra-one")
async def get_products_extra_one() -> Product:
    return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5, "description": "This is moto e"} # desc

@app.get("/products/list")
async def get_products_list() -> List[Product]:
    return [
       {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5},
       {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7}
    ]

@app.get("/products/list-extra-one")
async def get_products_list_extra_one() -> List[Product]:
    return [
       {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5, "description": "Hello Desc1"},
       {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7, "description": "Hello Desc2"}
    ]

@app.post("/products/product")
async def create_product_product(product: Product) -> Product:
  return product

@app.post("/products/productout")
async def create_product_productout(product: Product) -> ProductOut:
  return product

class BaseUser(BaseModel):
    username: str
    full_name: str | None = None

class UserIn(BaseUser):
    password: str

@app.post("/users/")
async def create_user(user: UserIn) -> BaseUser:
  return user


## without response_model Parameter
@app.get("/products/without/response_model/")
async def get_products_without_response_model():
  return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}

# with response_model Parameter
@app.get("/products/with/response_model/", response_model=Product)
async def get_products_with_response_model():
  return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}


@app.get("/products/with/list", response_model=List[Product])
async def get_products_response_model():
  return [
       {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5},
       {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7}
    ]

@app.get("/products/response/extra-one/", response_model=List[Product])
async def get_products_respone_extra_one():
  return [
       {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5, "description": "Hello Desc1"},
       {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7, "description": "Hello Desc2"}
    ]

@app.post("/products/response-model/", response_model=Product)
async def create_product_response_model(product: Product):
  return product

@app.post("/users/response-model/", response_model=BaseUser)
async def create_user_response_model(user: UserIn):
  return user

@app.post("/products/response-model/any/", response_model=Product)
async def create_product_res_any(product: Product) -> Any:
  return product

@app.post("/products/response-model/none", response_model=None)
async def create_product_res_none(product: Product) -> Any:
  return product



## Excluding Unset Default Values
products_db = {
    "1": {"id": "1", "name": "Laptop", "price": 999.99, "stock": 10, "is_active": True},
    "2": {"id": "2", "name": "Smartphone", "price": 499.99, "stock": 50, "is_active": False}
}

class Product_Exc(BaseModel):
    id: str
    name: str
    price: float
    description: Optional[str] = None
    tax: float = 15.0  # Default tax rate

@app.get("/products/unset/{product_id}", response_model=Product_Exc, response_model_exclude_unset=True)
async def get_product_unset(product_id: str):
    return products_db.get(product_id, {})

# Including Specific Fields
@app.get("/products/inc/{product_id}", response_model=Product_Exc, response_model_include={"name", "price"})
async def get_product_include(product_id: str):
    return products_db.get(product_id, {})

## Excluding Specific Fields
@app.get("/products/exc/{product_id}", response_model=Product_Exc, response_model_exclude={"tax", "description"})
async def get_product_exclude(product_id: str):
    return products_db.get(product_id, {})