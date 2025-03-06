from django.shortcuts import render
from apps.user.serializers import UserModel, UserSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class GetMeApi(RetrieveAPIView):
    serializer_class=UserSerializer
    permission_classes=(IsAuthenticated,)
    
    def get_object(self):
        return self.request.user