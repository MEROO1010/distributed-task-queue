import time
import random
from celery import shared_task

@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
)
def process_data(self, payload: dict):
    time.sleep(5)
    if random.random() < 0.3:
        raise Exception("Random failure")
    return {
        "input": payload,
        "summary": f"Processed {len(str(payload))} characters"
    }
