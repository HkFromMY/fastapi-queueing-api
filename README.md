# fastapi-queueing-api

Same issue:
https://stackoverflow.com/questions/76593563/redis-queue-task-is-queued-but-never-executed

basically need add __init__.py in the /app according to the sources below

From https://python-rq.org/docs/#considerations-for-jobs
Make sure that the function’s __module__ is importable by the worker. In particular, this means that you cannot enqueue functions that are declared in the __main__ module.

Self-reflection:
1. Please make sure the source code of both worker and worker generator (producer) are the same.
2. Make sure where you create the worker can access the source code of tasks. [Better if outside /app]
