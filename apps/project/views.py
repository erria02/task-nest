from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializer import ProjectSerializer
from .models import ProjectModel
# Create your views here.

class ListProjectApiView(ListAPIView):
    serializer_class = ProjectSerializer
    queryset = ProjectModel.objects.all()
    


