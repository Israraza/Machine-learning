from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the TODO API"}

@app.post("/todos/", response_model=schemas.TodoItem)
def create_todo_item(todo: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    return crud.create_todo_item(db=db, todo=todo)

@app.get("/todos/", response_model=list[schemas.TodoItem])
def read_todo_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_todo_items(db=db, skip=skip, limit=limit)


