from rest_framework import serializers
from registration.models import UserRegistration

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'mobile_no', 
            'whatsapp_no', 
            'company_name', 
            'registration_no', 
            'vat_no', 
            'address', 
            'role', 
            'designation'
        ]
        extra_kwargs = {
            "password": {"write_only": True},  
        }

    def create(self, validated_data):
        password = validated_data.pop("password")  
        user = UserRegistration(**validated_data)
        user.set_password(password)  
        user.save()
        return user
