#python modules
import os

#django modules
from django.core.wsgi import get_wsgi_application

#project modules
from settings.conf import ENV_ID, ENV_POSSIBLE_OPTIONS


assert ENV_ID in ENV_POSSIBLE_OPTIONS, f"ENV_ID must be one of {ENV_POSSIBLE_OPTIONS}"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'settings.env_{ENV_ID}')

application = get_wsgi_application()
