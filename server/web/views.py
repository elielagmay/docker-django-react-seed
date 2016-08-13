import os
from django.conf import settings
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        return {
            'WEBPACK_DEV_SERVER': settings.DEBUG
        }

    # def get(self, request):
    #     static_dir = settings.STATICFILES_DIRS[0]
    #     template_name = 'index.html'
    #     template_path = open(os.path.join(static_dir, template_name), 'r')
    #     return HttpResponse(content=template_path.read())
