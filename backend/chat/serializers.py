from rest_framework import serializers
from .models import ChatMessage, ChatRoom
from collections import OrderedDict



class MessageSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        result = super(MessageSerializer, self).to_representation(instance)
        return super([(key, result[key])]).to_representation(instance)
    
    class Meta:
        model = ChatMessage
        fields = ['__str__', 'message', 'timestamp']

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['name']