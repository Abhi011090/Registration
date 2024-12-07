from rest_framework import viewsets, permissions
from registration.models import UserRegistration
from registration.serializers import UserRegistrationSerializer

class UserRegistrationView(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
