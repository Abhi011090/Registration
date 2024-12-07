from rest_framework.permissions import BasePermission

class IsOwnerOrDirector(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['Owner', 'Director']