from .common import *
import dj_database_url

DEBUG=False
SECRET_KEY='imasecret'
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'),
                                      conn_max_age=500)
}
