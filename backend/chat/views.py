from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import ChatMessage, ChatRoom
from rest_framework.response import Response
from .serializers import ChatRoomSerializer
from rest_framework import status
# Create your views here.


class LobbyView(APIView):

    def get(self, request):
        user = request.user
        chat_rooms = ChatRoom.objects.filter(member=user).prefetch_related('members')
        serializer = ChatRoomSerializer(chat_rooms)
        return Response(serializer.data)
    
    def post(self, request):
        room_name = request.POST.get('room_name', None)
        user = request.user
        if room_name and user:
            try:
                chat_room = ChatRoom.objects.get(room_name=room_name)
                if user in chat_room.members.all():
                    return JsonResponse({"status": 409})
                else:
                    return JsonResponse({"status":200})
            except ChatRoom.DoesNotExist:
                return JsonResponse({"status": 404})
        return JsonResponse({"status": 400})


class RoomView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            serializer = ChatRoomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)