import os

from celery import Celery

#shezhi huanjing bianliang jiazai django de settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','swiper3.settings')


celery_app = Celery('swiper3')
celery_app.config_from_object('worker.config')
celery_app.autodiscover_tasks()

def call_by_worker(func):
    task = celery_app.task(func)
    return task.delay