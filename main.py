from tasks import message


for i in range(2000):
    priority = ((i % 3)) * 3
    message.apply_async((priority,), priority=priority, queue="tasks", countdown=10)

