from fastapi import FastAPI,Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# ----------------------------------- 1 request body and pydantic model --------------------------------------------
# without pydantic
# create or insert data
@app.post("/products/m")
async def create_product_without_pydantic(product:dict):
    return product

# with pydantic
# define the product model
class Product(BaseModel):
    id:int
    name:str
    price:float
    stock:int| None = None

@app.post("/product-with-pydantic")
async def create_product_with_pydantic(product:Product):
    return product

# access attribut inside funtion
@app.post("/product")
async def create_product_with_access_attribut_inside_funtion(new_product:Product):
    print(new_product.id)
    print(new_product.name)
    print(new_product.price)
    print(new_product.stock)
    return new_product

# add new calculated attribute
@app.post("/c/product")
async def create_product_with_new_attribut(new_product:Product):
    product_dict = new_product.model_dump()
    price_with_tax = new_product.price+(new_product.price*18/100)
    product_dict["price_with_tax"]=price_with_tax
    return product_dict

# combining request parameter with path parameter
@app.put("/products/pp/{product_id}")
async def update_product_path_parameter(product_id:int,new_updated_product:Product):
    return {"product_id":product_id,"new_updated_product":new_updated_product}

# adding query parameter
@app.put("/products/qp/{product_id}")
async def update_product_query_parameter(product_id:int,new_updated_product:Product,discount:float | None = None):
    return {"product_id":product_id,"new_updated_product":new_updated_product,"discount":discount}


# ----------------------------------- 2 multiple body parameter--------------------------------------------
class Product(BaseModel):
    name:str
    price:float
    stock:int|None = None

class Seller(BaseModel):
    username : str
    fullname : str | None = None

@app.post("/products")
async def multiple_create_product(product:Product,seller:Seller):
    return {"product":product,"seller":seller}

# make body optional
@app.post("/body-optiona/products")
async def create_product_body_optional(product:Product,seller:Seller | None = None):
    return {"product":product,"seller":seller}

# singular values in body
@app.post("/s/products")
async def create_product_singular_values(
    product:Product,
    seller:Seller,
    sec_key:Annotated[str,Body()]
    ):
    return {"product":product,"seller":seller,"sec_key":sec_key}

# embed a single body parameter
# without embed
@app.post("/emw/product")
async def create_product_without_embed(product:Product):
    return product

# with embed
@app.post("/em/product")
async def create_product_with_embed(product:Annotated[Product,Body(embed=True)]):
    return product

# ----------------------------------- 3 Pydantic Field --------------------------------------------

class PyProduct(BaseModel):
    name:str = Field(
        title="Product Name",
        description=" the name of product",
        max_length= 50,
        min_length=3,
        pattern="^[A-Za-z0-9 ]+$"
    )
    price:float = Field(
        gt = 0,
        title="Product price",
        description=" the price of product",
    )
    stock:int = Field(
        default=None,
        ge = 0,
        title="Stock Quantity",
        description="the number of items in stock"
    )

@app.post("/py/product")
async def create_product_with_pydantic_field(product:PyProduct):
    return product

# ----------------------------------- 4 Nested Pydantic Body Model --------------------------------------------
# submodel
class NsCategory(BaseModel):
    name:str = Field(
        title="Category Name",
        description=" the name of Category",
        max_length= 50,
        min_length=3,
    )
    discription :str = Field(
        default=None,
        title="Product discription",
        description="A brief dispriction for product",
        max_length=200,
        min_length=10
    )

# model which is used submodel
class NsProducts(BaseModel):
    name:str = Field(
        title="Product Name",
        description=" the name of product",
        max_length= 50,
        min_length=3,
        pattern="^[A-Za-z0-9 ]+$"
    )
    price:float = Field(
        gt = 0,
        title="Product price",
        description=" the price of product",
    )
    stock:int = Field(
        default=None,
        gt = 0,
        title="Stock Quantity",
        description="the number of items in stock"
    )
    category : NsCategory | None = Field(
       default=None,
       title="Product Category",
       description="The category to which the product belongs"
    )

@app.post("/ns/product")
async def create_product_with_Nested_pydantic_field(product:NsProducts):
    return product

# attribute with list of submodels
class NsProduct(BaseModel):
    name:str = Field(
        title="Product Name",
        description=" the name of product",
        max_length= 50,
        min_length=3,
        pattern="^[A-Za-z0-9 ]+$"
    )
    price:float = Field(
        gt = 0,
        title="Product price",
        description=" the price of product",
    )
    stock:int = Field(
        default=None,
        gt = 0,
        title="Stock Quantity",
        description="the number of items in stock"
    )
    category : list[NsCategory] | None = Field(
       default=None,
       title="Product Category",
       description="The category to which the product belongs"
    )

@app.post("/ns/li/product")
async def create_product_with_Nested_pydantic_field_list(product:NsProduct):
    return product

#------------------------------- Pydantic json_schema_extra ------------------------------------------

## Using Field-level Examples
class fixedProduct(BaseModel):
    name: str = Field(examples=["Moto E"])
    price: float = Field(examples=[23.56])
    stock: int | None = Field(default=None, examples=[43])

@app.post("/products/fiexed")
async def create_product_fixed(product: fixedProduct):
    return product

## Using Pydantic’s json_schema_extra
class Product_fixed(BaseModel):
  name: str
  price: float
  stock: int | None = None

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "name": "Moto E",
          "price": 34.56,
          "stock": 45
        }
      ]
    }
  }

@app.post("/products/fixed")
async def create_product_json_shema(product: Product_fixed):
    return product