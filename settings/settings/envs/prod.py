# Project modules
from settings.base import *


DEBUG = False
ALLOWED_HOSTS = ["*"]

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}