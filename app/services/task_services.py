from sqlalchemy.orm import Session
from ..models import Task
from ..schemes import TaskCreate, TaskUpdate

def create_task(db: Session, task: TaskCreate, user_id: int):
    new_task = Task(
        title=task.title,
        description=task.description,
        owner_id=user_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session, user_id: int):
    return db.query(Task).filter(Task.owner_id == user_id).all()

def get_task(db: Session, task_id: int, user_id: int):
    return db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()

def update_task(db: Session, task_id: int, user_id: int, task_data: TaskUpdate):
    task = get_task(db, task_id, user_id)
    if task:
        for key, value in task_data.dict(exclude_unset=True).items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int, user_id: int):
    task = get_task(db, task_id, user_id)
    if task:
        db.delete(task)
        db.commit()
    return task