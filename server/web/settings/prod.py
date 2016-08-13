import os
from .base import *  # NOQA
from .base import PROJECT_DIR, SERVER_DIR, STATICFILES_DIRS, get_env_variable

DEBUG = False

ALLOWED_HOSTS = [
    get_env_variable('HOST_NAME'),
]

WEBPACK_DIST_JSON = os.path.join(PROJECT_DIR, 'client', 'dist', 'assets.json')

STATICFILES_DIRS += [
    os.path.join(SERVER_DIR, 'assets'),
]
