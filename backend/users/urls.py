from django.urls import path
from .views import ListUsersView, UserDetailView



urlpatterns = [
    path('list-users/', ListUsersView.as_view(), name='list-users'),
    path('user/details/', UserDetailView.as_view(), name="user_detail")
]