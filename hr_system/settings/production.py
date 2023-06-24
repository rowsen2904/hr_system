from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DANA_PD_SECRET_KEY")

DEBUG = False
ALLOWED_HOSTS = [os.getenv("DANA_PD_ALLOWED_HOSTS", "*")]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DANA_PD_DB_NAME"), 
        'USER': os.getenv("DANA_PD_DB_USER"),
        'PASSWORD': os.getenv("DANA_PD_DB_PASSWORD"),
        'HOST': os.getenv("DANA_PD_DB_HOST"), 
        'PORT': os.getenv("DANA_PD_DB_PORT"),
    }
}
