import os
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name, default_value=None):
    """ Get the environment variable or return exception """
    try:
        var = os.environ[var_name]
    except KeyError:
        if default_value is None:
            error_msg = 'Set the %s environment variable' % var_name
            raise ImproperlyConfigured(error_msg)
        else:
            return default_value
    return var


SERVER_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROJECT_DIR = os.path.dirname(SERVER_DIR)

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

DEBUG = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'reversion',
    'rest_framework',

    'api',
    'api.account',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(SERVER_DIR, 'templates')
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'web.context_processors.webpack',
            )
        }
    },
]

ROOT_URLCONF = 'web.urls'
WSGI_APPLICATION = 'web.wsgi.application'
AUTH_USER_MODEL = 'account.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'postgres',
        'NAME': get_env_variable('POSTGRES_DB'),
        'USER': get_env_variable('POSTGRES_USER'),
        'PASSWORD': get_env_variable('POSTGRES_PASSWORD'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(SERVER_DIR, 'assets'),
]

WEBPACK_DEV_BUNDLE = False
WEBPACK_DIST_JSON = False

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_THOUSAND_SEPARATOR = True
NUMBER_GROUPING = 3

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
}
