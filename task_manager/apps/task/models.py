from django.db import models
from apps.project.models import ProjectModel

# Create your models here.
class TagModel(models.Model):
    
    class Meta:
        db_table = 'Tag'
        
    title = models.CharField(max_length=20, unique=True)

class TaskModel(models.Model):
    class Meta:
        db_table='Task'
        
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]
    
    title = models.CharField(max_length=255, blank=False)
    priority = models.CharField(max_length=8, choices=PRIORITY_CHOICES, default='medium')
    completed = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(TagModel, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, blank=True, null=True, related_name='task')
    
    def __str__(self):
        return f"ID: {self.id} \n Title: {self.title} \n Priority: {self.priority}"
    
