import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stock_ap.settings")
app = Celery("stock_ap")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
