from rest_framework.decorators import api_view
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.response import Response
from .models import Chat, Message
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User




@api_view(['GET'])
def chat_list(request):
    if request.method == 'GET':
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True, context={'request': request})
        return Response(serializer.data)
        
@api_view(['POST'])
def new_chat(request):
    user_id1 = request.POST.get('id')
    user_id2 = request.POST.get('id')

    user1 = get_object_or_404(User, id=user_id1)
    user2 = get_object_or_404(User, id=user_id2)
    try:
        chat = Chat.objects.filter(user1=user1, user2=user2)
        if chat.exists():
            return Response('chat already exists')
        else:
            new_chat = Chat.objects.create(user1=user1, user2=user2)
            serializer = ChatSerializer(new_chat)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
        
@api_view(['GET', 'DELETE'])
def chat_detail(request, pk):
    try:
        chat = Chat.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
                   
    if request.method == 'GET':
        
        if request.user == chat.user1:
            other_participant = chat.user2
        else:
            other_participant = chat.user1
        serializer = ChatSerializer(chat)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        try:
            chat.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET'])
def message_list(request):
    messages = Message.objects.all()
    serializer = MessageSeriazer(messages, many=True)

    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def same_chat_messages(request, pk):
    messages = Message.objects.filter(chat__id=pk)
    serializer = MessageSerializer(messages, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)