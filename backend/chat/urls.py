from django.urls import path
from .views import chat_list, chat_detail, new_chat, message_list, same_chat_messages, send_message, delete_message, loged_user_chats

urlpatterns = [
    path('', loged_user_chats, name='chat-list'),
    path('new-chat/', new_chat, name='new-chat'),
    path('list/<int:pk>/', chat_detail, name='chat_detail'),
    path('messages/all-messages/', message_list, name="all-messages"),
    path('messages/all-messages/<int:pk>/', same_chat_messages, name="this-chat-messages"),
    # path('messages/send/', send_message, name="send-message")
    path('messages/send/<int:pk>/', send_message, name="send_message"),
    path('messages/delete/<int:pk>/', delete_message, name="delete_message")
]