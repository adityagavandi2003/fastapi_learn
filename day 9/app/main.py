from fastapi import FastAPI, File, Form, HTTPException, UploadFile,Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse,JSONResponse, PlainTextResponse
from typing import Annotated
from pydantic import BaseModel
import uuid
import shutil
import os
app = FastAPI()

# single file upload handling

# form
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
        <html>
            <body>
                <h2>Single File Upload (bytes)</h2>
                <form action="/files/" enctype="multipart/form-data" method="post">
                    <input name="file" type="file">
                    <input type="submit" value="Upload">
                </form>
                <form action="/file-upload/" enctype="multipart/form-data" method="post">
                    <input name="file" type="file">
                    <input type="submit" value="Upload">
                </form>
                <h2>Single File Upload (UploadFile)</h2>
                <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                    <input name="file" type="file">
                    <input type="submit" value="Upload">
                </form>
                <h2>Multiple File Upload (UploadFile)</h2>
                <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                    <input name="file" type="file">
                    <input type="submit" value="Upload">
                </form>
            </body>
        </html>
    """


@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "File not found"}
    return {"message": "file successfully uploaded!", "Size": len(file)}


@app.post("/file-upload/")
async def upload_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "File not found"}

    filename = f"{uuid.uuid4()}.bin"
    filepath = f"upload/{filename}"

    os.makedirs("upload", exist_ok=True)

    with open(filepath, "wb") as buffer:
        buffer.write(file)

    return {"file size": len(file)}


@app.post("/uploadfile/")
async def uploadfile(file: Annotated[UploadFile | None, File()] = None):
    if not file:
        return {"message": "File not found"}

    filepath = f"upload/{file.filename}"
    os.makedirs("upload", exist_ok=True)
    with open(filepath, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "Successfully uploaded", "File": file.filename, "content type": file.content_type}

# multiple
@app.post("/uploadfiles/")
async def create_upload_file(files: Annotated[list[UploadFile], File()]):
    save_files = []
    os.makedirs("uploads", exist_ok=True)
    for file in files:
        save_path = f"uploads/{file.filename}"
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        save_files.append({"filename": file.filename})
    return save_files

@app.get("/form", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <head>
            <title>User Profile Upload</title>
        </head>
        <body>
            <h2>User Profile Form</h2>
            <form action="/user-with-file/" enctype="multipart/form-data" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username" required><br><br>
                <label for="file">Profile Picture (optional):</label><br>
                <input type="file" id="file" name="file" accept="image/*"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
@app.post("/user-with-file/")
async def create_user_with_file(
    username: Annotated[str, Form()],
    file: Annotated[UploadFile | None, File()] = None
):
    response = {"username": username}
    if file:
        save_path = f"uploads/{file.filename}"
        os.makedirs("uploads", exist_ok=True)
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        response["filename"] = file.filename
    return response

# section 9 Handling Errors
# HTTPExpection and CustomErrors
# from fastapi import FastAPI,Request,HTTPException
# from fastapi.responses import JSONResponse
# app = FastAPI()

items = {'apple':'eat apple keep away docter','banana':'nauty horare'}

## Using HTTPException
@app.get("/items/{item_id}")
async def read_item(item_id: str):
  if item_id not in items:
    raise HTTPException(status_code=404, detail="Item not found")
  return items[item_id]

# # Adding Custom Header
@app.get("/item/{item_id}")
async def read_itemPcus(item_id: str):
  if item_id not in items:
    raise HTTPException(
      status_code=404, 
      detail="Item not found",
      headers={"x-error-type": "itemmissing"}
      )
  return items[item_id]


fruits = {
  "apple": "A juicy fruit", 
  "banana": "A yellow delight"
  }


# Create Exception
class FruitException(Exception):
  def __init__(self, fruit_name: str):
    self.fruit_name = fruit_name

# Custom Exception Handler
@app.exception_handler(FruitException)
async def fruit_exception_handler(request: Request, exc: FruitException):
  return JSONResponse(
    status_code=418,
    content={"message": f"{exc.fruit_name} is not valid"}
  )

@app.get("/fruits/{fruit_name}")
async def read_fruit(fruit_name: str):
    if fruit_name not in fruits:
      raise FruitException(fruit_name=fruit_name)
    return fruits[fruit_name]

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc:RequestValidationError):
  return PlainTextResponse(str(exc), status_code=400)

@app.get("/items/req/{item_id}")
async def read_item(item_id: int):
  return item_id