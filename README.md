# django-celery-beat-example

## Warnings
**This example does not work as intended.**

## Requirements (Must)
- rabbitmq <- (Using as `broker` and `backend_result`)
- sqlite3 (One of DataBases. Usually built-in app)

## How to Run
### On Terminal
```sh
$ pip install -r requirements.txt
$ ./manage.py makemigrations
$ ./manage.py migrate
$ python -m celery -A crontimezone.celery worker --loglevel INFO
$ python -m celery -A crontimezone.celery beat --loglevel INFO  # You need to run on other terminal.
$ ./manage.py shell
```

### Create
This reflects correctly :) -> The result is 3 because 1 + 2 = 3.
```python
>>> from django_celery_beat.models import CrontabSchedule, PeriodicTask
>>> schedule, _ = CrontabSchedule.objects.get_or_create(minute='*/1')
>>> PeriodicTask.objects.create(crontab=schedule, name='simple-add', task='demoapp.tasks.add', args='[1, 2]')
<PeriodicTask: simple-add: */1 * * * * (m/h/d/dM/MY)>
```

### Update
This does not reflect :(  -> The result is 3 yet.

But `celerybeat` is received `Schedule changed` and start `Writing entries`

```python
>>> task = PeriodicTask.objects.get(name='simple-add')
>>> task.args = '[43, 12]'
>>> task.save()
```

Restarting `celerybeat`, it reflects. But restarting to reflect this is not useful.

### Delete
This reflects correctly :) -> No result. No fired in `celerybeat`.
```python
>>> task = PeriodicTask.objects.get(name='simple-add')
>>> task.delete()
```

## My Environment
- Python 3.6.1
- Mac OS X 10.11.2 (El Capitan)
