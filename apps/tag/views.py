from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import TagSerializer
from .models import  TagModel
# Create your views here.

class ListTagApiView(ListAPIView):
    serializer_class = TagSerializer
    queryset = TagModel
