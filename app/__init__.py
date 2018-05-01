import redis
from config import Config
from flask import Flask


app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

# connect to Redis instance
redis_db = redis.StrictRedis(host=app.config['REDIS_SERVER'],
                             port=app.config['REDIS_PORT'],
                             db=app.config['REDIS_DB'])


from app import routes
