from fastapi import FastAPI
from pydantic import BaseModel
from typing import List  # List tipini ekledik

app = FastAPI()

class Address(BaseModel):
    city: str
    street: str
    zip_code: str

class User(BaseModel):
    name: str
    age: int
    addresses: List[Address]  # 'Address' sınıfını burada kullanmalısınız.

@app.post("/users")
async def create_user(user: User):
    return {"user": user}
