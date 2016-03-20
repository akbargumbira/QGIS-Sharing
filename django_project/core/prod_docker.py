"""Configuration for production server"""
# noinspection PyUnresolvedReferences
from .settings import *  # noqa
import os
print os.environ

DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Akbar Gumbira', 'akbargumbira@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USERNAME'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': 5432,
    }
}

MEDIA_ROOT = '/home/web/media'
STATIC_ROOT = '/home/web/static'
