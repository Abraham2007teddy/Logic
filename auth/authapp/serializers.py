# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserCheckSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
