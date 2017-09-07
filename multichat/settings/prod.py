from .common import *
import dj_database_url

DEBUG=False
SECRET_KEY=os.environ.get('SECRET_KEY')
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'),
                                      conn_max_age=500)
}
