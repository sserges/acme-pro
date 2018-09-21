import dj_database_url

from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = "x*(^3n(^)p%6vhig$l_#924qnw2jl-favui9mo2r4m4wx!wit("

ALLOWED_HOSTS = [
    'acme-pro.herokuapp.com',
]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
