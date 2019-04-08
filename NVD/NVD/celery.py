import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NVD.settings')

app = Celery('NVD')
app.conf.enable_utc = False
app.autodiscover_tasks()

app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    # 'downloader': {
    #     'task': 'backend.tasks.downloader',
    #     'schedule': crontab(hour=18, minute=0),
    # },
    # 'parser': {
    #     'task': 'backend.tasks.parser',
    #     'schedule': crontab(hour=18, minute=5),
    # },
    'vendors_analyser': {
        'task': 'backend.tasks.vendors_analyser',
        'schedule': crontab(hour=22, minute=21)
    }
}
