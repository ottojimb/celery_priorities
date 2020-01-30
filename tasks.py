from celery import Celery
from kombu import Exchange, Queue

app = Celery()
celeryconfig = {}
celeryconfig["BROKER_URL"] = "amqp://"
celeryconfig["CELERY_QUEUES"] = (
    Queue(
        "tasks",
        Exchange("tasks"),
        routing_key="tasks",
        queue_arguments={"x-max-priority": 10},
    ),
)
celeryconfig["CELERY_ACKS_LATE"] = True
celeryconfig["CELERYD_PREFETCH_MULTIPLIER"] = 1
app.config_from_object(celeryconfig)


@app.task
def add(x, y):
    return x + y


@app.task
def message(priority=0):
    return f"priority {priority}"
