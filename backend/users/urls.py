from django.urls import path
from .views import ListUsersView



urlpatterns = [
    path('list-users/', ListUsersView.as_view(), name='list-users')
]