from rest_framework.viewsets import ModelViewSet
from reversion.views import RevisionMixin
from . import models, serializers


class UserViewSet(RevisionMixin, ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
