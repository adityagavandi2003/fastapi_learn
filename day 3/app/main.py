from fastapi import FastAPI,status
from typing import Optional

app = FastAPI()

@app.get("/")
async def home():
    return {"message":"Welcome"}

# query parameter

# single query parameter
@app.get("/product")
async def product(category:str):
    return {"status":"OK","category":category}
# url -> /product?category=books
# status	"OK"
# category	"books"


# multiple query parameter
# @app.get("/search")
# async def search(category:str,limit:int):
#     return {"status":"OK","category":category,"limit":limit}
# url -> /search?category=books&limit=5
# status	"OK"
# category	"books"
# limit	     5

# default query parameter
# @app.get("/search")
# async def search(category:str,limit:int=10):
#     return {"status":"OK","category":category,"limit":limit}
# url -> /search?category=books
# status	"OK"
# category	"books"
# limit	    10

# optional query parameter
@app.get("/search")
async def search(limit: int, category: Optional[str] = None):
    return {"status": "OK", "category": category, "limit": limit}
# url -> /search?limit=5
# status	"OK"
# category	null
# limit	     5

# path and query parameter
@app.get("/product/{year}")
async def product(year:str,category:str):
    return {"status": "OK", "category": category, "year": year}
# url -> /product/2025?category=books
# status	"OK"
# category	"books"
# year	    "2025"

# response status code
# 100 - 199 are for "information"
# 200 - 299 are for "successful"
#       200 - OK
#       201 - created
#       204 - No content

# 300 - 399 are for "Redirection"
#       304 - not modified

# 400 - 499 are for "Client Error Response"
#       404 - Not found
#       400 - Generic Found

# 500 - 599 are for "Server Error"

# without status import
@app.get("/success",status_code=200) # "GET /success HTTP/1.1" 200
async def success():
    return {"message":"200"}

# with status import for 200
@app.get("/success",status_code=status.HTTP_200_OK) # "GET /success HTTP/1.1" 200
async def success():
    return {"status":"200","message":"200 Successful"}

# with status import for 201
@app.get("/created",status_code=status.HTTP_201_CREATED) # "GET /success HTTP/1.1" 201
async def created():
    return {"status":"200","message":"201 Created"}