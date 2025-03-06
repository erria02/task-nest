from django.contrib import admin
from .models import TaskModel, TagModel
# Register your models here.
admin.site.register(TaskModel)
admin.site.register(TagModel)