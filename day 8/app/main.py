from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel,Field

app = FastAPI()

# form handling with response class http response
@app.get("/",response_class=HTMLResponse)
async def userlogin():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Login Form</title>
        </head>
        <body>
            <h2>Login Form</h2>
            <form action="/py/login/validate" method="post">
                <label for="username">username:</label><br>
                <input type="username" id="username" name="username"><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>        
    """

@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username, "password_length": len(password)}

# validate login form
@app.post("/login/verfication/")
async def validate_login(
    username: Annotated[str, Form(min_length=3)], 
    password: Annotated[str, Form(min_length=3, max_length=20)]
    ):
    return {"username": username, "password_length": len(password)}

# pydantic models for form 
class FormData(BaseModel):
    username: str
    password: str

@app.post("/py/login/")
async def py_login(data:Annotated[FormData,Form()]):
    return data

# Pydantic Models for Forms with Validation
class FormDataVal(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=3, max_length=20)
    model_config = {"extra": "forbid"}

@app.post("/py/login/validate")
async def py_login_validate(data:Annotated[FormDataVal,Form()]):
    return data