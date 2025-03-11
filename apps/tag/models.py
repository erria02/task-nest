from django.db import models

# Create your models here.

class TagModel(models.Model):
    class Meta:
        db_table = 'tags'
        
    name=models.CharField(max_length=25, unique=True)
