import os
from .settings import *

DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

MEDIA_ROOT = os.environ.get('DJANGO_MEDIA_ROOT','/code/media/')
MEDIA_URL = os.environ.get('DJANGO_MEDIA_URL', '/media/')
STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT', '/code/static/')
STATIC_URL = os.environ.get('DJANGO_STATIC_URL', '/static/')
LOGIN_URL = os.environ.get('DJANGO_LOGIN_URL', '/login/')
LOGOUT_URL = os.environ.get('DJANGO_LOGOUT_URL', '/logout/')
LOGIN_REDIRECT_URL = os.environ.get('DJANGO_REDIRECT_URL', '/')

ADMIN_LOGIN_NETWORK_REGEXP = os.environ.get('DJANGO_ADMIN_LOGIN_NETWORK_REGEXP', '')

ALLOWED_HOSTS = [os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost')]
ADMINS = (
    ('Administrator', os.environ.get('DJANGO_ADMIN_EMAIL')),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DJANGO_DB_NAME', 'postgres'),
        'USER': os.environ.get('DJANGO_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', ''),
        'HOST': 'db',  # extra_hosts or link
        'PORT': '5432',
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_HOST_USER', 'example@example.com')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_HOST_PASSWORD', 'password')
EMAIL_PORT = 587
EMAIL_BACKEND = os.environ.get('DJANGO_EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')

# セッションの有効期限をブラウザを閉じるまでに
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

