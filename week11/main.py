from fastapi import FastAPI, HTTPException, Body, Request, Query, Path, Cookie, Header
from fastapi.responses import JSONResponse
from enum import Enum
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"x-Error": "There goes my error"},
        )
    return {"item": items[item_id]}

class UnicornException(Exception):
        def __init__(self,name: str):
            self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request,exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message":f"Oops ! {exc.name} did something wrong. There goes a rainbow.."},
    )
@app.get("unicorns/{name}")
async def read_unicorns(name: str):
        if name == "yolo":
            raise UnicornException(name= name)
        return {"unicorn_name": name}
@app.exception_handler(StarletteHTTPException)
async def custom_htpp_exception(request,exc):
    print(f"OMG! aN http ERROR:  {repr(exc)}")
    return await http_excepiton_handler(request,exc)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request,exc):
    print(f"OMG! The client sent invalid data!:  {exc}")
    return await request_validation_excepiton_handler(request,exc)


@app.get("/blash_items/{item_id}")
async def blash_items(item_id: int):
    if item_id ==3:
        raise HTTPException(status_code=418, detail="Nope Y don't like 3")
    return{"item_id": item_id}