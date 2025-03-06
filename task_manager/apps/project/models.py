from django.db import models


# Create your models here.

class ProjectModel(models.Model):
    class Meta:
        db_table='project'
        
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)

