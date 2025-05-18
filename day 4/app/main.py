from fastapi import FastAPI,Query,Path
from typing import Annotated, List
from pydantic import AfterValidator

app = FastAPI()


PRODUCTS = [
    {
        "id": 1,
        "name": "Wireless Mouse",
        "price": 599.00,
        "description": "A sleek and responsive wireless mouse with ergonomic design."
    },
    {
        "id": 2,
        "name": "Bluetooth Headphones",
        "price": 1499.00,
        "description": "Over-ear headphones with deep bass and noise cancellation."
    },
    {
        "id": 3,
        "name": "USB-C Charger",
        "price": 799.00,
        "description": "Fast-charging USB-C adapter compatible with most devices."
    },
    {
        "id": 4,
        "name": "Notebook",
        "price": 199.00,
        "description": "Hardcover ruled notebook for school or office use."
    },
    {
        "id": 5,
        "name": "Desk Lamp",
        "price": 999.00,
        "description": "LED desk lamp with adjustable brightness and flexible neck."
    }
]

# --------------------------------------Query Parameter validation part 1-----------------------------------------------------------

@app.get("/")
async def home():
    return {"message":"Welcome To Home"}

# basic query parameter
@app.get("/basicqueryparamter")
async def basicqueryparamter(search:str | None = None):
    if search:
        search_lower = search.lower()
        filtered_product = [ product for product in PRODUCTS if search_lower in product["name"].lower() ]
        return filtered_product
    return PRODUCTS
# url -> /product?search=wireless


# validation without annoted
@app.get("/validationwithoutannoted")
async def validationwithoutannoted(search:str | None = Query(default=None,max_length=5)):
    if search:
        search_lower = search.lower()
        filtered_product = [ product for product in PRODUCTS if search_lower in product["name"].lower() ]
        return filtered_product
    return PRODUCTS
# url -> /product?search=wirel

# validation with annoted
@app.get("/validationwithannoted")
async def validationwithannoted(
        search:
            Annotated[
                str|None,
                Query(max_length=5)
            ]=None):
    if search:
        search_lower = search.lower()
        filtered_product = [ product for product in PRODUCTS if search_lower in product["name"].lower() ]
        return filtered_product
    return PRODUCTS
# url -> /product?search=wirel if parameter not given display all products

# required parameter
@app.get("/requiredparameter")
async def requiredparameter(
        search:
            Annotated[
                str,
                Query(max_length=5)
            ]):
    if search:
        search_lower = search.lower()
        filtered_product = [ product for product in PRODUCTS if search_lower in product["name"].lower() ]
        return filtered_product
    return PRODUCTS
# url -> /product?search=wirel parameter is required if not given throgh an error

# add regurlar expression
@app.get("/regurlarexpression")
async def regurlarexpression(
    search:
        Annotated[
            str|None,
            Query(min_length=3,pattern="^[a-z]+$")
        ]=None
    ):
    filtered_product = [ product for product in PRODUCTS if search in product["name"].lower() ]
    return filtered_product
# url -> /product?search=mouse

# --------------------------------------Query Parameter validation part 2 -----------------------------------------------------------

# multiple search terms(list)
@app.get("/multiplesearch")
async def multiplesearch(
        search:
            Annotated[
                List[str]|None,
                Query()
            ]=None):
    if search:
        filtered_product = []
        for product in PRODUCTS:
            if any(term.lower() in product['name'].lower() for term in search):
                filtered_product.append(product)
        return filtered_product
    return PRODUCTS
# url -> /product?search=mouse&search=desk

# alias parameter 
@app.get("/alias")
async def alias(
        search:
            Annotated[
                str|None,
                Query(alias="q")
            ]=None
    ):
    if search:
        search_lower = search.lower()
        filtered_product = [ product for product in PRODUCTS if search_lower in product["name"].lower() ]
        return filtered_product
    return PRODUCTS
# url -> /product?q=mouse

# adding metadata
@app.get("/metadata")
async def metadata(search:Annotated[
        str|None,
        Query(alias='q',title="search product",description="Search by product name")
    ]=None):
    if search:
        search_lower = search.lower()
        filtered_product = [ product for product in PRODUCTS if search_lower in product["name"].lower() ]
        return filtered_product
    return PRODUCTS
# url -> /product?q=mouse

# deprecated parameter 
@app.get("/deprecated")
async def deprecated(search:Annotated[str|None,Query(deprecated=True)]=None):
    if search:
        search_lower = search.lower()
        filtered_product = [ product for product in PRODUCTS if search_lower in product["name"].lower() ]
        return filtered_product
    return PRODUCTS
# url -> /product?search=mouse

# custom validation
# from pydantic import AfterValidator
def check_valid_id(id:str):
    if not id.startswith("prod-"):
        raise ValueError("ID must start with (prod-)")
    return id

@app.get("/cusproduct")
async def get_cusproduct(id:Annotated[
    str|None,AfterValidator(check_valid_id)
]=None):
    if id:
        return {"id":id,"message":"valid parameter"}
    return {"message":"No id provided"}
# url -> /product?id=prod-1234

# path parameter validation
@app.get("/pathparametervalidation/{product_id}")
async def pathparametervalidation(product_id:int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
        return {'error':"product not found"}
# url -> /product/1

# Numeric validation
@app.get("/numericvalidation/{product_id}")
async def numeric_validation(product_id:Annotated[int,Path(ge=1,le=5)]):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return {'error':"product not found"}
# url -> /product/3

# adding metadata with path
@app.get("/metadatapath/{product_id}")
async def metadata_path(product_id:Annotated[int,Path(title="The id of the product",description="This is product id")]):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return {'error':"product not found"}
# url ->/product/3 this changes in doc

# combinig path and query parameter
@app.get("/compathquery/{product_id}")
async def compathquery(
    product_id:Annotated[int,Path(gt=0,lt=100)],
    search:Annotated[str|None,Query(max_length=20)]=None):
    for product in PRODUCTS:
        if product["id"] == product_id and search.lower() in product['name'].lower():
            return product
    return {'error':"product not found"}
# url -> /product/3?search=charger here 3 is id