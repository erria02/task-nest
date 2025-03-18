from django.db import models
from apps.tag.models import TagModel
# Create your models here.

class TaskModel(models.Model):
    class Meta:
        db_table = 'tasks'
    
    name = models.CharField(max_length=25)
    description = models.TextField()
    deadline = models.DateTimeField(blank=True, null=True)
    tag = models.ManyToManyField(TagModel, related_name='tasks', blank=True)
    
