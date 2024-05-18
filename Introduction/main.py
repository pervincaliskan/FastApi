from fastapi import FastAPI

app = FastAPI()


@app.get("/", description= "This is our first route") # path operation decorator
# @app.get("/", description= "This is our first route", deprecated=True ) -> we can say deprecated(kullanımdan kaldırıldığını) equals true
async def root(): #root route
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}