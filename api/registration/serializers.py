from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'mobile_number', 'whatsapp_number', 'company_name',
            'registration_no', 'vat_no', 'address', 'role', 'designation', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            mobile_number=validated_data['mobile_number'],
            whatsapp_number=validated_data.get('whatsapp_number'),
            company_name=validated_data['company_name'],
            registration_no=validated_data['registration_no'],
            vat_no=validated_data['vat_no'],
            address=validated_data['address'],
            role=validated_data['role'],
            designation=validated_data['designation']
        )
        user.set_password(validated_data['password'])  
        user.save()
        return user
