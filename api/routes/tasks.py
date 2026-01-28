from fastapi import APIRouter
from core.celery_app import celery_app
from celery.result import AsyncResult

router = APIRouter()

@router.post("/submit")
def submit_task(payload: dict):
    task = celery_app.send_task(
        "worker.tasks.heavy_task.process_data",
        args=[payload],
    )
    return {"task_id": task.id, "status": "submitted"}

@router.get("/{task_id}")
def get_task(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.successful() else None
    }
