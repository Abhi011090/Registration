from django.contrib import admin

from django.contrib import admin
from registration.models import UserRegistration

class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role', 'designation', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_editable = ('designation',)  


    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

# Register the model with the custom admin class
admin.site.register(UserRegistration, UserRegistrationAdmin)
