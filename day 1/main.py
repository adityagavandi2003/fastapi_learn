from fastapi import FastAPI

app = FastAPI()

# home with get method
@app.get('/')
async def home():
    return {'message': 'Hello FastAPI'}

# view all product with get method
@app.get('/product')
async def all_product():
    return {'message': 'All Product'}

# view single product with get id method
@app.get("/product/{product_id}")
async def product(product_id: int):
    return {'response': 'View Single Product', 'id': product_id}

# post product with post method
@app.post('/product/')
async def create_product(product:dict):
    return {'response':'Create New Product','Product':product}

# update a product with put id method
@app.put('/product/{product}')
async def update_product(update_product:dict,product:int):
    return {'response':'Update Product','Product':product,'New details':update_product}

# update partial part of product with patch id method
@app.patch('/product/{product}')
async def update_partial_product(update_product:dict,product:int):
    return {'response':'Update Partial Product','Product':product,'New details':update_product}

# delete single product with delete id method
@app.delete('/product/{product}')
async def delete_product(product:int):
    return {'response':'Delete Product','Product':product}

# day 1 end 