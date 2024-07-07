from sqlalchemy.orm import Session
from . import models, schemas

def get_todo_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TodoItem).offset(skip).limit(limit).all()

def create_todo_item(db: Session, todo: schemas.TodoItemCreate):
    db_todo = models.TodoItem(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
