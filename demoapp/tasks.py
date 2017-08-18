from crontimezone.celery import app


@app.task
def add(x, y):
    print(x, y)
    return x + y
