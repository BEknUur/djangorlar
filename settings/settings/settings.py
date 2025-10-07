







# Import base settings and environment-specific settings
from settings.base import *
from settings.conf import ENV_ID

# Import environment-specific settings
if ENV_ID == "local":
    from settings.envs.local import *
elif ENV_ID == "prod":
    from settings.envs.prod import *
else:
    # Default to local if ENV_ID is not set properly
    from settings.envs.local import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
