from fastapi import Body, FastAPI, Cookie, Header
from pydantic import BaseModel, Field
from typing import Annotated
app = FastAPI()

# cookie parameter


@app.get("/products/recom")
async def product_recom(session_id: Annotated[str | None, Cookie()] = None):
    if session_id:
        return {"message": f"recomended for {session_id}", "session_id": session_id}
    return {"message": "No session id provided, showing default recomendations"}

# C:\Users\asus>curl -H "Cookie: session_id=abc123" http://127.0.0.1:8000/products/recom
# {"message":"recomended for abc123","session_id":"abc123"}

# cookie paramter with pydantic


class ProductRecom(BaseModel):
    session_id: str
    preferred_category: str | None = None
    tracking_id: str | None = None


@app.get("/products/recommendations")
async def get_recommendations(cookies: Annotated[ProductRecom, Cookie()]):
    response = {"session_id": cookies.session_id}
    if cookies.preferred_category:
        response["message"] = f"Recommendations for {cookies.preferred_category} products"
    else:
        response["message"] = f"Default recommendations for session {cookies.session_id}"
    if cookies.tracking_id:
        response["tracking_id"] = cookies.tracking_id
    return response

# C:\Users\asus>curl -H "Cookie: session_id=abc123; preferred_category=Electronics; tracking_id=xyz789" http://127.0.0.1:8000/products/recommendations
# {"session_id":"abc123","message":"Recommendations for Electronics products","tracking_id":"xyz789"}

# Forbidding Extra Cookies


class ProductCookies(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str
    preferred_category: str | None = None
    tracking_id: str | None = None


@app.get("/products/recommendations/cookies")
async def get_recommendations_cookies(cookies: Annotated[ProductCookies, Cookie()]):
    response = {"session_id": cookies.session_id}
    if cookies.preferred_category:
        response["message"] = f"Recommendations for {cookies.preferred_category} products"
    else:
        response["message"] = f"Default recommendations for session {cookies.session_id}"
    if cookies.tracking_id:
        response["tracking_id"] = cookies.tracking_id
    return response

# C:\Users\asus>curl -H "Cookie: session_id=abc123; preferred_category=Electronics; tracking_id=xyz789" http://127.0.0.1:8000/products/recommendations/cookies
# {"session_id":"abc123","message":"Recommendations for Electronics products","tracking_id":"xyz789"}

# Combining Cookie with Body Parameters


class ProductCookiesC(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str = Field(
        title="Session ID", description="User session identifier")
    preferred_category: str | None = Field(
        default=None, title="Preferred Category", description="User's preferred product category")


class PriceFilter(BaseModel):
    min_price: float = Field(ge=0, title="Minimum Price",
                             description="Minimum price for recommendations")
    max_price: float | None = Field(
        default=None, title="Maximum Price", description="Maximum price for recommendations")


@app.post("/products/recommendations/com")
async def get_recommendations_combine(
    cookies: Annotated[ProductCookiesC, Cookie()],
    price_filter: Annotated[PriceFilter, Body(embed=True)]
):
    response = {"session_id": cookies.session_id}
    if cookies.preferred_category:
        response["category"] = cookies.preferred_category
    response["price_range"] = {
        "min_price": price_filter.min_price,
        "max_price": price_filter.max_price
    }
    response["message"] = f"Recommendations for session {cookies.session_id} with price range {price_filter.min_price} to {price_filter.max_price or 'unlimited'}"
    return response

# C:\Users\asus>curl -X POST -H "Cookie: session_id=abc123; preferred_category=Electronics" -H "Content-Type: application/json" -d "{\"price_filter\":{\"min_price\":50.0,\"max_price\":1000.0}}" http://127.0.0.1:8000/products/recommendations/com
# {"session_id":"abc123","category":"Electronics","price_range":{"min_price":50.0,"max_price":1000.0},"message":"Recommendations for session abc123 with price range 50.0 to 1000.0"}


# header paramters
@app.get("/products")
async def get_products(user_agent: Annotated[str | None, Header()] = None):
    return user_agent

# curl -H "User-Agent: Mozilla/5.0" http://127.0.0.1:8000/products
# "Mozilla/5.0"
# Handling Duplicate Headers


@app.get("/products/dup")
async def get_product_duplicate_headers(x_product_token: Annotated[list[str] | None, Header()] = None):
    return {
        "x_product_token": x_product_token or []
    }

# curl -H "X-Product-Token: token1" -H "X-Product-Token: token2" http://127.0.0.1:8000/products/dup
# {"x_product_token":["token1","token2"]}


# Headers with a Pydantic Model
class ProductHeaders(BaseModel):
    authorization: str
    accept_language: str | None = None
    x_tracking_id: list[str] = []


@app.get("/products/py")
async def get_product_py(headers: Annotated[ProductHeaders, Header()]):
    return {
        "headers": headers
    }

# curl -H "Authorization: Bearer token123" -H "Accept-Language: en-US" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" http://127.0.0.1:8000/products/py

# Forbidding Extra Headers


class ProductHeaders_for(BaseModel):
    model_config = {"extra": "forbid"}
    authorization: str
    accept_language: str | None = None
    x_tracking_id: list[str] = []


@app.get("/products/for")
async def get_product_py_for(headers: Annotated[ProductHeaders_for, Header()]):
    return {
        "headers": headers
    }

# curl -H "Authorization: Bearer token123" -H "Accept-Language: en-US" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" -H "extra-header: h123" http://127.0.0.1:8000/products/for
