from rest_framework import serializers
from .models import Chat, Message



class ChatSerializer(serializers.ModelSerializer):
    other_participant = serializers.SerializerMethodField()
    class Meta:
        model = Chat
        fields = ['id', 'user1', 'user2', 'other_participant']
        # extra_kwargs = {"participants": {"read_only": True}}

    def get_other_participant(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            if obj.user1 == request.user:
                return obj.user2.username
            return obj.user1.username
        
    

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','chat', 'message_sender', 'content']