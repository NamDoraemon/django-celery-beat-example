import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crontimezone.settings')

app = Celery('crontimezone')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
