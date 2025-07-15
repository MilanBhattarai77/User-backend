from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import UserInfo 
from .serializers import UserInfoSerializer
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    url(r'^$', schema_view)
]




class UserInfoView(APIView):
    """
    Handles CRUD operations for UserInfo model.
    List is public; all other actions require authentication.
    """



    def get_permissions(self):
        """
        Dynamically assign permissions based on the request method.
        """
        if self.request.method == 'GET' and self.kwargs.get('pk') is None:
            return [AllowAny()]
        return [IsAuthenticated()]



    def get_object(self, pk):
        try:
            return UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            return None



    def get(self, request, pk=None):
        if pk:
            user = self.get_object(pk)
            if user is None:
                return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserInfoSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Public list
            users = UserInfo.objects.all()
            serializer = UserInfoSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)



    def post(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def patch(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserInfoSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def put(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({'message': 'User deleted.'}, status=status.HTTP_200_OK)
