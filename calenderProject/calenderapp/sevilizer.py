from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    user = CustomUser()
    class Meta:
        model = CustomUser
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'date_of_birth', 
            'phone_number', 
            'email_confirmed', 
            'token', 
            'date_joined', 
            'last_login', 
            'is_active', 
            'is_staff', 
            'is_superuser'
        ]

    # def create(self, validated_data):
    #     user = CustomUser.objects.create(**validated_data)
    #     return user