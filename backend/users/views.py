# from django.http import JsonResponse
# from django.shortcuts import render
from .serializers import UserSerializer
from django.contrib.auth.models import User
# from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
from rest_framework import generics


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
        
                
                
class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]