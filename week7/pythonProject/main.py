from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field
from typing import Optional  # 1. import ekledik

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(default= None, title = "Description", max_length=300)
    price: float = Field(default= None,gt= 0,  title = "")
    tax: float | None = None

'''
@app.get("/items_validation/{item_id}")
async def read_item_validation(
    item_id: int = Path(..., title="The ID of the item to get", gt=10, ls=100),
    q: str = Query(None, description="Query parameter"),
    size: float = Query(..., gt=0, lt=7.75),
):
    results = {"item_id": item_id, "size": size}
    if q:
        results.update({"q": q})
    return results
'''
class User(BaseModel):
    username: str
    email: str

class Importance(BaseModel):
    importance: int
''''
@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int = Path(..., title="The ID of the item to", gt=10, ls=150),
        q: Optional[str] = None,  # 2. Optional kullanıldı
        item: Optional[Item] = None,  # 3. Optional kullanıldı
        # item : Item = Body (...,embed =True),
        user: User,  # 1. eksik import
      # 2. örnek ve yukarıda class ını da baseModel ile tanımladık
        # #importance : Importance

     #3. örnek
        importance: int = Body(..., description="The importance of the item")
):
    results = {"item_id": item_id}
    if q :
        results.update({"q": q})
        if item:
            results.update({"item": item})
            if user:
                results.update({"user": user})
                if importance :  # importance alanı varsa ve None değilse
                    results.update({"importance": importance})
                return results
                
                '''

