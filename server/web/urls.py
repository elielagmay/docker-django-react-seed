from django.conf.urls import url, include
from api.admin import admin_site
from . import views

urlpatterns = [
    url(r'^admin/', admin_site.urls),
    url(r'^api/', include('api.urls', namespace='api')),

    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^.*/$', views.IndexView.as_view()),
]
