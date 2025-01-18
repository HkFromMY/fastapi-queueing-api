from fastapi import FastAPI, APIRouter
from redis import Redis
from rq import Queue, Callback
from ..tasks.tasks import background_task
from ..utils.discord import report_success
from ..configs.constants import REDIS_HOST, REDIS_QUEUE

redis_conn = Redis(host=REDIS_HOST, port=6379)
queue = Queue(REDIS_QUEUE, connection=redis_conn)

router = APIRouter(
    prefix='/jobs',
    tags=['jobs'],
)

@router.post("/{seconds}")
async def enqueue_job(seconds: int):
    
    job = queue.enqueue(
        background_task, seconds,
        on_success=Callback(report_success),
    )
    return {"job_id": job.id}

@router.get("/{job_id}")
async def get_job_status(job_id: str):
    job = queue.fetch_job(job_id)
    return {"job_id": job.id, "status": job.get_status() if job else "not found"}
