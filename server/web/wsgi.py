import os
from django.core.wsgi import get_wsgi_application


settings_module = "web.settings.local"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
application = get_wsgi_application()
