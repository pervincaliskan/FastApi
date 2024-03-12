from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    tax: float [bool, None] = None


@app.get("/")
def read_root():
    return {"message": "Merhaba"}

@app.post("/")
async  def post_root(item : Item):
    return item

@app.post("/items")
async  def create_item(item : Item):
    item_dict=item.dict()
    price_with_tax = item.price + item.tax
    item_dict.update({"price": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item : Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": item.q})
        return result

