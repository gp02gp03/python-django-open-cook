
from .settings import *
import dj_database_url
DEBUG = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')
STATIC_ROOT = 'staticfiles'
DATABASES ={
    'default': dj_database_url.config()
}

# 允許所有網址連到此網站
ALLOWED_HOSTS = ['*']