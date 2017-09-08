from .settings import *
import dj_database_url
import urllib.parse


DEBUG=False
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'),
                                      conn_max_age=500)
}


redis_url = urllib.parse.urlparse(os.environ.get('REDIS_URL'))

# Channel layer는 heroku사의 heroku redis를 사용할 것임.
# 셋팅방법은 아래 url 참고.
# https://devcenter.heroku.com/articles/heroku-redis#connecting-in-django

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "ROUTING": "multichat.routing.channel_routing",
        "CONFIG": {
            "hosts": ['redis://h:p8caa905e339be0892c72bf56803dbc91874909d7ba639f86db4205d720ac1e8b@ec2-34-233-163-137.compute-1.amazonaws.com', 24499],
        },
    },
}

