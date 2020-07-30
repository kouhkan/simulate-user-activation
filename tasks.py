import redis
from celery import Celery
from random import randint


# Configurations / CELERY
app = Celery('tasks', broker='amqp://guest@localhost//')

# Configurations / REDIS
REDIS_HOST = 'localhost'
REDIS_DB = 3
REDIS_PORT = 6379
redis = redis.Redis(host=REDIS_HOST,
                    db=REDIS_DB,
                    port=REDIS_PORT)


# CELERY main codes
@app.task
def set_active_code(user):
    result = redis.set(user, randint(1000, 9999))
    redis.expire(user, 120)

    if result:
        return True
    else:
        return False


@app.task
def check_code(user, code):
    get_code = redis.get(user)

    if get_code.decode('utf-8') == code:
        redis.delete(user)
        return True
    else:
        return False