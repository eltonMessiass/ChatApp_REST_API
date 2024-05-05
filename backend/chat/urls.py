from django.urls import path
from .views import chat_list, chat_detail, new_chat, message_list, same_chat_messages

urlpatterns = [
    path('', chat_list, name='chat-list'),
    path('new-chat/', new_chat, name='new-chat'),
    path('list/<int:pk>/', chat_detail, name='chat_detail'),
    path('messages/all-messages/', message_list, name="all-messages"),
    path('messages/all-messages/<int:pk>/', same_chat_messages, name="this-chat-messages")
]