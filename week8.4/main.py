from enum import Enum
from typing import List, Optinol,Annotated
from fastapi import FastAPI,Query ,Path ,Body , Cookie, Headrer
from pydantic import BaseModel, Field


app = FastAPI()
@app.get("/")
async  def root():
    return {"message": "hello"}
class Item(BaseModel):
    name : str


