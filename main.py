from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

app = FastAPI()

# In-memory storage
tasks = {}

# Task model
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API!"}

# Create task
@app.post("/tasks")
def create_task(task: Task):
    task_id = str(uuid4())
    tasks[task_id] = task
    return {"id": task_id, "task": task}

# Get all tasks
@app.get("/tasks")
def get_all_tasks():
    return tasks

# Get a task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    task = tasks.get(task_id)
    if task:
        return {"id": task_id, "task": task}
    return {"error": "Task not found"}

# Update a task
@app.put("/tasks/{task_id}")
def update_task(task_id: str, updated_task: Task):
    if task_id in tasks:
        tasks[task_id] = updated_task
        return {"id": task_id, "task": updated_task}
    return {"error": "Task not found"}

