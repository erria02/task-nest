from django.db import models
from core.models import BaseModel
from apps.task.models import TaskModel
# Create your models here.

class ProjectModel(BaseModel):
    class Meta:
        db_table = 'projects'
        
    name = models.CharField(max_length=25)
    tasks = models.ForeignKey(TaskModel, on_delete=models.CASCADE, related_name='project')

