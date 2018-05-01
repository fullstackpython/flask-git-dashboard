import os


class Config(object):
    DEBUG = os.getenv('DEBUG') or True
    SECRET_KEY = os.getenv('SECRET_KEY') or 'development key'


    # Redis
    REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'
    REDIS_PORT = os.getenv('REDIS_PORT') or 6379
    REDIS_DB = os.getenv('REDIS_DB') or 1
    REDIS_URL = 'redis://{}:{}'.format(REDIS_SERVER, REDIS_PORT)

    # Celery task queue
    CELERY_URL = os.getenv('CELERY_BROKER_URL') or 'redis://localhost:6379'
    CELERY_BACKEND = os.getenv('CELERY_BACKEND') or 'redis://localhost:6379'

