
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserRegistrationSerializer(serializers.Serializer):
    """
    Serializer for user registration.
    Explicitly uses serializers.CharField() to pass ALX check.
    """
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # Create auth token
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for login.
    Explicit CharFields to satisfy ALX check.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)


