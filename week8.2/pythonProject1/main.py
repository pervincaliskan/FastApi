from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

# JSON schema ekstra özelliklerini sınıfın başında tanımlayalım
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Pervin",
                    "description": "Pervin is a nice girl",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
