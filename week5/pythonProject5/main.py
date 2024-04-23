from __future__ import annotations

from typing import Union


from fastapi import FastAPI, Query
from pydantic import BaseModel


app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
   tax: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/")
async def post_root():
    return {"Hello": "World"}
@app.post("/")
async  def post_root(item : Item):
    return item
@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item : Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": item.q})
        return result
@app.post("/items")
async  def create_item_with_put(item : Item):
    item_dict=item.dict()
    price_with_tax = item.price + item.tax
    item_dict.update({"price": price_with_tax})
    return item_dict

 @app.get("/items/")
async def read_items_1(q: list[str] = Query(["param"])):
   results = {"items": [{"item_id" : "description"]};
 if q:
         results.update({"q": q})
    return results
@app.get("/items/")
async def read_items(q: str = Query(
        title="Sample query string",
        alias="item-query",
        description="This is a sample query string",
        deprecated=False,

)):
    results = {"items": [{"item_id": "param"}]}
    if q:
        results.update({"q": q})
    return results

































