from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yx6&zuhuwx(=pu_fo@t0qy#00)w5$c*uyezz9&)g06_v6^6505'

# Django is_debug and Allowed Hosts
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Internal IPs for Django Debug Toolbar
INTERNAL_IPS = [
    "127.0.0.1"
]

# Django Installed Apps
INSTALLED_APPS += ["debug_toolbar"]

# Django Middlewares
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# Local Memory Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
