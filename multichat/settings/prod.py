from .common import *
import dj_database_url

DEBUG=False
SECRET_KEY='imasecret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#DATABASES = {
#    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'),
#                                      conn_max_age=500)
#}
