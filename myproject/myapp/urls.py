from rest_framework.views import APIView
from django.urls import path
from .views import UserInfoView

urlpatterns = [
    path('users/', UserInfoView.as_view(), name='user_list'),  # List all profiles or create a new profile
    path('users/<int:pk>/', UserInfoView.as_view(), name='user_detail'),  # Retrieve, update, or delete a profile by pk
]
