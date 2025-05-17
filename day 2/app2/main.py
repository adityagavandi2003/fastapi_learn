from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# path converter
@app.get("/files/{file_path:path}")
async def files(file_path:str):
    return {'message':'This is file path','file_path':file_path}

# predifined values (Enum)
class ProductCategory(str,Enum):
    books = "books"
    clothing = "clothing"
    mechanics = "mechanics"

# Enum as type for the path parameter
@app.get("/products/{product}")
async def product(product:ProductCategory):
    if product == ProductCategory.books:
        return {"Category":product,"Message":"Exllenant Choice"}
    elif product.value == "clothing":
        return {"Category":product,"Message":"Great Choice"}
    elif product == ProductCategory.mechanics.value:
        return {"Category":product,"Message":"Nice Choice"}
    else:
        return {"Product":product,'message':'unknown category'}