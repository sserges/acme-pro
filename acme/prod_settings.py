import dj_database_url

from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = "i=9c8j#miy0b$e(*kn13s#=82w4nu7g7)11)!fm_+yuogtsw]@"

ALLOWED_HOSTS = [
    'acme-pro.herokuapp.com',
]