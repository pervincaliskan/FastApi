from __future__ import annotations

from email.policy import default
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
    return {"message": "Merhaba"}
@app.post("/")
async  def post_root():
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

#@app.get("/items/")
# async def read_items_1(q: list[str] = Query(["Foo", "Bar"])):
   # results = {"items": [{"item_id" : "Foo"}, {"item_id": "Bar"}]}
   # if q:
         #results.update({"q": q})
   # return results

@app.get("/items/")
async def read_items(q: str = Query(
        default=None,
        min_length=3,
        max_length=10,
        title="Sample query string",
        description="This is a sample query string",
        alias="item-query",
)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items_hidden/")
async def hidden_query_route(hidden_query: str | None = Query(default=None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not Found"}
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}