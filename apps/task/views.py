from rest_framework.generics import CreateAPIView, ListAPIView
from .models import TaskModel
from .serializers import TaskSerializer


class CreateTaskApi(CreateAPIView):
    serializer_class = TaskSerializer
    
    
class ListTaskApi(ListAPIView):
    serializer_class =TaskSerializer
    queryset = TaskModel.objects.all() 
    