from __future__ import absolute_import

import os

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

# Default is local environment
environment = os.getenv("DJANGO_SETTINGS_MODULE", "local")

if environment.endswith("production"):
    from .production import *
else:
    from .local import *
