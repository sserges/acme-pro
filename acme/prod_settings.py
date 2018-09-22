import dj_database_url

from .settings import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = [
    'acme-pro.herokuapp.com',
]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
