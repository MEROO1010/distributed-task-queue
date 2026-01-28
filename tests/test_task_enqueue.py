from api.core.celery_app import celery_app

def test_task_enqueue():
    task = celery_app.send_task(
        "worker.tasks.heavy_task.process_data",
        args=[{"test": "data"}],
    )
    assert task.id is not None
