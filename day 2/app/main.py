from fastapi import FastAPI

app = FastAPI()

# first crud app 
products = [
    {
        "name": "Wireless Mouse",
        "price": 499.00,
        "description": "Compact wireless mouse with ergonomic design."
    },
    {
        "name": "Bluetooth Headphones",
        "price": 1599.00,
        "description": "Over-ear headphones with deep bass and noise cancellation."
    },
    {
        "name": "USB-C Charger",
        "price": 899.00,
        "description": "Fast-charging USB-C wall charger, 25W output."
    },
    {
        "name": "Laptop Stand",
        "price": 749.00,
        "description": "Adjustable aluminum laptop stand for better posture."
    },
    {
        "name": "32GB Pen Drive",
        "price": 299.00,
        "description": "Portable 32GB USB 3.0 pen drive for fast data transfer."
    }
]

# view all product
@app.get("/product")
async def View_product():
    return {'message':'Here are new Products','products':products}

# get a specific index data from product list
@app.get("/product/{product_id}")
async def product(product_id:int):
    for index,product in enumerate(products):
        if index == product_id:
            data = product
    return {'message':"here are data of this product", 'product ID':product_id,'proudct':data}

# create a new product with post method
@app.post("/product")
async def create_product(product:dict):
    products.append(product)
    return {'message':"here are data of this product",'new_product':product,'proudct':products}

# use put for update full data
@app.put("/product/{product_id}")
async def update_product(product_id:int,productss:dict):
    for index,product in enumerate(products):
        if index == product_id-1:
            products[product_id].update(productss)
    return {'message':"here are data of this product",'product_id':product_id,'new_product':productss,'proudct':products[product_id]}

# use patch for update_partial_data_of_product
@app.patch("/product/{product_id}")
async def update_partial_data_of_product(product_id:int,productss:dict):
    for index,product in enumerate(products):
        if index == product_id-1:
            products[product_id].update(productss)
    return {'message':"here are data of this product",'product_id':product_id,'new_product':productss,'proudct':products[product_id]}

# use delete for delete a single product
@app.delete("/product/{product_id}")
async def delete(product_id:int):
    index = product_id - 1
    delete_product = products.pop(index)
    return {'message':"here are data of this product",'product_id':product_id,'proudct':delete_product}
