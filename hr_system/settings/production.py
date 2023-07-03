from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DANA_PD_SECRET_KEY")

DEBUG = False
ALLOWED_HOSTS = [os.getenv("DANA_PD_ALLOWED_HOSTS", "*")]
