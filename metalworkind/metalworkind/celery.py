import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metalworkind.settings')

app = Celery('metalworkind')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = 'Europe/Moscow'

app.conf.beat_schedule = {
    'download-currency-everyday': {
        'task': 'homepage.tasks.download_currency_rate',
        'schedule': crontab(minute=0, hour=3),
    },
    'download-metal_prices_every_3h': {
        'task': 'homepage.tasks.download_metal_prices',
        'schedule': crontab(minute='*/180'),
    },
    'parse-news-every-2h-during-office-hours': {
        'task': 'homepage.tasks.parse_news',
        'schedule': crontab(minute=0, hour='*/2,8-20'),
    },
}


