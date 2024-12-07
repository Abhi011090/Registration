from rest_framework.viewsets import ModelViewSet

from registration.permissions import IsOwnerOrDirector
from registration.models import CustomUser
from registration.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update', 'partial_update']:
            return [IsAuthenticated()]
        elif self.action in ['destroy']:
            return [IsAdminUser()]
        return super().get_permissions()

    # def get_permissions(self):
    #     if self.action in ['create', 'destroy']:
    #         return [IsOwnerOrDirector()]
    #     return [IsAuthenticated()]
