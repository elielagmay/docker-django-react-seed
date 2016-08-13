from rest_framework.routers import DefaultRouter
from .account.views import UserViewSet

router = DefaultRouter(trailing_slash=True)

router.register(r'users', UserViewSet)

urlpatterns = router.urls
