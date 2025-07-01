from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from account.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'password', 'username', 'first_name', 
                   'last_name', 'email', 'bio', 
                   'profile', 'following']
    
    def create(self, validated_data):
        password = validated_data['password']
        validated_data['password'] = make_password(password)
        return super().create(validated_data)
        
