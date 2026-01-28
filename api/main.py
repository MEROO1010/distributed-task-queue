from fastapi import FastAPI
from routes.tasks import router as task_router

app = FastAPI(title="Distributed Task Queue System")

app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
