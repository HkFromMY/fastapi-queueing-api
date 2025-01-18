from redis import Redis
from rq import Queue, Worker

conn = Redis('redis', port=6379)
queue = Queue('task_queue', connection=conn)

worker = Worker([queue], connection=conn)
worker.work()
