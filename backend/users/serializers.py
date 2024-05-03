from django.contrib.auth.models import User
from  rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username","password"]
#         extra_kwargs = {"password": {"write_only": True}}

#         def create(self,validated_data):
#             user = User.objects.create_user(**validated_data)
#             return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username","first_name", "last_name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_staff = True
        return user