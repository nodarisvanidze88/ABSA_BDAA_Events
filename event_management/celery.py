import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
app = Celery('event_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'update-status-every-day': {
        'task': 'membership.tasks.update_membership_status',
        'schedule': crontab(minute='*/5'),
    },
}