from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView  
from .models import TaskModel, TagModel
from .serializers import TaskSerializer, UpdateTaskSerializer, TagSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class CreateTaskView(CreateAPIView):
    queryset=TaskModel.objects.all()
    serializer_class=TaskSerializer

class ListTaskView(ListAPIView):
    queryset=TaskModel.objects.all()
    serializer_class=TaskSerializer
    pagination_class = PageNumberPagination

class UpdateTaskView(UpdateAPIView):
    queryset=TaskModel.objects.all()
    serializer_class=UpdateTaskSerializer 

class CreateTagView(CreateAPIView):
    queryset=TagModel.objects.all()
    serializer_class=TagSerializer 

class ListTagView(ListAPIView):
    queryset=TagModel.objects.all()
    serializer_class=TagSerializer
    
class TagUpdateView(UpdateAPIView):
    queryset=TagModel.objects.all()
    serializer_class=TagSerializer
