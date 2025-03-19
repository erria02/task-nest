from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdminUser
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()
# Create your views here.

class GetMe(RetrieveAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
    
class ListUserApiView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    
class CreateUserApiView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()