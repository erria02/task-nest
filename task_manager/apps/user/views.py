from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserModel, UserSerializer, ProfileSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
# Create your views here.

class UserCreateApi(CreateAPIView):
    serializer_class=UserSerializer
    
class UpdateProfileUserApi(UpdateAPIView):
    serializer_class=ProfileSerializer
    permission_classes=(IsAuthenticated,)
    
    def get_object(self):
        return self.request.user.profile
    
class RemoveUserApi(DestroyAPIView):
    serializer_class=UserSerializer
    permission_classes=(IsAdminUser)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
