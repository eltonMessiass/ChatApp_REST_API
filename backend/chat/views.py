from django.urls import reverse
from rest_framework.decorators import api_view
from .serializers import ChatSerializer
from rest_framework.response import Response
from .models import Chat
from rest_framework import status
from django.shortcuts import redirect




@api_view(['GET', 'POST'])
def chat_list(request):
    if request.method == 'GET':
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET', 'DELETE'])
def chat_detail(request, pk):
    try:
        chat = Chat.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = ChatSerializer(chat)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        try:
            chat.delete()
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)