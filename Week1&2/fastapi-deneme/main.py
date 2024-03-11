from fastapi import FastAPI

# FastAPI uygulamasını oluştururuz
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}