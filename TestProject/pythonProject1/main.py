from fastapi import FastAPI, Path, Query, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum
from uuid import uuid4, UUID

app = FastAPI()

class PriorityStatus(str, Enum):
    HIGH = 'HIGH'
    LOW = 'LOW'
    NORMAL = 'NORMAL'

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(min_length=3, max_length=20)
    details: Optional[str]
    tags: Optional[List[str]] = Field(default_factory=list)
    priority: PriorityStatus = PriorityStatus.NORMAL

class TodoCreate(TodoUpdate):
    title: str = Field(min_length=3, max_length=20)
    details: str

class Todo(TodoCreate):
    id: Optional[int]
    # id: UUID = Field(
    #     default_factory=uuid4,
    #     primary_key=True,
    #     index=True,
    #     nullable=False,
    # )


todoList = []

@app.get("/", summary="Say Greeting")
def say_greeting():
    return "Hello World"

@app.get("/todos", summary="List of Todo", tags=["Todo"])
def getTodoList(q: str = Query(None, title="Search Text", description="Enter the text what you want to search in the list")):
    # First parameter of Query is default value
    if q:
        q = q.lower()
        return {"data": list(filter(lambda item: (
                                                    q in item.get("title").lower() or
                                                    q in item.get("details").lower() or
                                                    ("priority" in item and q in item.get("priority").lower()) or
                                                    ("tags" in item and any(tag for tag in item.get("tags") if q in tag.lower()))
                                                ), todoList))}
    return {"data": todoList}

@app.get("/todos/{id}", summary="Detail of the Todo item", tags=["Todo"])
def getTodoDetail(id: int = Path(description="The record ID of the todo element")):
    item = next(filter(lambda item: item.get("id") == id, todoList), None)
    if item:
        return {"data": item}
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Not Found"})

@app.post("/todos", summary="Create a Todo record", tags=["Todo"])
def createTodo(todo: TodoCreate):
    todoOut = dict(id=len(todoList)+1, **todo.dict(exclude_unset=True))
    todoList.append(todoOut)
    return {"data":  todoOut}

@app.put("/todos/{id}", summary="Update the Todo record", tags=["Todo"])
def updateTodo(todo: TodoUpdate, id: int = Path(description="The item ID of todo element")):
    item = next(filter(lambda item: item.get("id") == id, todoList), None)
    if item is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": f"Todo item with {id} not found"})
    item.update(todo.dict(exclude_unset=True))
    return {"message": "Todo updated successfully", "data": item}

@app.delete("/todos/{id}", summary="Delete the Todo record", tags=["Todo"])
def deleteTodo(id: int = Path(description="The item ID of todo element")):
    item = next(filter(lambda item: item.get("id") == id, todoList), None)
    if item is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": f"Todo item with {id} not found"})
    todoList.pop(todoList.index(item))
    return {"message": "Todo record deleted successfully"}