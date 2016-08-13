from django.conf import settings
import json

assets = {}

if not settings.WEBPACK_DEV_BUNDLE:
    filename = settings.WEBPACK_DIST_JSON
    try:
        with open(filename, 'r') as f:
            assets = json.load(f)['main']
    except Exception:
        raise Exception('Failed to read %s. Was frontend built?' % filename)


def webpack(request):
    return {
        "WEBPACK_DEV_BUNDLE": settings.WEBPACK_DEV_BUNDLE,
        "WEBPACK_DIST_ASSETS": assets
    }
