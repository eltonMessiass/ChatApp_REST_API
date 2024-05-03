from django.urls import path
from .views import chat_list, chat_detail, new_chat

urlpatterns = [
    path('', chat_list, name='chat-list'),
    path('new-chat/', new_chat, name='new-chat'),
    path('list/<int:pk>/', chat_detail, name='chat_detail'),
]