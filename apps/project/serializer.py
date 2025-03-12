from rest_framework.serializers import ModelSerializer
from apps.task.serializers import TaskSerializer
from .models import ProjectModel

class ProjectSerializer(ModelSerializer):
    task = TaskSerializer
    class Meta:
        model = ProjectModel
        fields = ('name', 'tasks')
    read_only_fields = ('tasks',)
    