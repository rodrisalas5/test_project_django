from .base import *
from pathlib import Path
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': 5432,
        'USER': 'admin',
        'PASSWORD': 'admin',
        'NAME': 'db_test_project',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = ['static'] 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')