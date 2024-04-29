from django.urls import path
from .views import chat_list, chat_detail

urlpatterns = [
    path('list/', chat_list, name='chat-list'),
    path('list/<int:pk>/', chat_detail, name='chat_detail'),
]