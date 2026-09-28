from fastapi import FastAPI
from database import connection, cursor

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Task Management API"}

@app.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    result = []

    for task in tasks:
        result.append({
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "completed": task[3],
        })

    return result

@app.post("/tasks")
def create_tasks(title: str, description: str):
    cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
    connection.commit()

    return {
        "message": "Task created successfully"
    }

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    cursor.execute("SELECT * from tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()

    if task is None:
        return {"message": "Task not found"}

    return {
        "id": task[0],
        "title": task[1],
        "description": task[2],
        "completed": task[3],
    }


@app.put("/tasks/{task_id}")
def update_task(task_id:int, title:str, description:str):
    cursor.execute("UPDATE tasks SET title=?, description=? WHERE id=?", (title, description, task_id))
    connection.commit()

    return {"message": "Task updated successfully"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    connection.commit()
    return {"message": "Task deleted successfully"}