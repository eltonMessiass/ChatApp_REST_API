from django.contrib.auth.models import User
from  rest_framework import serializers
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name","password"]
        extra_kwargs = {"password": {"write_only": True}}

    
        