# -*- coding: utf-8 -*-

DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.splite3',
    }
}

# update setting
import dj_database_url
db_from_env = dj_databese_url.config(conn_max_age=400)
DATABASES['default'].update(db_from_env)
