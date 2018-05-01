import redis
from config import Config
from flask import Flask
from app.utils import make_celery


app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

# connect to Redis instance
redis_db = redis.StrictRedis(host=app.config['REDIS_SERVER'],
                             port=app.config['REDIS_PORT'],
                             db=app.config['REDIS_DB'])
celery = make_celery(app)


from app import routes
