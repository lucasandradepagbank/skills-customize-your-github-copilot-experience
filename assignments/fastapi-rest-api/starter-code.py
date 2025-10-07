from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []

class Task(BaseModel):
    tarefa: str

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: Task):
    if not task.tarefa:
        raise HTTPException(status_code=400, detail="O campo 'tarefa' não pode estar vazio.")
    new_task = {"id": len(tasks) + 1, "tarefa": task.tarefa}
    tasks.append(new_task)
    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks.pop(i)
            return {"detail": "Tarefa removida com sucesso."}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
