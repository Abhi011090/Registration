from django.urls import path, include
from rest_framework.routers import DefaultRouter
from registration.views import UserRegistrationView

# Create a router and register the view
router = DefaultRouter()
router.register(r'users', UserRegistrationView, basename='user')

urlpatterns = [
    path('', include(router.urls)),  # This will map /api/ to the router's URLs
]
