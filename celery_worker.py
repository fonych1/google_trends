import os

from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

from file_handler import FileHandler
from trends import TrendAnalyzer

load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=0, hour='*/4'), analyze_trends.s(), name='every minute')


@celery.task
def analyze_trends():
    analyzer = TrendAnalyzer()
    analyzer.data()
    FileHandler.to_csv(df=analyzer.dataframe)
