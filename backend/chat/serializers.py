from rest_framework import serializers
from .models import Chat, Message



class ChatSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField()
    class Meta:
        model = Chat
        fields = ['id', 'participants']
        extra_kwargs = {"participants": {"read_only": True}}

    def get_participants(self, obj):
        return [participant.username for participant in obj.participants.all()]
    

class MessageSeriazer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','chat', 'sender', 'content']