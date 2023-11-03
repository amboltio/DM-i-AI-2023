#!/bin/bash

BIND=$HOST_IP:$CONTAINER_PORT  # Address to listen on.
N_WORKERS=$N_WORKERS  # The number of workers to run in parallel (provided by default in .prod.env)
WORKER_CLASS=uvicorn.workers.UvicornWorker  # The type of workers to use.
TIMEOUT=300  # Workers silent for more than this many seconds are killed and restarted.
GRACEFUL_TIMEOUT=120  # Timeout for graceful workers restart.
MAX_REQUESTS=10000  # The maximum number of requests a worker will process before restarting (useful for preventing memory leaks)
MAX_REQUESTS_JITTER=4  # The jitter causes the restart per worker to be randomized by randint(0, max_requests_jitter). This is intended to stagger worker restarts to avoid all workers restarting at the same time.
LOG_FILE=gunicorn.log  # Access/error logs from gunicorn

exec gunicorn 'api:app' \
    --bind=$BIND \
    --workers=$N_WORKERS \
    --worker-class=$WORKER_CLASS \
    --timeout=$TIMEOUT \
    --max-requests=$MAX_REQUESTS \
    --max-requests-jitter=$MAX_REQUESTS_JITTER \
    --graceful-timeout=$GRACEFUL_TIMEOUT